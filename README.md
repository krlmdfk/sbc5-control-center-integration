[![Validate](https://github.com/krlmdfk/sbc5-control-center-integration/actions/workflows/validate.yml/badge.svg)](https://github.com/krlmdfk/sbc5-control-center-integration/actions/workflows/validate.yml)
[![Release](https://img.shields.io/github/v/release/krlmdfk/sbc5-control-center-integration?display_name=tag)](https://github.com/krlmdfk/sbc5-control-center-integration/releases)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)

# SBC5 Control Center — Home Assistant Integration

**English** · [Polski](#polski)

> HACS-managed Home Assistant companion integration for SBC5 Control Center on Raspberry Pi 5.

**Version 2.8.25 · Home Assistant ≥ 2026.10.1 · Apache-2.0**

## English

### Important requirement

This repository contains the **Home Assistant integration only**. It is **not a standalone replacement for the SBC5 Control Center App**.

> **The SBC5 Control Center App/runtime must be installed and running.**

Main project and App releases:
**[krlmdfk/sbc5-control-center](https://github.com/krlmdfk/sbc5-control-center)**

The App provides Raspberry Pi 5 host telemetry and control services. This HACS integration exposes that data natively in Home Assistant through entities, device information, diagnostics and update/restart state.

### Repository relationship

| Repository | Purpose |
|---|---|
| **[sbc5-control-center](https://github.com/krlmdfk/sbc5-control-center)** | Main project and required App/runtime. |
| **[sbc5-control-center-integration](https://github.com/krlmdfk/sbc5-control-center-integration)** | This repository: HACS-managed Home Assistant integration. |

### What the integration provides

- native SBC5 device registration in Home Assistant;
- Raspberry Pi 5 model, revision, serial, MAC and SBC5 version information;
- system, cooling, power, storage, network and firmware entities;
- CPU0–CPU3 frequency and usage entities;
- update and Restart Manager state;
- diagnostics used by SBC5 Lovelace cards.

### Install with HACS

1. Install and start the **SBC5 Control Center App/runtime** from the main project.
2. Open **HACS → ⋮ → Custom repositories**.
3. Add `https://github.com/krlmdfk/sbc5-control-center-integration` as **Integration**.
4. Install **SBC5 Control Center**.
5. Restart **Home Assistant** when requested. A Raspberry Pi reboot is not required just for the HACS integration.
6. Open **Settings → Devices & services** and use the existing SBC5 Control Center entry or add it if it is not present.

### HACS ownership protection

The integration contains the `.hacs_managed` marker. SBC5 Control Center detects this marker and leaves `custom_components/sbc5_control_center` under HACS ownership, preventing the App from overwriting or downgrading a HACS-managed copy.

### Validation

Every push and pull request runs HACS repository validation, Home Assistant Hassfest and syntax/JSON checks.

### Support

- Integration/HACS issues: https://github.com/krlmdfk/sbc5-control-center-integration/issues
- App/runtime, cooling, boot configuration and host issues: https://github.com/krlmdfk/sbc5-control-center/issues

---

<a id="polski"></a>

## Polski

> Zarządzana przez HACS integracja towarzysząca Home Assistant dla SBC5 Control Center na Raspberry Pi 5.

**Wersja 2.8.25 · Home Assistant ≥ 2026.10.1 · Apache-2.0**

### Ważne wymaganie

To repozytorium zawiera **wyłącznie integrację Home Assistant**. Nie zastępuje ono samodzielnie aplikacji SBC5 Control Center.

> **Aplikacja/runtime SBC5 Control Center musi być zainstalowana i uruchomiona.**

Główny projekt i wydania aplikacji:
**[krlmdfk/sbc5-control-center](https://github.com/krlmdfk/sbc5-control-center)**

Aplikacja dostarcza telemetrię hosta Raspberry Pi 5 i usługi sterujące. Integracja HACS udostępnia te dane natywnie w Home Assistant jako encje, informacje o urządzeniu, diagnostykę oraz stan aktualizacji/restartów.

### Powiązanie repozytoriów

| Repozytorium | Przeznaczenie |
|---|---|
| **[sbc5-control-center](https://github.com/krlmdfk/sbc5-control-center)** | Główny projekt i wymagana aplikacja/runtime. |
| **[sbc5-control-center-integration](https://github.com/krlmdfk/sbc5-control-center-integration)** | To repozytorium: integracja Home Assistant zarządzana przez HACS. |

### Co udostępnia integracja

- natywne urządzenie SBC5 w Home Assistant;
- model Raspberry Pi 5, rewizję, numer seryjny, MAC i wersję SBC5;
- encje systemowe, chłodzenia, zasilania, storage, sieci i firmware;
- częstotliwość i użycie CPU0–CPU3;
- stan aktualizacji i Restart Managera;
- diagnostykę używaną przez karty Lovelace SBC5.

### Instalacja przez HACS

1. Zainstaluj i uruchom **aplikację/runtime SBC5 Control Center** z głównego repozytorium.
2. Otwórz **HACS → ⋮ → Niestandardowe repozytoria**.
3. Dodaj `https://github.com/krlmdfk/sbc5-control-center-integration` jako **Integracja**.
4. Zainstaluj **SBC5 Control Center**.
5. Uruchom ponownie **Home Assistant**, gdy HACS o to poprosi. Sama integracja HACS nie wymaga restartu Raspberry Pi.
6. Otwórz **Ustawienia → Urządzenia i usługi** i użyj istniejącego wpisu SBC5 Control Center albo dodaj go, jeśli go nie ma.

### Ochrona własności HACS

Integracja zawiera marker `.hacs_managed`. SBC5 Control Center wykrywa ten marker i pozostawia `custom_components/sbc5_control_center` pod kontrolą HACS, dzięki czemu aplikacja nie nadpisuje ani nie cofa wersji integracji zarządzanej przez HACS.

### Walidacja

Każdy push i pull request uruchamia walidację repozytorium HACS, Home Assistant Hassfest oraz kontrolę składni/JSON.

### Wsparcie

- Problemy integracji/HACS: https://github.com/krlmdfk/sbc5-control-center-integration/issues
- Problemy aplikacji/runtime, chłodzenia, konfiguracji boot i hosta: https://github.com/krlmdfk/sbc5-control-center/issues

SBC5 Control Center jest niezależnym projektem i nie jest sponsorowany ani zatwierdzony przez Raspberry Pi Ltd., Home Assistant ani Open Home Foundation.
