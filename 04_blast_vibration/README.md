# Exercise 4: Blast Design and Vibration Control

## Goal
Teach Hermes to optimize blast design while keeping vibration within regulatory limits.

## Engineering Focus
Open-pit gold mine near residential area. Bench height 15 m, hole diameter 150 mm.
Engineers design blast pattern, predict PPV, and check compliance.

## Hermes Commands
```text
/hermes -w
/skill mining-engineering
/init
```

## Before Prompt (vague)
```
Make sure the blast doesn't damage houses.
```

## After Prompt (precise)
```
Read exercise.py. The mine blasts near a residential area:
- Bench: 15 m
- Hole diameter: 150 mm
- Rock: weathered granite, mi=18
- Nearest house: 350 m
- Regulatory limit: 5 mm/s (residential)

Calculate:
1. Blast design: burden, spacing, stemming, subdrill, charge per hole, powder factor
2. PPV at 350 m using USBM RI 8507 with K=800, α=1.6
3. Compliance assessment (pass/fail + safety margin)
4. If fail: redesign with reduced charge per delay

Plot PPV vs distance for 25, 80, and 200 kg/delay on one figure.
Show regulatory limit lines (5 mm/s residential, 10 mm/s industrial).
Run pytest tests/test_blasting.py.
```

## Learning Objective
- USBM scaling law for blast vibration
- Site-specific constants (K, α) and their physical meaning
- Regulatory compliance assessment
