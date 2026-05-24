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

## Sample Output

```text
============================================================
EXERCISE 9: Slope Stability with Groundwater
============================================================

[Task 1] FOS vs Pore Pressure
  ru=0.05 (dry            ) → FOS=4.75 → stable
  ru=0.15 (moderate       ) → FOS=4.25 → stable
  ru=0.30 (heavy rainfall ) → FOS=3.50 → stable

[Task 2] Critical ru for FOS=1.0
  Critical ru ≈ 0.500 (FOS=2.500)

[Task 3] Drainage Measures
  → Horizontal drain holes: 50 mm, 30 m long, 5 m spacing
  → Drainage blanket at toe
  → Pumped wells if ru > 0.20
  → Monitor piezometers weekly

[Task 4] Bench Design (ru=0.30)
  Inter-ramp angle: 38.8°
  Overall slope:    33.8°
  Status:           REVIEW — Bench height > 10m for soft_rock

============================================================
Exercise 9 complete.
============================================================
```
