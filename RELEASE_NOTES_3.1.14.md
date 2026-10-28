# SBC5 Control Center Integration 3.1.14

## English

This release keeps the HACS integration version aligned with SBC5 Control Center 3.1.14.

- No sensor, coordinator or polling behavior changes.
- SBC5 Control Center 3.1.14 fixes Active Cooler `custom1` overlay reconciliation after Home Assistant OS A/B RAUC slot switches.
- The App now validates the custom DTBO in the currently booted HAOS slot and repairs a missing active-slot overlay instead of accepting a stale copy from another slot.
- The integration continues to expose the existing relay/runtime data to Home Assistant without additional polling.
- The integration itself does not require a Raspberry Pi host restart; the companion App 3.1.14 requires one full host restart after it repairs the boot overlay so firmware can load it.

## Polski

To wydanie synchronizuje wersję integracji HACS z SBC5 Control Center 3.1.14.

- Brak zmian w sensorach, koordynatorze i częstotliwości pollingu.
- SBC5 Control Center 3.1.14 naprawia uzgadnianie nakładki `custom1` Active Cooler po przełączeniu slotu A/B RAUC przez Home Assistant OS.
- Aplikacja sprawdza teraz DTBO w aktualnie uruchomionym slocie HAOS i naprawia brak nakładki w aktywnym slocie zamiast akceptować starą kopię z innego slotu.
- Integracja nadal udostępnia istniejące dane relay/runtime do Home Assistant bez dodatkowego pollingu.
- Sama integracja nie wymaga restartu hosta Raspberry Pi; aplikacja towarzysząca 3.1.14 wymaga jednego pełnego restartu hosta po naprawie nakładki boot, aby firmware ją wczytał.
