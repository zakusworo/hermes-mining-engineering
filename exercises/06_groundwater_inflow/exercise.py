"""
Exercise 6: Groundwater Inflow Estimation

Problem:
An open-pit copper mine intersects a confined aquifer:
- Hydraulic conductivity: k = 8.5 m/day
- Aquifer thickness: 45 m
- Pit base elevation: -85 m (120 m below water table)
- Influence radius: 800 m
- Pit floor area: 125,000 m²
- Pump efficiency: 0.72

Tasks:
1. Estimate steady-state groundwater inflow using Theim equation
2. Calculate total pump head (lift + friction + discharge)
3. Size dewatering pumps (number and power)
4. Assess annual dewatering cost at $0.08/kWh
5. Recommend wellfield layout (spacing, depth)
"""
import sys
sys.path.insert(0, "../../src")

from mining import dewatering as dw

print("=" * 60)
print("EXERCISE 6: Groundwater Inflow Estimation")
print("=" * 60)

k = 8.5
thickness = 45.0
drawdown = 120.0
R = 800.0
A = 125000.0

inflow = dw.groundwater_inflow_empirical(k, thickness, drawdown, R, A)
print(f"\n[Task 1] Groundwater Inflow")
print(f"  Theim inflow:     {inflow:.1f} m³/h")
print(f"  Daily inflow:     {inflow*24:.0f} m³/day")
print(f"  Annual inflow:    {inflow*24*365/1e6:.2f} million m³/year")

head = drawdown + 15.0  # lift + discharge head
n_pumps = max(1, int(inflow / 300) + 1)  # 300 m3/h per pump max
flow_per_pump = inflow / n_pumps
power_per_pump = dw.pump_power(flow_per_pump, head, 1000, 0.72)
total_power = power_per_pump * n_pumps

print(f"\n[Task 2] Pump System")
print(f"  Total head:       {head:.0f} m")
print(f"  Pumps required:   {n_pumps} × {flow_per_pump:.0f} m³/h")
print(f"  Power/pump:       {power_per_pump:.1f} kW")
print(f"  Total power:      {total_power:.1f} kW")

annual_mwh = total_power * 8760 / 1000
cost = annual_mwh * 1000 * 0.08
print(f"\n[Task 3] Annual Cost")
print(f"  Energy:           {annual_mwh:.0f} MWh/year")
print(f"  Cost @ $0.08/kWh: ${cost:,.0f}/year")

print(f"\n[Task 4] Wellfield Layout")
print(f"  Wells:            {n_pumps} vertical wells, 150 mm diameter")
print(f"  Depth:            {drawdown + 10:.0f} m (10 m into aquifer)")
print(f"  Spacing:          {min(200, R/3):.0f} m triangular pattern")
print(f"  Screen:           Slotted PVC, 0.5 mm slot")
print(f"  Filter pack:      2-4 mm gravel")

print("\n" + "=" * 60)
print("Exercise 6 complete.")
print("=" * 60)
