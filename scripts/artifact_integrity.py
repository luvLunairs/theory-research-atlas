"""Check retained local evidence and version metadata without network access."""
import hashlib
import re
from pathlib import Path, PureWindowsPath
from urllib.parse import urlsplit


ARTIFACT_FIELDS = (
    'input_artifacts', 'process_artifacts', 'candidate_answer_artifacts',
    'evidence_artifacts',
)
DIGEST_PATTERN = re.compile(r'^sha256:[0-9a-f]{64}$')


def validate_record_artifacts(record, root):
    """Validate referenced files; remote version declarations remain unverified."""
    errors = []
    label = record['id']
    root = Path(root).resolve()
    references = {ref for field in ARTIFACT_FIELDS for ref in record.get(field, [])}
    manifest = record.get('artifact_manifest', [])
    indexed = {}
    for item in manifest:
        reference = item['reference']
        if reference in indexed:
            errors.append(f'{label}: duplicate artifact manifest reference {reference}')
        indexed[reference] = item
    for reference in sorted(references - indexed.keys()):
        errors.append(f'{label}: artifact reference lacks a manifest entry: {reference}')
    for reference in sorted(indexed.keys() - references):
        errors.append(f'{label}: artifact manifest entry is not referenced: {reference}')

    for reference, item in indexed.items():
        version = item['version']
        digest = item['sha256']
        if not version.strip():
            errors.append(f'{label}: artifact needs a retained version description: {reference}')
        if digest is not None and not DIGEST_PATTERN.fullmatch(digest):
            errors.append(f'{label}: invalid artifact SHA-256 digest: {reference}')
        try:
            parsed = urlsplit(reference)
        except ValueError:
            errors.append(f'{label}: invalid artifact reference: {reference}')
            continue
        if parsed.scheme.lower() in {'http', 'https'}:
            if not parsed.netloc or not parsed.hostname:
                errors.append(f'{label}: remote artifact needs a complete HTTP(S) URL: {reference}')
            continue
        windows_path = PureWindowsPath(reference)
        relative = Path(reference.replace('\\', '/'))
        if parsed.scheme or relative.is_absolute() or windows_path.drive or windows_path.root:
            errors.append(f'{label}: local artifact must use a repository-relative path: {reference}')
            continue
        if any(part.lower() in {'work', '.git'} for part in relative.parts):
            errors.append(f'{label}: artifact cannot be retained in work/ or .git/: {reference}')
            continue
        try:
            path = (root / relative).resolve()
            if not path.is_relative_to(root):
                errors.append(f'{label}: artifact path escapes the repository: {reference}')
                continue
            if any(part.lower() in {'work', '.git'} for part in path.relative_to(root).parts):
                errors.append(f'{label}: artifact cannot resolve into work/ or .git/: {reference}')
                continue
            if not path.is_file():
                errors.append(f'{label}: local artifact file does not exist: {reference}')
                continue
            if digest is None:
                errors.append(f'{label}: local artifact requires a SHA-256 digest: {reference}')
                continue
            checksum = hashlib.sha256()
            with path.open('rb') as stream:
                for chunk in iter(lambda: stream.read(1024 * 1024), b''):
                    checksum.update(chunk)
            actual = 'sha256:' + checksum.hexdigest()
            if digest != actual:
                errors.append(f'{label}: local artifact digest differs from retained bytes: {reference}')
        except (OSError, ValueError, RuntimeError) as exc:
            errors.append(f'{label}: cannot read retained artifact {reference}: {exc}')
    return errors
