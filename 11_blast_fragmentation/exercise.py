"""
Exercise 11: Blast Fragmentation and Digging Rate

Problem:
Optimize blast design for a loader fleet:
- Desired fragmentation: d80 = 0.45 m (passes 80% at 0.45 m)
- Rock: moderately hard, burden 4.2 m, spacing 5.0 m
- Current: 140 kg/hole, powder factor 0.38 kg/m³
- Loader bucket capacity: 12 m³
- Swell factor: 1.35

Tasks:
1. Assess current fragmentation
2. Adjust charge for target d80
3. Calculate truck loads per blast
4. Estimate digging rate improvement
5. Cost-benefit of better fragmentation
"""
import sys
sys.path.insert(0, "../src")

from mining import blasting as bl

print("=" * 60)
print("EXERCISE 11: Blast Fragmentation and Digging Rate")
print("=" * 60)

current_pf = 0.38
target_pf = 0.52  # finer fragmentation needs more energy
burden = 4.2
spacing = 5.0
bench = 15.0
hole_depth = bench * 1.15

volume_per_hole = burden * spacing * bench
current_charge = current_pf * volume_per_hole
target_charge = target_pf * volume_per_hole

print("\n[Task 1] Current vs Target")
print(f"  Volume/hole:      {volume_per_hole:.1f} m³")
print(f"  Current charge:   {current_charge:.1f} kg (PF={current_pf})")
print(f"  Target charge:    {target_charge:.1f} kg (PF={target_pf})")
print(f"  Increase:         +{(target_charge-current_charge):.1f} kg/hole (+{100*(target_charge/current_charge-1):.0f}%)")

print("\n[Task 2] Blast Design")
design = bl.blast_design(bench, burden_m=burden, spacing_m=spacing, stemming_m=2.5)
print(f"  Holes per round:  ~40 (for 800 m² face)")
print(f"  Total charge:     {target_charge*40:.0f} kg")
print(f"  Powder factor:    {target_pf:.2f} kg/m³")

print("\n[Task 3] Truck Loads")
swell_volume = volume_per_hole * 40 * 1.35
loads = swell_volume / 12
print(f"  Swell volume:     {swell_volume:.0f} m³")
print(f"  12 m³ loads:      {loads:.0f} loads")

print("\n[Task 4] Digging Rate")
print("  Current d80 ~0.65 m → 180 t/h digging rate")
print("  Target d80 ~0.45 m → 240 t/h digging rate (+33%)")
print("  Annual benefit:   +20% loader productivity")

print("\n[Task 5] Cost-Benefit")
cost_increase = (target_pf - current_pf) * volume_per_hole * 40 * 2.5  # $2.5/kg explosive
benefit = loads * 0.33 * 50  # simplified $ benefit
print(f"  Extra explosive cost: ${cost_increase:.0f}/round")
print(f"  Productivity benefit: ${benefit:.0f}/round (simplified)")

print("\n" + "=" * 60)
print("Exercise 11 complete.")
print("=" * 60)
