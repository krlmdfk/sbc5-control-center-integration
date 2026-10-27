# SBC5 Control Center Integration 3.1.7

> Version parity with SBC5 Control Center App/runtime 3.1.7.

## English

### Highlights
- Aligns the HACS integration with SBC5 Control Center App/runtime 3.1.7.
- App/runtime 3.1.7 uses bucket-aware AI Cooling qualification so medium/high workloads can accumulate qualified learning samples without inheriting stale low-load qualification windows.
- App/runtime 3.1.7 includes the upward-only Adaptive PWM thermal fast path: up to +8 pp/cycle from target +5°C and +12 pp/cycle from target +7°C.
- Existing AI Thermal Predictor forecasts, MAE/quality diagnostics and Shadow Assist telemetry remain available through the same coordinator.
- The integration adds no new polling loop and does not take ownership of physical PWM control.

### Upgrade
Update the integration through HACS. Restart Home Assistant only if HACS requests it. A Raspberry Pi host reboot is not required by this integration update.

## Polski

### Najważniejsze
- Wyrównuje integrację HACS z aplikacją/runtime SBC5 Control Center 3.1.7.
- App/runtime 3.1.7 używa kwalifikacji AI Cooling zależnej od bucketa, dzięki czemu obciążenia medium/high mogą zbierać próbki jakościowe bez dziedziczenia starych okien kwalifikacji z low.
- App/runtime 3.1.7 zawiera thermal fast path Adaptive PWM wyłącznie w górę: do +8 pp/cykl od target +5°C i +12 pp/cykl od target +7°C.
- Istniejące prognozy AI Thermal Predictor, diagnostyka MAE/jakości oraz telemetria Shadow Assist pozostają dostępne przez ten sam koordynator.
- Integracja nie dodaje nowej pętli pollingu i nie przejmuje fizycznego sterowania PWM.

### Aktualizacja
Aktualizuj integrację przez HACS. Uruchom ponownie Home Assistant tylko wtedy, gdy HACS tego zażąda. Ta aktualizacja integracji nie wymaga restartu hosta Raspberry Pi.
