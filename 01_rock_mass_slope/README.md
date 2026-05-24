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
