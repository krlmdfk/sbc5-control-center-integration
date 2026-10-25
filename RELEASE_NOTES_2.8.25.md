# SBC5 Control Center Integration 2.8.25

First public GitHub/HACS-ready release of the native Home Assistant integration for SBC5 Control Center.

## Included

- native SBC5 device and entity model for Home Assistant;
- Raspberry Pi device identity and firmware diagnostics;
- CPU, GPU/V3D/ISP, cooling, AI and update telemetry;
- Restart Manager and Repairs integration;
- update entity support;
- Polish and English translations;
- HACS ownership marker to prevent the SBC5 App from overwriting an integration managed by HACS;
- HACS, Hassfest, Python and JSON validation workflow.

## Requirements

- Home Assistant 2026.10.1 or newer;
- SBC5 Control Center App/runtime already installed and running on Raspberry Pi 5.

## Upgrade notes

Installing or updating this integration requires a Home Assistant restart. A Raspberry Pi host restart is not required by the integration update itself.
