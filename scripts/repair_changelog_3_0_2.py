#!/usr/bin/env python3
from pathlib import Path
import subprocess

TITLE = '# Changelog — SBC5 Control Center\n\n'
BLOCK = '''## 3.0.2 — 2026-10-27

- Aligned the HACS integration release with SBC5 Control Center App/runtime 3.0.2.
- Updated integration version metadata and bilingual release/current-state documentation.
- No entity, coordinator, telemetry, repairs, update or Restart Manager behavior changes.

'''

text = subprocess.check_output(
    ['git', 'show', 'origin/main:CHANGELOG.md'],
    text=True,
    encoding='utf-8',
)
if not text.startswith(TITLE):
    raise SystemExit('unexpected CHANGELOG header')
if '## 3.0.2 — 2026-10-27' not in text:
    text = TITLE + BLOCK + text[len(TITLE):]
Path('CHANGELOG.md').write_text(text, encoding='utf-8')
print('Restored full CHANGELOG history and prepended 3.0.2')
