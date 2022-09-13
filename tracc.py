import gpxpy 
import gpxpy.gpx 
import folium


gpx_file = open('20220909.gpx', 'r') 
lat_pts=[]
lon_pts=[]
ele=[]

#fieldnames=["Latitude", "Longitude", "Elevation"]
MapLoc=folium.Map(location=[12.993213333333332, 79.98719166666666], zoom_start=9)
folium.TileLayer('Stamen Terrain').add_to(MapLoc)
folium.TileLayer('Stamen Toner').add_to(MapLoc)
folium.TileLayer('Stamen Water Color').add_to(MapLoc)
folium.TileLayer('cartodbpositron').add_to(MapLoc)
folium.TileLayer('cartodbdark_matter').add_to(MapLoc)
folium.LayerControl().add_to(MapLoc)

gpx = gpxpy.parse(gpx_file) 
for track in gpx.tracks: 
    for segment in track.segments: 
        for point in segment.points: 
            lat_pts.append(point.latitude)
            lon_pts.append(point.longitude)
            ele.append(point.elevation)
            folium.Marker([point.latitude, point.longitude]).add_to(MapLoc)
MapLoc.save("myloc.html")
