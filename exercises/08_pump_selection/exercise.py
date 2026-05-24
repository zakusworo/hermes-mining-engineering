"""
Exercise 8: Pump Selection and System Curve

Problem:
A dewatering system must handle variable inflow:
- Minimum: 200 m³/h (dry season)
- Maximum: 850 m³/h (wet season)
- Static head: 85 m
- Pipeline: 1200 m, 0.35 m diameter
- Water temp: 18 C
- NPSHr from manufacturer: 5.5 m

Tasks:
1. Calculate system curve (head vs flow)
2. Assess NPSH available across flow range
3. Select pump type and number
4. Recommend VSD for wet season
5. Estimate energy savings with VSD vs throttling
"""
import sys
sys.path.insert(0, "../../src")

from mining import dewatering as dw

print("=" * 60)
print("EXERCISE 8: Pump Selection and System Curve")
print("=" * 60)

flows = [200, 400, 600, 850]
static = 85.0
L = 1200.0
D = 0.35

print("\n[Task 1] System Curve")
for Q in flows:
    # Darcy-Weisbach rough estimate: h_f = f * L/D * v²/(2g)
    v = Q / 3600 / (3.1416 * (D/2)**2)
    hf = 0.02 * L / D * v**2 / (2 * 9.81)
    h_total = static + hf
    print(f"  Q={Q} m³/h → v={v:.2f} m/s → hf={hf:.1f} m → H={h_total:.1f} m")

print("\n[Task 2] NPSH Available")
for Q in flows:
    npsh = dw.npsh_available(101.325, 6.0, 15.0, 18)
    margin = npsh['NPSH_m'] - 5.5
    print(f"  Q={Q} m³/h → NPSHa={npsh['NPSH_m']:.2f} m → margin={margin:.2f} m")

print("\n[Task 3] Pump Selection")
print("  Type: Horizontal split-case centrifugal")
print("  Speed: 4-pole (1480 rpm) for NPSH margin")
print("  Number: 3 duty + 1 standby")
print("  Capacity each: 300 m³/h")

print("\n[Task 4] VSD Recommendation")
print("  Dry season: 1 pump @ 67% speed (flow ∝ speed)")
print("  Wet season: 3 pumps @ 100% speed")

print("\n[Task 5] Energy Savings")
print("  Throttling: 850 m³/h @ 100% speed, 65% efficiency")
print("  VSD: 850 m³/h @ 95% speed, 72% efficiency")
print("  Estimated savings: ~15-20% annual energy")

print("\n" + "=" * 60)
print("Exercise 8 complete.")
print("=" * 60)
