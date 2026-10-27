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

**Version:** 3.1.0
**Home Assistant:** >= 2026.10.1

The App provides Raspberry Pi 5 host telemetry and control services. This HACS integration exposes device information, telemetry, diagnostics, update state and Restart Manager entities in Home Assistant.

The integration is aligned with App/runtime 3.1.0 and exposes the runtime and AI data surfaces used by the observe-only AI Thermal Predictor. Adaptive PWM and AI Cooling remain authoritative; Recorder-friendly thermal forecast sensors are provided by the SBC5 package.

For the complete SBC5 Lovelace dashboard, also install through HACS: **Mushroom**, **card-mod**, and **ApexCharts Card**.

**[Open the required SBC5 Control Center App →](https://github.com/krlmdfk/sbc5-control-center)**

---

## Polski

Natywna integracja towarzysząca Home Assistant dla **SBC5 Control Center** na Raspberry Pi 5.

**Wersja:** 3.1.0
**Home Assistant:** >= 2026.10.1

Aplikacja dostarcza telemetrię hosta Raspberry Pi 5 oraz usługi sterujące. Integracja HACS udostępnia w Home Assistant informacje o urządzeniu, telemetrię, diagnostykę, stan aktualizacji oraz encje Restart Managera.

Integracja jest zgodna z aplikacją/runtime 3.1.0 i udostępnia dane runtime oraz AI wykorzystywane przez obserwacyjny AI Thermal Predictor. Adaptive PWM i AI Cooling pozostają nadrzędne; sensory prognozy termicznej przyjazne Recorderowi są dostarczane przez pakiet SBC5.

Dla kompletnego dashboardu Lovelace SBC5 zainstaluj również przez HACS: **Mushroom**, **card-mod** i **ApexCharts Card**.

**[Otwórz wymaganą aplikację SBC5 Control Center →](https://github.com/krlmdfk/sbc5-control-center)**
