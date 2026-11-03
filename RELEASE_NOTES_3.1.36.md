# SBC5 Control Center Integration 3.1.36

## English
- Addresses all HACS reviewer feedback: non-blocking Repairs marker I/O, correct integration documentation/issues links and `template`-scoped AI Thermal Predictor entity migration.
- Fixes an additional collision case in native entity-ID canonicalization so SBC5 records are not deleted when another integration owns the target ID.
- Adds regression tests, consistent `APP_VERSION` and manifest metadata, and clearer bilingual HACS documentation.
- No change to AI Cooling, Adaptive PWM, physical fan control or telemetry polling.

## Polski
- Łączy poprawki z przeglądu HACS: operacje plikowe Repairs w executorze, właściwe linki dokumentacji i ograniczenie migracji czujników AI Thermal Predictor do platformy `template`.
- Naprawia dodatkową kolizję podczas kanonizacji ID encji, chroniąc natywne wpisy SBC5, gdy docelowy ID zajmuje obca integracja.
- Dodaje testy regresyjne, spójne wersjonowanie i przejrzysty opis HACS w PL/EN.
- Bez zmian AI Cooling, Adaptive PWM, fizycznego sterowania wentylatorem i odpytywania.
