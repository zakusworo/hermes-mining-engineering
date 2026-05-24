# Exercise 15: Pre-Feasibility Study — Cash Flow and NPV

## Goal
Teach Hermes to build a financial model for a mining project and run sensitivity analysis.

## Engineering Focus
Small-scale underground gold mine. Investors need NPV, payback, and sensitivity to gold price.

## Hermes Commands
```text
/hermes -w
/skill mining-engineering
/init
```

## Before Prompt (vague)
```
Is this gold mine profitable?
```

## After Prompt (precise)
```
Read exercise.py. The project:
- Resource: 2.8 Mt @ 3.2 g/t Au
- Mining rate: 1800 tpd
- Recovery: 92%
- Gold price: $1950/oz
- Capex: $85M
- Opex: $85/t ore
- Discount rate: 8%

Calculate:
1. Mine life (years)
2. Annual gold production (oz/year)
3. Annual revenue and operating cost
4. Annual cash flow and cumulative NPV
5. Payback period
6. If gold price drops to $1700/oz: new NPV and go/no-go decision

Plot annual cash flow bar chart with NPV annotation.
Run sensitivity on gold price ($1500–$2200) and plot NPV vs price.
```

## Learning Objective
- NPV = Σ(CF_t / (1+r)^t)
- Payback = first year cumulative CF turns positive
- Sensitivity analysis drives go/no-go decisions

## Illustrated Output

![Feasibility Cash Flow](assets/figures/15_feasibility_cash_flow.png)

## Sample Output

```text
============================================================
EXERCISE 15: Pre-Feasibility Study
============================================================

[Task 1] Production Profile
  Annual throughput: 0.56 Mt/year
  Grade:             3.2 g/t
  Recovery:          92%
  Annual gold:       52.9 koz/year
  Revenue:           $103.1M/year

[Task 2] Yearly Cash Flow
  Year 1: mined=0.56Mt, rev=$103.1M, opex=$47.5M, CF=$36.0M, DCF=$33.4M
  Year 2: mined=0.56Mt, rev=$103.1M, opex=$47.5M, CF=$36.0M, DCF=$30.9M
  Year 3: mined=0.56Mt, rev=$103.1M, opex=$47.5M, CF=$36.0M, DCF=$28.6M
  Year 4: mined=0.56Mt, rev=$103.1M, opex=$47.5M, CF=$36.0M, DCF=$26.5M
  Year 5: mined=0.56Mt, rev=$103.1M, opex=$47.5M, CF=$36.0M, DCF=$24.5M

[Task 3] NPV
  Undiscounted cumulative: $95.2M
  NPV @ 8%:          $58.9M

[Task 4] Payback Period
  Approx payback: 2.4 years

[Task 5] Sensitivity to Gold Price
  $1500/oz → annual CF=$20.1M → NPV=$-4.9M
  $1750/oz → annual CF=$28.9M → NPV=$30.5M
  $1950/oz → annual CF=$36.0M → NPV=$58.9M
  $2200/oz → annual CF=$44.9M → NPV=$94.3M
  $2500/oz → annual CF=$55.6M → NPV=$136.9M

============================================================
Exercise 15 complete.
=====
... (truncated)
```
