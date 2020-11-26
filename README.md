# Coin Bot

### Installation Instructions
0. Install conda on your computer
0. `$ conda create --name=coin-bot` to start a new virtual environment
0. `$ conda activate coin-bot` to load your new virtual environment
0. `$ conda env update -f packges.yaml` to load all project dependencies onto your virtual environment
0. `$ python main.py init` to start downloading information about all coins
0. `$ python main.py analize` to run analisis on all coins

#### Services in use:
- CoinGecko API

#### Main Packges in Use:
- Pandas
- pycoingecko