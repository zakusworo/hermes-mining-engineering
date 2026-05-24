"""
Exercise 12: Subsidence Prediction for Underground Mine

Problem:
A longwall coal mine at 280 m depth:
- Seam thickness: 3.5 m
- Panel width: 220 m
- Panel length: 1800 m
- Overburden: sandstone/shale sequence
- Critical angle of draw: 35°

Tasks:
1. Estimate maximum subsidence (empirical)
2. Calculate subsidence profile across panel
3. Assess surface structure impact at 150 m from panel edge
4. Recommend monitoring and mitigation
"""
import sys, math
sys.path.insert(0, "../src")

print("=" * 60)
print("EXERCISE 12: Subsidence Prediction")
print("=" * 60)

depth = 280.0
thickness = 3.5
width = 220.0
length = 1800.0

# UK/NCB empirical: S_max ≈ 0.9 × thickness for width/depth > 1.2
wh_ratio = width / depth
if wh_ratio > 1.2:
    S_max = 0.90 * thickness
else:
    S_max = 0.90 * thickness * (wh_ratio / 1.2)

print("\n[Task 1] Maximum Subsidence")
print(f"  Width/depth ratio: {wh_ratio:.2f}")
print(f"  S_max:             {S_max:.2f} m")
print(f"  As % of thickness: {100*S_max/thickness:.0f}%")

print("\n[Task 2] Subsidence Profile")
# Gaussian-ish profile
half_width = width / 2
for x in [-300, -150, -50, 0, 50, 150, 300]:
    # Simplified bell curve
    S = S_max * math.exp(-(x**2) / (2 * (half_width/2)**2))
    print(f"  x={x:4d} m → S={S:.3f} m")

print("\n[Task 3] Surface Impact at 150 m from edge")
# Angle of draw: structures affected within 35° from seam
angle_of_draw = 35.0
influence_distance = depth * math.tan(math.radians(90 - angle_of_draw))
print(f"  Angle of draw:     {angle_of_draw}°")
print(f"  Influence zone:    ±{influence_distance:.0f} m from panel edge")

if 150 < influence_distance:
    print(f"  150 m from edge:   WITHIN influence zone")
    print(f"  Expected subsidence: ~{S_max * 0.3:.2f} m")
else:
    print(f"  150 m from edge:   OUTSIDE influence zone")

print("\n[Task 4] Monitoring and Mitigation")
print("  → Survey prisms every 50 m along transects")
print("  → InSAR satellite monitoring monthly")
print("  → Crack gauges on structures within influence zone")
print("  → Pre-load foundations in high-risk area")
print("  → Grout injection if tilt > 5 mm/m")

print("\n" + "=" * 60)
print("Exercise 12 complete.")
print("=" * 60)
