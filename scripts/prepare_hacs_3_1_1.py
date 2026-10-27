#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = "3.1.1"
DATE = "2026-10-27"

manifest_path = ROOT / "custom_components" / "sbc5_control_center" / "manifest.json"
manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
manifest["version"] = VERSION
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

const_path = ROOT / "custom_components" / "sbc5_control_center" / "const.py"
const = const_path.read_text(encoding="utf-8")
const = re.sub(r'APP_VERSION = "[^"]+"', f'APP_VERSION = "{VERSION}"', const, count=1)
const_path.write_text(const, encoding="utf-8")

readme_path = ROOT / "README.md"
readme = readme_path.read_text(encoding="utf-8")
readme = readme.replace("Version 3.1.0", "Version 3.1.1")
readme = readme.replace("Current release — 3.1.0", "Current release — 3.1.1")
readme = readme.replace("Aktualne wydanie — 3.1.0", "Aktualne wydanie — 3.1.1")
readme = readme.replace(
    "Version 3.1.0 is aligned with SBC5 Control Center App/runtime 3.1.0. The integration exposes the runtime and AI surfaces used by the observe-only AI Thermal Predictor, while Adaptive PWM and AI Cooling remain authoritative. Recorder-friendly 30/60/120-second thermal forecast and confidence sensors are provided by the SBC5 package.",
    "Version 3.1.1 is aligned with SBC5 Control Center App/runtime 3.1.1. This release keeps the integration behavior unchanged and aligns HACS metadata with the 3.1.1 YAML/Card UI release that exposes responsive AI Thermal Predictor tiles for +30 s, +60 s, +120 s and predictor confidence. Adaptive PWM and AI Cooling remain authoritative.",
)
readme = readme.replace(
    "Wersja 3.1.0 jest zgodna z aplikacją/runtime SBC5 Control Center 3.1.0. Integracja udostępnia powierzchnie runtime i AI wykorzystywane przez obserwacyjny AI Thermal Predictor, a Adaptive PWM i AI Cooling pozostają nadrzędne. Sensory prognozy termicznej 30/60/120 s oraz confidence przyjazne Recorderowi są dostarczane przez pakiet SBC5.",
    "Wersja 3.1.1 jest zgodna z aplikacją/runtime SBC5 Control Center 3.1.1. Zachowanie integracji pozostaje bez zmian; wydanie wyrównuje metadane HACS z wersją 3.1.1 karty YAML/Card UI, która udostępnia responsywne kafelki AI Thermal Predictor dla +30 s, +60 s, +120 s oraz pewności predyktora. Adaptive PWM i AI Cooling pozostają nadrzędne.",
)
readme_path.write_text(readme, encoding="utf-8")

changelog_path = ROOT / "CHANGELOG.md"
changelog = changelog_path.read_text(encoding="utf-8")
if f"## {VERSION}" not in changelog:
    entry = f"""## {VERSION} — {DATE}\n\n- Aligned the HACS integration release with SBC5 Control Center App/runtime and Card UI 3.1.1.\n- Integration behavior is unchanged; 3.1.1 adds the responsive YAML/Lovelace AI Thermal Predictor presentation on the App/package side.\n- Preserved HACS ownership protection, existing entities, coordinator, telemetry, Repairs, update and Restart Manager behavior.\n- No Raspberry Pi host restart is required; restart Home Assistant only when requested by HACS.\n\n"""
    marker = "# Changelog — SBC5 Control Center\n\n"
    if marker not in changelog:
        raise SystemExit("CHANGELOG header not found")
    changelog = changelog.replace(marker, marker + entry, 1)
    changelog_path.write_text(changelog, encoding="utf-8")

notes = f"""# SBC5 Control Center Integration {VERSION}\n\n## English\n\n### Highlights\n\n- Aligned with SBC5 Control Center App/runtime and Card UI **{VERSION}**.\n- Integration behavior remains unchanged from 3.1.0.\n- App/package 3.1.1 adds responsive YAML/Lovelace AI Thermal Predictor tiles for +30 s, +60 s, +120 s and predictor confidence.\n- HACS ownership protection remains active through `.hacs_managed`.\n\n### Requirements\n\n- SBC5 Control Center App/runtime {VERSION} installed and running\n- Home Assistant Core >= 2026.10.1\n- HACS-managed installation\n- Raspberry Pi 5\n\n### Upgrade notes\n\n- Update the App through the Home Assistant Apps Store / configured SBC5 repository.\n- Update this companion integration through HACS.\n- Existing integration configuration is preserved during a normal HACS upgrade.\n- Restart Home Assistant only when requested by HACS.\n- No Raspberry Pi host restart is required by this release.\n\n---\n\n## Polski\n\n### Najważniejsze zmiany\n\n- Wyrównanie z aplikacją/runtime i Card UI SBC5 Control Center **{VERSION}**.\n- Zachowanie integracji pozostaje bez zmian względem 3.1.0.\n- App/package 3.1.1 dodaje responsywne kafelki YAML/Lovelace AI Thermal Predictor dla +30 s, +60 s, +120 s i pewności predyktora.\n- Ochrona kopii zarządzanej przez HACS pozostaje aktywna dzięki `.hacs_managed`.\n\n### Wymagania\n\n- Zainstalowana i uruchomiona aplikacja/runtime SBC5 Control Center {VERSION}\n- Home Assistant Core >= 2026.10.1\n- Instalacja zarządzana przez HACS\n- Raspberry Pi 5\n\n### Informacje o aktualizacji\n\n- Aplikację aktualizuj przez Sklep Apps Home Assistant / skonfigurowane repozytorium SBC5.\n- Integrację towarzyszącą aktualizuj przez HACS.\n- Istniejąca konfiguracja integracji jest zachowywana podczas standardowej aktualizacji HACS.\n- Uruchom ponownie Home Assistant tylko wtedy, gdy HACS tego wymaga.\n- To wydanie nie wymaga restartu hosta Raspberry Pi.\n"""
(ROOT / f"RELEASE_NOTES_{VERSION}.md").write_text(notes, encoding="utf-8")

print("Prepared HACS integration 3.1.1 version parity")
