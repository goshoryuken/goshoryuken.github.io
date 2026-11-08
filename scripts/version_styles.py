#!/usr/bin/env python3
"""Publish CSS under a content-derived URL and update every page that uses it."""
from hashlib import sha256
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def main():
    css = (ROOT / 'assets/site.css').read_bytes()
    filename = f'site.{sha256(css).hexdigest()[:12]}.css'
    destination = ROOT / 'assets' / filename
    # A previously published URL must always keep the same contents.
    if destination.exists() and destination.read_bytes() != css:
        raise RuntimeError(f'Conflicting stylesheet contents: {filename}')
    if not destination.exists():
        destination.write_bytes(css)

    pattern = re.compile(r'(href="(?:\.\./)*assets/)site(?:\.[0-9a-f]{12})?\.css(?:\?[^"\s]*)?(?=")')
    count = 0
    for page in ROOT.rglob('*.html'):
        original = page.read_text()
        updated, matches = pattern.subn(lambda match: match[1] + filename, original)
        if matches:
            count += 1
            if updated != original:
                page.write_text(updated)
    print(f'{count} pages reference assets/{filename}')


if __name__ == '__main__':
    main()
