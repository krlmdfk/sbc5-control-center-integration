# SBC5 Control Center Integration 3.1.33

## English

- Fixes blocking file I/O in the Home Assistant repair flow by moving marker-file reads and deletes to the executor.
- Keeps `issue_registry.async_delete_issue()` on the Home Assistant event loop.
- Corrects the integration `documentation` and `issue_tracker` links to point to the integration repository.
- Maintenance release prepared in response to the HACS review feedback.

## Polski

- Naprawia blokujące operacje plikowe w przepływie napraw Home Assistant, przenosząc odczyt i usuwanie pliku znacznika do executora.
- Pozostawia `issue_registry.async_delete_issue()` w pętli zdarzeń Home Assistanta.
- Poprawia linki `documentation` i `issue_tracker`, aby wskazywały repozytorium integracji.
- Wydanie serwisowe przygotowane zgodnie z uwagami z przeglądu HACS.
