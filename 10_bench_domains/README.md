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

## Sample Output

```text
============================================================
EXERCISE 10: Bench Design Across Geotechnical Domains
============================================================

[Task 1-3] Bench Design Comparison

  Hard iron formation:
    Bench height:        15 m
    Bench face angle:    70°
    Berm width:          10 m
    Inter-ramp angle:    44.1°
    Overall slope:       39.1°
    Catch capacity:      75 m³/m
    Status:              OK

  Transitional zone:
    Bench height:        12 m
    Bench face angle:    55°
    Berm width:          8 m
    Inter-ramp angle:    36.2°
    Overall slope:       31.7°
    Catch capacity:      48 m³/m
    Status:              OK

  Weathered oxide:
    Bench height:        8 m
    Bench face angle:    45°
    Berm width:          6 m
    Inter-ramp angle:    29.7°
    Overall slope:       25.2°
    Catch capacity:      24 m³/m
    Status:              OK

[Task 4] Rockfall Containment
  Hard domain: 10 m berm (catches 90% of design rockfall)
  Transitional: 8 m berm + shotcrete face
  Weathered: 6 m berm + mesh + bench scaling

[Task 5] Domain Transition
  → 20 m wide step-out at domain boundary
  → Additional berm + monitoring prisms
  →
... (truncated)
```
