# European Train Routes Visualization

This is a simple Python project that visualizes train routes between major European cities using coordinates.  
It shows connections between cities on an interactive map.

## 🔍 What this project does

- Reads a `.csv` file with city names and coordinates
- Calculates real distances between cities using geopy
- Draws lines between cities on a map using folium
- Outputs a clickable HTML map

## 📁 Files included

- `main.py` → Python script that creates the map
- `train_routes.csv` → CSV file with city names and lat/lon
- `train_routes_map.html` → The output interactive map

## 🗺️ What the map shows

- Each city is marked with a pin
- Lines show direct train routes between cities
- You can zoom and click on cities for names

## 💡 What I learned

- How to work with geospatial data in Python
- How to calculate distances using `geopy`
- How to use `folium` to build a map

## 🔧 Tools/Libraries Used

- Python 3
- [pandas](https://pandas.pydata.org/)
- [folium](https://python-visualization.github.io/folium/)
- [geopy](https://geopy.readthedocs.io/)

---
