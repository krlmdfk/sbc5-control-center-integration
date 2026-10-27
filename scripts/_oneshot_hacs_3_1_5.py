#!/usr/bin/env python3
from __future__ import annotations

import json
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COMP = ROOT / "custom_components" / "sbc5_control_center"

sensor_url = "https://raw.githubusercontent.com/krlmdfk/sbc5-control-center/feature/3.1.5-thermal-predictor-shadow-assist/custom_components/sbc5_control_center/sensor.py"
with urllib.request.urlopen(sensor_url, timeout=30) as r:
    sensor_text = r.read().decode("utf-8")
if "sbc5_ai_thermal_shadow_delta" not in sensor_text or "sbc5_ai_thermal_shadow_state" not in sensor_text:
    raise SystemExit("canonical 3.1.5 Shadow Assist sensors not found")
(COMP / "sensor.py").write_text(sensor_text, encoding="utf-8")

manifest = COMP / "manifest.json"
data = json.loads(manifest.read_text(encoding="utf-8"))
data["version"] = "3.1.5"
manifest.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

const = COMP / "const.py"
text = const.read_text(encoding="utf-8")
if 'APP_VERSION = "3.1.4"' not in text:
    raise SystemExit("unexpected APP_VERSION in const.py")
const.write_text(text.replace('APP_VERSION = "3.1.4"', 'APP_VERSION = "3.1.5"', 1), encoding="utf-8")

readme = ROOT / "README.md"
text = readme.read_text(encoding="utf-8")
text = text.replace("**Version 3.1.4 · HACS-ready", "**Version 3.1.5 · HACS-ready", 1)
text = text.replace("### Current release — 3.1.4", "### Current release — 3.1.5", 1)
old_en = "Version 3.1.4 is aligned with SBC5 Control Center App/runtime 3.1.4. The integration exposes native AI Thermal Predictor forecast and quality diagnostics, including MAE, last error, confidence, quality state, temperature slope, validated samples and data age. Raspberry Pi host MAC/interface diagnostics remain available for Device Registry verification. Adaptive PWM and AI Cooling control behavior is unchanged."
new_en = "Version 3.1.5 is aligned with SBC5 Control Center App/runtime 3.1.5. The integration adds native Thermal Predictor Shadow Assist telemetry: suggested PWM delta, hypothetical PWM, activation-gate state, decision reason and weighted forecast. Shadow Assist remains telemetry-only with `control_output_enabled=false`; Adaptive PWM and AI Cooling remain authoritative."
text = text.replace(old_en, new_en, 1)
text = text.replace("### Aktualne wydanie — 3.1.4", "### Aktualne wydanie — 3.1.5", 1)
old_pl = "Wersja 3.1.4 jest zgodna z aplikacją/runtime SBC5 Control Center 3.1.4. Integracja udostępnia natywne sensory prognozy i jakości AI Thermal Predictor, w tym MAE, ostatni błąd, confidence, stan jakości, trend temperatury, liczbę zweryfikowanych prognoz i wiek danych. Diagnostyka fizycznego MAC/interfejsu Raspberry Pi pozostaje dostępna do weryfikacji Device Registry. Sterowanie Adaptive PWM i AI Cooling pozostaje bez zmian."
new_pl = "Wersja 3.1.5 jest zgodna z aplikacją/runtime SBC5 Control Center 3.1.5. Integracja dodaje natywną telemetrię Thermal Predictor Shadow Assist: sugerowaną deltę PWM, hipotetyczny PWM, stan bramki aktywacji, powód decyzji i prognozę ważoną. Shadow Assist pozostaje wyłącznie telemetrią z `control_output_enabled=false`; Adaptive PWM i AI Cooling pozostają nadrzędne."
text = text.replace(old_pl, new_pl, 1)
readme.write_text(text, encoding="utf-8")

changelog = ROOT / "CHANGELOG.md"
entry = """## 3.1.5 — 2026-10-27

### English
- Added native Thermal Predictor Shadow Assist sensors for suggested PWM delta, hypothetical PWM, activation-gate state, decision reason and weighted forecast.
- Aligned HACS integration metadata with App/runtime 3.1.5.
- No new polling loop; Shadow Assist reuses the existing 15-second coordinator and AI runtime relay.
- Shadow Assist is telemetry-only (`control_output_enabled=false`); Adaptive PWM and AI Cooling remain authoritative.
- Update through HACS. Restart Home Assistant only if HACS requests it. No Raspberry Pi host restart is required.

### Polski
- Dodano natywne sensory Thermal Predictor Shadow Assist: sugerowana delta PWM, hipotetyczny PWM, stan bramki aktywacji, powód decyzji i prognoza ważona.
- Wyrównano metadane integracji HACS z App/runtime 3.1.5.
- Bez nowej pętli pollingowej; Shadow Assist korzysta z istniejącego 15-sekundowego koordynatora i relay AI runtime.
- Shadow Assist jest wyłącznie telemetrią (`control_output_enabled=false`); Adaptive PWM i AI Cooling pozostają nadrzędne.
- Aktualizuj przez HACS. Home Assistant uruchom ponownie tylko wtedy, gdy HACS tego zażąda. Restart hosta Raspberry Pi nie jest wymagany.

"""
changelog.write_text(entry + changelog.read_text(encoding="utf-8"), encoding="utf-8")

notes = ROOT / "RELEASE_NOTES_3.1.5.md"
notes.write_text("""# SBC5 Control Center Integration 3.1.5

## English
- Native AI Thermal Predictor Shadow Assist telemetry for App/runtime 3.1.5.
- Suggested PWM delta and hypothetical PWM are bounded diagnostics only; `control_output_enabled=false`.
- Activation gate reports Predictor quality/confidence/MAE/sample readiness through the existing runtime relay.
- No additional polling. Adaptive PWM and AI Cooling remain authoritative.
- Update through HACS; restart Home Assistant only if HACS requests it. No Raspberry Pi host restart.

## Polski
- Natywna telemetria AI Thermal Predictor Shadow Assist dla App/runtime 3.1.5.
- Sugerowana delta PWM i hipotetyczny PWM są wyłącznie ograniczoną diagnostyką; `control_output_enabled=false`.
- Bramka aktywacji raportuje gotowość jakości/confidence/MAE/liczby próbek Predictora przez istniejący relay runtime.
- Bez dodatkowego pollingu. Adaptive PWM i AI Cooling pozostają nadrzędne.
- Aktualizacja przez HACS; restart Home Assistant tylko jeśli HACS tego zażąda. Bez restartu hosta Raspberry Pi.
""", encoding="utf-8")

print("Prepared HACS Integration 3.1.5 Shadow Assist parity")
