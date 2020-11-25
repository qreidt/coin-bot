import pandas as pd
import os, time
import src.controllers.CoinController as CoinController
from env import COINS_PATH, API_AWAIT_TIME
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()


coins = pd.DataFrame(cg.get_coins_list())
coins['path'] = coins['id'].map(lambda x: COINS_PATH + x + '/')
coins.to_csv('./data/coins.csv', sep=';', index=False)

time.sleep(API_AWAIT_TIME)

if not os.path.exists(COINS_PATH):
	os.mkdir(COINS_PATH)

for i, coin in coins.iterrows():

	already_exists = os.path.exists(coin['path'])

	if not already_exists:
		os.mkdir(coin['path'])

		CoinController.writeInfo(coin)

	CoinController.writeMarketHistory(coin)
	CoinController.writeOHLC(coin)
	print(str(i+1) + '/' + str(len(coins)) + ' | ' + coin['name'])
