<p align="center">
  <a href="https://github.com/krlmdfk/sbc5-control-center">
    <img src="https://raw.githubusercontent.com/krlmdfk/sbc5-control-center/main/branding/logo-512.png" alt="SBC5 Control Center" width="180">
  </a>
</p>

<h1 align="center">SBC5 Control Center — Home Assistant Integration</h1>

<p align="center">
  Native HACS companion integration for SBC5 Control Center on Raspberry Pi 5.<br>
  Natywna integracja HACS dla SBC5 Control Center na Raspberry Pi 5.
</p>

<p align="center">
  <a href="https://github.com/krlmdfk/sbc5-control-center-integration/actions/workflows/validate.yml"><img src="https://github.com/krlmdfk/sbc5-control-center-integration/actions/workflows/validate.yml/badge.svg" alt="Validate"></a>
  <a href="https://github.com/krlmdfk/sbc5-control-center-integration/releases"><img src="https://img.shields.io/github/v/release/krlmdfk/sbc5-control-center-integration?display_name=tag" alt="Release"></a>
  <img src="https://img.shields.io/badge/HACS-Custom%20Integration-41BDF5" alt="HACS">
  <img src="https://img.shields.io/badge/Home%20Assistant-%3E%3D%202026.10.1-18BCF2" alt="Home Assistant">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-Apache--2.0-blue.svg" alt="License"></a>
</p>

> [!IMPORTANT]
> **SBC5 Control Center App/runtime is required.** This repository contains only the Home Assistant integration. The App/runtime provides Raspberry Pi 5 host telemetry and control services.
>
> **Wymagana jest aplikacja/runtime SBC5 Control Center.** To repozytorium zawiera wyłącznie integrację Home Assistant. Aplikacja/runtime dostarcza telemetrię hosta Raspberry Pi 5 oraz usługi sterujące.

**Version 3.0.1 · HACS-ready · Home Assistant ≥ 2026.10.1 · Apache-2.0**

[Main App](https://github.com/krlmdfk/sbc5-control-center) · [Documentation](https://krlmdfk.github.io/sbc5-control-center/) · [Releases](https://github.com/krlmdfk/sbc5-control-center-integration/releases) · [Issues](https://github.com/krlmdfk/sbc5-control-center-integration/issues)

---

## English

### Overview

SBC5 Control Center Integration exposes SBC5 runtime data as native Home Assistant entities and device diagnostics. It is the HACS-managed companion to the main SBC5 Control Center App/runtime.

### Current release — 3.0.0

Hybrid Rust Core generation with the proven compatibility/control plane retained for safety. The integration is aligned with App 3.0.0, preserved-state migration, Adaptive PWM/AI Cooling recovery, CPU/GPU profile reconciliation, Card UI synchronization and the verified Raspberry Pi 5 release gate.

### Capabilities

| Area | Integration capability |
|---|---|
| Device | Native Home Assistant device entry and diagnostic metadata |
| Telemetry | Raspberry Pi 5 CPU, temperature, fan/PWM and system state |
| Cooling | SBC5 cooling, controller, Adaptive PWM and AI Cooling state |
| Profiles | CPU/GPU profile state and diagnostics |
| Updates | App/integration version and update visibility |
| Restart Manager | Native restart-requirement and state entities |
| Diagnostics | Troubleshooting data without replacing App/runtime host diagnostics |

### Requirements

- Raspberry Pi 5
- SBC5 Control Center App/runtime installed and running
- Home Assistant Core 2026.10.1 or newer
- HACS for HACS-managed installation

### Install / upgrade with HACS

1. Install and start the SBC5 Control Center App/runtime from the main repository.
2. Open **HACS → Integrations**.
3. Add `https://github.com/krlmdfk/sbc5-control-center-integration` as a custom **Integration** repository if needed.
4. Install or update **SBC5 Control Center**.
5. Restart Home Assistant when requested by HACS.
6. Open **Settings → Devices & services** and add SBC5 Control Center if it is not already configured.

The integration update itself does not require a Raspberry Pi host reboot. A Home Assistant restart may be requested by HACS after updating the custom integration.

### HACS ownership protection

The integration contains `.hacs_managed`. The App detects this marker and does not overwrite or downgrade the HACS-managed copy.

---

## Polski

### Przegląd

SBC5 Control Center Integration udostępnia dane runtime SBC5 jako natywne encje Home Assistant oraz diagnostykę urządzenia. Jest to zarządzana przez HACS integracja towarzysząca głównej aplikacji/runtime SBC5 Control Center.

### Aktualne wydanie — 3.0.0

Generacja z hybrydowym Rust Core i zachowaną, sprawdzoną warstwą sterowania bezpieczeństwem. Integracja jest wyrównana z aplikacją 3.0.0, migracją z zachowaniem stanu, odzyskiwaniem Adaptive PWM/AI Cooling, uzgadnianiem profili CPU/GPU, synchronizacją Card UI oraz zweryfikowaną bramką wydania na Raspberry Pi 5.

### Możliwości

| Obszar | Możliwości integracji |
|---|---|
| Urządzenie | Natywny wpis urządzenia Home Assistant i metadane diagnostyczne |
| Telemetria | CPU Raspberry Pi 5, temperatura, wentylator/PWM i stan systemu |
| Chłodzenie | Stan SBC5 Cooling, regulatora, Adaptive PWM i AI Cooling |
| Profile | Stan profili CPU/GPU i diagnostyka |
| Aktualizacje | Widoczność wersji i stanu aktualizacji aplikacji/integracji |
| Restart Manager | Natywne encje wymaganego restartu i jego stanu |
| Diagnostyka | Dane troubleshooting bez zastępowania diagnostyki hosta App/runtime |

### Wymagania

- Raspberry Pi 5
- zainstalowana i uruchomiona aplikacja/runtime SBC5 Control Center
- Home Assistant Core 2026.10.1 lub nowszy
- HACS do instalacji zarządzanej przez HACS

### Instalacja / aktualizacja przez HACS

1. Zainstaluj i uruchom aplikację/runtime SBC5 Control Center z głównego repozytorium.
2. Otwórz **HACS → Integrations**.
3. W razie potrzeby dodaj `https://github.com/krlmdfk/sbc5-control-center-integration` jako niestandardowe repozytorium typu **Integration**.
4. Zainstaluj lub zaktualizuj **SBC5 Control Center**.
5. Uruchom ponownie Home Assistant, gdy HACS tego zażąda.
6. Otwórz **Ustawienia → Urządzenia i usługi** i dodaj SBC5 Control Center, jeśli nie jest jeszcze skonfigurowany.

Sama aktualizacja integracji nie wymaga restartu hosta Raspberry Pi. Po aktualizacji niestandardowej integracji HACS może poprosić o restart Home Assistant.

### Ochrona własności HACS

Integracja zawiera znacznik `.hacs_managed`. Aplikacja wykrywa ten znacznik i nie nadpisuje ani nie obniża wersji kopii zarządzanej przez HACS.

### License / Licencja

Apache License 2.0. SBC5 Control Center is an independent project and is not endorsed by Raspberry Pi Ltd., Home Assistant or the Open Home Foundation.
