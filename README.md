# Martian Map

A focused route planner for a Marswalk in Jezero Crater, built for the NASA Space Apps Challenge 2026 ("Interplanetary Survival Guide: Martian Map").

**Live site:** https://m000n-o00o.github.io/martian-map/

## What it does
Brings NASA data about Jezero together for one route. The astronaut sees the path, slopes and troughs, can toggle layers (high-resolution imagery, geology, structures), and reads why each stop matters: a science target or a hazard. An elevation profile shows where the walk gets steep.

## Route
1. Perseverance Landing Ellipse (start)
2. Delta Front Climb (hazard: ~53 m climb at the delta front)
3. Western Delta Deposit (science)
4. Western Breach (science)

Each leg was measured in Mars Trek and checked against NASA EVA range limits.

## Project structure
- `index.html`: the map page (Leaflet, Chart.js)
- `data/geology.geojson`, `data/structures.geojson`: USGS geology clipped to Jezero
- `data/points.csv`: route stops (edit this file to change stops)
- `data/route.geojson`: generated from `points.csv`
- `data/elevation_*.csv`: MOLA elevation profiles exported from Mars Trek
- `build_route.py`: builds `route.geojson` from `points.csv`
- `images/`: stop images

## Update the route
python3 build_route.py

## Data sources
- NASA Mars Trek: Viking MDIM 2.1 mosaic, Jezero Visible Mosaic (HiRISE, CTX, HRSC), points of interest, distance and elevation tools
- MGS MOLA Global DEM
- USGS Geologic Map of Mars (SIM 3292)
- Mars 2020 Perseverance raw images (NASA/JPL-Caltech)
- NASA Lunar Surface EVA Concept of Operations
- HRSC on ESA Mars Express (ESA/DLR/FU Berlin)

## Team
- Sarah Al-Ghamdi: Data Science (data processing, route data, repository)
- Rahma Alsharif: Human-Computer Interaction (design, content, presentation)
- Reham Wan Deraman: Computer Science (map development)
- Maab Abdelrahim: Computer & Network Engineering (images, references, testing)

## AI assistance
Claude (Anthropic) assisted with data-processing scripts, parts of the map code, and phrasing. AI-assisted files are marked with a comment. Route decisions and the project idea were made by the team.
