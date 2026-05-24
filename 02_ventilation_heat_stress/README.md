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

## Sample Output

```text
============================================================
EXERCISE 2: Mine Ventilation and Heat Stress Management
============================================================

[Task 1] Psychrometric State
  Intake:    T=22.0C, RH=60%, WB=16.8C, h=47.3 kJ/kg
  Working:   T=30.0C, RH=85%, WB=27.9C, h=88.9 kJ/kg

  Enthalpy rise:   41.6 kJ/kg
  Mass flow:       53.0 kg/s
  Sensible+latent heat pick-up: 2.2 kW

[Task 2] Heat Stress Assessment
  WBGT:            28.5 C
  Classification:  extreme_caution
  Work/rest:       50:50
  Max continuous:  2.0 hours
  Action:          Provide cooling/shade/hydration

[Task 3] Ventilation System
  Friction ΔP:     122 Pa
  Fan power:       8.1 kW
  Annual energy:   71 MWh/year

[Task 4] Heat from Machinery
  Diesel heat:     484 kW (approx)
  Total heat load: 520.3 kW

[Task 5] Recommendations
  → Install chilled water service (CWS) or spot coolers
  → Increase airflow to 58 m³/s minimum
  → Reduce diesel equipment where possible (switch to electric)
  → Implement work/rest: 50:50

============================================================
Exercise 2 complete.
============================================================
```
