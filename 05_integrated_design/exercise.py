"""
Exercise 5: Integrated Mine Design Case Study

Scenario:
A new underground copper-gold mine at 1200 m depth with the following:

Geology:
- Host rock: altered andesite, moderately fractured
- RQD: 62% from 150 m drill holes
- GSI: 55 (fair quality rock mass)
- mi: 18 (andesite)
- In situ stress: σv = 30 MPa, σH = 25 MPa

Mine Layout:
- Production level at 1200 m
- Main decline: 5.2 m × 5.2 m, 3200 m long, 6% grade
- Ventilation raise: 2.5 m diameter, 1200 m vertical
- Stope dimensions: 30 m × 20 m × 40 m high

Operations:
- Production rate: 3000 tpd
- Diesel fleet: 1200 kW total (LHDs, trucks, jumbos)
- Electric fleet: 600 kW total (crushers, conveyors, pumps)
- Dewatering: 650 m³/h from 125 m sump depth
- Slurry to surface: 0.3 m pipe, 1800 m, 28% solids

Tasks:
1. Rock mass characterization + pillar design stress
2. Ventilation network sizing + heat load balance
3. Dewatering system NPSH + pump sizing
4. Slurry transport pressure + power
5. Slope stability (open pit portion, 80 m deep, 38°)
6. Blast vibration control (surface crusher 400 m away)
7. Overall energy balance and sustainability assessment
"""
import sys, math
sys.path.insert(0, "../src")

from mining import rock_mechanics as rm
from mining import ventilation as vent
from mining import dewatering as dw
from mining import slurry
from mining import slope_stability as ss
from mining import blasting as bl

print("=" * 60)
print("EXERCISE 5: Integrated Mine Design Case Study")
print("=" * 60)

# ========================================================================
# Task 1: Rock Mass + Pillar Design
# ========================================================================
print("\n[Task 1] Rock Mass Characterization")
gsi = 55
mi = 18
D = 0.4
sigma_ci = 85.0

params = rm.hoek_brown_parameters(gsi, mi, D)
print(f"  GSI={gsi}, mi={mi}, D={D}")
print(f"  mb={params['mb']:.3f}, s={params['s']:.6f}, a={params['a']}")
print(f"  E_rm={params['E_rm_MPa']:.0f} MPa")

mc = rm.mohr_coulomb_from_hoek_brown(params['mb'], params['s'], params['a'], sigma_ci, 20.0)
print(f"  Mohr-Coulomb: c={mc['cohesion_MPa']:.2f} MPa, φ={mc['friction_angle_deg']:.1f}°")

# Pillar stress (tributary area)
stope_w = 30.0; stope_h = 20.0; pillar_w = 20.0  # realistic pillar
area_total = (stope_w + pillar_w) * (stope_h + pillar_w)
area_pillar = pillar_w * pillar_w
area_stope = stope_w * stope_h
tributary_stress = 30.0 * area_total / area_pillar
print(f"\n  Pillar stress (tributary): {tributary_stress:.1f} MPa")
print(f"  Pillar strength:           {params['sigma_cm_MPa']:.2f} MPa")
sf = params['sigma_cm_MPa'] / tributary_stress if tributary_stress > 0 else float('inf')
print(f"  Pillar safety factor:      {sf:.2f}")
if sf < 1.0:
    print(f"  ⚠️  Pillar too slender — increase width or reduce stope span")

# ========================================================================
# Task 2: Ventilation
# ========================================================================
print("\n[Task 2] Ventilation Network")
T_intake = 20.0; RH_intake = 0.55
T_return = 32.0; RH_return = 0.88

psych_in = vent.psychrometric_properties(T_intake, RH_intake)
psych_out = vent.psychrometric_properties(T_return, RH_return)

Q_req = 65.0  # m3/s for 3000 tpd + diesel
rho = psych_in['density_kg_m3']

# Decline friction
dp_decline = vent.friction_pressure_drop(Q_req, 3200, 5.2, rho)
# Raise friction
dp_raise = vent.friction_pressure_drop(Q_req, 1200, 2.5, rho * 1.05)
total_dp = dp_decline + dp_raise + 500  # +500 Pa for regulators/leaks

power = vent.fan_power(Q_req, total_dp, 0.70)
machinery_heat = vent.heat_load_from_machinery(1200, 600, 0.75)

print(f"  Intake:  {psych_in['T_dry_C']}C, RH={psych_in['RH']*100:.0f}%, WB={psych_in['wet_bulb_C']:.1f}C")
print(f"  Return:  {psych_out['T_dry_C']}C, RH={psych_out['RH']*100:.0f}%, WB={psych_out['wet_bulb_C']:.1f}C")
print(f"  Airflow: {Q_req} m³/s")
print(f"  Total ΔP: {total_dp:.0f} Pa (decline {dp_decline:.0f} + raise {dp_raise:.0f})")
print(f"  Fan power: {power:.1f} kW")
print(f"  Machinery heat: {machinery_heat:.1f} kW")

hsi = vent.heat_stress_index(T_return, psych_out['wet_bulb_C'])
print(f"  Heat stress: {hsi['classification']} (WBGT={hsi['WBGT_C']:.1f}C)")

# ========================================================================
# Task 3: Dewatering
# ========================================================================
print("\n[Task 3] Dewatering System")
npsh = dw.npsh_available(101.325, 125.0, 20.0, 28)
Q_dw = 650.0
H_dw = 125.0 + 25.0  # lift + discharge head
P_dw = dw.pump_power(Q_dw, H_dw, 1000, 0.75)

print(f"  Flow: {Q_dw} m³/h, Head: {H_dw} m")
print(f"  NPSH available: {npsh['NPSH_m']:.2f} m ({npsh['status']})")
print(f"  Pump power: {P_dw:.1f} kW")
print(f"  Annual energy: {P_dw*8760/1000:.0f} MWh")

# ========================================================================
# Task 4: Slurry Transport
# ========================================================================
print("\n[Task 4] Slurry Transport to Surface")
rho_m = slurry.slurry_density(1000, 2800, 0.28)
bing = slurry.slurry_viscosity_bingham(0.001, 0.28, 0.4, 2800)
Q_sl = 3000.0 / 3600.0  # tpd → m3/s rough

# Recalculate for known solids flow
# 3000 tpd ore × 0.28 = 840 tpd solids = 35 t/h = 0.0097 t/s
# Slurry flow = solids_flow / (Cw × ρ_m) approx
# Simplified: assume 800 m3/h slurry
dp_slurry = slurry.slurry_pressure_drop_bingham(800/3600, 0.3, 1800, rho_m,
                                                 bing['yield_stress_Pa'], bing['plastic_viscosity_Pas'])
static = rho_m * 9.81 * 1200  # 1200m vertical
P_slurry = dw.pump_power(800, (dp_slurry+static)/(rho_m*9.81), rho_m, 0.70)

print(f"  Slurry density: {rho_m:.1f} kg/m³")
print(f"  Pipe ΔP: {dp_slurry/1000:.0f} kPa + static {(static/1000):.0f} kPa")
print(f"  Pump power: {P_slurry:.1f} kW")

# ========================================================================
# Task 5: Slope Stability (open pit portal area)
# ========================================================================
print("\n[Task 5] Open-Pit Slope Stability (Portal)")
F = ss.bishop_factor_of_safety(50, 15, 80, 38, 180, 32, 24, 0.08)
status = ss.slope_stability_status(F, 80, 38)
print(f"  FOS: {F}")
print(f"  Status: {status['status']} — {status['recommended_action']}")

# ========================================================================
# Task 6: Blast Vibration (development headings near crusher)
# ========================================================================
print("\n[Task 6] Blast Vibration Control")
ppv = bl.peak_particle_velocity(400, 25, 900, 1.6)
assess = bl.vibration_assessment(ppv, "industrial")
print(f"  PPV at crusher (400m): {ppv:.2f} mm/s")
print(f"  Status: {assess['status']}")
print(f"  Action: {assess['recommendation']}")

# ========================================================================
# Task 7: Overall Energy Balance
# ========================================================================
print("\n[Task 7] Overall Energy Balance")
total_mech = power + P_dw + P_slurry + machinery_heat
total_kwh_per_tonne = total_mech * 24 / 3000  # kWh/tonne
print(f"  Ventilation:    {power:.1f} kW")
print(f"  Dewatering:     {P_dw:.1f} kW")
print(f"  Slurry:         {P_slurry:.1f} kW")
print(f"  Machinery heat: {machinery_heat:.1f} kW (thermal load, not electrical)")
print(f"  Total electrical: {power+P_dw+P_slurry:.1f} kW")
print(f"  Annual electrical: {(power+P_dw+P_slurry)*8760/1000:.0f} MWh")
print(f"  Specific energy: {total_kwh_per_tonne:.1f} kWh/tonne")
print(f"\n  Sustainability note: {total_kwh_per_tonne:.1f} kWh/tonne is")
if total_kwh_per_tonne < 50:
    print(f"    ✓ Excellent (industry-leading)")
elif total_kwh_per_tonne < 100:
    print(f"    ✓ Good (below industry average ~120 kWh/t)")
elif total_kwh_per_tonne < 150:
    print(f"    ⚠ Average (improvement opportunities)")
else:
    print(f"    ✗ High (energy audit recommended)")

print("\n" + "=" * 60)
print("Exercise 5 complete. Integrated design validated.")
print("=" * 60)
