# Hermes Mining Engineering

Pure mining engineering calculations — NO IAPWS dependency.

This repository implements empirical, industry-standard methods for
mining engineering:
- **Rock Mechanics**: Hoek-Brown, RMR, GSI, Mohr-Coulomb (ISRM/SME)
- **Ventilation**: ASHRAE psychrometrics, heat stress index (NIOSH/ACGIH)
- **Slurry Transport**: Bingham plastic rheology, settling velocity
- **Dewatering**: NPSH, pump power, groundwater inflow (empirical fluid mechanics)

## Why NO IAPWS?

[IAPWS](https://iapws.org) standardizes **water and steam** only.
Mining engineering deals with **rock, soil, slurry, ore** — none of which
are covered by IAPWS. For mine water calculations at typical temperatures
(5–35 °C), simplified empirical formulas (Tetens, linear density) are
sufficient and industry-standard. Exact IAPWS-IF97 is unnecessary overkill
for NPSH and pump sizing.

## Standards Referenced

| Area | Standard | Module |
|------|----------|--------|
| Rock mechanics | Hoek-Brown (2002), RMR (Bieniawski), GSI | `rock_mechanics` |
| Ventilation | ASHRAE Fundamentals, McPherson (1993), NIOSH | `ventilation` |
| Slurry | Bingham plastic, Wilson et al. (2006), SME | `slurry` |
| Dewatering | SME Handbook, Hartman & Mutmansky | `dewatering` |
| Heat stress | ACGIH TLV, NIOSH criteria | `ventilation.heat_stress_index` |
| Rock testing | ASTM D7012, D5731, D4543 | referenced in docs |
| Mine safety | MSHA regulations, ISO/TC 82 | referenced in docs |

## Quick Start

```bash
# No dependencies beyond Python standard library
cd hermes-mining-engineering
PYTHONPATH=src python3 -m pytest tests/ -v

# Run individual module demos
PYTHONPATH=src python3 src/mining/rock_mechanics.py
PYTHONPATH=src python3 src/mining/ventilation.py
PYTHONPATH=src python3 src/mining/slurry.py
PYTHONPATH=src python3 src/mining/dewatering.py
PYTHONPATH=src python3 src/mining/slope_stability.py
PYTHONPATH=src python3 src/mining/blasting.py

# Run exercises
PYTHONPATH=src python3 exercises/01_rock_mass_slope/exercise.py
PYTHONPATH=src python3 exercises/02_ventilation_heat_stress/exercise.py
PYTHONPATH=src python3 exercises/03_slurry_dewatering/exercise.py
PYTHONPATH=src python3 exercises/04_blast_vibration/exercise.py
PYTHONPATH=src python3 exercises/05_integrated_design/exercise.py
```

## Modules

### `rock_mechanics.py`

```python
from mining import rock_mechanics as rm

# Hoek-Brown for granite rock mass
params = rm.hoek_brown_parameters(gsi=65, mi=25, D=0.5)
# → mb, s, a, E_rm_MPa

# Strength at confining stress 5 MPa
sigma1 = rm.hoek_brown_strength(5.0, params['mb'], params['s'], params['a'], 150.0)

# Mohr-Coulomb equivalent
c_phi = rm.mohr_coulomb_from_hoek_brown(params['mb'], params['s'], params['a'], 150.0, 15.0)
# → cohesion_MPa, friction_angle_deg

# RQD from drill core
rqd = rm.rqd_from_core_recovery([15, 8, 22, 5, 30, 12, 18, 7, 25, 10])
```

### `ventilation.py`

```python
from mining import ventilation as vent

# Psychrometric state
psych = vent.psychrometric_properties(T_C=30, RH=0.60)
# → humidity_ratio, enthalpy, wet_bulb, density

# Ventilation sizing
dp = vent.friction_pressure_drop(Q=40, L=2000, D=3.5, rho=1.15)
power = vent.fan_power(Q=40, delta_P=dp)

# Heat stress compliance
hsi = vent.heat_stress_index(T_dry=35, Tw=psych['wet_bulb_C'])
# → classification, work_rest_ratio, max_hours
```

### `slurry.py`

```python
from mining import slurry

# Slurry density (copper ore, 35% solids)
rho_m = slurry.slurry_density(1000, 2800, 0.35)

# Bingham plastic parameters
bingham = slurry.slurry_viscosity_bingham(0.001, 0.35, 0.5, 2800)
# → yield_stress_Pa, plastic_viscosity_Pas

# Pipeline pressure drop
dp = slurry.slurry_pressure_drop_bingham(0.5, 0.3, 1000, rho_m,
                                          bingham['yield_stress_Pa'],
                                          bingham['plastic_viscosity_Pas'])
```

### `dewatering.py`

```python
from mining import dewatering as dw

# NPSH for deep sump pump
npsh = dw.npsh_available(101.325, water_level_below=5.0,
                        suction_losses=15.0, T_water_C=28)

# Pump power
P = dw.pump_power(Q_m3h=500, head_m=350, rho=996)

# Groundwater inflow estimate
Q_in = dw.groundwater_inflow_empirical(k=2.5, b=50, drawdown=80,
                                       R=2000, pit_area=50000)
```

## Tests

23 tests, all pass, zero external dependencies:

```bash
PYTHONPATH=src python3 -m pytest tests/ -v
```

| Test file | Coverage |
|-----------|----------|
| `test_rock_mechanics.py` | RQD, Hoek-Brown, Mohr-Coulomb, GSI validation |
| `test_ventilation.py` | Psychrometrics, friction, fan power, heat stress |
| `test_slurry.py` | Density, Bingham viscosity, pressure drop, settling |
| `test_dewatering.py` | NPSH, pump power, inflow, water property approx |
| `test_slope_stability.py` | Bishop FOS, bench design, inter-ramp/overall angle |
| `test_blasting.py` | PPV, overpressure, blast design, regulatory limits |

## Exercises

| # | Exercise | Modules | Standards |
|---|----------|---------|-----------|
| 1 | Rock Mass Characterization + Slope Stability | rock_mechanics, slope_stability | RMR, Hoek-Brown, Bishop |
| 2 | Ventilation + Heat Stress Management | ventilation | ASHRAE, NIOSH, ACGIH |
| 3 | Slurry Pipeline + Dewatering Design | slurry, dewatering | Bingham, SME |
| 4 | Blast Design + Vibration Control | blasting | USBM RI 8507, AS 2187.2 |
| 5 | Integrated Mine Design Case Study | ALL 6 modules | Combined |

```bash
PYTHONPATH=src python3 exercises/01_rock_mass_slope/exercise.py
PYTHONPATH=src python3 exercises/02_ventilation_heat_stress/exercise.py
PYTHONPATH=src python3 exercises/03_slurry_dewatering/exercise.py
PYTHONPATH=src python3 exercises/04_blast_vibration/exercise.py
PYTHONPATH=src python3 exercises/05_integrated_design/exercise.py
```

`research/` directory contains crawled standards pages:
| Source | File | Size | Relevance |
|--------|------|------|-----------|
| SME Handbook | `sme_handbook.html` | 8 KB | Mining methods, ground control |
| NIOSH Mining | `niosh_mining.html` | 2 KB | Safety, ventilation, heat stress |
| MSHA Regulations | `msha_regulations.html` | 3 KB | Standards, enforcement |
| ASTM D5731 | `astm_d5731.html` | 285 KB | Point load strength test |
| Wikipedia Mine Ventilation | `mcpherson_ventilation.html` | 76 KB | Psychrometrics, fans |
| Hoek-Brown | `hoek_brown.html` | 24 KB | Failure criterion background |
| Underground Methods | `underground_methods.html` | — | Stoping, cut-and-fill, block caving |
| Tailings Dam | `tailings_dam.html` | 264 KB | Water balance, seepage |
| USGS Critical Minerals | `usgs_critical_minerals.html` | 86 KB | Strategic mineral list |

## Hermes Agent Usage

```text
hermes -w                               # isolated workspace
PYTHONPATH=src python3 -m pytest tests/  # run all tests
PYTHONPATH=src python3 src/mining/rock_mechanics.py  # run demo
```

## License

MIT License — Copyright 2026 Zulfikar Aji Kusworo
