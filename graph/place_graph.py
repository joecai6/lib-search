import geopandas as geopandas
import matplotlib.pyplot as plt

world = geopandas.read_file('./us_outline2.json')
cities = geopandas.read_file('./points.csv')
cities['geometry'] = geopandas.points_from_xy(cities.Longitude, cities.Latitude)

cities.crs = world.crs

print(cities.head())

plt.rcParams["figure.figsize"] = (16,9)

base = world.plot()
cities.plot(ax=base, color='red', markersize=1);


plt.xlim(-125,-67)
plt.ylim(25,50)
plt.savefig('./graph_imgs/place_graph.png')

plt.show()