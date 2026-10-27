# SBC5 Control Center Integration 3.1.2

## English

### Highlights

- AI Thermal Predictor is now exposed as native Home Assistant sensors for +30 s, +60 s, +120 s and predictor confidence.
- Existing Predictor entity IDs are migrated from the 3.1.1 package templates, preserving the canonical IDs used by dashboards and Recorder.
- Device Registry network identity is reconciled to one physical Raspberry Pi host MAC, removing accumulated container/virtual MAC connections.
- No extra high-frequency polling is introduced; the integration reuses the existing coordinator and AI runtime relay.

### Upgrade notes

- Update SBC5 Control Center App/runtime to 3.1.2 through the Home Assistant Apps Store / configured SBC5 repository.
- Update this companion integration to 3.1.2 through HACS.
- Restart Home Assistant only when requested by HACS.
- No Raspberry Pi host restart is required by this release.

## Polski

### Najważniejsze zmiany

- AI Thermal Predictor jest teraz udostępniany jako natywne sensory Home Assistant dla +30 s, +60 s, +120 s oraz pewności predyktora.
- Dotychczasowe identyfikatory encji Predictora są migrowane z template package 3.1.1 z zachowaniem kanonicznych ID używanych przez dashboard i Recorder.
- Tożsamość sieciowa Device Registry jest uzgadniana do jednego fizycznego adresu MAC hosta Raspberry Pi, a nagromadzone adresy kontenerowe/wirtualne są usuwane.
- Nie dodano dodatkowego szybkiego odpytywania; integracja wykorzystuje istniejący koordynator i przekaźnik AI runtime.

### Informacje o aktualizacji

- App/runtime SBC5 Control Center zaktualizuj do 3.1.2 przez Sklep Apps Home Assistant / skonfigurowane repozytorium SBC5.
- Integrację towarzyszącą zaktualizuj do 3.1.2 przez HACS.
- Home Assistant uruchom ponownie tylko wtedy, gdy HACS tego zażąda.
- To wydanie nie wymaga restartu hosta Raspberry Pi.
