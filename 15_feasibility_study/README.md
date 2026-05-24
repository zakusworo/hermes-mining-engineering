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
