import pandas as pd
import moment, os, time, json
from env import COINS_PATH, BASE_CURRENCY, API_AWAIT_TIME, API_ERROR_AWAIT_TIME
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()


def getInfo(coin):

	try:

		info = cg.get_coin_by_id(coin['id'], localization='false', tickers='false', market_data='false', community_data='false', developer_data='false')

		del info['description']
		del info['links']

		with (open(coin['path'] + 'info.json', 'w+')) as outfile:
			json.dump(info, outfile, indent=2)

		time.sleep(API_AWAIT_TIME)

	except Exception as e:
		print(e)
		print('error with ' + coin['name'] + ' | getInfo')
		time.sleep(API_ERROR_AWAIT_TIME)


def getMarketHistory(coin):
	try:

		history = cg.get_coin_market_chart_by_id(coin['id'], BASE_CURRENCY, 'max')['prices']
		df = pd.DataFrame(history, columns=['date', 'value'])

		df.date = df.date.apply(lambda x: moment.unix(x).format('YYYY-M-D'))

		df.to_csv(coin['path'] + 'history.csv', sep=';', index=False)

		time.sleep(API_AWAIT_TIME)

	except:
		print('error with ' + coin['name'] + ' | getMarketHistory')
		time.sleep(API_ERROR_AWAIT_TIME)


def getOHLC(coin):

	try:

		history = cg.get_coin_ohlc_by_id(coin['id'], BASE_CURRENCY, 'max')
		df = pd.DataFrame(history, columns=['date', 'open', 'high', 'low', 'close'])

		df.date = df.date.apply(lambda x: moment.unix(x).format('YYYY-M-D'))
		df.to_csv(coin['path'] + 'ohlc.csv', sep=';', index=False)

		time.sleep(API_AWAIT_TIME)

	except:
		print('error with ' + coin['name'] + ' | getOHLC')
		time.sleep(API_ERROR_AWAIT_TIME)


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

		getInfo(coin)

	getMarketHistory(coin)
	getOHLC(coin)
	print(str(i+1) + '/' + str(len(coins)) + ' | ' + coin['name'])
