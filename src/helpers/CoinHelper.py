import pandas as pd
import moment, time, json
from env import DATA_PATH, BASE_CURRENCY, API_AWAIT_TIME, API_ERROR_AWAIT_TIME
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()


def writeTrending():
	try:

		trending = cg.get_search_trending()['coins']

		def getItem(item):
			item = item['item']

			if 'thumb' in item:
				del item['thumb']

			if 'large' in item:
				del item['large']

			if 'score' in item:
				del item['score']

			return item

		trending = list(map(getItem, trending))

		pd.DataFrame(trending).to_csv(DATA_PATH + 'trending.csv', sep=';', index=False)

		time.sleep(API_AWAIT_TIME)

	except Exception as e:
		time.sleep(API_ERROR_AWAIT_TIME)


def writeInfo(coin):

	try:

		info = cg.get_coin_by_id(coin['id'], localization='false', tickers='false', market_data='false', community_data='false', developer_data='false')

		del info['description']
		del info['links']

		with (open(coin['path'] + 'info.json', 'w+')) as outfile:
			json.dump(info, outfile, indent=2)

		time.sleep(API_AWAIT_TIME)

	except:
		print('error with ' + coin['name'] + ' | getInfo')
		time.sleep(API_ERROR_AWAIT_TIME)


def writeMarketHistory(coin):
	try:

		history = cg.get_coin_market_chart_by_id(coin['id'], BASE_CURRENCY, 'max')['prices']
		df = pd.DataFrame(history, columns=['date', 'value'])

		df.date = df.date.apply(lambda x: moment.unix(x).format('YYYY-M-D'))

		df.to_csv(coin['path'] + 'history.csv', sep=';', index=False)

		time.sleep(API_AWAIT_TIME)

	except:
		print('error with ' + coin['name'] + ' | getMarketHistory')
		time.sleep(API_ERROR_AWAIT_TIME)


def writeOHLC(coin):

	try:

		history = cg.get_coin_ohlc_by_id(coin['id'], BASE_CURRENCY, 'max')
		df = pd.DataFrame(history, columns=['date', 'open', 'high', 'low', 'close'])

		df.date = df.date.apply(lambda x: moment.unix(x).format('YYYY-M-D'))
		df.to_csv(coin['path'] + 'ohlc.csv', sep=';', index=False)

		time.sleep(API_AWAIT_TIME)

	except:
		print('error with ' + coin['name'] + ' | getOHLC')
		time.sleep(API_ERROR_AWAIT_TIME)