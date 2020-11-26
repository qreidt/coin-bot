import sys


def init():
    from src import Init


def analize():
    from src import Analize


def update():
    from src import Update


args = sys.argv

if 'init' in args:
    init()

if 'update' in args:
    update()

if 'analize' in args:
    analize()
