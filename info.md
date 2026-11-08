# SBC5 Control Center — Home Assistant Integration

**Version / Wersja:** 3.2.0 · **Home Assistant Core:** 2026.10.1+ · **Platform:** Raspberry Pi 5

> **App required / Wymagana aplikacja.** The integration reads telemetry from the SBC5 Control Center App, installed separately through Home Assistant Apps. / Integracja odczytuje dane z aplikacji SBC5 Control Center instalowanej osobno przez Home Assistant Apps.

## Polski

Integracja udostępnia w Home Assistant natywne czujniki Raspberry Pi 5, stan chłodzenia, profile CPU/GPU, diagnostykę AI Cooling i Thermal Predictor oraz Restart Manager.

**Instalacja:** najpierw zainstaluj [aplikację SBC5 Control Center](https://github.com/krlmdfk/sbc5-control-center) ze sklepu Apps, następnie zainstaluj tę [integrację przez HACS](https://github.com/krlmdfk/sbc5-control-center-integration). Dodaj integrację w **Ustawienia → Urządzenia i usługi**. Jeśli HACS poprosi o ponowne uruchomienie Home Assistant, wykonaj je.

**Pełny panel Lovelace:** wymaga dodatkowo Mushroom, card-mod i ApexCharts Card z HACS. Nie są konieczne do działania samych encji integracji.

**Zmiany 3.2.0:** zgodność z aplikacją SBC5 Global Community Edition dla Raspberry Pi 5; dodano dokumentację instalacji międzynarodowej i ostrzeżenie o szerokich uprawnieniach aplikacji. Bez zmian enkji, odpytywania i PWM.

## English

SBC5 Control Center exposes native Raspberry Pi 5 telemetry, cooling and CPU/GPU profile state, AI Cooling and Thermal Predictor diagnostics and Restart Manager in Home Assistant.

**Installation:** install the [SBC5 Control Center App](https://github.com/krlmdfk/sbc5-control-center) through Home Assistant Apps, then install this [HACS companion integration](https://github.com/krlmdfk/sbc5-control-center-integration). Add the integration under **Settings → Devices & services**. Restart Home Assistant when requested by HACS.

**Complete Lovelace dashboard:** additionally install Mushroom, card-mod and ApexCharts Card from HACS. These are not needed for the integration's native entities.

**3.2.0:** version parity with the Raspberry Pi 5 Global Community Edition App, including a security disclosure for elevated host access. No integration polling or PWM changes.

[Documentation](https://github.com/krlmdfk/sbc5-control-center-integration) · [Issues](https://github.com/krlmdfk/sbc5-control-center-integration/issues) · [Main App](https://github.com/krlmdfk/sbc5-control-center)
