"""
Exercise 4: Blast Design and Vibration Control

Problem:
An open-pit gold mine plans production blasting near a residential area:
- Bench height: 15 m
- Hole diameter: 150 mm
- Rock: weathered granite (site factor K=1200, α=1.6)
- Nearest house: 350 m
- Charge per delay: 80 kg (maximum for regulatory compliance)
- Regulatory limit for residential: 5 mm/s PPV
- Blasting occurs 5 days/week, 2 rounds/day

Tasks:
1. Design blast pattern (burden, spacing, stemming, subdrill)
2. Predict PPV at nearest house and assess compliance
3. Predict air overpressure and assess noise impact
4. If PPV exceeds limit, calculate required charge reduction or distance
5. Estimate annual blast events and monitoring strategy
"""
import sys, math
sys.path.insert(0, "../src")

from mining import blasting as bl

# ---------------------------------------------------------------------------
# INPUT DATA
# ---------------------------------------------------------------------------
bench_h = 15.0
hole_dia = 150.0
site_k = 1200.0
alpha = 1.6
distance = 350.0
charge_per_delay = 80.0  # kg
ppv_limit = 5.0  # mm/s
overpressure_k = 400.0
beta = 1.4

print("=" * 60)
print("EXERCISE 4: Blast Design and Vibration Control")
print("=" * 60)

# Task 1: Blast design
design = bl.blast_design(bench_h, hole_diameter_mm=hole_dia)
print(f"\n[Task 1] Blast Design")
print(f"  Hole diameter:    {design['hole_diameter_mm']} mm")
print(f"  Hole depth:       {design['hole_depth_m']:.1f} m")
print(f"  Burden:           {design['burden_m']:.1f} m")
print(f"  Spacing:          {design['spacing_m']:.1f} m")
print(f"  Stemming:         {design['stemming_m']:.1f} m")
print(f"  Subdrill:         {design['subdrill_m']:.1f} m")
print(f"  Charge/hole:      {design['charge_kg']:.1f} kg")
print(f"  Volume/hole:      {design['volume_m3']:.1f} m³")
print(f"  Powder factor:    {design['powder_factor_kg_m3']:.3f} kg/m³")
print(f"  Status:           {design['status']}")

# Task 2: PPV prediction
ppv = bl.peak_particle_velocity(distance, charge_per_delay, site_k, alpha)
ppv_assess = bl.vibration_assessment(ppv, "residential")
print(f"\n[Task 2] Blast Vibration at {distance}m")
print(f"  Predicted PPV:    {ppv} mm/s")
print(f"  Regulatory limit:   {ppv_limit} mm/s")
print(f"  Exceedance:       {ppv_assess['exceedance_factor']:.2f}×")
print(f"  Status:           {ppv_assess['status']}")
print(f"  Action:           {ppv_assess['recommendation']}")

# Task 3: Air overpressure
op = bl.air_overpressure(distance, charge_per_delay * 6, overpressure_k, beta)  # 6 holes per round
op_assess = bl.overpressure_assessment(op, "residential")
print(f"\n[Task 3] Air Overpressure")
print(f"  Predicted OP:     {op} dB")
print(f"  Threshold:        {op_assess['threshold_dB']} dB")
print(f"  Status:           {op_assess['status']}")
print(f"  Action:           {op_assess['recommendation']}")

# Task 4: Compliance redesign
if ppv > ppv_limit:
    print(f"\n[Task 4] Redesign for Compliance")
    # Option A: Reduce charge per delay
    # PPV = K * (D/√W)^(-α)  →  W_new = W * (PPV_new/PPV)^(2/α)
    ratio = ppv_limit / ppv
    W_new = charge_per_delay * (ratio ** (2.0 / alpha))
    print(f"  Option A — Reduce charge/delay:")
    print(f"    Max charge/delay: {W_new:.1f} kg (was {charge_per_delay} kg)")
    print(f"    Delays per round: {math.ceil(design['charge_kg'] * 6 / W_new)}")
    
    # Option B: Increase distance
    # D_new = D * (PPV/PPV_new)^(1/α)
    D_new = distance * ((ppv / ppv_limit) ** (1.0 / alpha))
    print(f"\n  Option B — Increase distance:")
    print(f"    Required setback: {D_new:.0f} m (current {distance} m)")
    
    # Option C: Decked charge
    print(f"\n  Option C — Decked charge:")
    print(f"    Split each hole into 2 decks with 25 ms delay")
    print(f"    Effective charge/delay: {design['charge_kg']/2:.1f} kg")
    print(f"    PPV with decked: {bl.peak_particle_velocity(distance, design['charge_kg']/2, site_k, alpha):.2f} mm/s")

# Task 5: Annual monitoring
rounds_per_year = 5 * 2 * 52  # 5 days × 2 rounds × 52 weeks
print(f"\n[Task 5] Monitoring Strategy")
print(f"  Annual rounds:    {rounds_per_year}")
print(f"  Monitoring:       Continuous seismograph at house + 2 mid-field stations")
print(f"  Trigger level:    2.5 mm/s (50% of limit)")
print(f"  Alarm level:      4.0 mm/s (80% of limit)")
print(f"  Reporting:        Daily blast report to regulator")
print(f"  Community:        Pre-blast notification app")

print("\n" + "=" * 60)
print("Exercise 4 complete.")
print("=" * 60)
