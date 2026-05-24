# Exercise 8: Pump Selection and System Curve

## Goal
Teach Hermes to match pump performance curves with system requirements.

## Engineering Focus
Variable inflow dewatering system. Engineers select pumps that can handle both minimum and maximum flow at required head.

## Hermes Commands
```text
/hermes -w
/skill mining-engineering
/init
```

## Before Prompt (vague)
```
Pick a pump for the dewatering system.
```

## After Prompt (precise)
```
Read exercise.py. The dewatering system needs:
- Min flow: 200 m³/h (dry season)
- Max flow: 850 m³/h (wet season)
- Static head: 85 m
- Pipeline: 1200 m, 0.35 m diameter
- Hazen-Williams C=120

Calculate:
1. System curve: head vs flow (static + friction)
2. Operating point with a single pump (H = 140 - 0.00008·Q²)
3. Is a single pump sufficient for max flow?
4. If not, propose a VSD pump and estimate energy savings

Plot system curve + pump curve, mark operating point.
Run pytest tests/test_dewatering.py.
```

## Learning Objective
- System curve = static head + friction head
- Operating point = system curve ∩ pump curve
- VSD pumps for variable inflow = energy savings

## Illustrated Output

![Pump System Curve](assets/figures/08_pump_system_curve.png)

## Sample Output

```text
============================================================
EXERCISE 8: Pump Selection and System Curve
============================================================

[Task 1] System Curve
  Q=200 m³/h → v=0.58 m/s → hf=1.2 m → H=86.2 m
  Q=400 m³/h → v=1.15 m/s → hf=4.7 m → H=89.7 m
  Q=600 m³/h → v=1.73 m/s → hf=10.5 m → H=95.5 m
  Q=850 m³/h → v=2.45 m/s → hf=21.0 m → H=106.0 m

[Task 2] NPSH Available
  Q=200 m³/h → NPSHa=2.57 m → margin=-2.93 m
  Q=400 m³/h → NPSHa=2.57 m → margin=-2.93 m
  Q=600 m³/h → NPSHa=2.57 m → margin=-2.93 m
  Q=850 m³/h → NPSHa=2.57 m → margin=-2.93 m

[Task 3] Pump Selection
  Type: Horizontal split-case centrifugal
  Speed: 4-pole (1480 rpm) for NPSH margin
  Number: 3 duty + 1 standby
  Capacity each: 300 m³/h

[Task 4] VSD Recommendation
  Dry season: 1 pump @ 67% speed (flow ∝ speed)
  Wet season: 3 pumps @ 100% speed

[Task 5] Energy Savings
  Throttling: 850 m³/h @ 100% speed, 65% efficiency
  VSD: 850 m³/h @ 95% speed, 72% efficiency
  Estimated savings: ~15-20% annual energy

============================================================
Exercise 8 complete.
============================================================
```
