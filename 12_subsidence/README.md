# Exercise 12: Subsidence Prediction for Underground Mine

## Goal
Teach Hermes to predict surface subsidence from longwall mining using empirical methods.

## Engineering Focus
Longwall coal mine at 280 m depth. Engineers predict maximum subsidence, angle of draw, and affected area.

## Hermes Commands
```text
/hermes -w
/skill mining-engineering
/init
```

## Before Prompt (vague)
```
Predict ground settlement above the mine.
```

## After Prompt (precise)
```
Read exercise.py. Longwall panel:
- Depth = 280 m
- Seam thickness = 3.5 m
- Panel width = 220 m, length = 1800 m
- Subsidence factor = 0.90

Calculate:
1. Maximum subsidence (S_max = factor × seam thickness)
2. Angle of draw (≈ 35° from UK NCB)
3. Subsidence profile over panel center using Gaussian
4. Total affected surface area
5. At what distance does subsidence drop below 50 mm? (building damage threshold)

Plot subsidence profile (m) vs distance from panel center (m).
Show building damage threshold at 50 mm.
```

## Learning Objective
- UK NCB empirical subsidence method
- Gaussian profile approximation
- Building damage threshold (50 mm)

## Illustrated Output

![Subsidence Profile](assets/figures/12_subsidence_profile.png)

## Sample Output

```text
============================================================
EXERCISE 12: Subsidence Prediction
============================================================

[Task 1] Maximum Subsidence
  Width/depth ratio: 0.79
  S_max:             2.06 m
  As % of thickness: 59%

[Task 2] Subsidence Profile
  x=-300 m → S=0.000 m
  x=-150 m → S=0.050 m
  x= -50 m → S=1.364 m
  x=   0 m → S=2.062 m
  x=  50 m → S=1.364 m
  x= 150 m → S=0.050 m
  x= 300 m → S=0.000 m

[Task 3] Surface Impact at 150 m from edge
  Angle of draw:     35.0°
  Influence zone:    ±400 m from panel edge
  150 m from edge:   WITHIN influence zone
  Expected subsidence: ~0.62 m

[Task 4] Monitoring and Mitigation
  → Survey prisms every 50 m along transects
  → InSAR satellite monitoring monthly
  → Crack gauges on structures within influence zone
  → Pre-load foundations in high-risk area
  → Grout injection if tilt > 5 mm/m

============================================================
Exercise 12 complete.
============================================================
```
