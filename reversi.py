from os import system
from Board import *

my_board = Board()
my_board.show()
system('clear')
if my_board.add(True, 5, 3):
    my_board.show()
else:
    print('no')
