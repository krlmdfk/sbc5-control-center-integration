#!/usr/bin/env python3
from pathlib import Path
import json, re

ROOT = Path(__file__).resolve().parents[1]
VERSION = '3.0.1'
SUMMARY_EN = 'Aligned with SBC5 Control Center App/runtime 3.0.1 maintenance optimization; integration behavior is unchanged while version parity and HACS release metadata are updated.'
SUMMARY_PL = 'Wyrównanie z aplikacją/runtime SBC5 Control Center 3.0.1 po optymalizacji utrzymaniowej; zachowanie integracji pozostaje bez zmian, aktualizowane są wersja i metadane wydania HACS.'

manifest = ROOT/'custom_components/sbc5_control_center/manifest.json'
data = json.loads(manifest.read_text(encoding='utf-8'))
data['version'] = VERSION
manifest.write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

const = ROOT/'custom_components/sbc5_control_center/const.py'
text = const.read_text(encoding='utf-8')
text = re.sub(r'^APP_VERSION = "[^"]+"$', f'APP_VERSION = "{VERSION}"', text, flags=re.M)
const.write_text(text, encoding='utf-8')

for name in ('README.md','info.md'):
    p = ROOT/name
    text = p.read_text(encoding='utf-8')
    text = text.replace('Version 3.0.0', f'Version {VERSION}')
    text = text.replace('**Version:** 3.0.0', f'**Version:** {VERSION}')
    old_en = 'Aligned with SBC5 Control Center App/runtime 3.0.0 and its hybrid Rust Core generation.'
    old_pl = 'Wyrównanie z aplikacją/runtime SBC5 Control Center 3.0.0 i generacją z hybrydowym Rust Core.'
    text = text.replace(old_en, SUMMARY_EN)
    text = text.replace(old_pl, SUMMARY_PL)
    p.write_text(text, encoding='utf-8')

changelog = ROOT/'CHANGELOG.md'
ch = changelog.read_text(encoding='utf-8')
if '## 3.0.1 — 2026-10-27' not in ch:
    entry = '''## 3.0.1 — 2026-10-27\n\n- Aligned the HACS integration release with SBC5 Control Center App/runtime 3.0.1.\n- Updated integration version metadata and bilingual release documentation.\n- No entity, coordinator, telemetry, repairs, update or Restart Manager behavior changes.\n\n'''
    first_nl = ch.find('\n') + 1 if ch.startswith('#') else 0
    ch = ch[:first_nl] + '\n' + entry + ch[first_nl:].lstrip('\n') if first_nl else entry + ch
    changelog.write_text(ch, encoding='utf-8')

notes = ROOT/f'RELEASE_NOTES_{VERSION}.md'
notes.write_text(f'''# SBC5 Control Center Integration {VERSION}\n\n## English\n\n### Highlights\n\n- Aligned with SBC5 Control Center App/runtime **{VERSION}**.\n- Keeps the same native Home Assistant device, telemetry, diagnostics, update and Restart Manager behavior as 3.0.0.\n- This integration release only restores version parity with the App/runtime maintenance release.\n- HACS ownership protection remains active through `.hacs_managed`.\n\n### Requirements\n\n- SBC5 Control Center App/runtime installed and running\n- Home Assistant Core >= 2026.10.1\n- HACS-managed installation\n- Raspberry Pi 5\n\n### Upgrade notes\n\n- Existing integration configuration is preserved during a normal HACS upgrade.\n- Restart Home Assistant after the update when requested by HACS.\n- The integration update itself does not require a Raspberry Pi host restart.\n\n---\n\n## Polski\n\n### Najważniejsze zmiany\n\n- Wyrównanie z aplikacją/runtime SBC5 Control Center **{VERSION}**.\n- Zachowano bez zmian natywne urządzenie Home Assistant, telemetrię, diagnostykę, aktualizacje i encje Restart Managera względem 3.0.0.\n- To wydanie integracji przywraca zgodność wersji z wydaniem utrzymaniowym aplikacji/runtime.\n- Ochrona kopii zarządzanej przez HACS pozostaje aktywna dzięki `.hacs_managed`.\n\n### Wymagania\n\n- Zainstalowana i uruchomiona aplikacja/runtime SBC5 Control Center\n- Home Assistant Core >= 2026.10.1\n- Instalacja zarządzana przez HACS\n- Raspberry Pi 5\n\n### Informacje o aktualizacji\n\n- Istniejąca konfiguracja integracji jest zachowywana przy standardowej aktualizacji HACS.\n- Po aktualizacji uruchom ponownie Home Assistant, gdy HACS tego wymaga.\n- Sama aktualizacja integracji nie wymaga restartu hosta Raspberry Pi.\n''', encoding='utf-8')
print('Prepared HACS integration 3.0.1')
