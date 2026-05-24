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

## Sample Output

```text
============================================================
EXERCISE 14: Mine Closure Water Balance
============================================================

[Task 1] Water Balance
  Rainfall on pit:    +312000 m³/year
  Evaporation:        -576000 m³/year
  Catchment runoff:   +234000 m³/year
  Groundwater inflow: +306600 m³/year
  Net annual:         +276600 m³/year

[Task 2] Time to Fill
  Target volume:      67200000 m³
  Years to target:    243.0 years

[Task 3] Water Quality
  pH: acidic (pyrite oxidation) → 3-5 expected
  Metals: elevated Fe, Cu, Zn, Mn
  Sulfate: 2000-8000 mg/L
  Treatment: lime precipitation + wetland

[Task 4] Overflow Spillway
  Design flow: 1:100 year flood = 4.2 m³/s
  Spillway: rock-lined trapezoidal channel
  Freeboard: 1.5 m above design flood

[Task 5] Closure Cost
  Spillway construction          $   850,000
  Water treatment plant          $ 2,500,000
  Revegetation                   $   450,000
  Monitoring (10 years)          $   300,000
  Contingency (15%)              $   615,000
  TOTAL                          $ 4,715,000

============================================================
Exercise 14 complete.
===============================
... (truncated)
```
