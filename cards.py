import random

COLORS = ['♡', '♤', '♧', '♢']
VALUES = {
    '2' : 15,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    '10': 10,
    'V' : 11,
    'D' : 12,
    'R' : 13,
    'A' : 14
}
class Deck:
    """ Deck du jeu de société du Président. """
    __cards : list = []
    def __init__(self):
        """ Génération d'un deck de 52 cartes"""
        for (symbol, val) in VALUES.items():
            for color in COLORS:
                new_card = Card(symbol, val, color)
                self.__cards.append(new_card)

    def shuffle(self) -> None:
        """ Mélanger les cartes de mon deck. """
        random.shuffle(self.__cards)

    def __str__(self) -> str:
        return str(self.__cards)

class Card:
    __symbol : str
    __value : int
    __color: str

    def __init__(self, symbol: str, value: int, color:str):
        self.__symbol = symbol
        self.__value = value
        self.__color = color

    def __lt__(self, other):
        return self.__value < other.value

    def __gt__(self, other):
        return self.__value > other.value

    def __eq__(self, other):
        return self.__value == other.value

    def __ne__(self, other):
        return self.__value != other.value

    @property
    def value(self):
        return self.__value

    def __repr__(self):
        return f"{self.__symbol} {self.__color}"



