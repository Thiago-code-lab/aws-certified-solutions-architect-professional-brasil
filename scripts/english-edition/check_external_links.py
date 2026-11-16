"""Optional bounded HTTP reachability check; does not validate page semantics."""
from __future__ import annotations

import json
import re
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit, urlunsplit
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup

from validate import AUDIT, MARKDOWN, ROOT


def urls_in_file(path: Path) -> set[str]:
    raw = path.read_text(encoding='utf-8-sig')
    soup = BeautifulSoup(MARKDOWN.render(raw), 'html.parser')
    values = {str(node.get('href', node.get('src', ''))) for node in soup.select('[href], [src]')}
    values.update(re.findall(r'https?://[^\s<>"\])]+', raw))
    result: set[str] = set()
    for value in values:
        parsed = urlsplit(value)
        if parsed.scheme in {'http', 'https'} and parsed.netloc:
            result.add(urlunsplit((parsed.scheme, parsed.netloc, parsed.path, parsed.query, '')))
    return result


def check(url: str) -> dict[str, Any]:
    request = Request(url, headers={'User-Agent': 'CloudStudy-Documentation-Validation/1.0'})
    try:
        with urlopen(request, timeout=12) as response:
            return {'url': url, 'status': response.status, 'final_url': response.url}
    except HTTPError as error:
        return {'url': url, 'status': error.code, 'error': str(error.reason)}
    except (URLError, TimeoutError, OSError) as error:
        return {'url': url, 'status': None, 'error': str(error)}


def main() -> None:
    urls: set[str] = set()
    for path in ROOT.rglob('*.md'):
        if '.git' not in path.parts:
            urls.update(urls_in_file(path))
    with ThreadPoolExecutor(max_workers=8) as executor:
        results = list(executor.map(check, sorted(urls)))
    summary = dict(Counter(str(row['status']) for row in results))
    report = {'method': 'HTTP GET with redirects, 12-second timeout and eight workers; fragment anchors and page semantics are not checked.',
              'unique_urls': len(urls), 'summary': summary, 'results': results}
    (AUDIT / 'external-link-results.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'unique_urls': len(urls), 'summary': summary}))
    for row in results:
        if row['status'] != 200:
            print(json.dumps(row))


if __name__ == '__main__':
    main()
