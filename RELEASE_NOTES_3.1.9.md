# SBC5 Control Center Integration 3.1.9

> Version parity with SBC5 Control Center App/runtime 3.1.9 for Restart Manager HACS handoff.

## English

### Highlights
- Aligns the HACS integration version with SBC5 Control Center App/runtime 3.1.9.
- Allows the App/runtime Restart Manager to recognize that HACS already owns and has installed the current bridge version.
- Prevents a second duplicate SBC5 restart Repair while Home Assistant Core is still reloading the matching package.
- Existing entities, coordinator behavior, AI Cooling telemetry, Thermal Predictor telemetry and polling cadence are unchanged.
- The integration does not take ownership of physical PWM control and adds no new polling loop.

### Upgrade
Update through HACS. Restart Home Assistant only if HACS requests it. No Raspberry Pi host reboot is required by this integration update.

## Polski

### Najważniejsze
- Wyrównuje wersję integracji HACS z aplikacją/runtime SBC5 Control Center 3.1.9.
- Pozwala Restart Managerowi App/runtime rozpoznać, że HACS już zarządza i ma zainstalowaną bieżącą wersję bridge.
- Zapobiega tworzeniu drugiego, zduplikowanego Repair SBC5 w czasie, gdy Home Assistant Core przeładowuje zgodny package.
- Istniejące encje, zachowanie koordynatora, telemetria AI Cooling, telemetria Thermal Predictor i częstotliwość pollingu pozostają bez zmian.
- Integracja nie przejmuje fizycznego sterowania PWM i nie dodaje nowej pętli pollingu.

### Aktualizacja
Aktualizuj przez HACS. Uruchom ponownie Home Assistant tylko wtedy, gdy HACS tego zażąda. Ta aktualizacja integracji nie wymaga restartu hosta Raspberry Pi.
