# SBC5 Control Center Integration 3.0.3

## English

### Highlights

- Aligned with SBC5 Control Center App/runtime **3.0.3**.
- Integration behavior remains unchanged from 3.0.2.
- Restores App/integration version parity after the main runtime log I/O optimization.
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

---

## Polski

### Najważniejsze zmiany

- Wyrównanie z aplikacją/runtime SBC5 Control Center **3.0.3**.
- Zachowanie integracji pozostaje bez zmian względem 3.0.2.
- Przywrócono zgodność wersji aplikacji i integracji po optymalizacji I/O logów głównego runtime.
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
