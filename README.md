# Hermes for Mining Engineering

Hermes Agent course for **mining engineering**, adapted from the `hermes-reservoir-engineering` workflow framework. Every exercise maps the same AI-assisted guardrail (explore-plan-code-verify-review) to real mining workflows: rock mass characterization, slope stability, ventilation design, slurry transport, dewatering, blasting vibration control, tailings dam stability, and pre-feasibility economics.

The goal: teach mining engineers to direct AI like a disciplined technical assistant — context, constraints, units in SI, verification with tests, proven empirical libraries over hand-rolled formulas.

## Why This Course Exists

Mining engineering has its own set of high-consequence small details:

- **Rock mechanics**: intact rock vs rock mass strength, Hoek-Brown, RMR, GSI
- **Slope stability**: Bishop simplified, pore pressure, bench/inter-ramp/overall angles
- **Ventilation**: psychrometrics, heat stress (WBGT), fan power, airflow sizing
- **Slurry transport**: Bingham plastic rheology, pipeline pressure drop
- **Dewatering**: NPSH, pump power, groundwater inflow (Theim)
- **Blasting**: USBM PPV scaling, air overpressure, regulatory compliance
- **Tailings**: dam stability, pseudo-static seismic, breach consequence
- **Economics**: NPV, payback, sensitivity to commodity price

AI tools accelerate this work only when engineers demand domain context, SI units, known-value checks, and physical-bounds verification. This course teaches that workflow concretely.

## What You Will Learn

By the end:

- use Hermes explore-plan-code-verify on mining scripts
- write prompts with file, function, SI units, and expected stress-strain relationship
- ask Hermes for tests: known Hoek-Brown values, monotonicity, physical bounds
- create `CLAUDE.md` / `AGENTS.md` with mining standards
- package repeatable workflows as Hermes skills
- use parallel fanout for sensitivity studies (gold price, slope angle, powder factor)

## Course Structure (15 Exercises)

Each exercise is a numbered folder with:
- `README.md` — learning objective, before/after prompt, engineering context
- `exercise.py` — starter code with TODO markers
- `test_exercise.py` — pytest suite (TDD: test first, then code)

| # | Exercise | Engineering Focus | AI Skill |
|---|----------|-------------------|----------|
| 1 | Rock Mass + Slope Stability | RQD, RMR, GSI, Hoek-Brown, Bishop FOS | explore codebase before editing |
| 2 | Ventilation + Heat Stress | Psychrometrics, WBGT, fan power, work/rest | specific context (file, function, test) |
| 3 | Slurry + Dewatering | Bingham plastic, pipeline ΔP, NPSH, pump power | verify with tests before trusting |
| 4 | Blast + Vibration | USBM PPV, blast design, regulatory compliance | CLAUDE.md standards |
| 5 | Integrated Mine Design | ALL 6 modules combined | multi-module workflow |
| 6 | Groundwater Inflow | Theim equation, drawdown, cost | subagent review for risky calculations |
| 7 | Rock Mass Comparison | Granite vs shale, support selection | CLI workflow for data inspection |
| 8 | Pump Selection | System curve, operating point, VSD savings | MCP tool integration |
| 9 | Slope + Groundwater | FOS vs pore pressure, sensitivity | parallel fanout for parameter sweeps |
| 10 | Bench Domains | Inter-ramp vs overall slope, 3 domains | project memory (save conventions) |
| 11 | Blast Fragmentation | Powder factor, digging rate, cost-benefit | skills packaging |
| 12 | Subsidence | UK NCB empirical, angle of draw, monitoring | review subagent for empirical methods |
| 13 | Tailings Dam | Bishop FOS, pseudo-static seismic, ANCOLD | consequence category assessment |
| 14 | Mine Closure | Water balance, pit lake, reclamation cost | lifecycle economics |
| 15 | Feasibility Study | NPV, payback, gold price sensitivity | Monte Carlo + tornado charts |

## Quick Start

```bash
# Install
pip install pytest matplotlib

# Run a single exercise
cd 01_rock_mass_slope
PYTHONPATH=../src python3 exercise.py

# Run tests for that exercise
PYTHONPATH=../src pytest tests/test_rock_mechanics.py -v

# Run ALL tests
PYTHONPATH=src pytest tests/ -v

# Generate all course figures
python3 scripts/generate_course_figures.py
```

## Hermes Agent Usage

```text
/hermes -w                        # isolated worktree
/skill mining-engineering         # load mining skill
/init                             # reload CLAUDE.md
```

## Agentic AI Workflow

Each exercise follows the same guardrail:

```
Explore → Plan → Code → Verify → Review
```

1. **Explore**: Hermes reads code, data, and tests before editing
2. **Plan**: Hermes writes a brief plan before modifying code
3. **Code**: Implement with tests first (TDD)
4. **Verify**: Run tests and check physical plausibility
5. **Review**: Send risky code to subagent reviewer (AGENTS.md)

## Standards Documented

- `CLAUDE.md` — Mining engineering standards: units, Hoek-Brown, Bishop, USBM, ASHRAE, SME
- `AGENTS.md` — Reviewer checklist: unit consistency, FOS thresholds, PPV limits, physical bounds
- `BEGINNERS_GUIDE.txt` — Panduan awam dalam Bahasa Indonesia

## Illustrated Outputs

Every exercise produces both **console output** (engineering calculations) and a **matplotlib figure** (dark-themed). Run all figures with:

```bash
pip install matplotlib
python3 scripts/generate_course_figures.py
```

### Exercise 1: Rock Mass Characterization + Slope Stability
![01_rock_mass_gsi_strength.png](assets/figures/01_rock_mass_gsi_strength.png)
*Rock mass strength σ_cm vs GSI for mi=15, 25, 35. Higher mi → stronger rock at same GSI.*

### Exercise 2: Ventilation + Heat Stress
![02_ventilation_psychrometric.png](assets/figures/02_ventilation_psychrometric.png)
*Enthalpy vs dry-bulb temperature at RH=40, 60, 80, 95%. Heat stress zone at high T+RH.*

### Exercise 3: Slurry + Dewatering
![03_slurry_density_concentration.png](assets/figures/03_slurry_density_concentration.png)
*Slurry density vs solids concentration for copper, iron, and gold ore.*

### Exercise 4: Blast + Vibration Control
![04_blast_vibration_distance.png](assets/figures/04_blast_vibration_distance.png)
*PPV decay with distance for 25, 80, 200 kg/delay. Regulatory limits shown.*

### Exercise 5: Integrated Mine Design
![05_integrated_dashboard.png](assets/figures/05_integrated_dashboard.png)
*6-panel dashboard: rock modulus, psychrometrics, slurry viscosity, NPSH, slope FOS, blast PPV.*

### Exercise 6: Groundwater Inflow
![06_groundwater_inflow_drawdown.png](assets/figures/06_groundwater_inflow_drawdown.png)
*Steady-state inflow vs drawdown (Theim equation) for varying hydraulic conductivity.*

### Exercise 7: Rock Mass Comparison
![07_rock_comparison_bar.png](assets/figures/07_rock_comparison_bar.png)
*Granite vs shale: modulus, cohesion, friction angle, and rock mass strength side by side.*

### Exercise 8: Pump Selection
![08_pump_system_curve.png](assets/figures/08_pump_system_curve.png)
*System curve (static + friction) vs pump curve. Operating point at intersection.*

### Exercise 9: Slope Stability with Groundwater
![09_slope_fos_ru.png](assets/figures/09_slope_fos_ru.png)
*Factor of safety vs pore pressure ratio ru. Red zone = FOS < 1.0 (FAIL).*

### Exercise 10: Bench Design
![10_bench_cross_section.png](assets/figures/10_bench_cross_section.png)
*Bench geometry: face angle, berm, catch bench, inter-ramp, and overall slope.*

### Exercise 11: Blast Fragmentation
![11_blast_fragmentation_curve.png](assets/figures/11_blast_fragmentation_curve.png)
*Fragmentation distribution: current vs improved powder factor. Target d80 = 0.45 m.*

### Exercise 12: Subsidence
![12_subsidence_profile.png](assets/figures/12_subsidence_profile.png)
*Gaussian subsidence profile over longwall panel. Building damage threshold at 50 mm.*

### Exercise 13: Tailings Dam
![13_tailings_cross_section.png](assets/figures/13_tailings_cross_section.png)
*Tailings dam cross-section: upstream 3H:1V, downstream 2.5H:1V, crest width 8 m.*

### Exercise 14: Mine Closure
![14_closure_water_balance.png](assets/figures/14_closure_water_balance.png)
*Pit lake water balance: rainfall + runoff + groundwater – evaporation.*

### Exercise 15: Feasibility Study
![15_feasibility_cash_flow.png](assets/figures/15_feasibility_cash_flow.png)
*Annual cash flow for pre-feasibility gold mine. NPV positive at $1950/oz.*

## Modules (Library)

Core library in `src/mining/`:

- `rock_mechanics.py` — Hoek-Brown, RMR, GSI, Mohr-Coulomb
- `ventilation.py` — ASHRAE psychrometrics, WBGT heat stress
- `slurry.py` — Bingham plastic, settling velocity
- `dewatering.py` — NPSH, pump power, groundwater inflow
- `slope_stability.py` — Bishop FOS, bench design
- `blasting.py` — USBM PPV, overpressure, blast design

All modules use **stdlib Python only** — zero external dependencies.

## Tests

36 tests, all pass:

```bash
PYTHONPATH=src pytest tests/ -v
```

| Test file | Coverage |
|-----------|----------|
| `test_rock_mechanics.py` | RQD, Hoek-Brown, Mohr-Coulomb, GSI |
| `test_ventilation.py` | Psychrometrics, friction, fan power, heat stress |
| `test_slurry.py` | Density, Bingham viscosity, pressure drop, settling |
| `test_dewatering.py` | NPSH, pump power, inflow |
| `test_slope_stability.py` | Bishop FOS, bench design, inter-ramp/overall |
| `test_blasting.py` | PPV, overpressure, blast design, regulatory limits |

## Companion Toolbox

[`miningtoolbox-mcp`](https://github.com/zakusworo/miningtoolbox-mcp) — 24 MCP tools for Hermes Agent, same 6 modules, zero external dependencies.

## License

MIT License — Copyright 2026 Zulfikar Aji Kusworo
