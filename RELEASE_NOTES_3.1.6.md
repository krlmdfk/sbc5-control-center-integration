# SBC5 Control Center Integration 3.1.6

> Version parity for AI Thermal Predictor v2 accuracy calibration.

## English

### Highlights
- Aligns the HACS integration with SBC5 Control Center App/runtime 3.1.6.
- The App/runtime now uses Thermal Predictor v2 with horizon-specific target anchoring and bounded signed online bias calibration.
- Existing forecast, MAE/quality and Shadow Assist native entities remain available through the same coordinator.
- No new polling loop and no physical PWM control path is added by the integration.
- Shadow Assist remains telemetry-only (`control_output_enabled=false`).

### Upgrade
Update the integration through HACS. Restart Home Assistant only if HACS requests it. A Raspberry Pi host reboot is not required.

## Polski

### Najważniejsze
- Wyrównuje integrację HACS z App/runtime SBC5 Control Center 3.1.6.
- App/runtime używa teraz Thermal Predictor v2 z zależnym od horyzontu dociąganiem do celu i ograniczoną znakowaną korektą błędu online.
- Istniejące natywne encje prognoz, MAE/jakości i Shadow Assist pozostają dostępne przez ten sam koordynator.
- Integracja nie dodaje nowej pętli pollingu ani fizycznej ścieżki sterowania PWM.
- Shadow Assist pozostaje wyłącznie telemetryczny (`control_output_enabled=false`).

### Aktualizacja
Aktualizuj integrację przez HACS. Uruchom ponownie Home Assistant tylko wtedy, gdy HACS tego zażąda. Restart hosta Raspberry Pi nie jest wymagany.
