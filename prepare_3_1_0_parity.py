#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
VERSION = "3.1.0"
OLD = "3.0.4"

manifest = ROOT / "custom_components/sbc5_control_center/manifest.json"
data = json.loads(manifest.read_text(encoding="utf-8"))
data["version"] = VERSION
manifest.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

const = ROOT / "custom_components/sbc5_control_center/const.py"
text = const.read_text(encoding="utf-8").replace('APP_VERSION = "3.0.4"', 'APP_VERSION = "3.1.0"', 1)
const.write_text(text, encoding="utf-8")

readme = ROOT / "README.md"
text = readme.read_text(encoding="utf-8")
text = text.replace('**Version 3.0.4 · HACS-ready', '**Version 3.1.0 · HACS-ready', 1)
text = text.replace('### Current release — 3.0.4', '### Current release — 3.1.0', 1)
text = text.replace(
    'Version-parity release aligned with SBC5 Control Center App/runtime 3.0.4. Integration behavior remains unchanged; App/runtime 3.0.4 lowers steady-state Config.txt watchdog and AI relay polling overhead without changing Adaptive PWM, AI evaluator, realtime cooling, telemetry cadence or the verified 49°C boot curve.',
    'Version 3.1.0 is aligned with SBC5 Control Center App/runtime 3.1.0. The integration exposes the runtime and AI surfaces used by the observe-only AI Thermal Predictor, while Adaptive PWM and AI Cooling remain authoritative. Recorder-friendly 30/60/120-second thermal forecast and confidence sensors are provided by the SBC5 package.',
    1,
)
text = text.replace('### Aktualne wydanie — 3.0.4', '### Aktualne wydanie — 3.1.0', 1)
text = text.replace(
    'Wydanie wyrównujące wersję integracji z aplikacją/runtime SBC5 Control Center 3.0.4. Zachowanie integracji pozostaje bez zmian; aplikacja/runtime 3.0.4 zmniejsza stałe obciążenie pollingiem Config.txt Manager i relay AI bez zmian Adaptive PWM, evaluatora AI, realtime cooling, telemetrii ani zweryfikowanej krzywej boot 49°C.',
    'Wersja 3.1.0 jest zgodna z aplikacją/runtime SBC5 Control Center 3.1.0. Integracja udostępnia powierzchnie runtime i AI wykorzystywane przez obserwacyjny AI Thermal Predictor, a Adaptive PWM i AI Cooling pozostają nadrzędne. Sensory prognozy termicznej 30/60/120 s oraz confidence przyjazne Recorderowi są dostarczane przez pakiet SBC5.',
    1,
)
readme.write_text(text, encoding="utf-8")

info = ROOT / "info.md"
text = info.read_text(encoding="utf-8")
text = text.replace('**Version:** 3.0.4', '**Version:** 3.1.0', 1)
text = text.replace(
    'The integration is aligned with App/runtime 3.0.4. Integration behavior is unchanged; the main App reduces steady-state Config.txt watchdog and AI relay polling overhead while preserving cooling-control cadence.',
    'The integration is aligned with App/runtime 3.1.0 and exposes the runtime and AI data surfaces used by the observe-only AI Thermal Predictor. Adaptive PWM and AI Cooling remain authoritative; Recorder-friendly thermal forecast sensors are provided by the SBC5 package.',
    1,
)
text = text.replace('**Wersja:** 3.0.4', '**Wersja:** 3.1.0', 1)
text = text.replace(
    'Integracja jest wyrównana z aplikacją/runtime 3.0.4. To wydanie nie zmienia zachowania integracji; główna aplikacja zmniejsza stałe obciążenie pollingiem Config.txt Manager i relay AI bez zmiany częstotliwości sterowania chłodzeniem.',
    'Integracja jest zgodna z aplikacją/runtime 3.1.0 i udostępnia dane runtime oraz AI wykorzystywane przez obserwacyjny AI Thermal Predictor. Adaptive PWM i AI Cooling pozostają nadrzędne; sensory prognozy termicznej przyjazne Recorderowi są dostarczane przez pakiet SBC5.',
    1,
)
info.write_text(text, encoding="utf-8")

changelog = ROOT / "CHANGELOG.md"
text = changelog.read_text(encoding="utf-8")
entry = '''## 3.1.0 — 2026-10-27\n\n- Aligned HACS integration metadata with SBC5 Control Center App/runtime 3.1.0.\n- Updated bilingual current-state documentation for the observe-only AI Thermal Predictor and Recorder-friendly thermal forecast surfaces.\n- Preserved existing integration entities, coordinator, telemetry, Repairs, update and Restart Manager behavior.\n- No Raspberry Pi host restart is required; restart Home Assistant only when requested by HACS.\n\n'''
if '## 3.1.0 — 2026-10-27' not in text:
    text = text.replace('# Changelog — SBC5 Control Center\n\n', '# Changelog — SBC5 Control Center\n\n' + entry, 1)
changelog.write_text(text, encoding="utf-8")

release = ROOT / "RELEASE_NOTES_3.1.0.md"
release.write_text('''# SBC5 Control Center Integration 3.1.0\n\n## English\n\n### Highlights\n\n- Aligned with SBC5 Control Center App/runtime **3.1.0**.\n- Integration behavior remains unchanged from 3.0.4.\n- App/runtime 3.1.0 introduces the observe-only **AI Thermal Predictor** with 30/60/120-second forecasts and online prediction-error scoring.\n- HACS ownership protection remains active through `.hacs_managed`.\n\n### Requirements\n\n- SBC5 Control Center App/runtime 3.1.0 installed and running\n- Home Assistant Core >= 2026.10.1\n- HACS-managed installation\n- Raspberry Pi 5\n\n### Upgrade notes\n\n- Existing integration configuration is preserved during a normal HACS upgrade.\n- Restart Home Assistant after the update only when requested by HACS.\n- The integration update does not require a Raspberry Pi host restart.\n\n---\n\n## Polski\n\n### Najważniejsze zmiany\n\n- Wyrównanie z aplikacją/runtime SBC5 Control Center **3.1.0**.\n- Zachowanie integracji pozostaje bez zmian względem 3.0.4.\n- Aplikacja/runtime 3.1.0 wprowadza obserwacyjny **AI Thermal Predictor** z prognozami 30/60/120 s i walidacją błędu prognoz online.\n- Ochrona kopii zarządzanej przez HACS pozostaje aktywna dzięki `.hacs_managed`.\n\n### Wymagania\n\n- Zainstalowana i uruchomiona aplikacja/runtime SBC5 Control Center 3.1.0\n- Home Assistant Core >= 2026.10.1\n- Instalacja zarządzana przez HACS\n- Raspberry Pi 5\n\n### Informacje o aktualizacji\n\n- Istniejąca konfiguracja integracji jest zachowywana podczas standardowej aktualizacji HACS.\n- Uruchom ponownie Home Assistant po aktualizacji tylko wtedy, gdy HACS tego wymaga.\n- Aktualizacja integracji nie wymaga restartu hosta Raspberry Pi.\n''', encoding="utf-8")

for p in (readme, info, changelog, release, manifest, const):
    s = p.read_text(encoding="utf-8")
    s = "\n".join(line.rstrip() for line in s.splitlines()) + "\n"
    p.write_text(s, encoding="utf-8")

print('Prepared HACS integration parity 3.1.0')
