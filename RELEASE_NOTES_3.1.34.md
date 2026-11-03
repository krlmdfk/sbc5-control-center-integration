# SBC5 Control Center Integration 3.1.34

## English

- Fixes the HACS review finding: AI Thermal Predictor entity migration removes only legacy `template` sensor registry entries with an exact match in `PREDICTOR_NATIVE_IDS`.
- Protects entities of other platforms/integrations from unintended removal even if their unique IDs collide.
- Keeps native sensors, telemetry polling, AI Cooling and physical fan control unchanged.

## Polski

- Poprawka po przeglądzie HACS: migracja encji AI Thermal Predictor usuwa wyłącznie stare wpisy czujników platformy `template` z dokładnie zgodnym identyfikatorem z `PREDICTOR_NATIVE_IDS`.
- Chroni encje innych platform i integracji przed przypadkowym usunięciem, nawet przy zbieżności `unique_id`.
- Bez zmian w natywnych czujnikach, odpytywaniu telemetrii, AI Cooling i fizycznym sterowaniu wentylatorem.
