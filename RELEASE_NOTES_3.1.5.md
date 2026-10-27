# SBC5 Control Center Integration 3.1.5

## English
- Native AI Thermal Predictor Shadow Assist telemetry for App/runtime 3.1.5.
- Suggested PWM delta and hypothetical PWM are bounded diagnostics only; `control_output_enabled=false`.
- Activation gate reports Predictor quality/confidence/MAE/sample readiness through the existing runtime relay.
- No additional polling. Adaptive PWM and AI Cooling remain authoritative.
- Update through HACS; restart Home Assistant only if HACS requests it. No Raspberry Pi host restart.

## Polski
- Natywna telemetria AI Thermal Predictor Shadow Assist dla App/runtime 3.1.5.
- Sugerowana delta PWM i hipotetyczny PWM są wyłącznie ograniczoną diagnostyką; `control_output_enabled=false`.
- Bramka aktywacji raportuje gotowość jakości/confidence/MAE/liczby próbek Predictora przez istniejący relay runtime.
- Bez dodatkowego pollingu. Adaptive PWM i AI Cooling pozostają nadrzędne.
- Aktualizacja przez HACS; restart Home Assistant tylko jeśli HACS tego zażąda. Bez restartu hosta Raspberry Pi.
