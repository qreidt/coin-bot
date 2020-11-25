import sys
import src.controllers.CoinController as CoinHelper

update_cmd = sys.argv[(sys.argv.index('update') + 1)]

if update_cmd == 'all':

	pass

elif update_cmd == 'trending':

	CoinHelper.writeTrending()

elif update_cmd == 'best':

	pass

