"""
Exercise 1: Rock Mass Characterization and Slope Stability

Problem:
A granite open-pit mine has the following geotechnical data:
- Drill core RQD measurements: [18, 12, 25, 8, 30, 15, 22, 10, 28, 14] cm
- Joint spacing: 0.45 m average
- Joint condition rating: 20 (good condition, some clay)
- Groundwater: dry (rating 15)
- Orientation: slightly unfavorable (adjustment -5)
- Intact rock UCS: 120 MPa
- Intact mi: 23
- Disturbance D: 0.3 (moderate blasting)
- Slope height: 180 m
- Slope angle: 44°
- Pore pressure ratio ru: 0.10

Tasks:
1. Calculate RQD and basic RMR
2. Determine Hoek-Brown parameters (mb, s, a, E_rm)
3. Convert to Mohr-Coulomb equivalent (c, φ)
4. Assess slope stability with Bishop simplified FOS
5. Recommend bench design for hard rock domain
"""
import sys, math
sys.path.insert(0, "../../src")

from mining import rock_mechanics as rm
from mining import slope_stability as ss

# ---------------------------------------------------------------------------
# INPUT DATA
# ---------------------------------------------------------------------------
core_lengths = [18, 12, 25, 8, 30, 15, 22, 10, 28, 14]  # cm
joint_spacing = 0.45
joint_condition = 20
groundwater_rating = 15
orientation_adj = -5
sigma_ci = 120.0  # MPa
mi = 23
D = 0.3
slope_h = 180.0  # m
slope_angle = 44.0  # degrees
unit_weight = 26.0  # kN/m3
ru = 0.10

print("=" * 60)
print("EXERCISE 1: Rock Mass Characterization and Slope Stability")
print("=" * 60)

# Task 1: RQD and RMR
rqd = rm.rqd_from_core_recovery(core_lengths)
rmr = rm.rmr_basic(rqd, joint_spacing, joint_condition, groundwater_rating, orientation_adj)
print(f"\n[Task 1] Rock Mass Rating")
print(f"  RQD:           {rqd:.1f}%")
print(f"  Basic RMR:     {rmr}/100")
if rmr > 60:
    rmr_class = "Good rock"
elif rmr > 40:
    rmr_class = "Fair rock"
elif rmr > 20:
    rmr_class = "Poor rock"
else:
    rmr_class = "Very poor rock"
print(f"  Classification: {rmr_class}")

# Estimate GSI from RMR (rough correlation: GSI ≈ RMR - 5)
gsi = min(100, max(10, rmr - 5))
print(f"  Estimated GSI:  {gsi}")

# Task 2: Hoek-Brown
params = rm.hoek_brown_parameters(gsi, mi, D)
print(f"\n[Task 2] Hoek-Brown Parameters")
print(f"  mb:            {params['mb']}")
print(f"  s:             {params['s']}")
print(f"  a:             {params['a']}")
print(f"  E_rm:          {params['E_rm_MPa']} MPa")
print(f"  σ_cm:          {params['sigma_cm_MPa']} MPa")

# Task 3: Mohr-Coulomb equivalent
mc = rm.mohr_coulomb_from_hoek_brown(params['mb'], params['s'], params['a'], sigma_ci, sigma_ci/4)
print(f"\n[Task 3] Mohr-Coulomb Equivalent")
print(f"  Cohesion (c):   {mc['cohesion_MPa']:.2f} MPa")
print(f"  Friction (φ):   {mc['friction_angle_deg']:.1f}°")
print(f"  Tensile:        {mc['tensile_strength_MPa']:.2f} MPa")

# Task 4: Bishop FOS
F = ss.bishop_factor_of_safety(
    slip_radius_m=120, slip_depth_m=40,
    slope_height_m=slope_h, slope_angle_deg=slope_angle,
    cohesion_kPa=mc['cohesion_MPa']*1000,
    friction_angle_deg=mc['friction_angle_deg'],
    unit_weight_kN_m3=unit_weight,
    pore_pressure_ratio_ru=ru
)
status = ss.slope_stability_status(F, slope_h, slope_angle)
print(f"\n[Task 4] Slope Stability")
print(f"  Factor of Safety: {F}")
print(f"  Status:           {status['status']} ({status['risk_level']} risk)")
print(f"  Action:           {status['recommended_action']}")

# Task 5: Bench design
bench = ss.bench_design(15, 65, 8, "hard_rock")
print(f"\n[Task 5] Bench Design (Hard Rock)")
print(f"  Inter-ramp angle: {bench['inter_ramp_angle_deg']}°")
print(f"  Overall slope:    {bench['overall_slope_angle_deg']}°")
print(f"  Catch capacity:   {bench['catch_capacity_m3_per_m']:.0f} m³/m")
print(f"  Status:           {bench['status']}")

print("\n" + "=" * 60)
print("Exercise 1 complete.")
print("=" * 60)
