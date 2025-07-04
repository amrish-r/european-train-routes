import pandas as pd
import folium
from geopy.distance import geodesic

# Loading the city data
cities = pd.read_csv("city_coords.csv")
routes = pd.read_csv("routes.csv")

# Creating a base map
m = folium.Map(location=[50, 10], zoom_start=4)

# Adding city markers
for _, row in cities.iterrows():
    folium.Marker([row.lat, row.lon], popup=row.city).add_to(m)

# Drawing routes and calculating distance
for _, route in routes.iterrows():
    city1 = cities[cities.city == route['from']].iloc[0]
    city2 = cities[cities.city == route['to']].iloc[0]
    coords = [(city1.lat, city1.lon), (city2.lat, city2.lon)]
    
    distance_km = geodesic(coords[0], coords[1]).km
    est_time_hr = distance_km / 150  # Assuming avg speed = 150 km/h
    
    line = folium.PolyLine(locations=coords, color='blue')
    line.add_to(m)

    folium.Popup(f"{route['from']} → {route['to']}: {distance_km:.1f} km, {est_time_hr:.1f} h").add_to(line)

# Saving the map
m.save("train_routes_map.html")
print("Map saved as train_routes_map.html")
