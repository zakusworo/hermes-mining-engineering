"""
Mine Dewatering Demo using pygeotoolbox IAPWS models.

Demonstrates:
1. NPSH calculation for submersible pump at 300 m depth
2. Mine ventilation psychrometrics (wet-bulb, cooling load)
3. Brine density for critical mineral processing
4. Scale risk (CaCO3/SiO2) in dewatering discharge lines
"""

import sys, os
sys.path.insert(0, "../../pygeotoolbox-mcp/src")

from pygeotoolbox import thermo, humid_air, siapws_saturation, seawater, scaling, sbtl

print("=" * 60)
print("Mine Dewatering / Ventilation / Brine Processing Demo")
print("=" * 60)

# ------------------------------------------------------------------
# 1. Dewatering Pump NPSH
# ------------------------------------------------------------------
print("\n[1] Dewatering Pump — Net Positive Suction Head")
Depth_m = 300                         # mine level below surface
T_water = 28                          # water temperature, C
P_atm = 101.325                         # surface pressure, kPa

# Hydrostatic pressure at pump suction
rho_water = thermo.density_from_TP(T_water, P_atm)
P_suction = P_atm + rho_water * 9.81 * Depth_m / 1000  # kPa

# Vapor pressure
P_vapor = siapws_saturation.saturation_pressure(T_water)

# NPSH available (kPa → m water column)
NPSH_kPa = P_suction - P_vapor
NPSH_m = NPSH_kPa * 1000 / (rho_water * 9.81)

print(f"  Depth:           {Depth_m} m")
print(f"  Water density:   {rho_water:.2f} kg/m³ ({T_water} C)")
print(f"  Suction pressure: {P_suction:.1f} kPa")
print(f"  Vapor pressure:   {P_vapor:.3f} kPa")
print(f"  NPSH available:   {NPSH_kPa:.1f} kPa  ≈  {NPSH_m:.1f} m")
print(f"  Status:          {'SAFE' if NPSH_m > 3.0 else 'CAUTION — cavitation risk'}")

# ------------------------------------------------------------------
# 2. Mine Ventilation Psychrometrics
# ------------------------------------------------------------------
print("\n[2] Mine Ventilation — Psychrometric Heat Load")
T_in = 32              # intake air temperature, C
RH_in = 0.65           # relative humidity (65%)
T_out = 38             # exhaust / working face temperature, C
RH_out = 0.85          # exhaust humidity (higher due to water evaporation)

# Enthalpy difference (latent + sensible)
h_in = humid_air.enthalpy_humid_air(T_in, RH_in)
h_out = humid_air.enthalpy_humid_air(T_out, RH_out)
delta_h = h_out - h_in  # J/kg dry air

# Ventilation flow (typical for 5 m × 4 m drift, 2 m/s)
Area = 5 * 4           # m²
Velocity = 2.0         # m/s
volumetric_m3s = Area * Velocity
rho_dry = humid_air.density_humid_air(T_in, P_atm, RH_in)
mass_flow = volumetric_m3s * rho_dry

Heat_load = mass_flow * delta_h  # W

print(f"  Mine drift:        {Area} m² × {Velocity} m/s")
print(f"  Ventilation flow:  {volumetric_m3s:.0f} m³/s")
print(f"  Dry air density:   {rho_dry:.3f} kg/m³")
print(f"  Enthalpy rise:     {delta_h/1000:.1f} kJ/kg")
print(f"  Heat load:         {Heat_load/1000:.1f} kW")
print(f"  Wet-bulb (inlet):  {humid_air.dew_point(T_in, P_atm, RH_in):.1f} C")

# ------------------------------------------------------------------
# 3. Brine Processing — Critical Mineral Density
# ------------------------------------------------------------------
print("\n[3] Brine Processing — Density for Critical Mineral Extraction")
T_brine = 25
S_psu = 35            # seawater range (extend to brine for DLE demonstration)

print("  NOTE: Standard seawater module valid to S=40 psu.")
print("        For salar brines (S=120-350 psu), extend with")
print("        Pitzer equations or empirical brine correlations.")

brine_data = seawater.seawater_density(T_brine, S_psu)
rho_brine = brine_data.get("rho_kg_m3")

print(f"  Brine T:           {T_brine} C")
print(f"  Salinity:          {S_psu} psu")
print(f"  Brine density:     {rho_brine:.2f} kg/m³")
print(f"  Density advantage: {((rho_brine - 1000)/1000):.1%} over fresh water")
print(f"  Use case:          Direct Lithium Extraction (DLE) settling ponds")

# ------------------------------------------------------------------
# 4. Scale Risk in Dewatering Discharge Line
# ------------------------------------------------------------------
print("\n[4] Scale Risk — CaCO₃ / SiO₂ in Discharge Line")
T_discharge = 55
pH = 7.2
Ca_mgL = 250
HCO3_mgL = 180
SiO2_mgL = 180

ryznar = scaling.ryznar_index(T_discharge, Ca_mgL, HCO3_mgL, pH)
sio2_data = scaling.sio2_scaling_risk(SiO2_mgL, T_discharge)

print(f"  Discharge T:       {T_discharge} C")
print(f"  Ryznar index:      {ryznar:.1f}")
print(f"  CaCO₃ risk:        {'SCALE — acid wash needed' if ryznar < 6.0 else 'Stable'}")
print(f"  SiO₂ risk level:   {sio2_data['risk']} (concentration {sio2_data['limit_mg_L']:.0f} mg/L, ratio {sio2_data['ratio']:.2f})")
print(f"  Maintenance:       {'Inline acid injection' if ryznar < 6.0 or sio2_data['risk'] != 'low' else 'Monitor quarterly'}")

# ------------------------------------------------------------------
# 5. Fast Lookup for SCADA (SBTL)
# ------------------------------------------------------------------
print("\n[5] SBTL Fast Lookup for SCADA Mine Water Dashboard")
# Compare: CoolProp vs SBTL coarse lookup
import time

n = 50000
start = time.perf_counter()
for _ in range(n):
    # Full thermodynamic calculation (CoolProp, slower)
    try:
        rho_cp = thermo.density(50, 2000)
    except:
        pass
dt_cp = time.perf_counter() - start

start2 = time.perf_counter()
for _ in range(n):
    sbtl.lookup(50, 2.0, "rho")
dt_sbtl = time.perf_counter() - start2

print(f"  {n:,} evaluations:")
print(f"    CoolProp:  {dt_cp:.3f} s ({n/dt_cp:,.0f} /s)")
print(f"    SBTL:      {dt_sbtl:.3f} s ({n/dt_sbtl:,.0f} /s)")
print(f"    Speedup:   {dt_cp/dt_sbtl:.1f}×")

print("\n" + "=" * 60)
print("Demo complete. All pygeotoolbox modules applicable to mining.")
print("=" * 60)
