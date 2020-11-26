import pandas as pd


# CALCULAR SMA
# MÉDIA MÓVEL SIMPLES - SIMPLE MOVING AVERAGE
def writeSMA(coin_history):

	coin_history['SMA10'] = coin_history['value'].rolling(window=10).mean()
	coin_history['SMA25'] = coin_history['value'].rolling(window=25).mean()
	coin_history['SMA50'] = coin_history['value'].rolling(window=50).mean()
	coin_history['SMA100'] = coin_history['value'].rolling(window=100).mean()
	coin_history['SMA200'] = coin_history['value'].rolling(window=200).mean()

	return coin_history


# CALCULAR RSI
# ÍNDICE DE FORÇA RELATIVA - RELATIVE STRENGTH INDEX
def writeRSI(coin_history, algorithm='sma'):

	coin_history['U'] = coin_history['value'].diff()
	coin_history['U'] = coin_history['U'].mask(coin_history['U'].lt(0), 0)
	coin_history['D'] = -coin_history['value'].diff()
	coin_history['D'] = coin_history['D'].mask(coin_history['D'].lt(0), 0)

	N = 14

	# SMA14
	if algorithm == 'sma':
		coin_history['RSI-AVG-U'] = coin_history['U'].rolling(window=N).mean()
		coin_history['RSI-AVG-D'] = coin_history['D'].rolling(window=N).mean()
		coin_history['RSI-RS'] = coin_history['RSI-AVG-U'] / coin_history['RSI-AVG-D']

	# EMA (EXPONENTIAL MOVING AVERAGE)
	# EMA14 (Price(today) × a + EMA(yesterday) × (1 − a))
	elif algorithm == 'ema':
		a = 2 / (N + 1)
		coin_history['RSI-AVG-U'], coin_history['RSI-AVG-D'] = [0, 0]
		coin_history['RSI-AVG-U'] = coin_history['U'] * a + coin_history['RSI-AVG-U'].shift() * (1 - a)
		coin_history['RSI-AVG-D'] = coin_history['D'] * a + coin_history['RSI-AVG-D'].shift() * (1 - a)
		coin_history['RSI-RS'] = coin_history['RSI-AVG-U'].rolling(window=N).mean() / coin_history['RSI-AVG-D'].rolling(window=N).mean()

	# WSM14 (WILDER’S SMOOTHING METHOD)
	elif algorithm == 'wsm':
		coin_history['RSI-AVG-U'], coin_history['RSI-AVG-D'] = [0, 0]
		coin_history['RSI-AVG-U'] = coin_history['U'] * (1 / N) + coin_history['RSI-AVG-U'].shift() * ((N - 1) / N)
		coin_history['RSI-AVG-D'] = coin_history['D'] * (1 / N) + coin_history['RSI-AVG-D'].shift() * ((N - 1) / N)
		coin_history['RSI-RS'] = coin_history['RSI-AVG-U'].rolling(window=N).mean() / coin_history['RSI-AVG-D'].rolling(window=N).mean()

	coin_history['RSI'] = 100 - 100 / (1 + coin_history['RSI-RS'])

	return coin_history
