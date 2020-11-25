import pandas as pd


# CALCULAR SMA
# MÉDIA MÓVEL SIMPLES - SIMPLE MOVING AVERAGE
def writeSMA(coin_history):

	coin_history['SMA10'] = coin_history['value'].rolling(window=10).mean()
	coin_history['SMA25'] = coin_history['value'].rolling(window=25).mean()
	coin_history['SMA50'] = coin_history['value'].rolling(window=50).mean()
	coin_history['SMA100'] = coin_history['value'].rolling(window=100).mean()
	coin_history['SMA200'] = coin_history['value'].rolling(window=200).mean()

	del coin_history['value']

	return coin_history
