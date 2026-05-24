# Exercise 10: Bench Design Across Geotechnical Domains

## Goal
Teach Hermes to design bench geometry that satisfies inter-ramp and overall slope constraints.

## Engineering Focus
Open-pit iron ore mine crossing 3 geotechnical domains with different bench parameters.

## Hermes Commands
```text
/hermes -w
/skill mining-engineering
/init
```

## Before Prompt (vague)
```
Design benches for the pit.
```

## After Prompt (precise)
```
Read exercise.py. The mine crosses 3 domains:
- Hard iron formation: benches 15 m, face 70°, berm 8 m
- Transitional zone: benches 12 m, face 60°, berm 10 m
- Weathered zone: benches 10 m, face 45°, berm 12 m

For each domain:
1. Calculate inter-ramp angle
2. Calculate overall slope angle for 5 benches
3. Check if overall angle ≤ 45° (regulatory)
4. Which domain governs the pit wall design?

Plot cross-section showing bench, berm, and overall slope for the critical domain.
Run pytest tests/test_slope_stability.py.
```

## Learning Objective
- Bench height × face angle × berm width = inter-ramp angle
- Overall slope angle ≤ regulatory limit
- Weakest domain governs wall design

## Illustrated Output

![Bench Cross-Section](assets/figures/10_bench_cross_section.png)
