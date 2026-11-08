# SBC5 Control Center — Home Assistant Integration

**Version / Wersja:** 3.1.37 · **Home Assistant Core:** 2026.10.1+ · **Platform:** Raspberry Pi 5

> **App required / Wymagana aplikacja.** The integration reads telemetry from the SBC5 Control Center App, installed separately through Home Assistant Apps. / Integracja odczytuje dane z aplikacji SBC5 Control Center instalowanej osobno przez Home Assistant Apps.

## Polski

Integracja udostępnia w Home Assistant natywne czujniki Raspberry Pi 5, stan chłodzenia, profile CPU/GPU, diagnostykę AI Cooling i Thermal Predictor oraz Restart Manager.

**Instalacja:** najpierw zainstaluj [aplikację SBC5 Control Center](https://github.com/krlmdfk/sbc5-control-center) ze sklepu Apps, następnie zainstaluj tę [integrację przez HACS](https://github.com/krlmdfk/sbc5-control-center-integration). Dodaj integrację w **Ustawienia → Urządzenia i usługi**. Jeśli HACS poprosi o ponowne uruchomienie Home Assistant, wykonaj je.

**Pełny panel Lovelace:** wymaga dodatkowo Mushroom, card-mod i ApexCharts Card z HACS. Nie są konieczne do działania samych encji integracji.

**Zmiany 3.1.37:** zgodność wersji z aplikacją SBC5; poprawka wygładzania Thermal Predictora znajduje się w runtime aplikacji. Bez zmian natywnych encji i odpytywania.

## English

SBC5 Control Center exposes native Raspberry Pi 5 telemetry, cooling and CPU/GPU profile state, AI Cooling and Thermal Predictor diagnostics and Restart Manager in Home Assistant.

**Installation:** install the [SBC5 Control Center App](https://github.com/krlmdfk/sbc5-control-center) through Home Assistant Apps, then install this [HACS companion integration](https://github.com/krlmdfk/sbc5-control-center-integration). Add the integration under **Settings → Devices & services**. Restart Home Assistant when requested by HACS.

**Complete Lovelace dashboard:** additionally install Mushroom, card-mod and ApexCharts Card from HACS. These are not needed for the integration's native entities.

**3.1.37:** aligns the HACS integration with the SBC5 App Thermal Predictor context-reset fix. No changes to native entities, polling or fan control.

[Documentation](https://github.com/krlmdfk/sbc5-control-center-integration) · [Issues](https://github.com/krlmdfk/sbc5-control-center-integration/issues) · [Main App](https://github.com/krlmdfk/sbc5-control-center)
