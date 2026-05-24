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

## Sample Output

```text
============================================================
EXERCISE 3: Slurry Pipeline and Dewatering System Design
============================================================

[Task 1] Slurry Properties
  Water density:        1001.2 kg/m³
  Slurry density:       1260.3 kg/m³ (Δ = +259.1 kg/m³)
  Volume concentration: 0.144
  Yield stress:         0.00 Pa
  Plastic viscosity:    0.0016 Pa·s
  Relative viscosity:   1.60

[Task 2] Pipeline Hydraulics
  Flow velocity:        4.53 m/s
  Friction ΔP:          464.9 kPa
  Static lift ΔP:       432.7 kPa
  Total ΔP:             897.6 kPa
  Equivalent head:      72.6 m

[Task 3] Pump Power
  Shaft power:          277.1 kW
  Motor size:           308 kW (at 90% motor efficiency)
  Annual energy:        2427 MWh/year

[Task 4] NPSH Assessment
  NPSH available:       4.33 m
  Status:              SAFE
  Vapor pressure:      2.64 kPa

[Task 5] Pump Specification
  Type:                 Horizontal centrifugal, hard-metal lined
  Flow:                 800 m³/h
  Head:                 72.6 m
  Solids handling:      d50=0.35mm, Cw=32%
  NPSHr requirement:    < 3.3 m (safety margin 1m)
  Material:             High-chrome white iron (ASTM A532)

... (truncated)
```
