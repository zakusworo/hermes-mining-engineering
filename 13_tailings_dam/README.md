# Exercise 13: Tailings Dam Stability

## Goal
Teach Hermes to assess tailings dam stability under static and seismic conditions.

## Engineering Focus
45 m high tailings storage facility. Engineers check FOS for normal operation and pseudo-static earthquake.

## Hermes Commands
```text
/hermes -w
/skill mining-engineering
/init
```

## Before Prompt (vague)
```
Check if the tailings dam is safe.
```

## After Prompt (precise)
```
Read exercise.py. The tailings dam:
- Height = 45 m
- Crest width = 8 m
- Upstream slope = 3H:1V (18.4°)
- Downstream slope = 2.5H:1V (21.8°)
- Tailings: γ = 18 kN/m³, c = 20 kPa, φ = 22°
- Foundation: c = 50 kPa, φ = 30°

Calculate:
1. Bishop FOS for static condition (minimum 1.5)
2. Pseudo-static seismic FOS with kh = 0.15g (minimum 1.1)
3. ANCOLD consequence category based on population downstream
4. Required monitoring instrumentation

Plot cross-section with phreatic surface and failure circles.
Run pytest tests/test_slope_stability.py.
```

## Learning Objective
- Tailings dam = special case of slope stability
- Pseudo-static seismic analysis (kh)
- ANCOLD consequence category drives design standard

## Illustrated Output

![Tailings Dam Cross-Section](assets/figures/13_tailings_cross_section.png)
