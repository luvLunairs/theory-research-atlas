"""Run offline checks; optionally refresh generated views after data validation."""
import argparse
import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
CHECKS = (
    ('Data integrity', ('scripts/validate.py',)),
    ('Regression tests', ('-m', 'unittest', 'discover', '-s', 'scripts', '-p', 'test_*.py')),
    ('Generated pages', ('scripts/render.py', '--check')),
    ('Documentation', ('scripts/check_docs.py',)),
)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--render', action='store_true',
                        help='refresh generated pages after validating data, then run all checks')
    options = parser.parse_args(argv)
    environment = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', PYTHONUTF8='1')
    steps = list(CHECKS)
    if options.render:
        steps.insert(1, ('Page refresh', ('scripts/render.py',)))
    for label, arguments in steps:
        print(f'Checking {label.lower()}...', flush=True)
        result = subprocess.run((sys.executable, *arguments), cwd=ROOT, env=environment)
        if result.returncode:
            print(f'{label} failed.', file=sys.stderr)
            return result.returncode
    print('All repository checks passed. Scientific claims require their own review.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
