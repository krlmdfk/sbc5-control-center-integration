# SBC5 Control Center — HACS Integration / Integracja HACS

[![SBC5 Control Center App](https://raw.githubusercontent.com/krlmdfk/sbc5-control-center/main/branding/icon-256.png)](https://github.com/krlmdfk/sbc5-control-center)

> **App required / Aplikacja wymagana**
>
> The SBC5 Control Center App/runtime must already be installed and running.
>
> Aplikacja/runtime SBC5 Control Center musi być wcześniej zainstalowana i uruchomiona.

**[Main App / Główna aplikacja](https://github.com/krlmdfk/sbc5-control-center)** · **[Integration / Integracja](https://github.com/krlmdfk/sbc5-control-center-integration)**

## English

Native Home Assistant companion integration for **SBC5 Control Center** on Raspberry Pi 5.

**Version:** 3.1.10  
**Home Assistant:** >= 2026.10.1

The App provides Raspberry Pi 5 host telemetry and control services. This HACS integration exposes device information, telemetry, diagnostics, update state, AI Cooling state, AI Thermal Predictor diagnostics and Restart Manager entities in Home Assistant.

The integration is aligned with App/runtime 3.1.10. App/runtime 3.1.10 exposes AI Cooling v5 direct/global/effective confidence and prediction, transfer source and effective model coverage through the existing AI runtime relay and dashboard. Integration entities, coordinator behavior and polling cadence remain unchanged. Version parity also preserves the HACS Restart Manager handoff and duplicate-Repair suppression.

For the complete SBC5 Lovelace dashboard, also install through HACS: **Mushroom**, **card-mod**, and **ApexCharts Card**.

**[Open the required SBC5 Control Center App →](https://github.com/krlmdfk/sbc5-control-center)**

---

## Polski

Natywna integracja towarzysząca Home Assistant dla **SBC5 Control Center** na Raspberry Pi 5.

**Wersja:** 3.1.10  
**Home Assistant:** >= 2026.10.1

Aplikacja dostarcza telemetrię hosta Raspberry Pi 5 oraz usługi sterujące. Integracja HACS udostępnia w Home Assistant informacje o urządzeniu, telemetrię, diagnostykę, stan aktualizacji, stan AI Cooling, diagnostykę AI Thermal Predictor oraz encje Restart Managera.

Integracja jest zgodna z aplikacją/runtime 3.1.10. App/runtime 3.1.10 udostępnia przez istniejący relay AI i dashboard bezpośrednią, globalną i efektywną pewność/predykcję AI Cooling v5, źródło transferu oraz efektywne pokrycie modelu. Encje integracji, zachowanie koordynatora i częstotliwość pollingu pozostają bez zmian. Zgodność wersji zachowuje także handoff Restart Managera z HACS oraz ochronę przed zduplikowanym Repair.

Dla kompletnego dashboardu Lovelace SBC5 zainstaluj również przez HACS: **Mushroom**, **card-mod** i **ApexCharts Card**.

**[Otwórz wymaganą aplikację SBC5 Control Center →](https://github.com/krlmdfk/sbc5-control-center)**
