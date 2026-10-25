# SBC5 Control Center — Home Assistant Integration

Native Home Assistant integration for **SBC5 Control Center** on Raspberry Pi 5.

[![HACS validation](https://github.com/krlmdfk/sbc5-control-center-integration/actions/workflows/validate.yml/badge.svg)](https://github.com/krlmdfk/sbc5-control-center-integration/actions/workflows/validate.yml)

**Version 2.8.25 · HACS-ready · Home Assistant ≥ 2026.10.1 · Apache-2.0**

This repository contains exactly one custom integration: `sbc5_control_center`.
It exposes SBC5 telemetry, diagnostics, device information, update state and Restart Manager entities to Home Assistant.

## Requirements

The integration is a companion to the **SBC5 Control Center App** running on Raspberry Pi 5 with Home Assistant OS.
For this first public integration release, the App may still be installed locally; a separate public App repository can be published later.

Without the SBC5 Control Center App/runtime, the integration has no SBC5 host telemetry source to read.

## Install with HACS

1. Open **HACS**.
2. Open **⋮ → Custom repositories**.
3. Add:

   `https://github.com/krlmdfk/sbc5-control-center-integration`

4. Select category **Integration**.
5. Install **SBC5 Control Center**.
6. Restart Home Assistant when HACS asks for it.
7. Open **Settings → Devices & services** and add **SBC5 Control Center** if it is not already present.

## HACS ownership protection

The integration contains the `.hacs_managed` marker. SBC5 Control Center detects this marker and leaves `custom_components/sbc5_control_center` under HACS ownership, preventing the App from overwriting or downgrading a HACS-managed copy.

## Validation

Every push and pull request runs:

- HACS repository validation;
- Home Assistant Hassfest validation;
- Python compilation and JSON validation.

## Support

Use the GitHub issue tracker for reproducible integration problems:

`https://github.com/krlmdfk/sbc5-control-center-integration/issues`

For host/container, cooling, boot configuration or App-runtime issues, include the relevant SBC5 logs and clearly mark the issue as **App/runtime** until the separate App repository is public.

## License

Apache License 2.0.

SBC5 Control Center is an independent project and is not endorsed by Raspberry Pi Ltd., Home Assistant, or the Open Home Foundation.
