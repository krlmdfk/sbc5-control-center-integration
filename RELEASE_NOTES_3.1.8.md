# SBC5 Control Center Integration 3.1.8

> Version parity with SBC5 Control Center App/runtime 3.1.8 and AI Cooling v5 hierarchical continuous learning.

## English

### Highlights
- Aligns the HACS integration with SBC5 Control Center App/runtime 3.1.8.
- App/runtime 3.1.8 introduces AI Cooling v5 hierarchical continuous learning: a global continuous-load model supplements the existing bucket-aware learner so sparse `medium` and `high` workload ranges can reuse transferable evidence.
- Existing durable direct bucket learning is preserved; mature direct models remain authoritative.
- Short real-world CPU bursts can contribute bounded low-weight evidence without requiring long synthetic sustained load.
- Existing AI Thermal Predictor, MAE/quality and Shadow Assist telemetry remain available through the current coordinator.
- The integration adds no new polling loop and does not take ownership of physical PWM control.

### Upgrade
Update the integration through HACS. Restart Home Assistant only if HACS requests it. A Raspberry Pi host reboot is not required by this integration update.

## Polski

### Najważniejsze
- Wyrównuje integrację HACS z aplikacją/runtime SBC5 Control Center 3.1.8.
- App/runtime 3.1.8 wprowadza AI Cooling v5 z hierarchicznym ciągłym uczeniem: globalny model ciągłego obciążenia uzupełnia dotychczasowy learner bucket-aware, dzięki czemu rzadkie zakresy `medium` i `high` mogą korzystać z transferu wiedzy.
- Dotychczasowe trwałe uczenie bezpośrednie bucketów jest zachowane; dojrzałe modele lokalne pozostają nadrzędne.
- Krótkie rzeczywiste skoki CPU mogą wnosić dane o ograniczonej wadze bez potrzeby długiego sztucznego obciążania procesora.
- Istniejące dane AI Thermal Predictor, MAE/jakości i Shadow Assist pozostają dostępne przez obecny koordynator.
- Integracja nie dodaje nowej pętli pollingu i nie przejmuje fizycznego sterowania PWM.

### Aktualizacja
Aktualizuj integrację przez HACS. Uruchom ponownie Home Assistant tylko wtedy, gdy HACS tego zażąda. Ta aktualizacja integracji nie wymaga restartu hosta Raspberry Pi.
