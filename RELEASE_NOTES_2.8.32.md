# SBC5 Control Center Integration 2.8.32

[![SBC5 Control Center App](https://raw.githubusercontent.com/krlmdfk/sbc5-control-center/main/branding/icon-256.png)](https://github.com/krlmdfk/sbc5-control-center)

## English

Runtime robustness hotfix: guarantees writable runtime scratch storage, hardens AI qualification templates against partial telemetry, throttles repeated boot/config write warnings when Host Access is unavailable, and adds explicit Protection Mode/Host PID diagnostics. No Adaptive PWM, AI Cooling model/qualification, fan calibration, CPU/GPU profile, or boot-control algorithm changes.

### Requirement

This integration **requires the SBC5 Control Center App/runtime to be installed and running**:

**[Open main SBC5 Control Center App repository →](https://github.com/krlmdfk/sbc5-control-center)**

- Home Assistant >= 2026.10.1
- HACS-managed integration
- Complete Lovelace dashboard: Mushroom + card-mod + ApexCharts Card
- Restart Home Assistant after installation/update when requested
- A Raspberry Pi host restart is not required by the integration update itself

---

## Polski

Hotfix odporności runtime: gwarantuje zapisywalny katalog roboczy runtime, zabezpiecza szablony kwalifikacji AI na niepełną telemetrię, ogranicza powtarzane komunikaty o niedostępnym config.txt i dodaje jawną diagnostykę Protection Mode/Host PID. Bez zmian Adaptive PWM, modelu/kwalifikacji AI Cooling, kalibracji wentylatora, profili CPU/GPU ani algorytmów sterowania boot.

### Wymaganie

Integracja **wymaga zainstalowanej i uruchomionej aplikacji/runtime SBC5 Control Center**:

**[Otwórz główne repozytorium SBC5 Control Center →](https://github.com/krlmdfk/sbc5-control-center)**

- Home Assistant >= 2026.10.1
- Integracja zarządzana przez HACS
- Kompletny dashboard Lovelace: Mushroom + card-mod + ApexCharts Card
- Po instalacji/aktualizacji uruchom ponownie Home Assistant, gdy zostaniesz o to poproszony
- Sama aktualizacja integracji nie wymaga restartu hosta Raspberry Pi
