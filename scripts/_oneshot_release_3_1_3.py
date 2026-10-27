#!/usr/bin/env python3
from pathlib import Path
import json

VERSION='3.1.3'
DATE='2026-10-27'

manifest=Path('custom_components/sbc5_control_center/manifest.json')
data=json.loads(manifest.read_text(encoding='utf-8'))
data['version']=VERSION
manifest.write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

const=Path('custom_components/sbc5_control_center/const.py')
text=const.read_text(encoding='utf-8')
import re
text=re.sub(r'APP_VERSION\s*=\s*"[^"]+"', f'APP_VERSION = "{VERSION}"', text, count=1)
const.write_text(text, encoding='utf-8')

readme=Path('README.md')
text=readme.read_text(encoding='utf-8')
text=re.sub(r'(?i)(current release[^\n]*?)3\.1\.2', lambda m:m.group(1)+VERSION, text)
text=re.sub(r'(?i)(aktualn(?:a|e) wersj[^\n]*?)3\.1\.2', lambda m:m.group(1)+VERSION, text)
readme.write_text(text, encoding='utf-8')

entry=f'''## {VERSION} — {DATE}\n\n### English\n- Added native AI Thermal Predictor quality diagnostics: average MAE, per-horizon MAE, last error, temperature slope, validated sample count and data age.\n- Added explicit physical Raspberry Pi host MAC and interface sensors for Device Registry verification.\n- Reuses the existing SBC5 coordinator and AI runtime relay; no new high-frequency polling loop.\n- Aligned integration metadata with SBC5 Control Center App/runtime and Card UI {VERSION}.\n\n### Polski\n- Dodano natywną diagnostykę jakości AI Thermal Predictor: średnie MAE, MAE dla horyzontów, ostatni błąd, trend temperatury, liczbę zweryfikowanych prognoz i wiek danych.\n- Dodano jawne sensory fizycznego MAC i interfejsu hosta Raspberry Pi do weryfikacji Device Registry.\n- Wykorzystano istniejący koordynator SBC5 i relay AI runtime; bez nowej szybkiej pętli odpytywania.\n- Wyrównano metadane integracji z App/runtime i Card UI SBC5 Control Center {VERSION}.\n\n'''
ch=Path('CHANGELOG.md')
old=ch.read_text(encoding='utf-8')
if not old.startswith(f'## {VERSION}'):
    ch.write_text(entry+old, encoding='utf-8')

notes=Path(f'RELEASE_NOTES_{VERSION}.md')
notes.write_text(f'''# SBC5 Control Center Integration {VERSION}\n\n## English\n\n### Highlights\n- Native AI Thermal Predictor quality diagnostics: average MAE, MAE and last error for +30 s/+60 s/+120 s, temperature slope, validated forecasts and data age.\n- Explicit physical Raspberry Pi host MAC and interface diagnostics make Device Registry cleanup verifiable.\n- No additional high-frequency polling; all diagnostics reuse the existing 15-second coordinator and AI runtime relay.\n\n### Upgrade notes\n- Update SBC5 Control Center App/runtime to {VERSION} through the Home Assistant Apps Store / configured SBC5 repository.\n- Update this companion integration through HACS.\n- Restart Home Assistant only when HACS requests it.\n- No Raspberry Pi host restart is required by this release.\n\n## Polski\n\n### Najważniejsze zmiany\n- Natywna diagnostyka jakości AI Thermal Predictor: średnie MAE, MAE i ostatni błąd dla +30 s/+60 s/+120 s, trend temperatury, liczba zweryfikowanych prognoz i wiek danych.\n- Jawne dane fizycznego MAC i interfejsu Raspberry Pi pozwalają zweryfikować porządkowanie Device Registry.\n- Bez dodatkowego szybkiego odpytywania; cała diagnostyka wykorzystuje istniejący 15-sekundowy koordynator i relay AI runtime.\n\n### Aktualizacja\n- App/runtime SBC5 Control Center zaktualizuj do {VERSION} przez Sklep Apps Home Assistant / skonfigurowane repozytorium SBC5.\n- Integrację towarzyszącą aktualizuj przez HACS.\n- Home Assistant uruchom ponownie tylko wtedy, gdy HACS tego zażąda.\n- To wydanie nie wymaga restartu hosta Raspberry Pi.\n''', encoding='utf-8')
print('Prepared HACS 3.1.3 metadata')
