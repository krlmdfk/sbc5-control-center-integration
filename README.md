# SBC5 Control Center — Home Assistant Integration

[![HACS validation](https://github.com/krlmdfk/sbc5-control-center-integration/actions/workflows/validate.yml/badge.svg)](https://github.com/krlmdfk/sbc5-control-center-integration/actions/workflows/validate.yml)

**Version 2.8.25 · HACS-ready · Home Assistant ≥ 2026.10.1 · Apache-2.0**

**English** · [Polski](#polski)

## English

Native Home Assistant companion integration for **SBC5 Control Center** on Raspberry Pi 5.

> **Important:** this repository contains the Home Assistant integration only. The **SBC5 Control Center App/runtime must also be installed and running**.

Main project and required App/runtime: **[krlmdfk/sbc5-control-center](https://github.com/krlmdfk/sbc5-control-center)**

This integration exposes SBC5 telemetry and control state natively in Home Assistant, including device information, diagnostics, update state and Restart Manager entities.

### Repository relationship

| Repository | Purpose |
|---|---|
| **[sbc5-control-center](https://github.com/krlmdfk/sbc5-control-center)** | Main SBC5 project and required App/runtime. |
| **[sbc5-control-center-integration](https://github.com/krlmdfk/sbc5-control-center-integration)** | HACS-managed Home Assistant integration. |

### Requirements

- Raspberry Pi 5 with the SBC5 Control Center App/runtime installed and running;
- Home Assistant Core 2026.10.1 or newer;
- HACS for HACS-managed installation.

Without the SBC5 Control Center App/runtime, this integration has no SBC5 host telemetry source to read.

### Install with HACS

1. Open **HACS**.
2. Open **⋮ → Custom repositories**.
3. Add `https://github.com/krlmdfk/sbc5-control-center-integration`.
4. Select category **Integration**.
5. Install **SBC5 Control Center**.
6. Restart Home Assistant when HACS asks for it.
7. Open **Settings → Devices & services** and add **SBC5 Control Center** if it is not already present.

### HACS ownership protection

The integration contains the `.hacs_managed` marker. SBC5 Control Center detects this marker and leaves `custom_components/sbc5_control_center` under HACS ownership, preventing the App from overwriting or downgrading a HACS-managed copy.

### Validation

Every push and pull request runs:

- HACS repository validation;
- Home Assistant Hassfest validation;
- Python compilation and JSON validation.

### Support

Integration/HACS issues: **[sbc5-control-center-integration/issues](https://github.com/krlmdfk/sbc5-control-center-integration/issues)**

App/runtime, cooling, host access, boot configuration and Raspberry Pi diagnostics: **[sbc5-control-center/issues](https://github.com/krlmdfk/sbc5-control-center/issues)**

### License

Apache License 2.0.

SBC5 Control Center is an independent project and is not endorsed by Raspberry Pi Ltd., Home Assistant, or the Open Home Foundation.

---

## Polski

Natywna integracja towarzysząca Home Assistant dla **SBC5 Control Center** na Raspberry Pi 5.

> **Ważne:** to repozytorium zawiera wyłącznie integrację Home Assistant. **Aplikacja/runtime SBC5 Control Center musi być również zainstalowana i uruchomiona**.

Główny projekt i wymagana aplikacja/runtime: **[krlmdfk/sbc5-control-center](https://github.com/krlmdfk/sbc5-control-center)**

Integracja udostępnia natywnie w Home Assistant telemetrię i stan sterowania SBC5, w tym informacje o urządzeniu, diagnostykę, stan aktualizacji oraz encje Restart Managera.

### Relacja repozytoriów

| Repozytorium | Przeznaczenie |
|---|---|
| **[sbc5-control-center](https://github.com/krlmdfk/sbc5-control-center)** | Główny projekt SBC5 oraz wymagana aplikacja/runtime. |
| **[sbc5-control-center-integration](https://github.com/krlmdfk/sbc5-control-center-integration)** | Integracja Home Assistant zarządzana przez HACS. |

### Wymagania

- Raspberry Pi 5 z zainstalowaną i uruchomioną aplikacją/runtime SBC5 Control Center;
- Home Assistant Core 2026.10.1 lub nowszy;
- HACS do instalacji zarządzanej przez HACS.

Bez aplikacji/runtime SBC5 Control Center integracja nie ma źródła telemetrii hosta SBC5.

### Instalacja przez HACS

1. Otwórz **HACS**.
2. Otwórz **⋮ → Niestandardowe repozytoria**.
3. Dodaj `https://github.com/krlmdfk/sbc5-control-center-integration`.
4. Wybierz kategorię **Integracja**.
5. Zainstaluj **SBC5 Control Center**.
6. Uruchom ponownie Home Assistant, gdy HACS o to poprosi.
7. Otwórz **Ustawienia → Urządzenia i usługi** i dodaj **SBC5 Control Center**, jeśli integracja nie została jeszcze skonfigurowana.

### Ochrona własności HACS

Integracja zawiera znacznik `.hacs_managed`. SBC5 Control Center wykrywa ten znacznik i pozostawia `custom_components/sbc5_control_center` pod zarządzaniem HACS, dzięki czemu aplikacja nie nadpisuje ani nie obniża wersji kopii zarządzanej przez HACS.

### Walidacja

Każdy push i pull request uruchamia:

- walidację repozytorium HACS;
- walidację Home Assistant Hassfest;
- kompilację Pythona i walidację JSON.

### Wsparcie

Problemy integracji/HACS: **[sbc5-control-center-integration/issues](https://github.com/krlmdfk/sbc5-control-center-integration/issues)**

Problemy aplikacji/runtime, chłodzenia, dostępu do hosta, konfiguracji boot oraz diagnostyki Raspberry Pi: **[sbc5-control-center/issues](https://github.com/krlmdfk/sbc5-control-center/issues)**

### Licencja

Apache License 2.0.

SBC5 Control Center jest niezależnym projektem i nie jest oficjalnie wspierany ani zatwierdzony przez Raspberry Pi Ltd., Home Assistant ani Open Home Foundation.
