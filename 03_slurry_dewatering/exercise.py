"""
Exercise 3: Slurry Pipeline and Dewatering System Design

Problem:
A copper concentrator handles 800 m³/h of tailings slurry with:
- Solids concentration by weight: 32%
- Copper ore density: 2800 kg/m³
- Particle size d50: 0.35 mm
- Pipeline: 450 m horizontal, 0.25 m diameter
- Vertical lift: 35 m (tailings dam elevation)
- Water temperature: 22 C
- Sump pump depth below water: 4.5 m
- Suction losses: 12 kPa
- Pump efficiency: 0.72

Tasks:
1. Calculate slurry density and Bingham plastic parameters
2. Estimate pipeline pressure drop
3. Calculate total pump head and shaft power
4. Assess NPSH available and cavitation risk
5. Recommend pump specification
"""
import sys
sys.path.insert(0, "../src")

from mining import slurry
from mining import dewatering as dw

# ---------------------------------------------------------------------------
# INPUT DATA
# ---------------------------------------------------------------------------
Q_m3h = 800.0
Cw = 0.32
rho_s = 2800.0
d50 = 0.35  # mm
L_pipe = 450.0
D_pipe = 0.25
lift_m = 35.0
T_water = 22.0
sump_depth = 4.5
suction_losses = 12.0
pump_eff = 0.72

print("=" * 60)
print("EXERCISE 3: Slurry Pipeline and Dewatering System Design")
print("=" * 60)

# Task 1: Slurry properties
rho_w = dw.water_density_approx(T_water)
rho_m = slurry.slurry_density(rho_w, rho_s, Cw)
bingham = slurry.slurry_viscosity_bingham(0.001, Cw, d50, rho_s)

print(f"\n[Task 1] Slurry Properties")
print(f"  Water density:        {rho_w:.1f} kg/m³")
print(f"  Slurry density:       {rho_m:.1f} kg/m³ (Δ = +{rho_m - rho_w:.1f} kg/m³)")
print(f"  Volume concentration: {bingham['volume_concentration_Cv']:.3f}")
print(f"  Yield stress:         {bingham['yield_stress_Pa']:.2f} Pa")
print(f"  Plastic viscosity:    {bingham['plastic_viscosity_Pas']:.4f} Pa·s")
print(f"  Relative viscosity:   {bingham['relative_viscosity']:.2f}")

# Task 2: Pipeline pressure drop
Q_m3s = Q_m3h / 3600.0
dp_pipe = slurry.slurry_pressure_drop_bingham(
    Q_m3s, D_pipe, L_pipe, rho_m,
    bingham['yield_stress_Pa'], bingham['plastic_viscosity_Pas']
)
# Add static head
static_head_Pa = rho_m * 9.81 * lift_m
total_dp = dp_pipe + static_head_Pa
total_head_m = total_dp / (rho_m * 9.81)

print(f"\n[Task 2] Pipeline Hydraulics")
print(f"  Flow velocity:        {Q_m3s/(3.1416*(D_pipe/2)**2):.2f} m/s")
print(f"  Friction ΔP:          {dp_pipe/1000:.1f} kPa")
print(f"  Static lift ΔP:       {static_head_Pa/1000:.1f} kPa")
print(f"  Total ΔP:             {total_dp/1000:.1f} kPa")
print(f"  Equivalent head:      {total_head_m:.1f} m")

# Task 3: Pump sizing
power = dw.pump_power(Q_m3h, total_head_m, rho_m, pump_eff)
print(f"\n[Task 3] Pump Power")
print(f"  Shaft power:          {power:.1f} kW")
print(f"  Motor size:           {power/0.90:.0f} kW (at 90% motor efficiency)")
print(f"  Annual energy:        {power*8760/1000:.0f} MWh/year")

# Task 4: NPSH
npsh = dw.npsh_available(101.325, sump_depth, suction_losses, T_water)
print(f"\n[Task 4] NPSH Assessment")
print(f"  NPSH available:       {npsh['NPSH_m']:.2f} m")
print(f"  Status:              {npsh['status']}")
print(f"  Vapor pressure:      {npsh['vapor_pressure_kPa']:.2f} kPa")

# Task 5: Pump specification
print(f"\n[Task 5] Pump Specification")
print(f"  Type:                 Horizontal centrifugal, hard-metal lined")
print(f"  Flow:                 {Q_m3h:.0f} m³/h")
print(f"  Head:                 {total_head_m:.1f} m")
print(f"  Solids handling:      d50={d50}mm, Cw={Cw*100:.0f}%")
print(f"  NPSHr requirement:    < {npsh['NPSH_m']-1.0:.1f} m (safety margin 1m)")
print(f"  Material:             High-chrome white iron (ASTM A532)")
print(f"  Seal:                 Mechanical seal with flush")

print("\n" + "=" * 60)
print("Exercise 3 complete.")
print("=" * 60)
