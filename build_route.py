import csv
import json
from pathlib import Path

DATA = Path(__file__).parent / "data"

with open(DATA / "points.csv", newline="", encoding="utf-8") as f:
    rows = sorted(csv.DictReader(f), key=lambda r: int(r["order"]))

features = []

# One point feature per stop
for r in rows:
    features.append({
        "type": "Feature",
        "geometry": {"type": "Point", "coordinates": [float(r["lon"]), float(r["lat"])]},
        "properties": {
            "order": int(r["order"]),
            "name": r["name"],
            "type": r["type"],
            "description": r["description"],
            "image": r["image"] or None,
        },
    })

# A line connecting the stops in order (the Marswalk route)
features.append({
    "type": "Feature",
    "geometry": {
        "type": "LineString",
        "coordinates": [[float(r["lon"]), float(r["lat"])] for r in rows],
    },
    "properties": {"name": "Marswalk route"},
})

out = DATA / "route.geojson"
out.write_text(json.dumps({"type": "FeatureCollection", "features": features}, indent=2))
print(f"Wrote {out} with {len(rows)} stops")
