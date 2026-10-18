"""Check documentation targets, submission references and citation markers.

Temporary files, Git metadata and Python caches are excluded from these checks.
"""
import re
import sys
from functools import lru_cache
from pathlib import Path, PureWindowsPath
from urllib.parse import parse_qs, unquote, urlparse

ROOT=Path(__file__).resolve().parents[1]
SKIP={'work','.git','__pycache__'}
REPOSITORY_PATH='/luvLunairs/theory-research-atlas'
def included(p): return not (set(p.relative_to(ROOT).parts)&SKIP)

def markdown_targets(text):
    clean = re.sub(r'```.*?```', '', text, flags=re.S)
    return [target.strip('<>') for target in re.findall(r'\[[^\]]*\]\(([^\n)]+)\)', clean)]

def submission_reference_errors(relative, text):
    """Submission text must remain usable outside its source-file location."""
    name = relative.as_posix()
    submission = (name == '.github/PULL_REQUEST_TEMPLATE.md'
                  or name.startswith('.github/ISSUE_TEMPLATE/')
                  or name.startswith('templates/'))
    if not submission:
        return []
    return [f'{name}: file-relative link in submission text: {target}; '
            'use an absolute URL or a repository path in code formatting'
            for target in markdown_targets(text)
            if target and not target.startswith('#') and not urlparse(target).scheme]

def issue_form_errors(relative, text):
    """Catch reserved choices in block-style forms, without a YAML dependency."""
    if (relative.parent.as_posix() != '.github/ISSUE_TEMPLATE'
            or relative.suffix not in {'.yml', '.yaml'}):
        return []
    errors = []
    field_indent = field_type = options_indent = scalar_indent = None
    for number, line in enumerate(text.splitlines(), 1):
        stripped = line.strip()
        if not stripped or stripped.startswith('#'):
            continue
        indent = len(line) - len(line.lstrip())
        if scalar_indent is not None:
            if indent > scalar_indent:
                continue
            scalar_indent = None
        if re.fullmatch(r'(?:[^#]+:\s*|-\s*)[|>][+-]?\d*\s*(?:#.*)?', stripped):
            scalar_indent = indent
            continue
        field = re.fullmatch(r'-\s+type:\s*[\'"]?([a-z]+)[\'"]?\s*(?:#.*)?', stripped)
        if field and (field_indent is None or indent <= field_indent):
            field_indent, field_type = indent, field.group(1)
            options_indent = None
            continue
        if field_indent is None:
            continue
        if indent <= field_indent:
            field_type = options_indent = None
        if field_type != 'dropdown':
            continue
        if re.fullmatch(r'options:\s*(?:#.*)?', stripped):
            options_indent = indent
            continue
        if options_indent is not None:
            if indent < options_indent or (indent == options_indent and not stripped.startswith('-')):
                options_indent = None
            elif re.fullmatch(r'-\s*(?:none|"none"|\'none\')\s*(?:#.*)?', stripped, re.I):
                errors.append(f'{relative.as_posix()}:{number}: dropdown option "None" is reserved '
                              'by GitHub; use a descriptive choice such as "No AI assistance"')
    return errors

def heading_anchors(text):
    anchors=set(re.findall(r'<a\s+id="([^"]+)"',text))
    for heading in re.findall(r'^#{1,6}\s+(.+)$',text,re.M):
        anchor=re.sub(r'[^\w\- ]','',heading.lower()).replace(' ','-')
        anchors.add(anchor)
    return anchors

@lru_cache(maxsize=None)
def file_anchors(path):
    return heading_anchors(path.read_text(encoding='utf-8'))

def target_errors(relative, target, dest, fragment, root):
    """Check a resolved local destination without following external links."""
    prefix = relative.as_posix()
    if not dest.is_relative_to(root):
        return [f'{prefix}: link escapes project: {target}']
    if not dest.is_file():
        return [f'{prefix}: missing target {target}']
    if fragment and dest.suffix == '.md' and unquote(fragment) not in file_anchors(dest):
        return [f'{prefix}: missing fragment {target}']
    return []

def repository_link_errors(relative, target, root=None):
    """Validate supported GitHub links against this checkout; None means uninspected."""
    root = ROOT if root is None else root
    parsed = urlparse(target)
    if parsed.scheme != 'https' or parsed.netloc.lower() != 'github.com':
        return None
    blob_prefix = REPOSITORY_PATH + '/blob/main/'
    if parsed.path.startswith(blob_prefix):
        name = unquote(parsed.path[len(blob_prefix):])
        if name.startswith('/') or '\\' in name or PureWindowsPath(name).drive:
            return [f'{relative.as_posix()}: link escapes project: {target}']
        dest = (root / name).resolve()
        return target_errors(relative, target, dest, parsed.fragment, root)
    if parsed.path != REPOSITORY_PATH + '/issues/new':
        return None
    query = parse_qs(parsed.query, keep_blank_values=True)
    if 'template' not in query:
        return None
    templates = query['template']
    if len(templates) != 1:
        return [f'{relative.as_posix()}: expected one issue form: {target}']
    name = templates[0]
    # A form selector is a filename, not a path relative to the forms directory.
    if (not name or '/' in name or '\\' in name or PureWindowsPath(name).drive
            or name == 'config.yml' or Path(name).suffix not in {'.yml', '.yaml'}):
        return [f'{relative.as_posix()}: invalid issue form name: {target}']
    forms = (root / '.github/ISSUE_TEMPLATE').resolve()
    dest = (forms / name).resolve()
    if not dest.is_relative_to(forms):
        return [f'{relative.as_posix()}: issue form escapes template directory: {target}']
    return target_errors(relative, target, dest, '', root)

def main():
    errors=[]; link_count=0; file_count=0
    for path in ROOT.rglob('*'):
        if not path.is_file() or not included(path) or path.suffix not in {'.md','.json','.py','.cff','.yml','.yaml','.txt'}: continue
        file_count+=1; text=path.read_text(encoding='utf-8')
        if re.search(r'\ue200|turn\d+(?:search|view|fetch)\d+',text): errors.append(f'{path.relative_to(ROOT)}: unresolved citation reference')
        errors.extend(submission_reference_errors(path.relative_to(ROOT), text))
        errors.extend(issue_form_errors(path.relative_to(ROOT), text))
        if path.suffix not in {'.md', '.yml', '.yaml'}: continue
        for target in markdown_targets(text):
            if urlparse(target).scheme:
                repository_errors = repository_link_errors(path.relative_to(ROOT), target)
                if repository_errors is not None:
                    link_count += 1
                    errors.extend(repository_errors)
                continue
            if path.suffix != '.md': continue
            name,_,frag=target.partition('#')
            dest=(path.parent/unquote(name)).resolve() if name else path
            link_count+=1
            errors.extend(target_errors(path.relative_to(ROOT), target, dest, frag, ROOT))
    print(f'Checked {file_count} text files and {link_count} local and repository Markdown links.')
    print('\n'.join(errors) if errors else 'PASS: local and repository links and citation references.')
    return bool(errors)
if __name__=='__main__': sys.exit(main())
