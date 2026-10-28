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

**Version:** 3.1.8  
**Home Assistant:** >= 2026.10.1

The App provides Raspberry Pi 5 host telemetry and control services. This HACS integration exposes device information, telemetry, diagnostics, update state, AI Cooling state, AI Thermal Predictor diagnostics and Restart Manager entities in Home Assistant.

The integration is aligned with App/runtime 3.1.8. AI Cooling v5 hierarchical continuous learning is implemented by the App/runtime: the existing qualified bucket learner remains authoritative for mature direct models, while a global continuous-load model can transfer conservative evidence into sparse `medium` and `high` ranges. The HACS integration exposes the resulting state and diagnostics without adding another polling loop or taking ownership of physical PWM control.

For the complete SBC5 Lovelace dashboard, also install through HACS: **Mushroom**, **card-mod**, and **ApexCharts Card**.

**[Open the required SBC5 Control Center App →](https://github.com/krlmdfk/sbc5-control-center)**

---

## Polski

Natywna integracja towarzysząca Home Assistant dla **SBC5 Control Center** na Raspberry Pi 5.

**Wersja:** 3.1.8  
**Home Assistant:** >= 2026.10.1

Aplikacja dostarcza telemetrię hosta Raspberry Pi 5 oraz usługi sterujące. Integracja HACS udostępnia w Home Assistant informacje o urządzeniu, telemetrię, diagnostykę, stan aktualizacji, stan AI Cooling, diagnostykę AI Thermal Predictor oraz encje Restart Managera.

Integracja jest zgodna z aplikacją/runtime 3.1.8. AI Cooling v5 z hierarchicznym ciągłym uczeniem jest realizowane przez App/runtime: dotychczasowy learner kwalifikowanych próbek bucketów pozostaje nadrzędny dla dojrzałych modeli bezpośrednich, a globalny model ciągłego obciążenia może konserwatywnie przenosić wiedzę do rzadkich zakresów `medium` i `high`. Integracja HACS udostępnia wynikowy stan i diagnostykę bez dodawania kolejnej pętli pollingu i bez przejmowania fizycznego sterowania PWM.

Dla kompletnego dashboardu Lovelace SBC5 zainstaluj również przez HACS: **Mushroom**, **card-mod** i **ApexCharts Card**.

**[Otwórz wymaganą aplikację SBC5 Control Center →](https://github.com/krlmdfk/sbc5-control-center)**
