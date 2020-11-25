import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
import moment, os, time, json
from pycoingecko import CoinGeckoAPI
from env import COINS_PATH, DATA_PATH


cg = CoinGeckoAPI()

coins = pd.read_csv(DATA_PATH + 'coins.csv', sep=';')

for index, coin in coins[coins['id'] == 'brz'].iterrows():

	history = pd.read_csv(coin['path'] + 'history.csv', sep=';', index_col='date')
	ohlc = pd.read_csv(coin['path'] + 'ohlc.csv', sep=';', index_col='date')

	join = history.join(ohlc)
	join = join[join['close'].notna()]

	x = pd.to_datetime(join.index.values)
	y = join['close'].values

	fig, ax = plt.subplots()
	fig.subplots_adjust(bottom=0.3)
	plt.xticks(rotation=90)

	plt.plot(x, y)

	plt.figure(figsize=(200, 150))

	plt.show()

	break

