#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
VERSION = "3.0.4"
OLD = "3.0.3"

manifest = ROOT / "custom_components" / "sbc5_control_center" / "manifest.json"
data = json.loads(manifest.read_text(encoding="utf-8"))
data["version"] = VERSION
manifest.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

const = ROOT / "custom_components" / "sbc5_control_center" / "const.py"
text = const.read_text(encoding="utf-8").replace(f'APP_VERSION = "{OLD}"', f'APP_VERSION = "{VERSION}"', 1)
const.write_text(text, encoding="utf-8")

readme = ROOT / "README.md"
text = readme.read_text(encoding="utf-8")
text = text.replace(f"**Version {OLD} ·", f"**Version {VERSION} ·", 1)
text = text.replace(f"### Current release — {OLD}", f"### Current release — {VERSION}", 1)
text = text.replace(
    "Version-parity release aligned with SBC5 Control Center App/runtime 3.0.2. Integration behavior is unchanged from 3.0.1; the App/runtime release optimizes local update discovery and Supervisor profile reconciliation while preserving Adaptive PWM, AI Cooling and the verified 49°C boot curve.",
    "Version-parity release aligned with SBC5 Control Center App/runtime 3.0.4. Integration behavior remains unchanged; App/runtime 3.0.4 lowers steady-state Config.txt watchdog and AI relay polling overhead without changing Adaptive PWM, AI evaluator, realtime cooling, telemetry cadence or the verified 49°C boot curve.",
    1,
)
text = text.replace(f"### Aktualne wydanie — {OLD}", f"### Aktualne wydanie — {VERSION}", 1)
text = text.replace(
    "Wydanie wyrównujące wersję integracji z aplikacją/runtime SBC5 Control Center 3.0.2. Zachowanie integracji pozostaje bez zmian względem 3.0.1; wydanie aplikacji/runtime optymalizuje wykrywanie lokalnych aktualizacji i uzgadnianie profili Supervisor bez zmian Adaptive PWM, AI Cooling i zweryfikowanej krzywej boot 49°C.",
    "Wydanie wyrównujące wersję integracji z aplikacją/runtime SBC5 Control Center 3.0.4. Zachowanie integracji pozostaje bez zmian; aplikacja/runtime 3.0.4 zmniejsza stałe obciążenie pollingiem Config.txt Manager i relay AI bez zmian Adaptive PWM, evaluatora AI, realtime cooling, telemetrii ani zweryfikowanej krzywej boot 49°C.",
    1,
)
readme.write_text(text, encoding="utf-8")

info = ROOT / "info.md"
text = info.read_text(encoding="utf-8")
text = text.replace(f"**Version:** {OLD}", f"**Version:** {VERSION}", 1)
text = text.replace(
    "The integration is aligned with App/runtime 3.0.2. This release keeps integration behavior unchanged while restoring version parity with the runtime efficiency hotfix in the main App.",
    "The integration is aligned with App/runtime 3.0.4. Integration behavior is unchanged; the main App reduces steady-state Config.txt watchdog and AI relay polling overhead while preserving cooling-control cadence.",
    1,
)
text = text.replace(f"**Wersja:** {OLD}", f"**Wersja:** {VERSION}", 1)
text = text.replace(
    "Integracja jest wyrównana z aplikacją/runtime 3.0.2. To wydanie nie zmienia zachowania integracji i przywraca zgodność wersji z hotfixem wydajności głównej aplikacji.",
    "Integracja jest wyrównana z aplikacją/runtime 3.0.4. To wydanie nie zmienia zachowania integracji; główna aplikacja zmniejsza stałe obciążenie pollingiem Config.txt Manager i relay AI bez zmiany częstotliwości sterowania chłodzeniem.",
    1,
)
info.write_text(text, encoding="utf-8")

changelog = ROOT / "CHANGELOG.md"
text = changelog.read_text(encoding="utf-8")
entry = """## 3.0.4 — 2026-10-27\n\n- Aligned the HACS integration release with SBC5 Control Center App/runtime 3.0.4.\n- Updated integration version metadata and bilingual current-state/release documentation.\n- No entity, coordinator, telemetry, repairs, update or Restart Manager behavior changes.\n- App/runtime 3.0.4 lowers steady-state Config.txt watchdog and AI relay polling overhead without changing cooling-control cadence.\n\n"""
if "## 3.0.4 —" not in text:
    marker = "# Changelog — SBC5 Control Center\n\n"
    text = text.replace(marker, marker + entry, 1)
changelog.write_text(text, encoding="utf-8")

notes = ROOT / "RELEASE_NOTES_3.0.4.md"
notes.write_text("""# SBC5 Control Center Integration 3.0.4\n\n## English\n\n### Highlights\n\n- Aligned with SBC5 Control Center App/runtime **3.0.4**.\n- Integration behavior remains unchanged from 3.0.3.\n- Restores App/integration version parity after the main runtime polling/I/O optimization.\n- HACS ownership protection remains active through `.hacs_managed`.\n\n### Requirements\n\n- SBC5 Control Center App/runtime installed and running\n- Home Assistant Core >= 2026.10.1\n- HACS-managed installation\n- Raspberry Pi 5\n\n### Upgrade notes\n\n- Existing integration configuration is preserved during a normal HACS upgrade.\n- Restart Home Assistant after the update when requested by HACS.\n- The integration update itself does not require a Raspberry Pi host restart.\n\n---\n\n## Polski\n\n### Najważniejsze zmiany\n\n- Wyrównanie z aplikacją/runtime SBC5 Control Center **3.0.4**.\n- Zachowanie integracji pozostaje bez zmian względem 3.0.3.\n- Przywrócono zgodność wersji aplikacji i integracji po optymalizacji pollingu/I/O głównego runtime.\n- Ochrona kopii zarządzanej przez HACS pozostaje aktywna dzięki `.hacs_managed`.\n\n### Wymagania\n\n- Zainstalowana i uruchomiona aplikacja/runtime SBC5 Control Center\n- Home Assistant Core >= 2026.10.1\n- Instalacja zarządzana przez HACS\n- Raspberry Pi 5\n\n### Informacje o aktualizacji\n\n- Istniejąca konfiguracja integracji jest zachowywana przy standardowej aktualizacji HACS.\n- Po aktualizacji uruchom ponownie Home Assistant, gdy HACS tego wymaga.\n- Sama aktualizacja integracji nie wymaga restartu hosta Raspberry Pi.\n""", encoding="utf-8")

for path in (readme, info, changelog, notes):
    t = path.read_text(encoding="utf-8")
    had_nl = t.endswith("\n")
    t = "\n".join(line.rstrip() for line in t.splitlines())
    if had_nl:
        t += "\n"
    path.write_text(t, encoding="utf-8")

print("Prepared HACS integration 3.0.4 parity")
