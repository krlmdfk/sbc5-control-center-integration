#!/usr/bin/env python3
from pathlib import Path
import json, re

VERSION='3.1.2'
manifest=Path('custom_components/sbc5_control_center/manifest.json')
data=json.loads(manifest.read_text(encoding='utf-8')); data['version']=VERSION
manifest.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

const=Path('custom_components/sbc5_control_center/const.py')
s=const.read_text(encoding='utf-8')
s=re.sub(r'APP_VERSION\s*=\s*["\'][^"\']+["\']',f'APP_VERSION = "{VERSION}"',s,count=1)
const.write_text(s,encoding='utf-8')

readme=Path('README.md'); s=readme.read_text(encoding='utf-8')
s=s.replace('Current release: **3.1.1**','Current release: **3.1.2**').replace('Version: **3.1.1**','Version: **3.1.2**')
s=s.replace('App/runtime **3.1.1**','App/runtime **3.1.2**').replace('Card UI **3.1.1**','Card UI **3.1.2**')
readme.write_text(s,encoding='utf-8')

ch=Path('CHANGELOG.md'); old=ch.read_text(encoding='utf-8')
entry='''## 3.1.2 — 2026-10-27\n\n### English\n\n- Added native AI Thermal Predictor sensors for +30 s, +60 s, +120 s and predictor confidence, using the existing AI runtime relay without a new polling loop.\n- Migrated the 3.1.1 package-template Predictor entity IDs to native integration ownership while preserving canonical entity IDs for Recorder continuity.\n- Fixed Raspberry Pi device identity reconciliation: accumulated stale App/container MAC connections are replaced with the single physical host MAC supplied by the App.\n- Aligned integration metadata with SBC5 Control Center App/runtime and Card UI 3.1.2.\n- No Raspberry Pi host restart is required; restart Home Assistant only when requested by HACS after the integration update.\n\n### Polski\n\n- Dodano natywne sensory AI Thermal Predictor dla +30 s, +60 s, +120 s oraz pewności predyktora, korzystające z istniejącego przekaźnika AI runtime bez nowej pętli odpytywania.\n- Zmigrowano identyfikatory encji Predictora z template package 3.1.1 do natywnej integracji przy zachowaniu kanonicznych entity_id dla ciągłości Recordera.\n- Naprawiono identyfikację urządzenia Raspberry Pi: nagromadzone stare adresy MAC aplikacji/kontenera są zastępowane pojedynczym fizycznym MAC hosta przekazanym przez aplikację.\n- Wyrównano metadane integracji z App/runtime i Card UI SBC5 Control Center 3.1.2.\n- Restart hosta Raspberry Pi nie jest wymagany; Home Assistant uruchom ponownie tylko wtedy, gdy HACS tego zażąda po aktualizacji integracji.\n\n'''
if not re.search(r'^## 3\.1\.2\b',old,re.M):
    m=re.match(r'(#[^\n]*\n(?:\n)?)',old)
    old=old[:m.end()]+entry+old[m.end():] if m else entry+old
ch.write_text(old,encoding='utf-8')

notes=Path('RELEASE_NOTES_3.1.2.md')
notes.write_text('''# SBC5 Control Center Integration 3.1.2\n\n## English\n\n### Highlights\n\n- AI Thermal Predictor is now exposed as native Home Assistant sensors for +30 s, +60 s, +120 s and predictor confidence.\n- Existing Predictor entity IDs are migrated from the 3.1.1 package templates, preserving the canonical IDs used by dashboards and Recorder.\n- Device Registry network identity is reconciled to one physical Raspberry Pi host MAC, removing accumulated container/virtual MAC connections.\n- No extra high-frequency polling is introduced; the integration reuses the existing coordinator and AI runtime relay.\n\n### Upgrade notes\n\n- Update SBC5 Control Center App/runtime to 3.1.2 through the Home Assistant Apps Store / configured SBC5 repository.\n- Update this companion integration to 3.1.2 through HACS.\n- Restart Home Assistant only when requested by HACS.\n- No Raspberry Pi host restart is required by this release.\n\n## Polski\n\n### Najważniejsze zmiany\n\n- AI Thermal Predictor jest teraz udostępniany jako natywne sensory Home Assistant dla +30 s, +60 s, +120 s oraz pewności predyktora.\n- Dotychczasowe identyfikatory encji Predictora są migrowane z template package 3.1.1 z zachowaniem kanonicznych ID używanych przez dashboard i Recorder.\n- Tożsamość sieciowa Device Registry jest uzgadniana do jednego fizycznego adresu MAC hosta Raspberry Pi, a nagromadzone adresy kontenerowe/wirtualne są usuwane.\n- Nie dodano dodatkowego szybkiego odpytywania; integracja wykorzystuje istniejący koordynator i przekaźnik AI runtime.\n\n### Informacje o aktualizacji\n\n- App/runtime SBC5 Control Center zaktualizuj do 3.1.2 przez Sklep Apps Home Assistant / skonfigurowane repozytorium SBC5.\n- Integrację towarzyszącą zaktualizuj do 3.1.2 przez HACS.\n- Home Assistant uruchom ponownie tylko wtedy, gdy HACS tego zażąda.\n- To wydanie nie wymaga restartu hosta Raspberry Pi.\n''',encoding='utf-8')
print('HACS 3.1.2 release metadata prepared')
