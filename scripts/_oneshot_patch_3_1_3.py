#!/usr/bin/env python3
from pathlib import Path

p = Path('custom_components/sbc5_control_center/sensor.py')
text = p.read_text(encoding='utf-8')
if 'import time\n' not in text:
    text = text.replace('from dataclasses import dataclass\n', 'from dataclasses import dataclass\nimport time\n', 1)

anchor = 'def _cpu_usage_percent(data: SBC5CoordinatorData) -> float | None:\n'
helpers = '''def _predictor_nested_number(data: SBC5CoordinatorData, group: str, key: str) -> float | None:
    values = data.thermal_predictor.get(group)
    if not isinstance(values, dict):
        return None
    try:
        value = values.get(key)
        return round(float(value), 3) if value is not None else None
    except (TypeError, ValueError):
        return None


def _predictor_validated_total(data: SBC5CoordinatorData) -> int | None:
    direct = data.thermal_predictor.get("validated_samples_total")
    try:
        if direct is not None:
            return int(direct)
    except (TypeError, ValueError):
        pass
    values = data.thermal_predictor.get("validated_samples")
    if not isinstance(values, dict):
        return None
    total = 0
    found = False
    for horizon in ("30", "60", "120"):
        try:
            value = values.get(horizon)
            if value is not None:
                total += int(value)
                found = True
        except (TypeError, ValueError):
            continue
    return total if found else None


def _predictor_age_seconds(data: SBC5CoordinatorData) -> float | None:
    try:
        updated = float(data.thermal_predictor.get("updated_epoch"))
    except (TypeError, ValueError):
        return None
    if updated <= 0:
        return None
    return round(max(0.0, time.time() - updated), 1)


'''
if '_predictor_nested_number' not in text:
    if anchor not in text:
        raise SystemExit('helper anchor missing')
    text = text.replace(anchor, helpers + anchor, 1)

confidence = '''    SensorSpec(unique_id="sbc5_ai_thermal_predictor_confidence", name="SBC5 AI Thermal Predictor Confidence",
               value_fn=lambda d: _predictor_number(d, "confidence_percent"), icon="mdi:brain",
               unit=PERCENTAGE, state_class=SensorStateClass.MEASUREMENT),
'''
extra = confidence + '''    SensorSpec(unique_id="sbc5_ai_thermal_predictor_mae", name="SBC5 AI Thermal Predictor Average MAE",
               value_fn=lambda d: _predictor_number(d, "average_mae_c"), icon="mdi:chart-bell-curve",
               unit=UnitOfTemperature.CELSIUS, state_class=SensorStateClass.MEASUREMENT),
    SensorSpec(unique_id="sbc5_ai_thermal_predictor_mae_30s", name="SBC5 AI Thermal Predictor MAE 30s",
               value_fn=lambda d: _predictor_nested_number(d, "mae_ema_c", "30"), icon="mdi:chart-timeline-variant",
               unit=UnitOfTemperature.CELSIUS, state_class=SensorStateClass.MEASUREMENT),
    SensorSpec(unique_id="sbc5_ai_thermal_predictor_mae_60s", name="SBC5 AI Thermal Predictor MAE 60s",
               value_fn=lambda d: _predictor_nested_number(d, "mae_ema_c", "60"), icon="mdi:chart-timeline-variant",
               unit=UnitOfTemperature.CELSIUS, state_class=SensorStateClass.MEASUREMENT),
    SensorSpec(unique_id="sbc5_ai_thermal_predictor_mae_120s", name="SBC5 AI Thermal Predictor MAE 120s",
               value_fn=lambda d: _predictor_nested_number(d, "mae_ema_c", "120"), icon="mdi:chart-timeline-variant",
               unit=UnitOfTemperature.CELSIUS, state_class=SensorStateClass.MEASUREMENT),
    SensorSpec(unique_id="sbc5_ai_thermal_predictor_last_error_30s", name="SBC5 AI Thermal Predictor Last Error 30s",
               value_fn=lambda d: _predictor_nested_number(d, "last_error_c", "30"), icon="mdi:delta",
               unit=UnitOfTemperature.CELSIUS, state_class=SensorStateClass.MEASUREMENT),
    SensorSpec(unique_id="sbc5_ai_thermal_predictor_last_error_60s", name="SBC5 AI Thermal Predictor Last Error 60s",
               value_fn=lambda d: _predictor_nested_number(d, "last_error_c", "60"), icon="mdi:delta",
               unit=UnitOfTemperature.CELSIUS, state_class=SensorStateClass.MEASUREMENT),
    SensorSpec(unique_id="sbc5_ai_thermal_predictor_last_error_120s", name="SBC5 AI Thermal Predictor Last Error 120s",
               value_fn=lambda d: _predictor_nested_number(d, "last_error_c", "120"), icon="mdi:delta",
               unit=UnitOfTemperature.CELSIUS, state_class=SensorStateClass.MEASUREMENT),
    SensorSpec(unique_id="sbc5_ai_thermal_predictor_slope", name="SBC5 AI Thermal Predictor Slope",
               value_fn=lambda d: _predictor_number(d, "slope_c_per_min"), icon="mdi:trending-up",
               unit="°C/min", state_class=SensorStateClass.MEASUREMENT),
    SensorSpec(unique_id="sbc5_ai_thermal_predictor_samples", name="SBC5 AI Thermal Predictor Validated Samples",
               value_fn=_predictor_validated_total, icon="mdi:counter", state_class=SensorStateClass.MEASUREMENT),
    SensorSpec(unique_id="sbc5_ai_thermal_predictor_age", name="SBC5 AI Thermal Predictor Data Age",
               value_fn=_predictor_age_seconds, icon="mdi:timer-sand", unit="s", state_class=SensorStateClass.MEASUREMENT),
    SensorSpec(unique_id="sbc5_network_mac", name="SBC5 Network MAC",
               value_fn=lambda d: d.telemetry.network_mac or None, icon="mdi:lan-connect"),
    SensorSpec(unique_id="sbc5_network_interface", name="SBC5 Network Interface",
               value_fn=lambda d: d.telemetry.network_interface or None, icon="mdi:ethernet"),
'''
if 'sbc5_ai_thermal_predictor_mae"' not in text:
    if confidence not in text:
        raise SystemExit('confidence anchor missing')
    text = text.replace(confidence, extra, 1)

p.write_text(text, encoding='utf-8')
print('HACS 3.1.3 sensor diagnostics applied')
