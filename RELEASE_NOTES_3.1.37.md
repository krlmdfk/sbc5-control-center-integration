# SBC5 Control Center Integration 3.1.37

## English

- Companion HACS release aligned with SBC5 Control Center App/runtime 3.1.37.
- The App resets short-term Thermal Predictor smoothing and hot/cool confirmations after setpoint changes, workload-regime changes, mode changes or gaps in telemetry.
- Existing HACS entity schemas, polling cadence, registry-migration protections and Repairs behavior remain unchanged.
- Restart Home Assistant when requested by HACS after updating this integration; no Raspberry Pi host restart is required by the integration alone.

## Polski

- Wydanie integracji HACS zgodne z aplikacją/runtime SBC5 Control Center 3.1.37.
- Aplikacja resetuje krótkoterminowe wygładzanie prognoz Thermal Predictora i potwierdzenia kierunku po zmianie temperatury docelowej, trybu, zakresu obciążenia lub przerwie w danych.
- Bez zmian schematu encji HACS, odpytywania, zabezpieczeń migracji encji oraz przepływu Repairs.
- Po aktualizacji integracji uruchom ponownie Home Assistant, jeśli HACS o to poprosi; restart hosta Raspberry Pi nie jest wymagany przez samą integrację.
