# Exercise 9: Slope Stability with Groundwater

## Goal
Teach Hermes to assess how groundwater affects slope stability and set drainage requirements.

## Engineering Focus
120 m high open-pit slope with varying groundwater conditions. Engineers need FOS under dry, moderate, and wet conditions.

## Hermes Commands
```text
/hermes -w
/skill mining-engineering
/init
```

## Before Prompt (vague)
```
Check if the slope is safe when it rains.
```

## After Prompt (precise)
```
Read exercise.py. A 120 m high slope with:
- Cohesion c = 85 kPa
- Friction φ = 38°
- Unit weight γ = 24 kN/m³
- Slope angle = 38°
- Pore pressure ratios: ru = 0.05, 0.15, 0.30

Calculate Bishop FOS for each ru.
Determine:
- At what ru does FOS drop below 1.3? (minimum temporary)
- What drainage system is needed to keep ru ≤ 0.15?

Plot FOS vs ru (0–0.5) with critical thresholds at FOS=1.0 and FOS=1.3.
Run pytest tests/test_slope_stability.py.
```

## Learning Objective
- Groundwater is the #1 enemy of slope stability
- Pore pressure ratio ru and its effect on FOS
- Drainage design target: keep ru below critical

## Illustrated Output

![Slope FOS vs Groundwater](assets/figures/09_slope_fos_ru.png)
