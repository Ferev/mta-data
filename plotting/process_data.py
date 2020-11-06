import os
import json
from datetime import datetime
import pytz
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib.ticker import FuncFormatter
import matplotlib.ticker as plticker
import matplotlib.patheffects as pe

station_mappings = {}
formatter = FuncFormatter(lambda x_val, tick_pos: datetime.fromtimestamp(x_val).astimezone(pytz.timezone('US/Eastern')).strftime("%Y-%m-%d %H:%M:%S"))


with open('stations.json') as fp:
    a = json.load(fp)
    for x in a['result']:
        station_mappings[x['id']] = x['name']

def read_file(filename):
    with open(filename) as fp:
        for line in fp:
            yield json.loads(line)


stops = {}
raw = []


for x in read_file('../data/A_C_E.json'):
    if 'entity' in x:
        data = x['entity']
        for element in data:
            id = element['id']
            if 'vehicle' in element and 'currentStatus' in element['vehicle']:
                if element['vehicle']['currentStatus'] == 'STOPPED_AT':
                    time = datetime.fromtimestamp(int(element['vehicle']['timestamp']))
                    if element['vehicle']['stopId'] not in stops:
                        stops[element['vehicle']['stopId']] = []
                    stops[element['vehicle']['stopId']].append(time)
                    raw.append((float(element['vehicle']['timestamp']), element['vehicle']['stopId']))


df = pd.DataFrame(raw, columns=['arrival_time', 'stop']).drop_duplicates()


stations_to_plot = ['115S','116S','117S','118S','119S','120S','121S','122S','123S','124S','125S','126S','127S','128S']
# stations_to_plot = ['115S','116S','117S','118S']
df = df[df['stop'].isin(stations_to_plot)]
def rename(x):
    if x in station_mappings:
        return station_mappings[x]
    else:
        return "Unknown"
df['stop'] = df['stop'].apply(rename)

pal = sns.cubehelix_palette(10, rot=-.25, light=.7) # color
g = sns.FacetGrid(df, row="stop", hue="stop", aspect=15, height=.5, palette=pal) # creates lines
g.map(sns.kdeplot, "arrival_time", clip_on=False, shade=True, alpha=1, lw=1.5, bw=.2)
g.map(sns.kdeplot, "arrival_time", clip_on=False, color="w", lw=2, bw=.2)
g.map(plt.axhline, y=0, lw=2, clip_on=False)



# Define and use a simple function to label the plot in axes coordinates
def label(x, color, label):
    ax = plt.gca()
    loc = plticker.MultipleLocator(base=10000.0) # this locator puts ticks at regular intervals
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_major_formatter(formatter)
    ax.text(0, .2, label, fontweight="bold", color=color,
            ha="left", va="center", transform=ax.transAxes, path_effects=[pe.withStroke(linewidth=2, foreground='w')])


g.map(label, "arrival_time")

# Set the subplots to overlap (i think overlap breaks it so I set hspace > 0?)
g.fig.subplots_adjust(hspace=0.35)

# Remove axes details that don't play well with overlap
g.set_titles("")
g.set(yticks=[])
g.despine(bottom=True, left=True)
g.fig.suptitle("Train Frequency")
plt.show()
