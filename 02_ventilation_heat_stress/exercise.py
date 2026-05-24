"""
Exercise 2: Mine Ventilation and Heat Stress Management

Problem:
A deep underground gold mine at 800 m depth has the following conditions:
- Working level: 30 C dry-bulb, 85% relative humidity
- Intake air: 22 C, 60% RH (surface conditions)
- Airflow required: 45 m³/s
- Airway: 2500 m horizontal drift, 3.8 m diameter
- Diesel equipment: 850 kW rated total
- Electric equipment: 420 kW rated total
- Load factor: 0.70
- Fan efficiency: 0.68

Tasks:
1. Calculate psychrometric state at intake and working level
2. Determine wet-bulb temperature and heat stress classification
3. Calculate friction pressure drop and fan power
4. Calculate heat load from machinery
5. Recommend work/rest schedule and cooling requirements
"""
import sys
sys.path.insert(0, "../src")

from mining import ventilation as vent

# ---------------------------------------------------------------------------
# INPUT DATA
# ---------------------------------------------------------------------------
T_intake = 22.0
RH_intake = 0.60
T_work = 30.0
RH_work = 0.85
Q = 45.0  # m3/s
L = 2500.0  # m
D = 3.8  # m
diesel_kw = 850.0
electric_kw = 420.0
load_factor = 0.70
fan_eff = 0.68

print("=" * 60)
print("EXERCISE 2: Mine Ventilation and Heat Stress Management")
print("=" * 60)

# Task 1: Psychrometrics
psych_in = vent.psychrometric_properties(T_intake, RH_intake)
psych_work = vent.psychrometric_properties(T_work, RH_work)
print(f"\n[Task 1] Psychrometric State")
print(f"  Intake:    T={psych_in['T_dry_C']}C, RH={psych_in['RH']*100:.0f}%, WB={psych_in['wet_bulb_C']:.1f}C, h={psych_in['enthalpy_kJ_kg']:.1f} kJ/kg")
print(f"  Working:   T={psych_work['T_dry_C']}C, RH={psych_work['RH']*100:.0f}%, WB={psych_work['wet_bulb_C']:.1f}C, h={psych_work['enthalpy_kJ_kg']:.1f} kJ/kg")

delta_h = psych_work['enthalpy_kJ_kg'] - psych_in['enthalpy_kJ_kg']
mass_flow = Q * psych_in['density_kg_m3']
total_heat = mass_flow * delta_h
print(f"\n  Enthalpy rise:   {delta_h:.1f} kJ/kg")
print(f"  Mass flow:       {mass_flow:.1f} kg/s")
print(f"  Sensible+latent heat pick-up: {total_heat/1000:.1f} kW")

# Task 2: Heat stress
hsi = vent.heat_stress_index(T_work, psych_work['wet_bulb_C'])
print(f"\n[Task 2] Heat Stress Assessment")
print(f"  WBGT:            {hsi['WBGT_C']:.1f} C")
print(f"  Classification:  {hsi['classification']}")
print(f"  Work/rest:       {hsi['work_rest_ratio']}")
print(f"  Max continuous:  {hsi['max_continuous_hours']:.1f} hours")
print(f"  Action:          {hsi['action']}")

# Task 3: Ventilation sizing
rho = psych_in['density_kg_m3']
dp = vent.friction_pressure_drop(Q, L, D, rho)
power = vent.fan_power(Q, dp, fan_eff)
print(f"\n[Task 3] Ventilation System")
print(f"  Friction ΔP:     {dp:.0f} Pa")
print(f"  Fan power:       {power:.1f} kW")
print(f"  Annual energy:   {power*24*365/1000:.0f} MWh/year")

# Task 4: Machinery heat
machinery_heat = vent.heat_load_from_machinery(diesel_kw, electric_kw, load_factor)
print(f"\n[Task 4] Heat from Machinery")
print(f"  Diesel heat:     {machinery_heat * diesel_kw*load_factor*0.65/(diesel_kw*load_factor*0.65 + electric_kw*load_factor*0.10):.0f} kW (approx)")
print(f"  Total heat load: {machinery_heat:.1f} kW")

# Task 5: Recommendations
print(f"\n[Task 5] Recommendations")
if hsi['classification'] != 'safe':
    print(f"  → Install chilled water service (CWS) or spot coolers")
    print(f"  → Increase airflow to {Q*1.3:.0f} m³/s minimum")
    print(f"  → Reduce diesel equipment where possible (switch to electric)")
    print(f"  → Implement work/rest: {hsi['work_rest_ratio']}")
else:
    print(f"  → Current ventilation adequate")

print("\n" + "=" * 60)
print("Exercise 2 complete.")
print("=" * 60)
