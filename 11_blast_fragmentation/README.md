# Exercise 11: Blast Fragmentation and Digging Rate

## Goal
Teach Hermes to optimize blast fragmentation for loader productivity.

## Engineering Focus
Open-pit gold mine. Finer fragmentation = faster digging = lower cost per tonne.

## Hermes Commands
```text
/hermes -w
/skill mining-engineering
/init
```

## Before Prompt (vague)
```
Improve blast fragmentation.
```

## After Prompt (precise)
```
Read exercise.py. Current blast:
- Burden = 4.5 m, spacing = 5.4 m
- Hole depth = 16 m
- Powder factor = 0.38 kg/m³
- Desired d80 = 0.45 m (passes 80% at 0.45 m)

Calculate:
1. Current fragmentation curve (Rosin-Rammler approximation)
2. Required powder factor to achieve d80 = 0.45 m
3. Digging rate: current vs improved (assume rate ∝ 1/d80)
4. Cost-benefit: extra explosive cost vs loader productivity gain

Plot fragmentation curves (current vs improved) with d80 target line.
Run pytest tests/test_blasting.py.
```

## Learning Objective
- Powder factor controls fragmentation
- Fragmentation affects digging rate and cost
- Optimal PF balances explosive cost vs productivity

## Illustrated Output

![Fragmentation Curve](assets/figures/11_blast_fragmentation_curve.png)

## Sample Output

```text
============================================================
EXERCISE 11: Blast Fragmentation and Digging Rate
============================================================

[Task 1] Current vs Target
  Volume/hole:      315.0 m³
  Current charge:   119.7 kg (PF=0.38)
  Target charge:    163.8 kg (PF=0.52)
  Increase:         +44.1 kg/hole (+37%)

[Task 2] Blast Design
  Holes per round:  ~40 (for 800 m² face)
  Total charge:     6552 kg
  Powder factor:    0.52 kg/m³

[Task 3] Truck Loads
  Swell volume:     17010 m³
  12 m³ loads:      1418 loads

[Task 4] Digging Rate
  Current d80 ~0.65 m → 180 t/h digging rate
  Target d80 ~0.45 m → 240 t/h digging rate (+33%)
  Annual benefit:   +20% loader productivity

[Task 5] Cost-Benefit
  Extra explosive cost: $4410/round
  Productivity benefit: $23389/round (simplified)

============================================================
Exercise 11 complete.
============================================================
```
