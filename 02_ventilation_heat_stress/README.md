# Exercise 2: Mine Ventilation and Heat Stress Management

## Goal
Teach Hermes to size ventilation systems and assess heat stress using psychrometrics.

## Engineering Focus
Deep underground gold mine. Working level at 800 m depth, 30°C, 85% RH.
Engineers calculate airflow, fan power, and WBGT heat stress index.

## Hermes Commands
```text
/hermes -w
/skill mining-engineering
/init
```

## Before Prompt (vague)
```
Fix the ventilation problem.
```

## After Prompt (precise)
```
Read exercise.py. The mine is at 800 m depth with working conditions:
- Intake: 22°C, 60% RH
- Working level: 30°C, 85% RH
- Diesel equipment: 4 trucks × 350 kW each
- Personnel: 40 workers × 150 W each

Calculate:
1. Psychrometric state at intake and working level (enthalpy, wet-bulb, humidity ratio)
2. Heat load from diesel + personnel + strata
3. Required airflow to keep wet-bulb below 27.5°C
4. Fan power for 2000 m duct, 3.5 m diameter, at required Q
5. WBGT classification and work/rest schedule per ACGIH

Plot enthalpy vs temperature for RH=40, 60, 80, 95% on one figure.
Run pytest tests/test_ventilation.py.
```

## Learning Objective
- Psychrometric calculations using Tetens/ASHRAE (not IAPWS)
- Heat stress index classification (safe, caution, extreme caution, danger)
- Ventilation sizing for deep mines
