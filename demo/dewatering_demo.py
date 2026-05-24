"""
Mine Dewatering / Ventilation / Brine Processing Demo.

DISTINCTION: IAPWS vs Mining Engineering
- IAPWS = water, steam, brine properties ONLY
- Mining = rock, soil, slurry, ore — NONE of which is covered by IAPWS
- This demo uses IAPWS for WATER parts and explicitly flags where mining
diverges from thermodynamic standards.
"""

import sys, os
sys.path.insert(0, "../../pygeotoolbox-mcp/src")

from pygeotoolbox import thermo, humid_air, siapws_saturation, seawater, scaling, sbtl

print("=" * 60)
print("MINING ENGINEERING × IAPWS WATER/STREAM ONLY")
print("=" * 60)

# ------------------------------------------------------------------
# 1. Dewatering Pump NPSH  (IAPWS-IF97: water density + vapor pressure)
# ------------------------------------------------------------------
print("\n[1] Dewatering Pump — Net Positive Suction Head")
print("    IAPWS-IF97: water density at T, P + saturation vapor pressure")
Depth_m = 300
T_water = 28
P_atm = 101.325

rho_water = thermo.density_from_TP(T_water, P_atm)
P_suction = P_atm + rho_water * 9.81 * Depth_m / 1000
P_vapor = siapws_saturation.saturation_pressure(T_water)
NPSH_kPa = P_suction - P_vapor
NPSH_m = NPSH_kPa * 1000 / (rho_water * 9.81)

print(f"  Water density (IF97):    {rho_water:.2f} kg/m3")
print(f"  Vapor pressure (IF97):   {P_vapor:.3f} kPa")
print(f"  NPSH available:          {NPSH_kPa:.1f} kPa  ≈  {NPSH_m:.1f} m")
print(f"  Status:                 {'SAFE' if NPSH_m > 3.0 else 'CAUTION'}")
print(f"  ⚠️  NOTE: Real dewatering handles SLURRY, not pure water.")
print(f"     Slurry density = water density + solids × concentration")
print(f"     IAPWS does NOT cover suspended ore particles.")

# ------------------------------------------------------------------
# 2. Mine Ventilation Psychrometrics  (IAPWS G11-15: humid air)
# ------------------------------------------------------------------
print("\n[2] Mine Ventilation — Psychrometric Heat Load")
print("    IAPWS G11-15: humid air enthalpy + density")
T_in = 32; RH_in = 0.65
T_out = 38; RH_out = 0.85

h_in = humid_air.enthalpy_humid_air(T_in, RH_in)
h_out = humid_air.enthalpy_humid_air(T_out, RH_out)
delta_h = h_out - h_in

Area = 20; Velocity = 2.0
volumetric = Area * Velocity
rho_dry = humid_air.density_humid_air(T_in, P_atm, RH_in)
mass_flow = volumetric * rho_dry
Heat_load = mass_flow * delta_h

print(f"  Ventilation flow:      {volumetric:.0f} m3/s")
print(f"  Enthalpy rise (G11):   {delta_h/1000:.1f} kJ/kg")
print(f"  Heat load (water):     {Heat_load/1000:.1f} kW")
print(f"  Wet-bulb (G11):        {humid_air.dew_point(T_in, P_atm, RH_in):.1f} C")
print(f"  ⚠️  NOTE: Real mines have DUST, diesel exhaust, explosive gases.")
print(f"     IAPWS humid air = clean air + water vapor only.")
print(f"     Use NIOSH / SME standards for dust/PM monitoring.")

# ------------------------------------------------------------------
# 3. Brine Density  (IAPWS G14-15: seawater)
#    WARNING: Valid to 40 psu only. Salar brines (120-350 psu) are
#    BEYOND IAPWS scope and need Pitzer/Krumgalz empirical equations.
# ------------------------------------------------------------------
print("\n[3] Brine Density — Seawater vs Salar Brine")
print("    IAPWS G14-15: seawater valid to S = 40 psu")
T_brine = 25
S_psu = 35

brine_data = seawater.seawater_density(T_brine, S_psu)
rho_brine = brine_data.get("rho_kg_m3")

print(f"  Seawater S=35 psu:     {rho_brine:.2f} kg/m3")
print(f"  Density vs fresh:      +{rho_brine - 1000:.2f} kg/m3")
print(f"  ⚠️  NOTE: Salar/Li brines = 120-350 psu — BEYOND IAPWS.")
print(f"     Need PITZER equations or empirical brine models (e.g., Krumgalz 1995)")
print(f"     IAPWS G14/G15 is for ocean water, NOT lithium extraction brines.")

# ------------------------------------------------------------------
# 4. Scale Risk  (IAPWS does NOT cover chemistry; empirical only)
# ------------------------------------------------------------------
print("\n[4] Scale Risk — CaCO3 / SiO2 in Discharge Line")
print("    NO IAPWS standard for CaCO3/silica chemistry. Empirical only.")
T_discharge = 55
pH = 7.2
Ca_mgL = 250
HCO3_mgL = 180
SiO2_mgL = 180

ryznar = scaling.ryznar_index(T_discharge, Ca_mgL, HCO3_mgL, pH)
sio2_data = scaling.sio2_scaling_risk(SiO2_mgL, T_discharge)

print(f"  Ryznar index:      {ryznar:.1f}")
print(f"  CaCO3 risk:        {'SCALE' if ryznar < 6.0 else 'Stable'}")
print(f"  SiO2 risk:         {sio2_data['risk']} (limit {sio2_data['limit_mg_L']:.0f} mg/L)")
print(f"  ⚠️  NOTE: Ryznar / SiO2 solubility = EMPIRICAL correlations.")
print(f"     IAPWS standardizes H2O phase properties, NOT multi-ion chemistry.")
print(f"     Full brine speciation requires PHREEQC, Geochemist's Workbench, or OLI.")

# ------------------------------------------------------------------
# 5. Fast Lookup  (IAPWS G13-15: SBTL method)
# ------------------------------------------------------------------
print("\n[5] SBTL Fast Lookup — SCADA Mine Water Dashboard")
print("    IAPWS G13-15: Span-Backus Tabulated Lookup for real-time monitoring")

# Quick benchmark: Full IF97 vs SBTL approximation
import time
n = 50000
start = time.perf_counter()
for _ in range(n):
    thermo.density_from_TP(50, 2000)
dt_cp = time.perf_counter() - start

start2 = time.perf_counter()
for _ in range(n):
    sbtl.lookup(50, 2.0, "rho")
dt_sbtl = time.perf_counter() - start2

print(f"  Full IF97:  {n/dt_cp:,.0f} eval/s")
print(f"  SBTL:       {n/dt_sbtl:,.0f} eval/s")
print(f"  Speedup:    {dt_cp/dt_sbtl:.1f}×")
print(f"  ⚠️  NOTE: SBTL is an IAPWS-endorsed APPROXIMATION, not exact.")
print(f"     Use full IF97 for design; SBTL for real-time monitoring.")

# ------------------------------------------------------------------
# MINING-SPECIFIC: WHAT IAPWS DOES NOT COVER
# ------------------------------------------------------------------
print("\n" + "=" * 60)
print("MINING-SPECIFIC: NOT COVERED BY ANY IAPWS STANDARD")
print("=" * 60)
print("""
| Property              | Mining Source               | Why IAPWS doesn't cover it |
|-----------------------|-----------------------------|------------------------------|
| Rock density          | SME Handbook, ASTM D421     | Rock is not H2O              |
| Slurry rheology       | Bingham/Herschel-Bulkley    | Particles ≠ fluid            |
| Ore mineralogy        | XRD, SEM, MLA               | Mineral phases ≠ H2O phase   |
| Explosive gas limits  | MSHA/OSHA                   | CH4/O2/H2S mixture ≠ humid air |
| Diesel particulate    | NIOSH method 5040           | PM2.5/soot ≠ water vapor     |
| Country rock thermal  | Lab measurement             | Solid conduction ≠ fluid     |
| Tailings consolidation| Geotechnical ( consolidation theory) | Soil mechanics ≠ thermophysics |

These require: SME, ASTM, ISO 19434, ASHRAE, Rocscience, FLAC3D.
""".strip())

print("\n" + "=" * 60)
print("Demo complete. IAPWS = water/steam ONLY. Mining = extend with empirical.")
print("=" * 60)
