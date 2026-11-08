# SBC5 Control Center Integration 3.2.0 — Global Community Edition

## English
- Public companion HACS integration aligned with SBC5 Control Center App/runtime 3.2.0 on Raspberry Pi 5 and Home Assistant OS.
- Worldwide community distribution through the public App repository; this is **not** acceptance into the official Home Assistant Apps catalog.
- Security: the separate App/runtime needs elevated host permissions and Protection Mode disabled. Review the [privilege audit](https://github.com/krlmdfk/sbc5-control-center/blob/main/docs/SECURITY_PRIVILEGE_AUDIT_3_2_0.md) before installation.
- No changes to HACS entity schemas, polling intervals, Repairs, or physical fan/PWM control.
- **Testing limitation:** CI and regression checks passed, but a fresh installation on a second Raspberry Pi 5 was not tested. The 3.1.37 → 3.2.0 upgrade on the existing device is to be verified after public release. Back up Home Assistant first.
- HACS and App are released separately. Install/update the App first, then update the integration, and restart Home Assistant if prompted.

## Polski
- Publiczna integracja HACS zgodna z aplikacją/runtime SBC5 Control Center 3.2.0 dla Raspberry Pi 5 i Home Assistant OS.
- Globalna dystrybucja przez publiczne repozytorium społecznościowe Apps; **nie** oznacza przyjęcia aplikacji do oficjalnego katalogu Home Assistant.
- Bezpieczeństwo: osobna aplikacja wymaga szerokich uprawnień hosta i wyłączonego Protection Mode. Przed instalacją przeczytaj [audyt uprawnień](https://github.com/krlmdfk/sbc5-control-center/blob/main/docs/SECURITY_PRIVILEGE_AUDIT_3_2_0.md).
- Bez zmian encji HACS, częstotliwości odpytywania, Repairs ani sterowania fizycznym PWM.
- **Ograniczenie testów:** walidacje CI i testy regresyjne przeszły poprawnie, ale nie wykonano czystej instalacji na drugim Raspberry Pi 5. Aktualizacja 3.1.37 → 3.2.0 na obecnym urządzeniu będzie weryfikowana po publikacji. Przed instalacją wykonaj kopię zapasową.
- Aplikacja i HACS są wydawane oddzielnie. Najpierw zaktualizuj aplikację, następnie integrację, a Home Assistant uruchom ponownie, jeżeli pojawi się taka prośba.
