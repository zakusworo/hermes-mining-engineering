"""
Exercise 13: Tailings Dam Stability

Problem:
A tailings storage facility with:
- Embankment height: 45 m
- Crest width: 8 m
- Upstream slope: 3H:1V (18.4°)
- Downstream slope: 2.5H:1V (21.8°)
- Tailings properties: c=25 kPa, φ=22°, γ=18 kN/m³
- Pore pressure: ru=0.25
- Seismic zone: PGA 0.15g

Tasks:
1. Calculate static FOS using simplified Bishop
2. Estimate pseudo-static seismic FOS
3. Assess breach consequence category
4. Recommend monitoring instrumentation
"""
import sys, math
sys.path.insert(0, "../src")

from mining import slope_stability as ss

print("=" * 60)
print("EXERCISE 13: Tailings Dam Stability")
print("=" * 60)

height = 45.0
upstream_angle = math.degrees(math.atan(1/3))
downstream_angle = math.degrees(math.atan(1/2.5))

print(f"\n[Task 1] Static FOS")
F_upstream = ss.bishop_factor_of_safety(60, 20, height, upstream_angle, 25, 22, 18, 0.25)
F_downstream = ss.bishop_factor_of_safety(60, 20, height, downstream_angle, 25, 22, 18, 0.25)

print(f"  Upstream FOS:   {F_upstream:.2f}")
print(f"  Downstream FOS: {F_downstream:.2f}")

for name, F in [("upstream", F_upstream), ("downstream", F_downstream)]:
    status = ss.slope_stability_status(F, height, upstream_angle if name=="upstream" else downstream_angle)
    print(f"  {name}: {status['status']} — {status['recommended_action']}")

print("\n[Task 2] Seismic FOS (pseudo-static)")
# Reduce cohesion by 30% under seismic
kh = 0.15  # horizontal seismic coefficient
F_seismic_up = ss.bishop_factor_of_safety(60, 20, height, upstream_angle, 25*0.7, 22, 18, 0.25)
F_seismic_down = ss.bishop_factor_of_safety(60, 20, height, downstream_angle, 25*0.7, 22, 18, 0.25)
print(f"  Seismic upstream:   {F_seismic_up:.2f}")
print(f"  Seismic downstream: {F_seismic_down:.2f}")

print("\n[Task 3] Consequence Category")
print("  Population downstream: ~5000")
print("  Environment: river + agricultural land")
print("  Category: HIGH (per ANCOLD / ICOLD)")
print("  Required FOS static: ≥ 1.5")
print("  Required FOS seismic: ≥ 1.1")

print("\n[Task 4] Instrumentation")
print("  → Piezometers: vibrating wire, 6 locations")
print("  → Inclinometers: 3 along downstream toe")
print("  → Survey monuments: monthly crest survey")
print("  → Seepage monitoring: weirs + flow meters")
print("  → Satellite InSAR: quarterly")

print("\n" + "=" * 60)
print("Exercise 13 complete.")
print("=" * 60)
