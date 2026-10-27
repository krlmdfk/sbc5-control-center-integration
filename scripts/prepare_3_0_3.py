#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = "3.0.3"
DATE = "2026-10-27"

# manifest + const
manifest = ROOT / "custom_components" / "sbc5_control_center" / "manifest.json"
data = json.loads(manifest.read_text(encoding="utf-8"))
data["version"] = VERSION
manifest.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

const = ROOT / "custom_components" / "sbc5_control_center" / "const.py"
text = const.read_text(encoding="utf-8")
text, n = re.subn(r'(?m)^APP_VERSION = "[^"]+"$', f'APP_VERSION = "{VERSION}"', text, count=1)
if n != 1:
    raise SystemExit("APP_VERSION anchor missing")
const.write_text(text, encoding="utf-8")

# Current-state docs: only update current version references, not historical changelog content.
for path in (ROOT / "README.md", ROOT / "info.md"):
    text = path.read_text(encoding="utf-8")
    text = text.replace("Version 3.0.2", f"Version {VERSION}")
    text = text.replace("Version 3.0.1", f"Version {VERSION}")
    text = text.replace("**Version:** 3.0.2", f"**Version:** {VERSION}")
    text = text.replace("**Version:** 3.0.1", f"**Version:** {VERSION}")
    text = text.replace("**Wersja:** 3.0.2", f"**Wersja:** {VERSION}")
    text = text.replace("**Wersja:** 3.0.1", f"**Wersja:** {VERSION}")
    text = re.sub(r"Current release — 3\.0\.\d+", f"Current release — {VERSION}", text)
    text = re.sub(r"Aktualne wydanie — 3\.0\.\d+", f"Aktualne wydanie — {VERSION}", text)
    text = text.replace("aligned with App 3.0.2", f"aligned with App {VERSION}")
    text = text.replace("aligned with App 3.0.1", f"aligned with App {VERSION}")
    text = text.replace("aligned with App 3.0.0", f"aligned with App {VERSION}")
    text = text.replace("wyrównana z aplikacją 3.0.2", f"wyrównana z aplikacją {VERSION}")
    text = text.replace("wyrównana z aplikacją 3.0.1", f"wyrównana z aplikacją {VERSION}")
    text = text.replace("wyrównana z aplikacją 3.0.0", f"wyrównana z aplikacją {VERSION}")
    path.write_text(text, encoding="utf-8")

# Preserve all historical changelog lines and prepend only the new release entry.
changelog = ROOT / "CHANGELOG.md"
text = changelog.read_text(encoding="utf-8")
heading = f"## {VERSION} — {DATE}"
if heading not in text:
    title = "# Changelog — SBC5 Control Center\n\n"
    if not text.startswith(title):
        raise SystemExit("Unexpected CHANGELOG header")
    entry = (
        f"{heading}\n\n"
        "- Aligned the HACS integration release with SBC5 Control Center App/runtime 3.0.3.\n"
        "- Updated integration version metadata and bilingual current-state/release documentation.\n"
        "- No entity, coordinator, telemetry, repairs, update or Restart Manager behavior changes.\n"
        "- App/runtime 3.0.3 reduces steady-state log I/O only; integration behavior remains unchanged.\n\n"
    )
    text = title + entry + text[len(title):]
    changelog.write_text(text, encoding="utf-8")

notes = ROOT / f"RELEASE_NOTES_{VERSION}.md"
notes.write_text(
    f"""# SBC5 Control Center Integration {VERSION}\n\n"
    "## English\n\n"
    "### Highlights\n\n"
    f"- Aligned with SBC5 Control Center App/runtime **{VERSION}**.\n"
    "- Integration behavior remains unchanged from 3.0.2.\n"
    "- Restores App/integration version parity after the main runtime log I/O optimization.\n"
    "- HACS ownership protection remains active through `.hacs_managed`.\n\n"
    "### Requirements\n\n"
    "- SBC5 Control Center App/runtime installed and running\n"
    "- Home Assistant Core >= 2026.10.1\n"
    "- HACS-managed installation\n"
    "- Raspberry Pi 5\n\n"
    "### Upgrade notes\n\n"
    "- Existing integration configuration is preserved during a normal HACS upgrade.\n"
    "- Restart Home Assistant after the update when requested by HACS.\n"
    "- The integration update itself does not require a Raspberry Pi host restart.\n\n"
    "---\n\n"
    "## Polski\n\n"
    "### Najważniejsze zmiany\n\n"
    f"- Wyrównanie z aplikacją/runtime SBC5 Control Center **{VERSION}**.\n"
    "- Zachowanie integracji pozostaje bez zmian względem 3.0.2.\n"
    "- Przywrócono zgodność wersji aplikacji i integracji po optymalizacji I/O logów głównego runtime.\n"
    "- Ochrona kopii zarządzanej przez HACS pozostaje aktywna dzięki `.hacs_managed`.\n\n"
    "### Wymagania\n\n"
    "- Zainstalowana i uruchomiona aplikacja/runtime SBC5 Control Center\n"
    "- Home Assistant Core >= 2026.10.1\n"
    "- Instalacja zarządzana przez HACS\n"
    "- Raspberry Pi 5\n\n"
    "### Informacje o aktualizacji\n\n"
    "- Istniejąca konfiguracja integracji jest zachowywana przy standardowej aktualizacji HACS.\n"
    "- Po aktualizacji uruchom ponownie Home Assistant, gdy HACS tego wymaga.\n"
    "- Sama aktualizacja integracji nie wymaga restartu hosta Raspberry Pi.\n"
    """,
    encoding="utf-8",
)

print(f"Prepared HACS integration {VERSION}")
