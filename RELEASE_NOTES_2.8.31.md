# SBC5 Control Center Integration 2.8.31

[![SBC5 Control Center App](https://raw.githubusercontent.com/krlmdfk/sbc5-control-center/main/branding/icon-256.png)](https://github.com/krlmdfk/sbc5-control-center)

## English

Migration finalization hotfix: imported durable CPU/GPU profile state now wins over stale Store/Supervisor defaults until native App options are synchronized; adds a verified manifest-driven local ZIP packer and automatic release asset publishing. No Adaptive PWM, AI Cooling, fan calibration or boot-control algorithm changes.

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

Hotfix finalizacji migracji: zaimportowany trwały stan profili CPU/GPU ma teraz pierwszeństwo przed starymi domyślnymi wartościami Store/Supervisor do czasu synchronizacji natywnych opcji aplikacji; dodano zweryfikowany generator lokalnych ZIP-ów oparty na manifeście i automatyczną publikację paczki w Release. Bez zmian Adaptive PWM, AI Cooling, kalibracji wentylatora ani algorytmów sterowania boot.

### Wymaganie

Integracja **wymaga zainstalowanej i uruchomionej aplikacji/runtime SBC5 Control Center**:

**[Otwórz główne repozytorium SBC5 Control Center →](https://github.com/krlmdfk/sbc5-control-center)**

- Home Assistant >= 2026.10.1
- Integracja zarządzana przez HACS
- Kompletny dashboard Lovelace: Mushroom + card-mod + ApexCharts Card
- Po instalacji/aktualizacji uruchom ponownie Home Assistant, gdy zostaniesz o to poproszony
- Sama aktualizacja integracji nie wymaga restartu hosta Raspberry Pi
