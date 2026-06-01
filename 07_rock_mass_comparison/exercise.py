"""
Exercise 7: Rock Mass Comparison — Granite vs. Shale

Problem:
Compare two rock masses for an underground mine development:

Granite:
- mi = 25, GSI = 65, D = 0.2, UCS = 140 MPa

Shale:
- mi = 8, GSI = 35, D = 0.5, UCS = 45 MPa

Tasks:
1. Calculate Hoek-Brown parameters for both
2. Convert to Mohr-Coulomb equivalents
3. Compare pillar strength and excavation span
4. Recommend support system for each
5. Estimate deformation modulus
"""
import sys
sys.path.insert(0, "../src")

from mining import rock_mechanics as rm

print("=" * 60)
print("EXERCISE 7: Rock Mass Comparison")
print("=" * 60)

rocks = {
    "Granite": {"mi": 25, "gsi": 65, "D": 0.2, "ucs": 140},
    "Shale": {"mi": 8, "gsi": 35, "D": 0.5, "ucs": 45}
}

for name, r in rocks.items():
    print(f"\n[{name}]")
    params = rm.hoek_brown_parameters(r["gsi"], r["mi"], r["D"], r["ucs"])
    mc = rm.mohr_coulomb_from_hoek_brown(params['mb'], params['s'], params['a'], r['ucs'], r['ucs']/4)
    
    print(f"  mb={params['mb']:.3f}, s={params['s']:.4f}, a={params['a']}")
    print(f"  E_rm={params['E_rm_MPa']:.0f} MPa")
    print(f"  c={mc['cohesion_MPa']:.2f} MPa, φ={mc['friction_angle_deg']:.1f}°")
    print(f"  σ_cm={params['sigma_cm_MPa']:.2f} MPa")
    print(f"  σ_t={mc['tensile_strength_MPa']:.2f} MPa")
    
    if params['E_rm_MPa'] > 20000:
        support = "Rock bolts + mesh (minimal)"
    elif params['E_rm_MPa'] > 10000:
        support = "Rock bolts + shotcrete + mesh"
    else:
        support = "Full support: bolts + shotcrete + steel sets"
    print(f"  Support: {support}")

print("\n" + "=" * 60)
print("Exercise 7 complete.")
print("=" * 60)
