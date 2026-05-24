# Exercise 3: Slurry Pipeline and Dewatering System Design

## Goal
Teach Hermes to design slurry transport and dewatering as an integrated hydraulic system.

## Engineering Focus
Copper concentrator tailings. 800 m³/h slurry at 32% solids by weight.
Engineers calculate slurry density, Bingham rheology, pipeline pressure drop, and pump specifications.

## Hermes Commands
```text
/hermes -w
/skill mining-engineering
/init
```

## Before Prompt (vague)
```
Design the slurry pump system.
```

## After Prompt (precise)
```
Read exercise.py. The concentrator handles:
- Flow: 800 m³/h
- Solids concentration (weight): 32%
- Ore density: 2800 kg/m³
- Pipe: 0.5 m diameter, 1500 m horizontal + 35 m vertical lift
- Water temperature: 25°C

Calculate:
1. Slurry density and volume concentration
2. Bingham plastic parameters (yield stress, plastic viscosity)
3. Pipeline pressure drop (viscous + yield stress components)
4. Static lift head
5. Total dynamic head and required pump power at 75% efficiency
6. NPSH available (check if ≥ NPSH required + 3 m margin)

Plot slurry density vs solids concentration for copper, iron, and gold ore.
Run pytest tests/test_slurry.py and tests/test_dewatering.py.
```

## Learning Objective
- Bingham plastic model for non-Newtonian slurry
- Pipeline hydraulics with yield stress contribution
- Pump selection and NPSH verification
