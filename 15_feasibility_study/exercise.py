"""
Exercise 15: Pre-Feasibility Study — Cash Flow and NPV

Problem:
Evaluate a small-scale underground gold mine:
- Resource: 2.8 Mt @ 3.2 g/t Au
- Mining rate: 1800 tpd
- Recovery: 92%
- Gold price: $1950/oz
- Capex: $85M (development + plant)
- Opex: $85/t ore
- Mine life: 4.5 years
- Discount rate: 8%
- Royalty: 4%
- Tax: 30%

Tasks:
1. Calculate annual gold production and revenue
2. Build yearly cash flow
3. Calculate undiscounted and discounted NPV
4. Determine payback period
5. Assess sensitivity to gold price
"""
import sys
sys.path.insert(0, "../src")

print("=" * 60)
print("EXERCISE 15: Pre-Feasibility Study")
print("=" * 60)

resource_t = 2.8e6
grade_g_t = 3.2
rate_tpd = 1800
recovery = 0.92
gold_price_usd_oz = 1950
opex_per_t = 85
capex = 85e6
mine_life = 4.5
discount = 0.08
royalty = 0.04
tax = 0.30
tpd_to_tpy = 365 * 0.85  # 85% availability

annual_t = rate_tpd * tpd_to_tpy
oz_per_t = grade_g_t * recovery / 31.1035  # 31.1035 g per troy oz
annual_oz = annual_t * oz_per_t
annual_revenue = annual_oz * gold_price_usd_oz
annual_opex = annual_t * opex_per_t

print("\n[Task 1] Production Profile")
print(f"  Annual throughput: {annual_t/1e6:.2f} Mt/year")
print(f"  Grade:             {grade_g_t} g/t")
print(f"  Recovery:          {recovery*100:.0f}%")
print(f"  Annual gold:       {annual_oz/1e3:.1f} koz/year")
print(f"  Revenue:           ${annual_revenue/1e6:.1f}M/year")

print("\n[Task 2] Yearly Cash Flow")
years = [1, 2, 3, 4, 5]
remaining = resource_t
cumulative = -capex
npv = -capex
discounted_flows = []

for y in years:
    mined = min(annual_t, remaining)
    oz_y = mined * oz_per_t
    rev_y = oz_y * gold_price_usd_oz
    opex_y = mined * opex_per_t
    royalty_y = rev_y * royalty
    ebitda = rev_y - opex_y - royalty_y
    tax_y = max(0, ebitda * tax)
    cf = ebitda - tax_y
    
    cumulative += cf
    dcf = cf / ((1 + discount) ** y)
    npv += dcf
    discounted_flows.append(dcf)
    remaining -= mined
    
    print(f"  Year {y}: mined={mined/1e6:.2f}Mt, rev=${rev_y/1e6:.1f}M, opex=${opex_y/1e6:.1f}M, CF=${cf/1e6:.1f}M, DCF=${dcf/1e6:.1f}M")

print(f"\n[Task 3] NPV")
print(f"  Undiscounted cumulative: ${cumulative/1e6:.1f}M")
print(f"  NPV @ {discount*100:.0f}%:          ${npv/1e6:.1f}M")

print("\n[Task 4] Payback Period")
# Simple interpolation
payback = capex / (annual_revenue - annual_opex - annual_revenue*royalty - max(0,(annual_revenue-annual_opex-annual_revenue*royalty)*tax))
print(f"  Approx payback: {payback:.1f} years")

print("\n[Task 5] Sensitivity to Gold Price")
for price in [1500, 1750, 1950, 2200, 2500]:
    rev = annual_oz * price
    ebitda = rev - annual_opex - rev*royalty
    tax_y = max(0, ebitda * tax)
    cf = ebitda - tax_y
    npv_s = -capex + sum(cf / ((1+discount)**y) for y in years)
    print(f"  ${price}/oz → annual CF=${cf/1e6:.1f}M → NPV=${npv_s/1e6:.1f}M")

print("\n" + "=" * 60)
print("Exercise 15 complete.")
print("=" * 60)
