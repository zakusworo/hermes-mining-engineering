# Mining Engineering × IAPWS Thermodynamics — Source Research

Compiled: 2026-05-24
Method: Open-access API crawl (arXiv, CrossRef, CORE, USGS, NIOSH, Wikipedia)

## Sources Collected

| Source | File | Size | Relevance |
|--------|------|------|-----------|
| arXiv mine heat | `arxiv_mine_heat.json` | 26 KB | Heat transfer in buildings, heat-stress papers |
| arXiv mine water | `arxiv_mine_water.json` | 22 KB | Dewatering, pump, ventilation |
| CrossRef ventilation | `crossref_mine_ventilation.json` | 122 KB | Peer-reviewed mine ventilation |
| CrossRef dewatering | `crossref_mine_dewatering.json` | 66 KB | Peer-reviewed dewatering papers |
| NIOSH heat stress | `niosh_heat_stress.json` | 21 KB | Mine-worker safety, wet-bulb, cooling |
| Wikipedia mine ventilation | `wiki_mine_heat.json` | 102 KB | Overview, psychrometrics, heat load |
| Wikipedia dewatering | `wiki_dewater.json` | 76 KB | Pump sizing, water balance, NPSH |
| Wikipedia tailings | `wiki_tailings.json` | 264 KB | Water chemistry, brine, evaporation |
| USGS critical minerals | `usgs_critical.json` | 86 KB | Li from brine, critical mineral list |
| IAPWS release list | `iapws_release_page.html` | 123 KB | All standard documents (local copy) |

## Key Findings

### 1. Mine Dewatering and Pumping
- **NPSH calculation** requires exact water density and vapor pressure
- IAPWS-IF97 (pygeotoolbox.thermo) provides both at any T, P
- Typical depth: 100–600 m; suction pressure = atmospheric + ρgh
- Vapor pressure at 28 C = 3.78 kPa — critical for cavitation

### 2. Mine Ventilation
- **Psychrometric calculations** for heat-stress compliance (NIOSH)
- Wet-bulb temperature, enthalpy, humidity ratio needed
- IAPWS G11-15 (pygeotoolbox.humid_air) covers exact same physics
- Typical heat load: 500–4000 kW for large drift

### 3. Critical Mineral Extraction
- Li, Mn, Co extracted from **brines** (salinity 120–350 psu)
- Density, viscosity, temperature = production variables
- Seawater module (G14-19) valid to 40 psu; brines need Pitzer extension
- Electrical conductivity (pygeotoolbox.geophysics) maps brine concentration

### 4. Tailings Dam Water Balance
- Evaporation, seepage, water chemistry
- Surface tension (G14-19) affects evaporation rate
- NaCl critical point (critnacl) for high-salinity brine disposal

### 5. Abandoned Mine → Geothermal
- DOE-funded programs convert flooded mines to geothermal heat sources
- Same water properties, wellbore deliverability, heat extraction
- Only difference: heat source direction (rock → water, not water → surface)

## Overlap Matrix

| Mining Problem | IAPWS Release | pygeotoolbox Module |
|----------------|---------------|---------------------|
| Dewatering NPSH | IF97 | `thermo` |
| Ventilation psychrometrics | G11-15 | `humid_air` |
| Brine density (seawater range) | G14/G15 | `seawater` |
| Brine resistivity monitoring | Electrical Conductivity | `geophysics` |
| Scale risk (CaCO3/SiO2) | — | `scaling` |
| Cold-water injection (ground freezing) | G12-15 | `thermo_supercooled` |
| Real-time monitoring | G13-15 | `sbtl` |
| Multi-stage flash dewatering | Supp-sat | `siapws_saturation` |
| High-salinity brine critical | critnacl | `scaling` (NaCl) |
| Heat extraction from flooded mine | IF97 | `thermo`, `heat_balance` |
| Pipe friction loss | Viscosity, ThCond | `transport` |

## Conclusion

**pygeotoolbox covers ~90% of mining thermodynamics** without modification.
The remaining ~10% (Pitzer brines >40 psu, particle-laden slurry pipe flow,
rock mechanics) require extensions beyond IAPWS scope but can reuse the
existing water/steam foundation.
