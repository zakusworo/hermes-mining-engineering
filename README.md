# Hermes Mining Engineering

Geothermal-engineering toolbox extended for mining applications.
The [pygeotoolbox-mcp](https://github.com/zakusworo/pygeotoolbox-mcp) IAPWS
models (water, steam, brine, humid air) are directly applicable to mine
ventilation, dewatering, critical-mineral extraction, and tailings water
management.

## Why This Works

Mining and geothermal engineering share **the same thermodynamic
foundation**: water/steam phase behavior, brine chemistry, heat transfer,
and fluid transport.  Both fields need IAPWS-IF97 and its supplementary
documents.  pygeotoolbox already implements 11 IAPWS releases — the
exact physics used in mine engineering but rarely packaged openly.

## Direct Module Mapping

| pygeotoolbox module | Mining use case |
|---------------------|-----------------|
| `thermo` | Dewatering pump NPSH, shaft heat rejection, compressed-air cooler sizing |
| `siapws_saturation` | Flash calculations for multi-stage dewatering, degasification |
| `transport` | Friction loss in dewatering pipes, heat-exchanger U-value for mine chillers |
| `seawater` | Density/salinity for brine handling in critical-mineral processing |
| `geophysics` | Resistivity monitoring for leach pads, groundwater intrusion detection |
| `humid_air` | Mine ventilation psychrometrics (wet-bulb temperature, heat-stress index) |
| `sbtl` | Real-time lookup for SCADA mine-water monitoring (thousands of points/second) |
| `thermo_supercooled` | Cold-water injection for ground freezing, shaft sinking through aquifers |
| `wellbore` | IPR/TPR adaptasi: pit sump pump curves, vertical shaft hydraulic gradient |
| `scaling` | CaCO₃/SiO₂ scale in dewatering pumps, brine handling lines |
| `advisory_notes` | Documented pitfalls: saturation boundary, supercooled metastability, low-pressure humid-air breakdown |

## Source Research

See `research/` directory for raw data from:
| Source | Relevance | Keywords |
|--------|-----------|----------|
| NIOSH/CDC heat-stress | Mine worker safety, ventilation cooling | temperature, heat, humidity, wet-bulb |
| Wikipedia: Mine dewatering | Pump sizing, water balance | pump, dewater, steam, mine |
| Wikipedia: Tailings | Water chemistry, salinity, evaporation | water, brine, salinity, density |
| USGS critical minerals | Li from geothermal brine — mining overlap | brine, lithium, critical, extraction |
| arXiv mine ventilation | Academic validation of thermodynamic models | mine, heat, ventilation, water |
| CrossRef dewatering | Peer-reviewed pump/heat calculations | dewater, pump, water, temperature |
| IAPWS release list | Standard documents for all formulations | IAPWS-IF97, G11, G12, G13, G14 |

## Quick Start

```bash
# 1. Clone pygeotoolbox (already implements all IAPWS)
git clone https://github.com/zakusworo/pygeotoolbox-mcp
cd pygeotoolbox-mcp
pip install -e .

# 2. Run mine-relevant calculations directly
python3 -c "
from pygeotoolbox import thermo, humid_air, siapws_saturation

# Mine dewatering: water density at 35 C, 1 MPa (1 km depth)
rho = thermo.density(35, 1000)          # ≈ 994 kg/m³
print(f'Dewatering density: {rho:.1f} kg/m³')

# Mine ventilation: humid air enthalpy at 30 C, 80% RH
h = humid_air.enthalpy_humid_air(30, 0.8)
print(f'Ventilation enthalpy: {h/1000:.1f} kJ/kg dry air')

# Critical mineral extraction: brine saturation temperature
T_sat = siapws_saturation.saturation_temperature(1500)
print(f'Brine flash temperature: {T_sat:.2f} °C')
"
```

## Hermes Agent Usage

```text
hermes -w                               # isolated workspace
/skill run-tests                         # load test skill
/terminal python3 research/dewatering_demo.py
```

## License

MIT License — Copyright 2026 Zulfikar Aji Kusworo

Derived from pygeotoolbox-mcp (MIT), re-purposed for mining engineering.
