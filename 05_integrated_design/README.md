# Exercise 5: Integrated Mine Design Case Study

## Goal
Combine all 6 modules into a single mine design workflow.

## Engineering Focus
Underground copper-gold mine at 1200 m depth. Engineers must simultaneously design:
- Rock support (pillar, roof bolt)
- Ventilation network
- Slurry transport
- Dewatering system
- Slope/bench stability
- Blast design

## Hermes Commands
```text
/hermes -w
/skill mining-engineering
/init
```

## Before Prompt (vague)
```
Design the whole mine.
```

## After Prompt (precise)
```
Read exercise.py. The mine has:
- Depth: 1200 m
- Rock: altered andesite, GSI=55, mi=18, D=0.4, UCS=85 MPa
- Production: 3500 tpd
- Ore density: 2800 kg/m³
- Groundwater inflow: 35 m³/h
- Working conditions: 32°C, 88% RH

Calculate all 6 subsystems:
1. Rock: Hoek-Brown parameters, Mohr-Coulomb, pillar stress vs strength, bolt support
2. Ventilation: airflow, fan power, heat stress classification
3. Slurry: density, pipeline ΔP for 1200 m + 85 m lift
4. Dewatering: NPSH, pump power, groundwater inflow cost
5. Slope: bench design at 65° face, check inter-ramp angle
6. Blast: PPV at 500 m, compliance check

Plot a 6-panel dashboard: rock modulus, psychrometrics, slurry viscosity, NPSH, slope FOS, blast PPV.
Run all pytest tests/.
```

## Learning Objective
- Integrated design: all subsystems interact
- Trade-offs: deeper = more dewatering, more ventilation, higher cost
- Agentic AI: Hermes manages multiple modules in one session

## Sample Output

```text
============================================================
EXERCISE 5: Integrated Mine Design Case Study
============================================================

[Task 1] Rock Mass Characterization
  GSI=55, mi=18, D=0.4
  mb=0.013, s=0.006738, a=0.5
  E_rm=20250 MPa
  Mohr-Coulomb: c=3.37 MPa, φ=2.0°

  Pillar stress (tributary): 150.0 MPa
  Pillar strength:           0.00 MPa
  Pillar safety factor:      0.00
  ⚠️  Pillar too slender — increase width or reduce stope span

[Task 2] Ventilation Network
  Intake:  20.0C, RH=55%, WB=14.4C
  Return:  32.0C, RH=88%, WB=30.3C
  Airflow: 65.0 m³/s
  Total ΔP: 1619 Pa (decline 68 + raise 1051)
  Fan power: 150.3 kW
  Machinery heat: 787.5 kW
  Heat stress: danger (WBGT=30.8C)

[Task 3] Dewatering System
  Flow: 650.0 m³/h, Head: 150.0 m
  NPSH available: -117.09 m (DANGER — cavitation likely)
  Pump power: 354.2 kW
  Annual energy: 3103 MWh

[Task 4] Slurry Transport to Surface
  Slurry density: 1219.5 kg/m³
  Pipe ΔP: 723 kPa + static 14356 kPa
  Pump power: 4787.1 kW

[Task 5] Open-Pit Slope Stability (Portal)
  FOS: 4.62
  Status: stable — Continue operations, routine monitoring

[Task 6] Blast Vibration Control
  PPV at crusher
... (truncated)
```
