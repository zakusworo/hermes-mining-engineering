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
