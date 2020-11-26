import pandas as pd
from pycoingecko import CoinGeckoAPI
import src.controllers.IndicatorController as ic
from env import DATA_PATH


cg = CoinGeckoAPI()

coins = pd.read_csv(DATA_PATH + 'coins.csv', sep=';')

# for index, coin in coins[coins['id'] == 'brz'].iterrows():
for index, coin in coins.iterrows():

	print(str(index + 1) + '/' + str(len(coins)) + ' | ' + coin['name'])

	history = pd.read_csv(coin['path'] + 'history.csv', sep=';')

	ic.writeSMA(history).to_csv(coin['path'] + 'sma.csv', sep=';', index=False)
	ic.writeRSI(history).to_csv(coin['path'] + 'rsi.csv', sep=';', index=False)

