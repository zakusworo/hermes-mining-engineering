"""
Exercise 14: Mine Closure and Reclamation Water Balance

Problem:
A closed open-pit mine becomes a pit lake:
- Pit dimensions: 800 m × 600 m × 180 m deep
- Annual rainfall: 650 mm
- Evaporation: 1200 mm/year
- Catchment area: 2.4 km²
- Groundwater inflow: 35 m³/h
- Target water level: 40 m below crest

Tasks:
1. Calculate pit lake water balance
2. Estimate time to fill to target level
3. Assess water quality evolution (simplified)
4. Design overflow spillway
5. Closure cost estimate
"""
import sys, math
sys.path.insert(0, "../../src")

print("=" * 60)
print("EXERCISE 14: Mine Closure Water Balance")
print("=" * 60)

pit_area = 800 * 600  # m2
pit_depth = 180.0
target_depth = 40.0  # below crest = 140 m depth
rainfall = 650.0  # mm/year
evap = 1200.0  # mm/year
catchment = 2.4e6  # m2
inflow = 35.0  # m3/h

print("\n[Task 1] Water Balance")
# Effective rainfall on pit surface
rain_m3 = pit_area * rainfall / 1000
evap_m3 = pit_area * evap / 1000
catchment_runoff = catchment * rainfall * 0.15 / 1000  # 15% runoff coefficient
inflow_m3 = inflow * 24 * 365

net_annual = rain_m3 - evap_m3 + catchment_runoff + inflow_m3
print(f"  Rainfall on pit:    +{rain_m3:.0f} m³/year")
print(f"  Evaporation:        -{evap_m3:.0f} m³/year")
print(f"  Catchment runoff:   +{catchment_runoff:.0f} m³/year")
print(f"  Groundwater inflow: +{inflow_m3:.0f} m³/year")
print(f"  Net annual:         {net_annual:+.0f} m³/year")

print("\n[Task 2] Time to Fill")
target_volume = pit_area * (pit_depth - target_depth)
years_to_fill = target_volume / net_annual if net_annual > 0 else float('inf')
print(f"  Target volume:      {target_volume:.0f} m³")
print(f"  Years to target:    {years_to_fill:.1f} years")

print("\n[Task 3] Water Quality")
print("  pH: acidic (pyrite oxidation) → 3-5 expected")
print("  Metals: elevated Fe, Cu, Zn, Mn")
print("  Sulfate: 2000-8000 mg/L")
print("  Treatment: lime precipitation + wetland")

print("\n[Task 4] Overflow Spillway")
print(f"  Design flow: 1:100 year flood = {catchment * 150 / 1000 / 86400:.1f} m³/s")
print("  Spillway: rock-lined trapezoidal channel")
print("  Freeboard: 1.5 m above design flood")

print("\n[Task 5] Closure Cost")
cost_items = {
    "Spillway construction": 850000,
    "Water treatment plant": 2500000,
    "Revegetation": 450000,
    "Monitoring (10 years)": 300000,
    "Contingency (15%)": 0,
}
subtotal = sum(v for v in cost_items.values() if v > 0)
cost_items["Contingency (15%)"] = int(subtotal * 0.15)
total = sum(cost_items.values())

for item, cost in cost_items.items():
    print(f"  {item:30s} ${cost:10,}")
print(f"  {'TOTAL':30s} ${total:10,}")

print("\n" + "=" * 60)
print("Exercise 14 complete.")
print("=" * 60)
