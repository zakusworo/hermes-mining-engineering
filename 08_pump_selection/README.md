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
