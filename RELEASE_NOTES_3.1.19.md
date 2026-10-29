# SBC5 Control Center Integration 3.1.19

> Version-parity companion release for SBC5 Control Center 3.1.19.

## English

### Changed

- Synchronizes the HACS integration version with SBC5 Control Center App/runtime 3.1.19.
- Keeps the existing Home Assistant entities, coordinator behavior and polling cadence unchanged.
- Exposes the 3.1.19 runtime telemetry produced by Thermal Predictor v3.1 without adding any new control loop in the integration.

### Runtime note

Thermal Predictor v3.1 is implemented by the SBC5 Control Center App/runtime. It validates +30/+60/+120 s forecasts at their exact due timestamps, adds path-aware context rejection and a robust thermal slope estimator. The predictor remains observe-only and has no physical PWM authority.

A Home Assistant Core restart is recommended after updating the HACS integration. A Raspberry Pi host reboot is not required for this integration update.

## Polski

### Zmieniono

- Zsynchronizowano wersję integracji HACS z aplikacją/runtime SBC5 Control Center 3.1.19.
- Zachowano dotychczasowe encje Home Assistant, działanie koordynatora i częstotliwość odpytywania.
- Integracja udostępnia telemetrię runtime 3.1.19 generowaną przez Thermal Predictor v3.1 bez dodawania nowej pętli sterującej.

### Informacja o runtime

Thermal Predictor v3.1 działa po stronie aplikacji/runtime SBC5 Control Center. Waliduje prognozy +30/+60/+120 s dokładnie dla czasu ich zapadalności, dodaje ścieżkową walidację kontekstu oraz odporny estymator trendu termicznego. Predyktor pozostaje w trybie observe-only i nie steruje fizycznym PWM.

Po aktualizacji integracji HACS zalecany jest restart Home Assistant Core. Restart hosta Raspberry Pi nie jest wymagany dla tej aktualizacji integracji.
