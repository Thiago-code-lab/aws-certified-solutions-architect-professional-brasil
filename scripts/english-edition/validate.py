"""Offline source-coverage, exercise and Markdown checks for the English edition.

Adapted to SAP-C02 from the CLF-C02 English edition's inventory, parsed-link,
anchor, question-audit and mutation-test conventions. Never calls AWS APIs.
"""
from __future__ import annotations

import hashlib
import io
import json
import re
import subprocess
import tarfile
from collections import Counter
from functools import lru_cache
from pathlib import Path
from typing import Any
from urllib.parse import unquote, urlsplit

from bs4 import BeautifulSoup
from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parents[2]
AUDIT = ROOT / 'docs/english-edition'
MARKDOWN = MarkdownIt('commonmark', {'html': True}).enable('table')
PORTUGUESE = re.compile(
    r'\b(?:voce|você|questoes|questões|restricao|restrição|requisito|requisitos|'
    r'governanca|governança|seguranca|segurança|explicacao|explicação|'
    r'cenario|cenário|conectividade|migracao|migração|atualizacao|atualização|'
    r'proximo|próximo|visao|visão|resposta|portugues|português)\b', re.I)


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding='utf-8'))


def digest(payload: bytes, path: str) -> str:
    normalized = payload if path.endswith('.png') else payload.replace(b'\r\n', b'\n')
    return hashlib.sha256(normalized).hexdigest()


@lru_cache(maxsize=2)
def source_tree(commit: str) -> dict[str, bytes]:
    """Read immutable source blobs in one Git operation rather than per file."""
    archive = subprocess.check_output(['git', 'archive', '--format=tar', commit], cwd=ROOT)
    result: dict[str, bytes] = {}
    with tarfile.open(fileobj=io.BytesIO(archive)) as files:
        for entry in files:
            if entry.isfile():
                stream = files.extractfile(entry)
                if stream is None:
                    raise ValueError(f'Unreadable Git archive member: {entry.name}')
                result[entry.name] = stream.read()
    return result


def source_bytes(path: str, commit: str) -> bytes:
    return source_tree(commit)[path]


def source_paths(commit: str) -> set[str]:
    result = subprocess.check_output(
        ['git', 'ls-tree', '-rz', '--name-only', commit], cwd=ROOT)
    return set(result.decode('utf-8').rstrip('\0').split('\0'))


def heading_slug(text: str) -> str:
    plain = BeautifulSoup(MARKDOWN.renderInline(text), 'html.parser').get_text().lower()
    return re.sub(r'[^\w\- ]', '', plain).replace(' ', '-')


def anchors(raw: str) -> set[str]:
    rendered = BeautifulSoup(MARKDOWN.render(raw), 'html.parser')
    found = {str(node['id']) for node in rendered.select('[id]')}
    found.update(str(node['name']) for node in rendered.select('a[name]'))
    duplicates: Counter[str] = Counter()
    tokens = MARKDOWN.parse(raw)
    for index, token in enumerate(tokens[:-1]):
        if token.type == 'heading_open':
            base = heading_slug(tokens[index + 1].content)
            suffix = f'-{duplicates[base]}' if duplicates[base] else ''
            found.add(base + suffix)
            duplicates[base] += 1
    return found


def link_failures(path: Path, root: Path = ROOT) -> list[str]:
    soup = BeautifulSoup(MARKDOWN.render(path.read_text(encoding='utf-8-sig')), 'html.parser')
    failures: list[str] = []
    for node in soup.select('[href], [src]'):
        href = str(node.get('href', node.get('src', '')))
        parsed = urlsplit(href)
        if parsed.scheme or parsed.netloc or href in {'', '#'}:
            continue
        target = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
        if not target.is_relative_to(root.resolve()) or not target.is_file():
            failures.append(f'{path.name}: missing or out-of-repository target {href}')
        elif parsed.fragment and target.suffix == '.md':
            if unquote(parsed.fragment) not in anchors(target.read_text(encoding='utf-8-sig')):
                failures.append(f'{path.name}: missing anchor {href}')
    return failures


def table_failures(raw: str) -> list[str]:
    failures: list[str] = []
    lines = raw.splitlines()
    for token in MARKDOWN.parse(raw):
        if token.type == 'table_open' and token.map:
            start, end = token.map
            widths = {len(re.split(r'(?<!\\)\|', row.strip().strip('|')))
                      for row in lines[start:end] if row.strip()}
            if len(widths) != 1:
                failures.append(f'inconsistent table columns at line {start + 1}')
    return failures


def markdown_failures(raw: str) -> list[str]:
    failures = table_failures(raw)
    lines = raw.splitlines()
    for token in MARKDOWN.parse(raw):
        if token.type == 'fence' and token.map:
            last = lines[token.map[1] - 1].strip()
            if not re.fullmatch(re.escape(token.markup[0]) + '{' + str(len(token.markup)) + r',}\s*', last):
                failures.append('unclosed code fence')
    soup = BeautifulSoup(MARKDOWN.render(raw), 'html.parser')
    if len(re.findall(r'<details(?:\s[^>]*)?>', raw)) != raw.count('</details>'):
        failures.append('unbalanced expandable answers')
    for details in soup.find_all('details'):
        summaries = details.find_all('summary', recursive=False)
        if len(summaries) != 1 or not summaries[0].get_text(strip=True):
            failures.append('expandable answer requires one nonempty summary')
    return failures


def language_failures(raw: str) -> list[str]:
    soup = BeautifulSoup(MARKDOWN.render(raw), 'html.parser')
    for code in soup.select('pre, code'):
        code.decompose()
    text = re.sub(r'https?://\S+', '', soup.get_text(' '))
    return sorted(set(PORTUGUESE.findall(text)))


def question_blocks(raw: str) -> list[dict[str, Any]]:
    """Parse headed multiple-choice items and numbered open-response items."""
    headings = list(re.finditer(r'^## (?:Question|Questao) (\d+)\s*$', raw, re.M))
    if not headings:
        return [{'number': int(m[1]), 'body': m[0], 'kind': 'open-response'}
                for m in re.finditer(r'^\s*(\d+)\. .+\*\*(?:Answer|Resposta):\*\*.+$', raw, re.M)]
    return [{'number': int(match[1]), 'kind': 'multiple-choice',
             'body': raw[match.end():headings[i + 1].start() if i + 1 < len(headings) else len(raw)]}
            for i, match in enumerate(headings)]


def question_signature(block: dict[str, Any]) -> dict[str, Any]:
    body = block['body']
    options = re.findall(r'^([A-F])[.)]\s+(.+)$', body, re.M)
    answer = re.search(r'\*\*(?:Correct answer|Answer|Resposta correta|Resposta):\*\*\s*([^\n]+)', body)
    value = answer[1].strip() if answer else ''
    letters = re.findall(r'\b[A-F]\b', value) if block['kind'] == 'multiple-choice' else []
    return {'number': block['number'], 'kind': block['kind'],
            'option_labels': [label for label, _ in options],
            'answer_set': sorted(letters), 'answer_text': value,
            'multi_select': bool(re.search(r'(?i)\b(?:choose|select|escolha|selecione)\s+(?:two|three|duas|dois|tres|três|[2-6])', body))}


def exercise_failures(source: str, target: str, corrections: dict[int, str]) -> list[str]:
    originals, translated = question_blocks(source), question_blocks(target)
    if len(originals) != len(translated):
        return ['question count changed']
    failures: list[str] = []
    for original, english in zip(originals, translated):
        old, new = question_signature(original), question_signature(english)
        for field in ('number', 'kind', 'option_labels', 'answer_set', 'multi_select'):
            if old[field] != new[field]:
                failures.append(f'question {old["number"]}: {field} changed')
        if not new['answer_text'] or not new['answer_set'] and new['kind'] == 'multiple-choice':
            failures.append(f'question {old["number"]}: missing answer')
        if any(letter not in new['option_labels'] for letter in new['answer_set']):
            failures.append(f'question {old["number"]}: answer is not an alternative')
        if old['kind'] == 'multiple-choice' and not has_explanation(english['body']):
            failures.append(f'question {old["number"]}: missing explanation')
        if old['number'] in corrections and new['answer_text'] != corrections[old['number']]:
            failures.append(f'question {old["number"]}: documented correction regressed')
    return failures


def has_explanation(body: str) -> bool:
    if re.search(r'\*\*Explanation:\*\*\s*\S', body):
        return True
    after_answer = re.split(r'\*\*Correct answer:\*\*[^\n]*', body, maxsplit=1)
    if len(after_answer) != 2:
        return False
    plain = BeautifulSoup(after_answer[1].split('</details>')[0], 'html.parser').get_text()
    return len(plain.split()) >= 5


def coverage_failures(inventory: dict[str, Any]) -> list[str]:
    rows = inventory['files']
    failures: list[str] = []
    if {row['original_path'] for row in rows} != source_paths(inventory['source_commit']):
        failures.append('source inventory differs from Git source tree')
    targets = [row['target_path'] for row in rows]
    if len(targets) != len(set(targets)):
        failures.append('duplicate mapped target paths')
    for row in rows:
        path = ROOT / row['target_path']
        if not path.is_file():
            failures.append(f'missing source equivalent: {row["target_path"]}')
            continue
        if digest(source_bytes(row['original_path'], inventory['source_commit']), row['original_path']) != row['source_sha256']:
            failures.append(f'source checksum mismatch: {row["original_path"]}')
        if row['kind'] == 'preserved' and digest(path.read_bytes(), row['target_path']) != row['source_sha256']:
            failures.append(f'preserved file changed: {row["target_path"]}')
        if row['original_path'] != row['target_path'] and (ROOT / row['original_path']).exists():
            failures.append(f'obsolete source path remains: {row["original_path"]}')
    return failures


def structure_failures(source: str, target: str, flashcards: bool) -> list[str]:
    failures: list[str] = []
    for kind in ('heading_open', 'table_open', 'fence'):
        before = sum(t.type == kind for t in MARKDOWN.parse(source))
        after = sum(t.type == kind for t in MARKDOWN.parse(target))
        if after < before:
            failures.append(f'lost {kind} structure')
    if len([line for line in target.splitlines() if line.strip()]) < len([line for line in source.splitlines() if line.strip()]):
        failures.append('nonempty source lines removed; review content coverage')
    if flashcards:
        pattern = r'^\s*\d+\.\s+'
        if len(re.findall(pattern, source, re.M)) != len(re.findall(pattern, target, re.M)):
            failures.append('flashcard count changed')
    return failures


def document_failures(row: dict[str, Any], commit: str, audit: dict[str, Any]) -> list[str]:
    path = ROOT / row['target_path']
    if not path.is_file():
        return []
    raw = path.read_text(encoding='utf-8-sig')
    source = source_bytes(row['original_path'], commit).decode('utf-8-sig')
    failures = structure_failures(source, raw, path.name == 'flashcards.md')
    failures.extend(f'Portuguese language regression: {word}' for word in language_failures(raw))
    failures.extend(promotional_failures(source, raw))
    if path.name in {'questions.md', 'domain-practice-exams.md'}:
        corrections = {r['number']: r['corrected_answer'] for r in audit['answer_corrections']
                       if r['target_path'] == row['target_path']}
        failures.extend(exercise_failures(source, raw, corrections))
    return [f'{row["target_path"]}: {failure}' for failure in failures]


def promotional_failures(source: str, target: str) -> list[str]:
    pattern = r'https?://(?:cloudstudy\.com\.br|www\.instagram\.com|www\.linkedin\.com|www\.udemy\.com|chat\.whatsapp\.com)[^\s)"<>]*'
    original = set(re.findall(pattern, source))
    translated = set(re.findall(pattern, target))
    return [f'promotional URL removed: {url}' for url in sorted(original - translated)]


def module_failures(inventory: dict[str, Any]) -> list[str]:
    actual = sorted(p.name for p in ROOT.iterdir() if p.is_dir() and re.match(r'^\d\d-', p.name))
    expected = [module['target'] for module in inventory['modules']]
    failures = [] if actual == expected and len(actual) == 31 else ['31-module sequence differs from inventory']
    for module in inventory['modules']:
        for filename in ('README.md', 'questions.md', 'flashcards.md', 'cheatsheet.md', 'use-cases.md', 'links.md'):
            if not (ROOT / module['target'] / filename).is_file():
                failures.append(f'{module["target"]}: missing {filename}')
    return failures


def audit_failures(inventory: dict[str, Any], audit: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    actual: list[tuple[str, int]] = []
    for row in inventory['files']:
        if row['target_path'].endswith(('/questions.md', '/domain-practice-exams.md')):
            for block in question_blocks(source_bytes(row['original_path'], inventory['source_commit']).decode('utf-8-sig')):
                actual.append((row['target_path'], block['number']))
    recorded = [(row['target_path'], row['number']) for row in audit['questions']]
    if Counter(actual) != Counter(recorded):
        failures.append('question audit omits or duplicates source prompts')
    for row in audit['questions']:
        path = ROOT / row['target_path']
        blocks = question_blocks(path.read_text(encoding='utf-8-sig')) if path.exists() else []
        block = next((b for b in blocks if b['number'] == row['number']), None)
        if block and question_signature(block) != row['reviewed_signature']:
            failures.append(f'{row["target_path"]} question {row["number"]}: reviewed signature changed')
    return failures


def run() -> dict[str, Any]:
    inventory = read_json(AUDIT / 'source-inventory.json')
    audit = read_json(AUDIT / 'question-audit.json')
    failures = coverage_failures(inventory) + module_failures(inventory) + audit_failures(inventory, audit)
    for row in inventory['files']:
        if row['kind'] == 'markdown':
            failures.extend(document_failures(row, inventory['source_commit'], audit))
    files = sorted(p for p in ROOT.rglob('*.md') if '.git' not in p.parts)
    for path in files:
        failures.extend(f'{path.relative_to(ROOT)}: {message}' for message in markdown_failures(path.read_text(encoding='utf-8-sig')))
        failures.extend(link_failures(path))
    return {'passed': not failures, 'source_commit': inventory['source_commit'],
            'source_files': len(inventory['files']), 'translated_markdown': inventory['markdown_documents'],
            'modules': len(inventory['modules']), 'questions': len(audit['questions']),
            'markdown_files_checked': len(files), 'failures': failures,
            'scope': 'Offline checks; no external URL reachability test or AWS lab execution.'}


if __name__ == '__main__':
    result = run()
    (AUDIT / 'validation-results.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result['passed'] else 1)
