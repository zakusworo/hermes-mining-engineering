# Hermes Mining Engineering

Thermodynamic and hydraulic tools for mining engineering drawn from
[pygeotoolbox-mcp](https://github.com/zakusworo/pygeotoolbox-mcp) plus
mining-specific empirical correlations.

**IMPORTANT DISTINCTION**

The [IAPWS](https://iapws.org) standards standardize **water and steam**
properties only. Mining engineering deals predominantly with **rock,
soil, slurry, and ore** — none of which are covered by IAPWS.
However, whenever water, steam, humid air, or brine appear in a mining
problem (dewatering, ventilation, tailings, critical-mineral brines),
the existing IAPWS formulations in pygeotoolbox apply directly and
exactly.

## Why Partial Overlap Works

| Field | IAPWS Coverage | Mining Extension Needed |
|-------|----------------|------------------------|
| Dewatering pump NPSH | ✅ Water density, vapor pressure (IF97) | Slurry density, particle settling |
| Mine ventilation | ✅ Humid-air psychrometrics (G11-15) | Dust load, diesel particulates |
| Tailings water chemistry | ✅ Brine density up to 40 psu (G14-15) | Particle-fluid interaction, consolidation |
| Cold-water injection | ✅ Supercooled liquid (G12-15) | Ground freezing through porous rock |
| Critical-mineral brines | ✅ Brine density <40 psu | Salars >350 psu need Pitzer/Krumgalz |
| Geothermal from flooded mine | ✅ Full IF97 + Supp-sat | Heat conduction through country rock |
| Pipe friction loss | ✅ Viscosity, thermal conductivity | Slurry rheology (Bingham/Herschel–Bulkley) |

## Direct IAPWS Module Mapping (Water/Steam ONLY)

| pygeotoolbox module | Mining use case | IAPWS Release |
|---------------------|-----------------|---------------|
| `thermo` | Mine water density, enthalpy, NPSH | IF97 |
| `siapws_saturation` | Flash degasification of mine water | Supp-sat |
| `transport` | Friction loss in water pipes | ThCond, Viscosity |
| `seawater` | Brine density <40 psu | G14/G15 |
| `geophysics` | Resistivity of water-saturated rock | Electrical Conductivity |
| `humid_air` | Mine ventilation psychrometrics | G11-15 |
| `sbtl` | Real-time SCADA water monitoring | G13-15 |
| `thermo_supercooled` | Cold-water injection, ground freezing | G12-15 |
| `wellbore` | Vertical shaft hydraulic gradient | IF97 |
| `scaling` | CaCO₃/SiO₂ in discharge lines | — (empirical) |
| `advisory_notes` | Documented water-property pitfalls | Advise 1–6 |

## Mining Engineering Has NO IAPWS Standard

IAPWS does **not** standardize:

- Rock density, porosity, thermal conductivity
- Ore mineralogy or grade
- Slurry density, viscosity, yield stress
- Mine dust/air mixture properties
- Explosive gas ignition energy
- Diesel exhaust particulate dispersion

For these, mining relies on:
- SME (Society for Mining Engineers) handbooks
- ISO 19434 (mine ventilation)
- ASTM D421, D422 (soil/rock properties)
- ASHRAE Fundamentals (ventilation, not IAPWS)

## Source Research

See `research/` for open-access data:
| Source | Relevance |
|--------|-----------|
| NIOSH/CDC heat-stress | Wet-bulb, ventilation cooling |
| Wikipedia: Mine dewatering | Pump sizing, NPSH |
| USGS critical minerals | Brine extraction methods |
| arXiv/CrossRef | Peer-reviewed ventilation, dewatering |

## Quick Start

```bash
# 1. Clone pygeotoolbox (IAPWS water/steam only)
git clone https://github.com/zakusworo/pygeotoolbox-mcp
cd pygeotoolbox-mcp
pip install -e .

# 2. Run MINING-WATER calculations (IAPWS-valid)
python3 -c "
from pygeotoolbox import thermo, humid_air

# Mine dewatering: water density = IAPWS-IF97
rho = thermo.density_from_TP(28, 101.325)  # 996 kg/m3
print(f'Mine water density: {rho:.1f} kg/m3')

# Ventilation: humid air = IAPWS G11-15
h = humid_air.enthalpy_humid_air(30, 0.8)
print(f'Ventilation enthalpy: {h/1000:.1f} kJ/kg dry air')
"

# 3. Rock mechanics = NOT IAPWS; use SME handbook or Rocscience
```

## Hermes Agent Usage

```text
hermes -w                               # isolated workspace
/terminal python3 demo/dewatering_demo.py # run IAPWS-based demo
```

## License

MIT License — Copyright 2026 Zulfikar Aji Kusworo
