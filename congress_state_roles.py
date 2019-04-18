# Cartopy Congress state roles goes here
import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader
import numpy as np
from pandas import read_csv
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


data = read_csv("ConsumerSpendingByState.csv")
data.columns = ['state', 'Latest_yearly_data']
sorted_by_amount = data.sort_values(by=['Latest_yearly_data'])
# print(sorted_by_amount.Latest_yearly_data)
#
# print(sorted_by_amount.head(50))

fig = plt.figure(figsize=(8, 8), dpi= 80, facecolor='w', edgecolor='k')
ax = fig.add_axes([0, 0, 1, 1], projection=ccrs.LambertConformal())
ax.set_extent([-160, -72, 20, 72], ccrs.Geodetic())
shapename = 'admin_1_states_provinces_lakes_shp'
states_shp = shpreader.natural_earth(resolution='110m', category='cultural', name=shapename)
ax.background_patch.set_visible(False)
ax.outline_patch.set_visible(False)
ax.set_title('Consumer Spending by State in USD, 2016')

for astate in shpreader.Reader(states_shp).records():

    employment_number = data[data['state'] == astate.attributes['name']].Latest_yearly_data.values
    # print(employment_number)
    try:
        employment_number = data[data['state'] == astate.attributes['name']].Latest_yearly_data.values
    except:
        employment_number = 0

    if employment_number >= 1000000:
        facecolor='#006d2c'
        label='More than 1 Million'
    elif employment_number >= 500000:
        facecolor='#2ca25f'
        label='500k - 1 Million'
    elif employment_number >= 100000:
        facecolor='#66c2a4'
        label='100k - 500k'
    elif employment_number >= 50000:
        facecolor='#99d8c9'
        label='50k - 100k'
    elif employment_number >= 0:
        facecolor='#ccece6'
        label='Less than 50k'
    else:
        facecolor='#edf8fb'
        label='Less than 10'

    ax.add_geometries([astate.geometry], ccrs.PlateCarree(), facecolor=facecolor, edgecolor='black',label=label)


patch1 = mpatches.Rectangle((0, 0), 1, 1, facecolor="#006d2c")
patch2 = mpatches.Rectangle((0, 0), 1, 1, facecolor="#2ca25f")
patch3 = mpatches.Rectangle((0, 0), 1, 1, facecolor="#66c2a4")
patch4 = mpatches.Rectangle((0, 0), 1, 1, facecolor="#b2e2e2")
patch5 = mpatches.Rectangle((0, 0), 1, 1, facecolor="#edf8fb")

labels = ['More than 1,000,000', '500,000 - 1,000,000', '100,000 - 500,000', '50,000 - 100,000', 'Less than 50,000']

plt.legend([patch1, patch2, patch3, patch4, patch5], labels,loc=1, fancybox=True, fontsize='x-large')
plt.show()