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
