"""
Classe qui représente un pion de Reversi
"""


class Pawn:

    # True == White
    # False == Black
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y

    def flip(self):
        self.color = not self.color

    def __str__(self):
        return str(self.color)

    def __repr__(self):
        return str(self.color)
