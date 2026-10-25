# Publishing SBC5 Control Center Integration

Repository: `https://github.com/krlmdfk/sbc5-control-center-integration`

## GitHub repository settings

**Visibility:** Public

**Description:**

`Native Home Assistant integration for SBC5 Control Center on Raspberry Pi 5.`

**Topics:**

`home-assistant`, `hacs`, `raspberry-pi-5`, `custom-integration`, `monitoring`, `cooling`, `sbc5`

Issues should remain enabled.

## First publication — 2.8.25

1. Publish the prepared repository contents to branch `main`.
2. Open **Actions** and wait for **HACS**, **Hassfest** and **Syntax** to finish.
3. Fix any validation error before creating the release.
4. Open **Releases → Draft a new release**.
5. Create tag `2.8.25` from `main`.
6. Release title: `SBC5 Control Center Integration 2.8.25`.
7. Use `RELEASE_NOTES_2.8.25.md` as the release description.
8. Publish the release.
9. Add the repository to HACS as **Custom repositories → Integration** and test installation/update.

## Version rule

When a GitHub Release is used, its tag should match the `version` field in `custom_components/sbc5_control_center/manifest.json`.
