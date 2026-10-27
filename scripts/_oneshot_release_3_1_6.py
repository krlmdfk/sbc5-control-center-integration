#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]

# manifest
p = ROOT / 'custom_components/sbc5_control_center/manifest.json'
data = json.loads(p.read_text(encoding='utf-8'))
data['version'] = '3.1.6'
p.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

# const
p = ROOT / 'custom_components/sbc5_control_center/const.py'
text = p.read_text(encoding='utf-8').replace('APP_VERSION = "3.1.5"', 'APP_VERSION = "3.1.6"', 1)
p.write_text(text, encoding='utf-8')

# README current state
p = ROOT / 'README.md'
text = p.read_text(encoding='utf-8')
text = text.replace('**Version 3.1.5 · HACS-ready', '**Version 3.1.6 · HACS-ready', 1)
text = text.replace('### Current release — 3.1.5', '### Current release — 3.1.6', 1)
old = 'Version 3.1.5 is aligned with SBC5 Control Center App/runtime 3.1.5. The integration adds native Thermal Predictor Shadow Assist telemetry: suggested PWM delta, hypothetical PWM, activation-gate state, decision reason and weighted forecast. Shadow Assist remains telemetry-only with `control_output_enabled=false`; Adaptive PWM and AI Cooling remain authoritative.'
new = 'Version 3.1.6 is aligned with SBC5 Control Center App/runtime 3.1.6. The App/runtime uses AI Thermal Predictor v2 with closed-loop target anchoring and bounded per-horizon online bias calibration. The integration continues to expose native forecast, MAE/quality and Shadow Assist telemetry through the existing 15-second coordinator. Shadow Assist remains telemetry-only with `control_output_enabled=false`; Adaptive PWM and AI Cooling remain authoritative.'
if old not in text:
    raise SystemExit('English README release paragraph anchor missing')
text = text.replace(old, new, 1)
text = text.replace('### Aktualne wydanie — 3.1.5', '### Aktualne wydanie — 3.1.6', 1)
old = 'Wersja 3.1.5 jest zgodna z aplikacją/runtime SBC5 Control Center 3.1.5. Integracja dodaje natywną telemetrię Thermal Predictor Shadow Assist: sugerowaną deltę PWM, hipotetyczny PWM, stan bramki aktywacji, powód decyzji i prognozę ważoną. Shadow Assist pozostaje wyłącznie telemetrią z `control_output_enabled=false`; Adaptive PWM i AI Cooling pozostają nadrzędne.'
new = 'Wersja 3.1.6 jest zgodna z aplikacją/runtime SBC5 Control Center 3.1.6. App/runtime używa AI Thermal Predictor v2 z dociąganiem prognozy do celu termicznego i ograniczoną korektą błędu online dla każdego horyzontu. Integracja nadal udostępnia natywne prognozy, MAE/jakość oraz telemetrię Shadow Assist przez istniejący 15-sekundowy koordynator. Shadow Assist pozostaje wyłącznie telemetrią z `control_output_enabled=false`; Adaptive PWM i AI Cooling pozostają nadrzędne.'
if old not in text:
    raise SystemExit('Polish README release paragraph anchor missing')
text = text.replace(old, new, 1)
p.write_text(text, encoding='utf-8')

# CHANGELOG history only
p = ROOT / 'CHANGELOG.md'
text = p.read_text(encoding='utf-8')
entry = '''## 3.1.6 — 2026-10-27\n\n### English\n- Aligned HACS integration metadata with SBC5 Control Center App/runtime 3.1.6.\n- Documented AI Thermal Predictor v2 closed-loop target anchoring and bounded per-horizon online bias calibration delivered by the App/runtime.\n- Preserved existing native forecast, MAE/quality and Shadow Assist entities; no coordinator or polling changes.\n- Shadow Assist remains telemetry-only (`control_output_enabled=false`); Adaptive PWM and AI Cooling remain authoritative.\n- Update through HACS. Restart Home Assistant only if HACS requests it. No Raspberry Pi host restart is required.\n\n### Polski\n- Wyrównano metadane integracji HACS z App/runtime SBC5 Control Center 3.1.6.\n- Udokumentowano AI Thermal Predictor v2 z dociąganiem do celu termicznego i ograniczoną korektą błędu online dla każdego horyzontu realizowaną przez App/runtime.\n- Zachowano istniejące natywne encje prognoz, MAE/jakości i Shadow Assist; bez zmian koordynatora i pollingu.\n- Shadow Assist pozostaje wyłącznie telemetrią (`control_output_enabled=false`); Adaptive PWM i AI Cooling pozostają nadrzędne.\n- Aktualizuj przez HACS. Home Assistant uruchom ponownie tylko wtedy, gdy HACS tego zażąda. Restart hosta Raspberry Pi nie jest wymagany.\n\n'''
if not text.startswith('## 3.1.6'):
    text = entry + text
p.write_text(text, encoding='utf-8')

# Release notes required by auto-release
notes = '''# SBC5 Control Center Integration 3.1.6\n\n> Version parity for AI Thermal Predictor v2 accuracy calibration.\n\n## English\n\n### Highlights\n- Aligns the HACS integration with SBC5 Control Center App/runtime 3.1.6.\n- The App/runtime now uses Thermal Predictor v2 with horizon-specific target anchoring and bounded signed online bias calibration.\n- Existing forecast, MAE/quality and Shadow Assist native entities remain available through the same coordinator.\n- No new polling loop and no physical PWM control path is added by the integration.\n- Shadow Assist remains telemetry-only (`control_output_enabled=false`).\n\n### Upgrade\nUpdate the integration through HACS. Restart Home Assistant only if HACS requests it. A Raspberry Pi host reboot is not required.\n\n## Polski\n\n### Najważniejsze\n- Wyrównuje integrację HACS z App/runtime SBC5 Control Center 3.1.6.\n- App/runtime używa teraz Thermal Predictor v2 z zależnym od horyzontu dociąganiem do celu i ograniczoną znakowaną korektą błędu online.\n- Istniejące natywne encje prognoz, MAE/jakości i Shadow Assist pozostają dostępne przez ten sam koordynator.\n- Integracja nie dodaje nowej pętli pollingu ani fizycznej ścieżki sterowania PWM.\n- Shadow Assist pozostaje wyłącznie telemetryczny (`control_output_enabled=false`).\n\n### Aktualizacja\nAktualizuj integrację przez HACS. Uruchom ponownie Home Assistant tylko wtedy, gdy HACS tego zażąda. Restart hosta Raspberry Pi nie jest wymagany.\n'''
(ROOT / 'RELEASE_NOTES_3.1.6.md').write_text(notes, encoding='utf-8')
print('Prepared HACS integration 3.1.6')
