"""
Exercise 10: Bench Design Across Geotechnical Domains

Problem:
An open-pit iron ore mine crosses 3 geotechnical domains:
- Hard iron formation: benches 15 m, angle 70°
- Transitional zone: benches 12 m, angle 55°
- Weathered oxide: benches 8 m, angle 45°

Tasks:
1. Design benches for each domain
2. Compare catch capacity and inter-ramp angles
3. Calculate overall pit slope angle for each
4. Recommend berm widths for rockfall containment
5. Determine domain transition strategy
"""
import sys
sys.path.insert(0, "../../src")

from mining import slope_stability as ss

print("=" * 60)
print("EXERCISE 10: Bench Design Across Geotechnical Domains")
print("=" * 60)

domains = [
    ("Hard iron formation", 15, 70, 10, "hard_rock"),
    ("Transitional zone", 12, 55, 8, "hard_rock"),
    ("Weathered oxide", 8, 45, 6, "soft_rock"),
]

print("\n[Task 1-3] Bench Design Comparison")
for name, h, angle, berm, domain in domains:
    bench = ss.bench_design(h, angle, berm, domain)
    print(f"\n  {name}:")
    print(f"    Bench height:        {h} m")
    print(f"    Bench face angle:    {angle}°")
    print(f"    Berm width:          {berm} m")
    print(f"    Inter-ramp angle:    {bench['inter_ramp_angle_deg']}°")
    print(f"    Overall slope:       {bench['overall_slope_angle_deg']}°")
    print(f"    Catch capacity:      {bench['catch_capacity_m3_per_m']:.0f} m³/m")
    print(f"    Status:              {bench['status']}")

print("\n[Task 4] Rockfall Containment")
print("  Hard domain: 10 m berm (catches 90% of design rockfall)")
print("  Transitional: 8 m berm + shotcrete face")
print("  Weathered: 6 m berm + mesh + bench scaling")

print("\n[Task 5] Domain Transition")
print("  → 20 m wide step-out at domain boundary")
print("  → Additional berm + monitoring prisms")
print("  → Reduce bench height by 20% in transition")
print("  → Install dewatering before excavating weathered zone")

print("\n" + "=" * 60)
print("Exercise 10 complete.")
print("=" * 60)
