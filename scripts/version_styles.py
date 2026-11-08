#!/usr/bin/env python3
"""Publish CSS under a content-derived URL and update every page that uses it."""
from hashlib import sha256
from html import escape, unescape
from urllib.parse import parse_qsl, urlencode
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
    navigation = re.compile(
        r'href="(?P<path>(?:\.\./)*[A-Za-z0-9_/-]+\.html)'
        r'(?:\?(?P<query>[^"#]*))?(?P<fragment>#[^"]*)?"'
    )
    def version_link(match, version=None):
        query = [(key, value) for key, value in parse_qsl(
            unescape(match['query'] or ''), keep_blank_values=True
        ) if key != 'v']
        if version is not None:
            query.append(('v', version))
        url = match['path'] + ('?' + urlencode(query) if query else '') + (match['fragment'] or '')
        return 'href="' + escape(url, quote=True) + '"'

    # Content edits need fresh page URLs even when the stylesheet is unchanged.
    # Strip generated versions first so repeated runs produce identical results.
    pages = sorted(ROOT.rglob('*.html'))
    digest = sha256(css)
    for page in pages:
        normalized = pattern.sub(lambda match: match[1] + 'site.css', page.read_text())
        normalized = navigation.sub(version_link, normalized)
        digest.update(page.relative_to(ROOT).as_posix().encode() + b'\0')
        digest.update(normalized.encode() + b'\0')
    version = digest.hexdigest()[:12]

    count = 0
    for page in pages:
        original = page.read_text()
        updated, matches = pattern.subn(lambda match: match[1] + filename, original)
        updated = navigation.sub(lambda match: version_link(match, version), updated)
        if matches:
            count += 1
            if updated != original:
                page.write_text(updated)
    print(f'{count} pages use assets/{filename} and navigation version {version}')


if __name__ == '__main__':
    main()
