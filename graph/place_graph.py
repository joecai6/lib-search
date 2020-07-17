import geopandas as geopandas
import matplotlib.pyplot as plt

world = geopandas.read_file('./us_outline2.json')
places = geopandas.read_file('./place_table/records.csv')
places['geometry'] = geopandas.points_from_xy(places['Longitude'], places['Latitude'])

for i, row in world.iterrows():
    state = row['NAME']

    coord_row = places.loc[places['Name'] == state]
    count = coord_row['Count'].to_string(index=False)
    if(coord_row.empty or state == 'District of Columbia'):
        count = 0
    world.loc[i, 'size'] = count

world['size'] = world['size'].astype(int)

print(world.head())
#geopandas read file has all values as strings maybe use read pkl instead
places['Count'] = places['Count'].astype(int)

places.crs = world.crs

plt.rcParams["figure.figsize"] = (14,8)

base = world.plot(column='size', legend=True, cmap='GnBu', edgecolor='black')
#places.plot(ax=base, color=places['Color'], edgecolor='black', markersize=10, alpha=0.5, label='a');

plt.title('Total Number of Records Published by State')
plt.xlim(-125,-67)
plt.ylim(25,50)
plt.savefig('./graph_imgs/place_graph.png')

plt.show()