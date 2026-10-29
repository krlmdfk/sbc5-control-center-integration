# SBC5 Control Center Integration 3.1.16

## English

This release keeps the HACS integration aligned with SBC5 Control Center App/runtime 3.1.16.

- Version metadata is synchronized with App/runtime 3.1.16.
- No sensor, coordinator or polling cadence changes are introduced by this integration release.
- App/runtime 3.1.16 introduces Thermal Predictor v3 with regime-aware dual-slope forecasting, per-bucket/per-horizon calibration and context-shift guards.
- Thermal Predictor v3 remains observe-only and does not take physical PWM control authority from Adaptive PWM.
- The integration continues to expose the existing SBC5 relay/runtime data to Home Assistant without additional polling.
- No Raspberry Pi host restart is required. Restart Home Assistant after the HACS update so Core loads integration 3.1.16.

## Polski

To wydanie synchronizuje integrację HACS z SBC5 Control Center App/runtime 3.1.16.

- Metadane wersji zostały wyrównane z App/runtime 3.1.16.
- To wydanie integracji nie zmienia sensorów, koordynatora ani częstotliwości pollingu.
- App/runtime 3.1.16 wprowadza Thermal Predictor v3 z predykcją zależną od reżimu pracy, dwoma trendami temperatury, kalibracją per bucket/per horyzont i zabezpieczeniem context-shift.
- Thermal Predictor v3 pozostaje observe-only i nie przejmuje fizycznego sterowania PWM od Adaptive PWM.
- Integracja nadal udostępnia istniejące dane relay/runtime SBC5 do Home Assistant bez dodatkowego pollingu.
- Restart hosta Raspberry Pi nie jest wymagany. Po aktualizacji przez HACS uruchom ponownie Home Assistant, aby Core wczytał integrację 3.1.16.
