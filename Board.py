from Pawn import Pawn

"""
Classe qui représente un plateau de Reversi
"""


class Board:

	def __init__(self):
		def is_in_middle_square(x, y):
			return ((x == 3) and (y == 3)) or ((x == 4) and (y == 4)) or ((x == 4) and (y == 3)) or (
					(x == 3) and (y == 4))

		# True == White
		# False == Black
		def middle_square_color(x, y):
			return ((x == 3) and (y == 3)) or ((x == 4) and (y == 4))

		board = []
		for i in range(8):
			new_line = []
			board.append(new_line)
			for j in range(8):
				if not is_in_middle_square(i, j):
					new_line.append('_')
				else:
					new_line.append(Pawn(middle_square_color(i, j), i, j))

		self.board = board

	def show(self):
		for line in self.board:
			print(line)

	def __find_pawns_to_flip(self, x, y):

		begin_x = x
		begin_y = y
		init_color = self.board[x][y]

		def is_inside_board_bounds(x, y):
			return (8 > x >= 0) and (8 > y >= 0)

		pawns_to_flip = []
		for i in range(8):
			new_set_of_paws = []
			pawns_to_flip.append(new_set_of_paws)
			while self.board[x][y] != '_' and self.board[x][y] != init_color and is_inside_board_bounds(x, y):
				if i == 0:
					new_set_of_paws.append((x, y))
					x -= 1
				elif i == 1:
					new_set_of_paws.append((x, y))
					x -= 1
					y += 1
				elif i == 2:
					new_set_of_paws.append((x, y))
					y += 1
				elif i == 3:
					new_set_of_paws.append((x, y))
					x += 1
					y += 1
				elif i == 4:
					new_set_of_paws.append((x, y))
					x += 1
				elif i == 5:
					new_set_of_paws.append((x, y))
					x += 1
					y -= 1
				elif i == 6:
					new_set_of_paws.append((x, y))
					y -= 1


			x = begin_x
			y = begin_y

	def add(self, color, x, y):
		if not self.board[x][y] == '_':
			return False
		else:
			self.board[x][y] = Pawn(color, x, y)
			return True
