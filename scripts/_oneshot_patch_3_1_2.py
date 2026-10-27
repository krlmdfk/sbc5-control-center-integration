#!/usr/bin/env python3
from pathlib import Path


def replace_once(path: str, old: str, new: str) -> None:
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    if old not in text:
        raise SystemExit(f"missing expected block in {path}: {old[:120]!r}")
    p.write_text(text.replace(old, new, 1), encoding="utf-8")

# Coordinator: expose the already-published AI Thermal Predictor relay without
# adding any new polling loop.
replace_once(
    "custom_components/sbc5_control_center/coordinator.py",
    '''class SBC5CoordinatorData:\n    telemetry: TelemetrySnapshot\n    app_update: AppUpdateInfo\n''',
    '''class SBC5CoordinatorData:\n    telemetry: TelemetrySnapshot\n    app_update: AppUpdateInfo\n    thermal_predictor: dict[str, Any]\n''',
)
replace_once(
    "custom_components/sbc5_control_center/coordinator.py",
    '''        app_update = AppUpdateInfo(\n''',
    '''        ai_state = self.hass.states.get("sensor.sbc5_control_center_ai_runtime")\n        ai_attrs: dict[str, Any] = dict(ai_state.attributes) if ai_state else {}\n        ai_cooling = ai_attrs.get("ai_cooling")\n        predictor = ai_cooling.get("thermal_predictor", {}) if isinstance(ai_cooling, dict) else {}\n        thermal_predictor = dict(predictor) if isinstance(predictor, dict) else {}\n\n        app_update = AppUpdateInfo(\n''',
)
replace_once(
    "custom_components/sbc5_control_center/coordinator.py",
    '''        return SBC5CoordinatorData(telemetry=telemetry, app_update=app_update)\n''',
    '''        return SBC5CoordinatorData(\n            telemetry=telemetry, app_update=app_update, thermal_predictor=thermal_predictor\n        )\n''',
)

# Native recorder-friendly Predictor sensors. Same IDs as 3.1.1 package templates,
# so recorder history remains continuous after registry migration.
replace_once(
    "custom_components/sbc5_control_center/sensor.py",
    '''def _cpu_usage_percent(data: SBC5CoordinatorData) -> float | None:\n''',
    '''def _predictor_number(data: SBC5CoordinatorData, key: str) -> float | None:\n    value = data.thermal_predictor.get(key)\n    try:\n        return round(float(value), 2) if value is not None else None\n    except (TypeError, ValueError):\n        return None\n\n\ndef _cpu_usage_percent(data: SBC5CoordinatorData) -> float | None:\n''',
)
replace_once(
    "custom_components/sbc5_control_center/sensor.py",
    '''SENSOR_SPECS: tuple[SensorSpec, ...] = (\n    SensorSpec(unique_id="sbc5_cpu_temperature",''',
    '''SENSOR_SPECS: tuple[SensorSpec, ...] = (\n    SensorSpec(unique_id="sbc5_ai_thermal_forecast_30s", name="SBC5 AI Thermal Forecast 30s",\n               value_fn=lambda d: _predictor_number(d, "forecast_30s_c"), icon="mdi:thermometer-chevron-up",\n               unit=UnitOfTemperature.CELSIUS, device_class=SensorDeviceClass.TEMPERATURE,\n               state_class=SensorStateClass.MEASUREMENT),\n    SensorSpec(unique_id="sbc5_ai_thermal_forecast_60s", name="SBC5 AI Thermal Forecast 60s",\n               value_fn=lambda d: _predictor_number(d, "forecast_60s_c"), icon="mdi:thermometer-chevron-up",\n               unit=UnitOfTemperature.CELSIUS, device_class=SensorDeviceClass.TEMPERATURE,\n               state_class=SensorStateClass.MEASUREMENT),\n    SensorSpec(unique_id="sbc5_ai_thermal_forecast_120s", name="SBC5 AI Thermal Forecast 120s",\n               value_fn=lambda d: _predictor_number(d, "forecast_120s_c"), icon="mdi:thermometer-chevron-up",\n               unit=UnitOfTemperature.CELSIUS, device_class=SensorDeviceClass.TEMPERATURE,\n               state_class=SensorStateClass.MEASUREMENT),\n    SensorSpec(unique_id="sbc5_ai_thermal_predictor_confidence", name="SBC5 AI Thermal Predictor Confidence",\n               value_fn=lambda d: _predictor_number(d, "confidence_percent"), icon="mdi:brain",\n               unit=PERCENTAGE, state_class=SensorStateClass.MEASUREMENT),\n    SensorSpec(unique_id="sbc5_cpu_temperature",''',
)

# Registry migration + stable DeviceInfo connection reconciliation.
replace_once(
    "custom_components/sbc5_control_center/__init__.py",
    '''from homeassistant.helpers import entity_registry as er\nfrom homeassistant.helpers import issue_registry as ir\n\nfrom .const import APP_VERSION, DOMAIN, LEGACY_DOMAIN, OLDER_LEGACY_DOMAIN, LEGACY_ENTITIES, PLATFORMS\n''',
    '''from homeassistant.helpers import device_registry as dr\nfrom homeassistant.helpers import entity_registry as er\nfrom homeassistant.helpers import issue_registry as ir\n\nfrom .const import APP_VERSION, DEVICE_IDENTIFIER, DOMAIN, LEGACY_DOMAIN, OLDER_LEGACY_DOMAIN, LEGACY_ENTITIES, PLATFORMS\n''',
)
insert_anchor = '''def _remove_deprecated_native_update_entity(hass: HomeAssistant) -> None:\n'''
insert_code = '''PREDICTOR_NATIVE_IDS = {\n    "sbc5_ai_thermal_forecast_30s",\n    "sbc5_ai_thermal_forecast_60s",\n    "sbc5_ai_thermal_forecast_120s",\n    "sbc5_ai_thermal_predictor_confidence",\n}\n\n\ndef _migrate_predictor_template_entities(hass: HomeAssistant) -> None:\n    \"\"\"Free the 3.1.1 package-template IDs before native sensors register.\n\n    Recorder history is keyed by entity_id, so the native sensors reclaim the same\n    canonical IDs after these template registry rows are removed.\n    \"\"\"\n    registry = er.async_get(hass)\n    data = hass.data.setdefault(DOMAIN, {})\n    overrides: dict[str, str] = data.setdefault("entity_id_overrides", {})\n    for unique_id in PREDICTOR_NATIVE_IDS:\n        canonical = f"sensor.{unique_id}"\n        for entry in list(registry.entities.values()):\n            if entry.unique_id != unique_id or not entry.entity_id.startswith("sensor."):\n                continue\n            if entry.platform == DOMAIN:\n                continue\n            overrides[unique_id] = canonical\n            _LOGGER.info("Migrating AI Thermal Predictor entity %s to native SBC5 integration", entry.entity_id)\n            registry.async_remove(entry.entity_id)\n\n\ndef _valid_mac(value: str) -> bool:\n    parts = (value or "").strip().lower().split(":")\n    return len(parts) == 6 and all(\n        len(part) == 2 and all(ch in "0123456789abcdef" for ch in part) for part in parts\n    ) and value.lower() != "00:00:00:00:00:00"\n\n\ndef _reconcile_device_connections(hass: HomeAssistant, coordinator: SBC5Coordinator) -> None:\n    \"\"\"Replace accumulated container MACs with the single physical host MAC.\"\"\"\n    telemetry = getattr(getattr(coordinator, "data", None), "telemetry", None)\n    mac = (getattr(telemetry, "network_mac", "") or "").strip().lower()\n    if not _valid_mac(mac):\n        return\n    registry = dr.async_get(hass)\n    device = next(\n        (d for d in registry.devices.values() if (DOMAIN, DEVICE_IDENTIFIER) in d.identifiers),\n        None,\n    )\n    if device is None:\n        return\n    desired = {(dr.CONNECTION_NETWORK_MAC, mac)}\n    if device.connections != desired:\n        registry.async_update_device(device.id, new_connections=desired)\n        _LOGGER.info("Reconciled SBC5 device network identity to physical host MAC %s", mac)\n\n\n'''
replace_once(
    "custom_components/sbc5_control_center/__init__.py",
    insert_anchor,
    insert_code + insert_anchor,
)
replace_once(
    "custom_components/sbc5_control_center/__init__.py",
    '''    _remove_deprecated_native_update_entity(hass)\n    await _prepare_sbc5_namespace_registry(hass)\n    _canonicalize_native_entity_registry(hass)\n\n    coordinator = SBC5Coordinator(hass, entry)\n    await coordinator.async_config_entry_first_refresh()\n    entry.runtime_data = coordinator\n\n    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)\n''',
    '''    _remove_deprecated_native_update_entity(hass)\n    await _prepare_sbc5_namespace_registry(hass)\n    _migrate_predictor_template_entities(hass)\n    _canonicalize_native_entity_registry(hass)\n\n    coordinator = SBC5Coordinator(hass, entry)\n    await coordinator.async_config_entry_first_refresh()\n    entry.runtime_data = coordinator\n    _reconcile_device_connections(hass, coordinator)\n\n    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)\n''',
)

print("3.1.2 integration behavior patch applied")
