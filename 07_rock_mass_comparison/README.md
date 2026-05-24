# Exercise 7: Rock Mass Comparison — Granite vs. Shale

## Goal
Teach Hermes to compare rock masses quantitatively and select appropriate support systems.

## Engineering Focus
Two rock types encountered in an underground development. Engineers compare strength, deformability, and support requirements.

## Hermes Commands
```text
/hermes -w
/skill mining-engineering
/init
```

## Before Prompt (vague)
```
Compare the two rock types.
```

## After Prompt (precise)
```
Read exercise.py. Two rock masses:
- Granite: mi=25, GSI=65, D=0.2, UCS=140 MPa
- Shale: mi=8, GSI=35, D=0.5, UCS=45 MPa

Calculate for each:
1. Hoek-Brown parameters (mb, s, a)
2. Rock mass modulus E_rm
3. Rock mass strength σ_cm
4. Mohr-Coulomb cohesion and friction angle

Then:
- Which rock needs more support? (bolts vs shotcrete vs arch)
- At what stress level does each fail?

Plot a bar chart: E_rm, cohesion, friction angle, σ_cm for both rocks side by side.
Run pytest tests/test_rock_mechanics.py.
```

## Learning Objective
- Rock mass classification drives support design
- Quantitative comparison with empirical parameters
- Support selection based on deformability and strength

## Illustrated Output

![Rock Mass Comparison](assets/figures/07_rock_comparison_bar.png)

## Sample Output

```text
============================================================
EXERCISE 7: Rock Mass Comparison
============================================================

[Granite]
  mb=0.436, s=0.0205, a=0.5
  E_rm=12250 MPa
  c=7.33 MPa, φ=17.6°
  σ_cm=0.06 MPa
  σ_t=-6.57 MPa
  Support: Rock bolts + shotcrete + mesh

[Shale]
  mb=0.001, s=0.0007, a=0.5
  E_rm=22452 MPa
  c=0.60 MPa, φ=0.5°
  σ_cm=0.00 MPa
  σ_t=-32.85 MPa
  Support: Rock bolts + mesh (minimal)

============================================================
Exercise 7 complete.
============================================================
```
