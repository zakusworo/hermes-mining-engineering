# Exercise 6: Groundwater Inflow Estimation

## Goal
Teach Hermes to estimate steady-state groundwater inflow using the Theim equation and size dewatering infrastructure.

## Engineering Focus
Open-pit copper mine intersecting a confined aquifer. Engineers estimate dewatering rates and annual pumping cost.

## Hermes Commands
```text
/hermes -w
/skill mining-engineering
/init
```

## Before Prompt (vague)
```
Calculate how much water comes into the pit.
```

## After Prompt (precise)
```
Read exercise.py. The open-pit intersects a confined aquifer with:
- Hydraulic conductivity k = 8.5 m/day
- Aquifer thickness = 45 m
- Pit base = -85 m, water table = +5 m
- Pit area = 125,000 m²

Calculate:
1. Steady-state inflow using the Theim equation for a large diameter well
2. Drawdown at the pit wall
3. Number of dewatering wells (assume 150 m³/h each)
4. Annual pumping cost at $0.08/kWh, pump efficiency 75%

Plot inflow (m³/h) vs drawdown (m) for k=5, 8.5, 15 m/day.
Run pytest tests/test_dewatering.py.
```

## Learning Objective
- Steady-state groundwater inflow (Theim)
- Dewatering well sizing and cost estimation
- Sensitivity to hydraulic conductivity

## Illustrated Output

![Groundwater Inflow vs Drawdown](assets/figures/06_groundwater_inflow_drawdown.png)
