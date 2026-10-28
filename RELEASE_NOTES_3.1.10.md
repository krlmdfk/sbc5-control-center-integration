# SBC5 Control Center Integration 3.1.10

> Version parity with SBC5 Control Center App/runtime 3.1.10 and AI Cooling v5 observability.

## English

### Highlights
- Aligns the HACS integration version with SBC5 Control Center App/runtime 3.1.10.
- App/runtime 3.1.10 exposes AI Cooling v5 direct, global and effective confidence/prediction, transfer source and effective model coverage through the existing AI runtime relay and dashboard.
- Preserves the HACS Restart Manager handoff and duplicate-Repair suppression introduced in 3.1.9.
- Existing integration entities, coordinator behavior and polling cadence are unchanged.
- No new polling loop and no physical PWM ownership changes.

### Upgrade
Update through HACS. Restart Home Assistant only if HACS requests it. No Raspberry Pi host reboot is required by this integration update.

## Polski

### Najważniejsze
- Wyrównuje wersję integracji HACS z aplikacją/runtime SBC5 Control Center 3.1.10.
- App/runtime 3.1.10 udostępnia przez istniejący relay AI i dashboard bezpośrednią, globalną i efektywną pewność/predykcję AI Cooling v5, źródło transferu oraz efektywne pokrycie modelu.
- Zachowuje handoff Restart Managera z HACS i ochronę przed zduplikowanym Repair wprowadzoną w 3.1.9.
- Istniejące encje integracji, zachowanie koordynatora i częstotliwość pollingu pozostają bez zmian.
- Bez nowej pętli pollingu i bez zmian własności fizycznego PWM.

### Aktualizacja
Aktualizuj przez HACS. Uruchom ponownie Home Assistant tylko wtedy, gdy HACS tego zażąda. Ta aktualizacja integracji nie wymaga restartu hosta Raspberry Pi.
