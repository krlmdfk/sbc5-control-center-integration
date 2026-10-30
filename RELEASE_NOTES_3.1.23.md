# SBC5 Control Center Integration 3.1.23

## English

Companion release for SBC5 Control Center App 3.1.23.

- Keeps HACS integration version parity with App 3.1.23.
- App 3.1.23 fixes Thermal Predictor guided-assist runtime wiring so forecast guidance is evaluated on every AI control cycle instead of only during model-learning updates.
- Thermal Predictor influence remains bounded and subordinate to the existing AI/Adaptive PWM safety path.
- No telemetry polling cadence or integration control behavior changes in the HACS component itself.
- Restart Home Assistant Core after updating the HACS integration.

## Polski

Wydanie towarzyszące dla SBC5 Control Center App 3.1.23.

- Utrzymuje zgodność wersji integracji HACS z aplikacją 3.1.23.
- Aplikacja 3.1.23 naprawia podłączenie Thermal Predictor guided assist w runtime, dzięki czemu wskazówki predykcyjne są obliczane w każdym cyklu sterowania AI, a nie tylko podczas aktualizacji modelu uczącego.
- Wpływ Thermal Predictora pozostaje ograniczony i podporządkowany istniejącej ścieżce bezpieczeństwa AI/Adaptive PWM.
- Sama integracja HACS nie zmienia częstotliwości odpytywania ani sposobu sterowania.
- Po aktualizacji integracji HACS należy zrestartować Home Assistant Core.
