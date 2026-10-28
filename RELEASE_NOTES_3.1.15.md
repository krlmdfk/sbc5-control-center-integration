# SBC5 Control Center Integration 3.1.15

## English

This release keeps the HACS integration aligned with SBC5 Control Center 3.1.15.

- Version metadata is synchronized with App/runtime 3.1.15.
- No sensor, coordinator or polling cadence changes are introduced by this integration release.
- App/runtime 3.1.15 fixes Card UI diagnostics for sparse AI workload buckets: direct confidence is no longer substituted with effective/general confidence, and missing direct PWM prediction is rendered explicitly as unavailable.
- The integration continues to expose the existing SBC5 relay/runtime data to Home Assistant without additional polling.
- No Raspberry Pi host restart is required by this integration release. Restart Home Assistant after the HACS update so Core loads integration 3.1.15.

## Polski

To wydanie synchronizuje integrację HACS z SBC5 Control Center 3.1.15.

- Metadane wersji zostały wyrównane z App/runtime 3.1.15.
- To wydanie integracji nie zmienia sensorów, koordynatora ani częstotliwości pollingu.
- App/runtime 3.1.15 naprawia diagnostykę Card UI dla rzadkich bucketów AI: pewność direct nie jest już zastępowana wartością effective/ogólną, a brak bezpośredniej predykcji PWM jest jednoznacznie prezentowany jako niedostępny.
- Integracja nadal udostępnia istniejące dane relay/runtime SBC5 do Home Assistant bez dodatkowego pollingu.
- Restart hosta Raspberry Pi nie jest wymagany. Po aktualizacji przez HACS uruchom ponownie Home Assistant, aby Core wczytał integrację 3.1.15.
