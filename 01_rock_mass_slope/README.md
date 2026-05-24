# Exercise 1: Rock Mass Characterization and Slope Stability

## Goal
Teach Hermes to explore drill core data and rock mass classification before designing slopes.

## Engineering Focus
Open-pit granite mine. Engineers classify rock mass (RQD, RMR, GSI), predict Hoek-Brown strength, then check slope stability with Bishop simplified method.

## Hermes Commands
```text
/hermes -w
/skill mining-engineering
/init
```

## Before Prompt (vague)
```
Analyze the rock data and check slope stability.
```

## After Prompt (precise)
```
Read exercise.py. The drill core lengths are: [18, 12, 25, 8, 30, 15, 22, 10, 28, 20, 14, 26, 19, 11, 23, 16, 27, 13, 21, 17] cm.
Calculate RQD (only pieces >= 10 cm).
Then estimate GSI from RMR using the relationship GSI ≈ RMR - 5 for RMR > 25.
Get Hoek-Brown parameters for mi=25, D=0.5, sigma_ci=150 MPa.
Convert to Mohr-Coulomb cohesion and friction angle.
Run Bishop FOS for a 150 m high slope at 42° with these parameters.
Plot GSI vs rock mass strength for mi=15, 25, 35 on one figure.
Run pytest tests/test_rock_mechanics.py and tests/test_slope_stability.py.
```

## Learning Objective
- Understand RQD → RMR → GSI → Hoek-Brown workflow
- See how rock mass strength differs from intact rock strength
- Verify slope FOS against minimum thresholds (FOS ≥ 1.3 temporary, ≥ 1.5 permanent)

## Sample Output

```text
============================================================
EXERCISE 1: Rock Mass Characterization and Slope Stability
============================================================

[Task 1] Rock Mass Rating
  RQD:           95.6%
  Basic RMR:     59/100
  Classification: Fair rock
  Estimated GSI:  54

[Task 2] Hoek-Brown Parameters
  mb:            0.067
  s:             0.006029
  a:             0.5
  E_rm:          21160.0 MPa
  σ_cm:          0.005 MPa

[Task 3] Mohr-Coulomb Equivalent
  Cohesion (c):   4.10 MPa
  Friction (φ):   7.3°
  Tensile:        -10.80 MPa

[Task 4] Slope Stability
  Factor of Safety: 35.88
  Status:           stable (low risk)
  Action:           Continue operations, routine monitoring

[Task 5] Bench Design (Hard Rock)
  Inter-ramp angle: 45.0°
  Overall slope:    39.8°
  Catch capacity:   60 m³/m
  Status:           OK

============================================================
Exercise 1 complete.
============================================================
```
