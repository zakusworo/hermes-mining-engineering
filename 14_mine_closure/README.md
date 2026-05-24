# Exercise 14: Mine Closure and Reclamation Water Balance

## Goal
Teach Hermes to predict pit lake evolution after mine closure and estimate reclamation cost.

## Engineering Focus
Closed open-pit mine becoming a pit lake. Engineers balance rainfall, runoff, evaporation, and groundwater.

## Hermes Commands
```text
/hermes -w
/skill mining-engineering
/init
```

## Before Prompt (vague)
```
What happens to the pit after we close the mine?
```

## After Prompt (precise)
```
Read exercise.py. The closed pit:
- Dimensions: 800 m × 600 m × 180 m deep
- Annual rainfall = 650 mm
- Evaporation = 1800 mm/year
- Catchment area = 2.5 × pit area
- Groundwater inflow = 15 m³/h

Calculate:
1. Annual water balance: inflows vs outflows
2. Net accumulation or deficit (m³/year)
3. Time to fill to 80% capacity (or if it never fills)
4. Steady-state lake elevation
5. Closure cost estimate: $2.5M base + $150k/year monitoring

Plot water balance bar chart: rainfall, runoff, groundwater, evaporation.
```

## Learning Objective
- Water balance = inflows – outflows
- Evaporation can exceed rainfall → lake may not fill
- Closure cost = capital + perpetual monitoring

## Illustrated Output

![Closure Water Balance](assets/figures/14_closure_water_balance.png)
