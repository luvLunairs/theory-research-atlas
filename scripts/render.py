"""Render Markdown views from the structured research collection."""
import argparse
import sys

from render_cards import render_cards
from render_indexes import render_indexes
from render_records import render_records
from render_verifications import render_verifications
from validate import ROOT, load_dataset, validate_dataset


def outputs(dataset, root=ROOT):
    indexes = render_indexes(dataset, root=root)
    cards = render_cards(dataset, root=root)
    overlap = indexes.keys() & cards.keys()
    if overlap:
        raise ValueError(f'Duplicate generated paths: {sorted(overlap)}')
    records = render_records(dataset, root=root)
    if records.keys() & (indexes.keys() | cards.keys()):
        raise ValueError('Duplicate generated record paths')
    verifications = render_verifications(dataset, root=root)
    if verifications.keys() & (indexes.keys() | cards.keys() | records.keys()):
        raise ValueError('Duplicate generated verification paths')
    return {**indexes, **cards, **records, **verifications}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Check views without writing files')
    args = parser.parse_args()
    dataset = load_dataset()
    errors = validate_dataset(dataset)
    if errors:
        print('\n'.join(errors))
        return 1
    rendered = outputs(dataset)
    stale = []
    for relative, content in rendered.items():
        path = ROOT / relative
        if args.check:
            if not path.exists() or path.read_text(encoding='utf-8') != content:
                stale.append(relative)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding='utf-8', newline='\n')
    if stale:
        print('STALE: ' + ', '.join(stale))
    else:
        print('Generated views are current.' if args.check else f'Rendered {len(rendered)} Markdown views.')
    return bool(stale)


if __name__ == '__main__':
    sys.exit(main())
