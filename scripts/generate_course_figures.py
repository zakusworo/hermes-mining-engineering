"""
Generate figures for all 15 mining engineering exercises.
Produces matplotlib PNGs into assets/figures/.

Usage:
    pip install matplotlib
    python3 scripts/generate_course_figures.py
"""
import sys, os, math
sys.path.insert(0, "src")
os.makedirs("assets/figures", exist_ok=True)

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from mining import rock_mechanics as rm
from mining import slope_stability as ss
from mining import blasting as bl
from mining import dewatering as dw
from mining import ventilation as vent
from mining import slurry

plt.rcParams.update({
    "figure.facecolor": "#1a1a2e",
    "axes.facecolor": "#16213e",
    "axes.edgecolor": "#e94560",
    "axes.labelcolor": "#eaeaea",
    "text.color": "#eaeaea",
    "xtick.color": "#a0a0a0",
    "ytick.color": "#a0a0a0",
    "grid.color": "#0f3460",
    "grid.alpha": 0.3,
})

def save(fig, name):
    path = f"assets/figures/{name}.png"
    fig.savefig(path, dpi=150, bbox_inches="tight", facecolor="#1a1a2e")
    plt.close(fig)
    print(f"  → {path}")

# 01: Rock Mass — GSI vs σ_cm
print("[01] rock_mass_gsi_strength.png")
fig, ax = plt.subplots(figsize=(8,5))
gsi_range = list(range(10, 101, 5))
for mi, color in [(15, "#e94560"), (25, "#0f3460"), (35, "#533483")]:
    strengths = [rm.hoek_brown_parameters(g, mi, 0.3)['sigma_cm_MPa'] for g in gsi_range]
    ax.plot(gsi_range, strengths, label=f"mi={mi}", color=color, lw=2)
ax.set_xlabel("GSI")
ax.set_ylabel("Rock Mass Strength σ_cm (MPa)")
ax.set_title("Exercise 1: Hoek-Brown Rock Mass Strength vs GSI")
ax.legend(); ax.grid(True); ax.set_yscale("log")
save(fig, "01_rock_mass_gsi_strength")

# 02: Ventilation — Enthalpy vs T
print("[02] ventilation_psychrometric.png")
fig, ax = plt.subplots(figsize=(8,5))
T_range = list(range(15, 41))
for rh, color, label in [(0.4, "#e94560", "RH=40%"), (0.6, "#0f3460", "RH=60%"),
                         (0.8, "#533483", "RH=80%"), (0.95, "#16c79a", "RH=95%")]:
    enthalpies = [vent.psychrometric_properties(t, rh)['enthalpy_kJ_kg'] for t in T_range]
    ax.plot(T_range, enthalpies, label=label, color=color, lw=2)
ax.set_xlabel("Dry-Bulb Temperature (C)"); ax.set_ylabel("Enthalpy (kJ/kg)")
ax.set_title("Exercise 2: Mine Air Enthalpy vs Temperature")
ax.legend(); ax.grid(True)
save(fig, "02_ventilation_psychrometric")

# 03: Slurry — Density vs Cw
print("[03] slurry_density_concentration.png")
fig, ax = plt.subplots(figsize=(8,5))
Cw_range = [i/100 for i in range(0, 71, 5)]
for rho_s, label, color in [(2800, "Copper (2800)", "#e94560"),
                            (4200, "Iron (4200)", "#0f3460"),
                            (7800, "Gold (7800)", "#533483")]:
    densities = [slurry.slurry_density(1000, rho_s, cw) for cw in Cw_range]
    ax.plot([c*100 for c in Cw_range], densities, label=label, color=color, lw=2)
ax.set_xlabel("Solids Concentration Cw (% by weight)"); ax.set_ylabel("Slurry Density (kg/m³)")
ax.set_title("Exercise 3: Slurry Density vs Solids Concentration")
ax.legend(); ax.grid(True)
save(fig, "03_slurry_density_concentration")

# 04: Blast — PPV vs Distance
print("[04] blast_vibration_distance.png")
fig, ax = plt.subplots(figsize=(8,5))
distances = list(range(100, 1001, 50))
for charge, color, label in [(25, "#16c79a", "25 kg/delay"), (80, "#e94560", "80 kg/delay"),
                              (200, "#533483", "200 kg/delay")]:
    ppvs = [bl.peak_particle_velocity(d, charge, 1000, 1.5) for d in distances]
    ax.plot(distances, ppvs, label=label, color=color, lw=2)
ax.axhline(5, color="#ff6b6b", linestyle="--", label="Residential limit (5 mm/s)")
ax.axhline(10, color="#ffd93d", linestyle="--", label="Industrial limit (10 mm/s)")
ax.set_xlabel("Distance (m)"); ax.set_ylabel("Peak Particle Velocity (mm/s)")
ax.set_title("Exercise 4: Blast Vibration Decay with Distance")
ax.set_yscale("log"); ax.legend(); ax.grid(True)
save(fig, "04_blast_vibration_distance")

# 05: Dashboard
print("[05] integrated_dashboard.png")
fig, axes = plt.subplots(2, 3, figsize=(14, 8))

ax = axes[0,0]
gsi_r = list(range(10, 101, 5))
E_vals = [rm.hoek_brown_parameters(g, 18, 0.4)['E_rm_MPa'] for g in gsi_r]
ax.plot(gsi_r, E_vals, color="#e94560", lw=2)
ax.set_xlabel("GSI"); ax.set_ylabel("E_rm (MPa)"); ax.set_title("Rock Mass Modulus")
ax.grid(True)

ax = axes[0,1]
T_r = list(range(15, 41))
for rh, c, l in [(0.5, "#0f3460", "50%"), (0.8, "#e94560", "80%")]:
    wbs = [vent.psychrometric_properties(t, rh)['wet_bulb_C'] for t in T_r]
    ax.plot(T_r, wbs, color=c, lw=2, label=l)
ax.set_xlabel("Dry T (C)"); ax.set_ylabel("Wet Bulb (C)"); ax.set_title("Psychrometric")
ax.legend(); ax.grid(True)

ax = axes[0,2]
Cw_r = [i/100 for i in range(0, 51, 5)]
viscs = [slurry.slurry_viscosity_bingham(0.001, cw, 0.4, 2800)['relative_viscosity'] for cw in Cw_r]
ax.plot([c*100 for c in Cw_r], viscs, color="#533483", lw=2)
ax.set_xlabel("Cw (%)"); ax.set_ylabel("Relative Viscosity"); ax.set_title("Slurry Viscosity")
ax.grid(True)

ax = axes[1,0]
depths = list(range(1, 21))
npshs = [dw.npsh_available(101.325, d, 10, 25)['NPSH_m'] for d in depths]
ax.plot(depths, npshs, color="#16c79a", lw=2)
ax.axhline(0, color="#ff6b6b", linestyle="--")
ax.set_xlabel("Sump Depth (m)"); ax.set_ylabel("NPSH Available (m)"); ax.set_title("Dewatering NPSH")
ax.grid(True)

ax = axes[1,1]
ru_r = [i/100 for i in range(0, 51, 5)]
F_vals = [ss.bishop_factor_of_safety(80, 25, 120, 40, 180, 30, 24, ru) for ru in ru_r]
ax.plot([r*100 for r in ru_r], F_vals, color="#e94560", lw=2)
ax.axhline(1.0, color="#ff6b6b", linestyle="--")
ax.set_xlabel("ru (%)"); ax.set_ylabel("Factor of Safety"); ax.set_title("Slope Stability vs Groundwater")
ax.grid(True)

ax = axes[1,2]
d_r = list(range(100, 801, 50))
ppvs = [bl.peak_particle_velocity(d, 100, 1000, 1.5) for d in d_r]
ax.plot(d_r, ppvs, color="#0f3460", lw=2)
ax.set_xlabel("Distance (m)"); ax.set_ylabel("PPV (mm/s)"); ax.set_title("Blast Vibration")
ax.set_yscale("log"); ax.grid(True)

fig.suptitle("Exercise 5: Integrated Mine Design Dashboard", fontsize=14, fontweight="bold")
fig.tight_layout(); save(fig, "05_integrated_dashboard")

# 06: Groundwater inflow vs drawdown
print("[06] groundwater_inflow_drawdown.png")
fig, ax = plt.subplots(figsize=(8,5))
drawdowns = list(range(20, 201, 10))
inflows = [dw.groundwater_inflow_empirical(8.5, 45, dd, 800, 125000) for dd in drawdowns]
ax.plot(drawdowns, inflows, color="#16c79a", lw=2)
ax.set_xlabel("Drawdown (m)"); ax.set_ylabel("Steady-State Inflow (m³/h)")
ax.set_title("Exercise 6: Groundwater Inflow vs Drawdown")
ax.grid(True); save(fig, "06_groundwater_inflow_drawdown")

# 07: Rock comparison bar
print("[07] rock_comparison_bar.png")
fig, ax = plt.subplots(figsize=(8,5))
rocks = {"Granite": {"gsi":65, "mi":25, "D":0.2, "ucs":140},
         "Shale": {"gsi":35, "mi":8, "D":0.5, "ucs":45}}
metrics = []
for name, r in rocks.items():
    p = rm.hoek_brown_parameters(r["gsi"], r["mi"], r["D"])
    mc = rm.mohr_coulomb_from_hoek_brown(p['mb'], p['s'], p['a'], r['ucs'], r['ucs']/4)
    metrics.append({"name": name, "E": p['E_rm_MPa'], "c": mc['cohesion_MPa'],
                    "phi": mc['friction_angle_deg'], "sigma_cm": p['sigma_cm_MPa']})
x = range(len(metrics)); width = 0.2
ax.bar([i-1.5*width for i in x], [m['E']/1000 for m in metrics], width, label="E (GPa)", color="#e94560")
ax.bar([i-0.5*width for i in x], [m['c'] for m in metrics], width, label="c (MPa)", color="#0f3460")
ax.bar([i+0.5*width for i in x], [m['phi'] for m in metrics], width, label="φ (°)", color="#533483")
ax.bar([i+1.5*width for i in x], [m['sigma_cm'] for m in metrics], width, label="σ_cm (MPa)", color="#16c79a")
ax.set_xticks(x); ax.set_xticklabels([m['name'] for m in metrics])
ax.set_ylabel("Value"); ax.set_title("Exercise 7: Rock Mass Property Comparison")
ax.legend(); ax.grid(True, axis="y"); save(fig, "07_rock_comparison_bar")

# 08: Pump system curve
print("[08] pump_system_curve.png")
fig, ax = plt.subplots(figsize=(8,5))
flows = list(range(100, 1001, 50))
static = 85; L, D_pipe = 1200, 0.35
heads = []
for Q in flows:
    v = Q / 3600 / (3.1416 * (D_pipe/2)**2)
    hf = 0.02 * L / D_pipe * v**2 / (2 * 9.81)
    heads.append(static + hf)
ax.plot(flows, heads, color="#0f3460", lw=3, label="System Curve")
pump_h = [140 - 0.00008 * Q**2 for Q in flows]
ax.plot(flows, pump_h, color="#e94560", lw=3, label="Pump Curve (single)")
ax.set_xlabel("Flow (m³/h)"); ax.set_ylabel("Head (m)")
ax.set_title("Exercise 8: Pump System Curve")
ax.legend(); ax.grid(True); save(fig, "08_pump_system_curve")

# 09: Slope FOS vs ru
print("[09] slope_fos_ru.png")
fig, ax = plt.subplots(figsize=(8,5))
ru_range = [i/100 for i in range(0, 51, 2)]
F_vals = [ss.bishop_factor_of_safety(100, 35, 120, 40, 180, 30, 24, ru) for ru in ru_range]
ax.plot([r*100 for r in ru_range], F_vals, color="#e94560", lw=2)
ax.axhline(1.0, color="#ff6b6b", linestyle="--", lw=2, label="FOS = 1.0 (critical)")
ax.axhline(1.3, color="#ffd93d", linestyle="--", lw=1, label="FOS = 1.3 (minimum)")
ax.fill_between([r*100 for r in ru_range], 0, 1.0, alpha=0.2, color="#ff6b6b")
ax.set_xlabel("Pore Pressure Ratio ru (%)"); ax.set_ylabel("Factor of Safety")
ax.set_title("Exercise 9: Slope FOS vs Groundwater Pressure")
ax.legend(); ax.grid(True); save(fig, "09_slope_fos_ru")

# 10: Bench cross-section
print("[10] bench_cross_section.png")
fig, ax = plt.subplots(figsize=(10, 6))
bench_h, face_angle, berm = 15, 65, 8
run = bench_h / math.tan(math.radians(face_angle))
ax.plot([0, run], [0, bench_h], color="#e94560", lw=3)
ax.plot([run, run + berm], [bench_h, bench_h], color="#16c79a", lw=3)
ax.plot([run + berm, run + berm + run], [bench_h, 2*bench_h], color="#e94560", lw=3)
overall = math.degrees(math.atan(2*bench_h / (2*run + berm)))
ax.plot([0, 2*run + berm], [0, 2*bench_h], color="#ffd93d", linestyle="--", lw=2, label=f"Overall slope ≈ {overall:.1f}°")
ax.set_xlim(-2, 35); ax.set_ylim(-2, 35); ax.set_aspect("equal")
ax.set_xlabel("Horizontal (m)"); ax.set_ylabel("Vertical (m)")
ax.set_title(f"Exercise 10: Bench Cross-Section (H={bench_h}m, face={face_angle}°, berm={berm}m)")
ax.legend(); ax.grid(True); save(fig, "10_bench_cross_section")

# 11: Fragmentation curve
print("[11] blast_fragmentation_curve.png")
fig, ax = plt.subplots(figsize=(8,5))
sizes = [0.05, 0.1, 0.2, 0.3, 0.5, 0.7, 1.0, 1.5, 2.0]
pass_current = [10, 25, 45, 60, 75, 85, 92, 97, 99]
pass_target = [20, 40, 62, 78, 90, 95, 98, 99.5, 99.9]
ax.plot(sizes, pass_current, color="#0f3460", lw=2, marker="o", label="Current PF=0.38")
ax.plot(sizes, pass_target, color="#e94560", lw=2, marker="s", label="Target PF=0.52")
ax.axvline(0.45, color="#16c79a", linestyle="--", label="Target d80 = 0.45 m")
ax.set_xlabel("Fragment Size (m)"); ax.set_ylabel("Cumulative Passing (%)")
ax.set_title("Exercise 11: Blast Fragmentation Distribution")
ax.legend(); ax.grid(True); save(fig, "11_blast_fragmentation_curve")

# 12: Subsidence profile
print("[12] subsidence_profile.png")
fig, ax = plt.subplots(figsize=(10, 5))
xs = list(range(-400, 401, 20))
S_max = 0.90 * 3.5
half_width = 220 / 2
Ss = [S_max * math.exp(-(x**2) / (2 * (half_width/2)**2)) for x in xs]
ax.plot(xs, Ss, color="#e94560", lw=2)
ax.fill_between(xs, 0, Ss, alpha=0.3, color="#e94560")
ax.axvline(-110, color="#16c79a", linestyle="--", label="Panel edge")
ax.axvline(110, color="#16c79a", linestyle="--")
ax.set_xlabel("Distance from Panel Center (m)"); ax.set_ylabel("Subsidence (m)")
ax.set_title("Exercise 12: Longwall Subsidence Profile")
ax.legend(); ax.grid(True); save(fig, "12_subsidence_profile")

# 13: Tailings cross-section
print("[13] tailings_cross_section.png")
fig, ax = plt.subplots(figsize=(10, 6))
height = 45; upstream_run = height * 3; downstream_run = height * 2.5; crest = 8
ax.plot([0, upstream_run], [0, height], color="#e94560", lw=2, label="Upstream slope 3H:1V")
ax.plot([upstream_run, upstream_run + crest], [height, height], color="#16c79a", lw=3, label="Crest")
ax.plot([upstream_run + crest, upstream_run + crest + downstream_run], [height, 0],
        color="#0f3460", lw=2, label="Downstream slope 2.5H:1V")
ax.plot([0, upstream_run + crest + downstream_run], [0, 0], color="#a0a0a0", lw=1)
ax.fill_between([0, upstream_run, upstream_run + crest, upstream_run + crest + downstream_run],
                [0, height, height, 0], alpha=0.2, color="#533483")
ax.set_aspect("equal")
ax.set_xlabel("Horizontal (m)"); ax.set_ylabel("Vertical (m)")
ax.set_title("Exercise 13: Tailings Dam Cross-Section")
ax.legend(); ax.grid(True); save(fig, "13_tailings_cross_section")

# 14: Closure water balance
print("[14] closure_water_balance.png")
fig, ax = plt.subplots(figsize=(8,5))
components = ["Rainfall", "Catchment Runoff", "Groundwater", "Evaporation"]
values = [312000, 234000, 306600, -576000]
colors = ["#16c79a", "#0f3460", "#533483", "#ff6b6b"]
bars = ax.barh(components, values, color=colors)
ax.axvline(0, color="#a0a0a0", lw=1)
ax.set_xlabel("Volume (m³/year)")
ax.set_title("Exercise 14: Pit Lake Water Balance")
for bar, val in zip(bars, values):
    ax.text(val + 10000 if val > 0 else val - 50000, bar.get_y() + bar.get_height()/2,
            f"{val:+,.0f}", va="center", color="#eaeaea")
ax.grid(True, axis="x"); save(fig, "14_closure_water_balance")

# 15: Feasibility cash flow
print("[15] feasibility_cash_flow.png")
fig, ax = plt.subplots(figsize=(10, 5))
years = [0, 1, 2, 3, 4, 5]
cash_flows = [-85, 18.5, 18.5, 18.5, 18.5, 9.2]
colors = ["#ff6b6b" if cf < 0 else "#16c79a" for cf in cash_flows]
ax.bar(years, cash_flows, color=colors, width=0.6)
ax.axhline(0, color="#a0a0a0", lw=1)
ax.set_xlabel("Year"); ax.set_ylabel("Cash Flow ($M)")
ax.set_title("Exercise 15: Pre-Feasibility Cash Flow ($1950/oz Au)")
for y, cf in zip(years, cash_flows):
    ax.text(y, cf + (1 if cf > 0 else -2), f"${cf:.1f}M", ha="center", color="#eaeaea", fontsize=9)
ax.grid(True, axis="y"); save(fig, "15_feasibility_cash_flow")

print("\n✅ All 15 figures generated in assets/figures/")
