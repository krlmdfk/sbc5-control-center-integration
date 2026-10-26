# SBC5 Control Center — HACS Integration / Integracja HACS

[![SBC5 Control Center App](https://raw.githubusercontent.com/krlmdfk/sbc5-control-center/main/branding/icon-256.png)](https://github.com/krlmdfk/sbc5-control-center)

> **App required / Aplikacja wymagana**
>
> Click the SBC5 logo above to open the required **SBC5 Control Center App/runtime** repository.
>
> Kliknij logo SBC5 powyżej, aby otworzyć repozytorium wymaganej **aplikacji/runtime SBC5 Control Center**.

**[Main App / Główna aplikacja](https://github.com/krlmdfk/sbc5-control-center)** · **[Integration / Integracja](https://github.com/krlmdfk/sbc5-control-center-integration)**

## English

Native Home Assistant companion integration for **SBC5 Control Center** on Raspberry Pi 5.

**Version:** 2.8.32

**Home Assistant:** >= 2026.10.1

**Requirement:** the **SBC5 Control Center App/runtime must already be installed and running**.

The App provides Raspberry Pi 5 host telemetry and control services. This HACS integration exposes device information, telemetry, diagnostics, update state and Restart Manager entities in Home Assistant.

For the **complete SBC5 Lovelace dashboard**, also install through HACS: **Mushroom**, **card-mod**, and **ApexCharts Card**. The native integration itself can operate without these frontend cards.

Runtime robustness hotfix: guarantees writable runtime scratch storage, hardens AI qualification templates against partial telemetry, throttles repeated boot/config write warnings when Host Access is unavailable, and adds explicit Protection Mode/Host PID diagnostics. No Adaptive PWM, AI Cooling model/qualification, fan calibration, CPU/GPU profile, or boot-control algorithm changes.

**[Open the required SBC5 Control Center App →](https://github.com/krlmdfk/sbc5-control-center)**

---

## Polski

Natywna integracja towarzysząca Home Assistant dla **SBC5 Control Center** na Raspberry Pi 5.

**Wersja:** 2.8.32

**Home Assistant:** >= 2026.10.1

**Wymaganie:** **aplikacja/runtime SBC5 Control Center musi być wcześniej zainstalowana i uruchomiona**.

Aplikacja dostarcza telemetrię hosta Raspberry Pi 5 oraz usługi sterujące. Integracja HACS udostępnia w Home Assistant informacje o urządzeniu, telemetrię, diagnostykę, stan aktualizacji oraz encje Restart Managera.

Dla **kompletnego dashboardu Lovelace SBC5** zainstaluj również przez HACS: **Mushroom**, **card-mod** i **ApexCharts Card**. Sama natywna integracja może działać bez tych kart frontendowych.

Hotfix odporności runtime: gwarantuje zapisywalny katalog roboczy runtime, zabezpiecza szablony kwalifikacji AI na niepełną telemetrię, ogranicza powtarzane komunikaty o niedostępnym config.txt i dodaje jawną diagnostykę Protection Mode/Host PID. Bez zmian Adaptive PWM, modelu/kwalifikacji AI Cooling, kalibracji wentylatora, profili CPU/GPU ani algorytmów sterowania boot.

**[Otwórz wymaganą aplikację SBC5 Control Center →](https://github.com/krlmdfk/sbc5-control-center)**
