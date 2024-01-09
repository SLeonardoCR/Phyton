import folium
import pandas

map = folium.Map(location=[38.73166457366876, -101.17628504707336], zoom_start=5, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="Volcanoes")
fg2 = folium.FeatureGroup(name="Population")
volcanoes = pandas.read_csv("Volcanoes.txt")
latitude = list(volcanoes["LAT"])
longitude = list(volcanoes["LON"])
elevation = list(volcanoes["ELEV"])

def mark(elevation):
    if elevation < 1000:
        return "green"
    elif elevation < 2000:
        return "darkgreen"
    elif elevation < 3000:
        return "orange"
    else:
        return "red"

fg2.add_child(folium.GeoJson(data=(open("world.json", "r", encoding="utf-8-sig").read()),
style_function=lambda x: {"fillColor":"green" if x["properties"]["POP2005"] < 10000000 else "orange" if x["properties"]["POP2005"] < 20000000 else "red"}))

for lat, lon, elev in zip(latitude, longitude, elevation):
    fg.add_child(folium.CircleMarker(location=[lat, lon], radius = 6, popup=str(elev) + " m", icon=folium.Icon(color=mark(elev)),
    fill_color=mark(elev), color = "grey", fill_opacity=0.7))


map.add_child(fg2)
map.add_child(fg)

map.add_child(folium.LayerControl())

map.save("Map1.html")