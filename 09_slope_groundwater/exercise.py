"""
Exercise 9: Slope Stability with Groundwater

Problem:
A 120 m high open-pit slope with varying groundwater:
- Dry condition: ru = 0.05
- Moderate: ru = 0.15
- Heavy rainfall: ru = 0.30
- Cohesion: 180 kPa, friction: 30°
- Unit weight: 24 kN/m³, slope angle: 40°

Tasks:
1. Calculate FOS for each pore pressure scenario
2. Determine critical ru for FOS = 1.0
3. Recommend drainage measures
4. Assess bench design under wettest condition
"""
import sys
sys.path.insert(0, "../src")

from mining import slope_stability as ss

print("=" * 60)
print("EXERCISE 9: Slope Stability with Groundwater")
print("=" * 60)

scenarios = [(0.05, "dry"), (0.15, "moderate"), (0.30, "heavy rainfall")]

print("\n[Task 1] FOS vs Pore Pressure")
for ru, label in scenarios:
    F = ss.bishop_factor_of_safety(100, 35, 120, 40, 180, 30, 24, ru)
    status = ss.slope_stability_status(F, 120, 40)
    print(f"  ru={ru:.2f} ({label:15s}) → FOS={F:.2f} → {status['status']}")

print("\n[Task 2] Critical ru for FOS=1.0")
# Binary search for critical ru
low, high = 0.0, 0.5
for _ in range(20):
    mid = (low + high) / 2
    F = ss.bishop_factor_of_safety(100, 35, 120, 40, 180, 30, 24, mid)
    if F > 1.0:
        low = mid
    else:
        high = mid
print(f"  Critical ru ≈ {mid:.3f} (FOS={F:.3f})")

print("\n[Task 3] Drainage Measures")
print("  → Horizontal drain holes: 50 mm, 30 m long, 5 m spacing")
print("  → Drainage blanket at toe")
print("  → Pumped wells if ru > 0.20")
print("  → Monitor piezometers weekly")

print("\n[Task 4] Bench Design (ru=0.30)")
bench = ss.bench_design(12, 60, 8, "soft_rock")
print(f"  Inter-ramp angle: {bench['inter_ramp_angle_deg']}°")
print(f"  Overall slope:    {bench['overall_slope_angle_deg']}°")
print(f"  Status:           {bench['status']}")

print("\n" + "=" * 60)
print("Exercise 9 complete.")
print("=" * 60)
