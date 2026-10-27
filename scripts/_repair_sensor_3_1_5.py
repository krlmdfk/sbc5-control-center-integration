#!/usr/bin/env python3
from __future__ import annotations
import subprocess
from pathlib import Path

path = Path('custom_components/sbc5_control_center/sensor.py')
base = subprocess.check_output(['git','show','origin/main:custom_components/sbc5_control_center/sensor.py'], text=True)
anchor = '''    SensorSpec(unique_id="sbc5_ai_thermal_predictor_age", name="SBC5 AI Thermal Predictor Data Age",\n               value_fn=_predictor_age_seconds, icon="mdi:timer-sand", unit="s", state_class=SensorStateClass.MEASUREMENT),\n'''
addition = anchor + '''    SensorSpec(unique_id="sbc5_ai_thermal_shadow_delta", name="SBC5 AI Thermal Shadow Delta",\n               value_fn=lambda d: _predictor_nested_number(d, "shadow_assist", "suggested_delta_pp"), icon="mdi:plus-minus-variant",\n               unit="pp", state_class=SensorStateClass.MEASUREMENT),\n    SensorSpec(unique_id="sbc5_ai_thermal_shadow_pwm", name="SBC5 AI Thermal Shadow PWM",\n               value_fn=lambda d: _predictor_nested_number(d, "shadow_assist", "suggested_pwm_percent"), icon="mdi:fan-auto",\n               unit=PERCENTAGE, state_class=SensorStateClass.MEASUREMENT),\n    SensorSpec(unique_id="sbc5_ai_thermal_shadow_state", name="SBC5 AI Thermal Shadow State",\n               value_fn=lambda d: (d.thermal_predictor.get("shadow_assist") or {}).get("gate_reason") if isinstance(d.thermal_predictor.get("shadow_assist"), dict) else None, icon="mdi:shield-search"),\n    SensorSpec(unique_id="sbc5_ai_thermal_shadow_decision", name="SBC5 AI Thermal Shadow Decision",\n               value_fn=lambda d: (d.thermal_predictor.get("shadow_assist") or {}).get("decision_reason") if isinstance(d.thermal_predictor.get("shadow_assist"), dict) else None, icon="mdi:brain"),\n    SensorSpec(unique_id="sbc5_ai_thermal_shadow_weighted_forecast", name="SBC5 AI Thermal Shadow Weighted Forecast",\n               value_fn=lambda d: _predictor_nested_number(d, "shadow_assist", "weighted_forecast_c"), icon="mdi:thermometer-lines",\n               unit=UnitOfTemperature.CELSIUS, device_class=SensorDeviceClass.TEMPERATURE, state_class=SensorStateClass.MEASUREMENT),\n'''
if anchor not in base:
    raise SystemExit('predictor age anchor missing in HACS main sensor.py')
path.write_text(base.replace(anchor, addition, 1), encoding='utf-8')
print('Rebuilt HACS sensor.py from main + five 3.1.5 Shadow Assist sensors')
