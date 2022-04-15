import numpy as np
import math
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# データの取得
world = gpd.datasets.get_path('naturalearth_lowres')      #世界地図
cities = gpd.datasets.get_path('naturalearth_cities')         #都市

# データの読み込み
df_world = gpd.read_file(world)
df_cities = gpd.read_file(cities)

# data表示
df_world.head()

# ■データのプロット
# 公式ドキュメントによるとdataflameに対して.plot()を使用することで、matplotlibが走るようです。

base = df_world.plot(color='white', edgecolor='black')
df_cities.plot(ax=base, marker='o', color='red', markersize=5)
plt.savefig('test001.png')
