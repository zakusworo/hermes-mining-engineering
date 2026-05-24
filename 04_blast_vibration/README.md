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

## Sample Output

```text
============================================================
EXERCISE 4: Blast Design and Vibration Control
============================================================

[Task 1] Blast Design
  Hole diameter:    150.0 mm
  Hole depth:       16.4 m
  Burden:           4.5 m
  Spacing:          5.4 m
  Stemming:         3.1 m
  Subdrill:         1.3 m
  Charge/hole:      167.5 kg
  Volume/hole:      364.5 m³
  Powder factor:    0.460 kg/m³
  Status:           OK

[Task 2] Blast Vibration at 350.0m
  Predicted PPV:    3.4 mm/s
  Regulatory limit:   5.0 mm/s
  Exceedance:       0.68×
  Status:           acceptable
  Action:           Monitor vibrations, maintain current practices

[Task 3] Air Overpressure
  Predicted OP:     52.3 dB
  Threshold:        115 dB
  Status:           acceptable
  Action:           No air blast concerns

[Task 5] Monitoring Strategy
  Annual rounds:    520
  Monitoring:       Continuous seismograph at house + 2 mid-field stations
  Trigger level:    2.5 mm/s (50% of limit)
  Alarm level:      4.0 mm/s (80% of limit)
  Reporting:        Daily blast report to regulator
  Community:        Pre-blast notification app

===========================================
... (truncated)
```
