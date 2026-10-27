# SBC5 Control Center Integration 3.0.0

<p align="center">
  <a href="https://github.com/krlmdfk/sbc5-control-center">
    <img src="https://raw.githubusercontent.com/krlmdfk/sbc5-control-center/main/branding/icon-256.png" alt="SBC5 Control Center" width="120">
  </a>
</p>

> Companion Home Assistant integration for SBC5 Control Center on Raspberry Pi 5.  
> Integracja towarzysząca Home Assistant dla SBC5 Control Center na Raspberry Pi 5.

## English

### Highlights

- Aligned with SBC5 Control Center App/runtime 3.0.0 and its hybrid Rust Core generation.
- Preserves the native Home Assistant device, telemetry, diagnostics, update and Restart Manager entities.
- Matches the verified App 3.0.0 preserved-state migration, Adaptive PWM/AI Cooling recovery and CPU/GPU profile reconciliation.
- HACS ownership protection remains active through `.hacs_managed`.

### Requirements

- SBC5 Control Center App/runtime installed and running
- Home Assistant Core >= 2026.10.1
- HACS-managed installation
- Raspberry Pi 5

### Upgrade notes

- Existing integration configuration is preserved during a normal HACS upgrade.
- Restart Home Assistant after the update when requested by HACS.
- The integration update itself does not require a Raspberry Pi host restart.

### Verification

- Repository validation
- Home Assistant Hassfest validation
- Python compilation
- JSON validation
- Version parity with the public SBC5 Control Center 3.0.0 release

---

## Polski

### Najważniejsze zmiany

- Wyrównanie z aplikacją/runtime SBC5 Control Center 3.0.0 i generacją z hybrydowym Rust Core.
- Zachowanie natywnego urządzenia Home Assistant, telemetrii, diagnostyki, aktualizacji i encji Restart Managera.
- Zgodność ze zweryfikowaną migracją stanu aplikacji 3.0.0, odzyskiwaniem Adaptive PWM/AI Cooling oraz uzgadnianiem profili CPU/GPU.
- Ochrona kopii zarządzanej przez HACS pozostaje aktywna dzięki `.hacs_managed`.

### Wymagania

- Zainstalowana i uruchomiona aplikacja/runtime SBC5 Control Center
- Home Assistant Core >= 2026.10.1
- Instalacja zarządzana przez HACS
- Raspberry Pi 5

### Informacje o aktualizacji

- Istniejąca konfiguracja integracji jest zachowywana przy standardowej aktualizacji HACS.
- Po aktualizacji uruchom ponownie Home Assistant, gdy HACS tego wymaga.
- Sama aktualizacja integracji nie wymaga restartu hosta Raspberry Pi.

### Weryfikacja

- Walidacja repozytorium
- Home Assistant Hassfest
- Kompilacja Pythona
- Walidacja JSON
- Zgodność wersji z publicznym wydaniem SBC5 Control Center 3.0.0
