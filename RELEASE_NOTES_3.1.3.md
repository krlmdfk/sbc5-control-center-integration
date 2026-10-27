# SBC5 Control Center Integration 3.1.3

## English

### Highlights
- Native AI Thermal Predictor quality diagnostics: average MAE, MAE and last error for +30 s/+60 s/+120 s, temperature slope, validated forecasts and data age.
- Explicit physical Raspberry Pi host MAC and interface diagnostics make Device Registry cleanup verifiable.
- No additional high-frequency polling; all diagnostics reuse the existing 15-second coordinator and AI runtime relay.

### Upgrade notes
- Update SBC5 Control Center App/runtime to 3.1.3 through the Home Assistant Apps Store / configured SBC5 repository.
- Update this companion integration through HACS.
- Restart Home Assistant only when HACS requests it.
- No Raspberry Pi host restart is required by this release.

## Polski

### Najważniejsze zmiany
- Natywna diagnostyka jakości AI Thermal Predictor: średnie MAE, MAE i ostatni błąd dla +30 s/+60 s/+120 s, trend temperatury, liczba zweryfikowanych prognoz i wiek danych.
- Jawne dane fizycznego MAC i interfejsu Raspberry Pi pozwalają zweryfikować porządkowanie Device Registry.
- Bez dodatkowego szybkiego odpytywania; cała diagnostyka wykorzystuje istniejący 15-sekundowy koordynator i relay AI runtime.

### Aktualizacja
- App/runtime SBC5 Control Center zaktualizuj do 3.1.3 przez Sklep Apps Home Assistant / skonfigurowane repozytorium SBC5.
- Integrację towarzyszącą aktualizuj przez HACS.
- Home Assistant uruchom ponownie tylko wtedy, gdy HACS tego zażąda.
- To wydanie nie wymaga restartu hosta Raspberry Pi.
