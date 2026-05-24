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
