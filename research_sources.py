"""
Research script: Mining Engineering x IAPWS Thermodynamics

Searches multiple open-access sources to determine which IAPWS
formulations and pygeotoolbox modules are applicable to mining
engineering problems.

Sources:
- NCBI/NIH papers on mine ventilation, heat stress
- arXiv mining engineering papers
- USGS reports on mineral extraction from brine
- ResearchGate public documents
- Academic PDFs via Google Scholar redirects
"""

import subprocess, json, os, time, textwrap

outdir = "/mnt/e/vibeco/hermes-mining-engineering/research"
os.makedirs(outdir, exist_ok=True)

# Sources to check (open-access APIs and known data pages)
sources = [
    {
        "name": "NCBI_mine_ventilation",
        "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8671234/",
        "note": "Mine ventilation and heat stress — PMC article"
    },
    {
        "name": "USGS_geothermal_brine_lithium",
        "url": "https://pubs.usgs.gov/publication/70170478",
        "note": "USGS: Lithium from geothermal brine"
    },
    {
        "name": "arXiv_mine_thermo",
        "url": "https://arxiv.org/search/?query=mine+ventilation+heat&searchtype=all",
        "note": "arxiv mining thermodynamics abstracts"
    },
    {
        "name": "DOE_mine_water_energy",
        "url": "https://www.energy.gov/eere/geothermal/articles/future-geothermal-could-include-former-mines",
        "note": "DOE: abandoned mine water to geothermal"
    },
    {
        "name": "Wikipedia_mine_dewatering",
        "url": "https://en.wikipedia.org/wiki/Mine_dewatering",
        "note": "Mine dewatering overview"
    },
    {
        "name": "IAPWS_release_list",
        "url": "https://iapws.org/documents/release",
        "note": "IAPWS documents listing (already downloaded)"
    },
    {
        "name": "Wikipedia_critical_minerals",
        "url": "https://en.wikipedia.org/wiki/Critical_mineral#Extraction_from_brines",
        "note": "Critical minerals from brines"
    },
    {
        "name": "USGS_tailings_water",
        "url": "https://www.usgs.gov/centers/national-minerals-information-center/tailings-dams-and-water-balance",
        "note": "Tailings dams and water balance"
    },
]

headers = "-H 'Accept: text/html,application/xhtml+xml' -H 'User-Agent: Mozilla/5.0 (compatible; AcademicBot/1.0)'"

def fetch(url, outname):
    cmd = f"curl -sL --max-time 20 {headers} '{url}' -o {outname} 2>/dev/null"
    subprocess.run(cmd, shell=True, timeout=30)
    sz = os.path.getsize(outname) if os.path.exists(outname) else 0
    return sz

results = {}
for src in sources:
    path = os.path.join(outdir, src["name"] + ".html")
    sz = fetch(src["url"], path)
    results[src["name"]] = {"size": sz, "path": path, "note": src["note"]}
    time.sleep(0.5)

# Summary
print("="*60)
print("Mining Engineering Research Sources")
print("="*60)
for name, info in results.items():
    print(f"{name:30s} {info['size']:>8d} bytes  ({info['note']})")

# Save summary as JSON
summary_path = os.path.join(outdir, "_research_summary.json")
with open(summary_path, "w") as f:
    json.dump(results, f, indent=2)
print(f"\nSummary saved to: {summary_path}")
