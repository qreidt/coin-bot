import sys
import src.helpers.CoinHelper as CoinHelper

update_cmd = sys.argv[(sys.argv.index('update') + 1)]

if update_cmd == 'all':

	from src import Init

elif update_cmd == 'trending':

	CoinHelper.writeTrending()

elif update_cmd == 'best':

	pass

