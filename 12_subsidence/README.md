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
