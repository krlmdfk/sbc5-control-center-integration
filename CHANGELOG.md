# Changelog — SBC5 Control Center

## 3.0.2 — 2026-10-27

- Aligned the HACS integration release with SBC5 Control Center App/runtime 3.0.2.
- Updated integration version metadata and bilingual release/current-state documentation.
- No entity, coordinator, telemetry, repairs, update or Restart Manager behavior changes.

## 3.0.1 — 2026-10-27

- Aligned the HACS integration release with SBC5 Control Center App/runtime 3.0.1.
- Updated integration version metadata and bilingual release documentation.
- No entity, coordinator, telemetry, repairs, update or Restart Manager behavior changes.

## 2.8.32

- Runtime robustness hotfix: guarantees writable runtime scratch storage, hardens AI qualification templates against partial telemetry, throttles repeated boot/config write warnings when Host Access is unavailable, and adds explicit Protection Mode/Host PID diagnostics. No Adaptive PWM, AI Cooling model/qualification, fan calibration, CPU/GPU profile, or boot-control algorithm changes.
- Hotfix odporności runtime: gwarantuje zapisywalny katalog roboczy runtime, zabezpiecza szablony kwalifikacji AI na niepełną telemetrię, ogranicza powtarzane komunikaty o niedostępnym config.txt i dodaje jawną diagnostykę Protection Mode/Host PID. Bez zmian Adaptive PWM, modelu/kwalifikacji AI Cooling, kalibracji wentylatora, profili CPU/GPU ani algorytmów sterowania boot.

## 2.8.31

- Migration finalization hotfix: imported durable CPU/GPU profile state now wins over stale Store/Supervisor defaults until native App options are synchronized; adds a verified manifest-driven local ZIP packer and automatic release asset publishing. No Adaptive PWM, AI Cooling, fan calibration or boot-control algorithm changes.
- Hotfix finalizacji migracji: zaimportowany trwały stan profili CPU/GPU ma teraz pierwszeństwo przed starymi domyślnymi wartościami Store/Supervisor do czasu synchronizacji natywnych opcji aplikacji; dodano zweryfikowany generator lokalnych ZIP-ów oparty na manifeście i automatyczną publikację paczki w Release. Bez zmian Adaptive PWM, AI Cooling, kalibracji wentylatora ani algorytmów sterowania boot.

## 2.8.30

- Migration/Hybrid release: safe local-to-Apps Store handoff preserves AI, fan calibration, CPU/GPU profiles and user options with SHA-256 validation and rollback; hybrid local ZIP updates delegate full Store runtime updates to Supervisor while retaining direct UI-only ZIP support. No cooling or AI control algorithm changes.
- Wydanie Migration/Hybrid: bezpieczny handoff Local → Apps Store zachowuje AI, kalibrację wentylatora, profile CPU/GPU i opcje użytkownika z walidacją SHA-256 oraz rollbackiem; hybrydowe lokalne ZIP-y delegują pełne aktualizacje runtime wersji sklepowej do Supervisora, zachowując bezpośrednie aktualizacje UI-only. Bez zmian algorytmów chłodzenia ani sterowania AI.

## 2.8.29

- App Store installation and automatic update delivery. Adds Home Assistant Apps repository support, automatic release delivery and improved first-install documentation. No cooling, AI, CPU/GPU or boot-control algorithm changes.
- Instalacja przez sklep Apps i automatyczna dystrybucja aktualizacji. Dodaje obsługę repozytorium Home Assistant Apps, automatyczne publikowanie wydań i ulepszoną dokumentację pierwszej instalacji. Bez zmian algorytmów chłodzenia, AI, CPU/GPU ani sterowania boot.

## 2.8.28

- Adds a complete first-installation guide and release automation. No runtime control logic changes.
- Dodaje kompletny przewodnik pierwszej instalacji i automatyzację wydań. Bez zmian logiki sterowania runtime.

Historia zmian projektu. Aktualny stan, instalacja i obsługa są opisane w `INFO.md`, `DOCUMENTATION.md` oraz `docs/QUICK_SETUP.md`. Starsza historia sprzed gałęzi 2.8.x pozostaje w `docs/CHANGELOG_ARCHIVE_PRE_2.8.0.md`.
