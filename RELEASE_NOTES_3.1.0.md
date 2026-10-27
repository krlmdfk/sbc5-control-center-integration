# SBC5 Control Center Integration 3.1.0

## English

### Highlights

- Aligned with SBC5 Control Center App/runtime **3.1.0**.
- Integration behavior remains unchanged from 3.0.4.
- App/runtime 3.1.0 introduces the observe-only **AI Thermal Predictor** with 30/60/120-second forecasts and online prediction-error scoring.
- HACS ownership protection remains active through `.hacs_managed`.

### Requirements

- SBC5 Control Center App/runtime 3.1.0 installed and running
- Home Assistant Core >= 2026.10.1
- HACS-managed installation
- Raspberry Pi 5

### Upgrade notes

- Existing integration configuration is preserved during a normal HACS upgrade.
- Restart Home Assistant after the update only when requested by HACS.
- The integration update does not require a Raspberry Pi host restart.

---

## Polski

### Najważniejsze zmiany

- Wyrównanie z aplikacją/runtime SBC5 Control Center **3.1.0**.
- Zachowanie integracji pozostaje bez zmian względem 3.0.4.
- Aplikacja/runtime 3.1.0 wprowadza obserwacyjny **AI Thermal Predictor** z prognozami 30/60/120 s i walidacją błędu prognoz online.
- Ochrona kopii zarządzanej przez HACS pozostaje aktywna dzięki `.hacs_managed`.

### Wymagania

- Zainstalowana i uruchomiona aplikacja/runtime SBC5 Control Center 3.1.0
- Home Assistant Core >= 2026.10.1
- Instalacja zarządzana przez HACS
- Raspberry Pi 5

### Informacje o aktualizacji

- Istniejąca konfiguracja integracji jest zachowywana podczas standardowej aktualizacji HACS.
- Uruchom ponownie Home Assistant po aktualizacji tylko wtedy, gdy HACS tego wymaga.
- Aktualizacja integracji nie wymaga restartu hosta Raspberry Pi.
