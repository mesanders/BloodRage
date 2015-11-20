# A figure is a "model" or piece that a player has in reserve.
# Figures have a STR rating { Which usually equals what their cost is to play }
# FIgures have a Cost of rage to play: Leaders are Free, Warriors cost one and Ships cost two.
# Figures can have upgrades that allow them to do cool stuff
# Figures have a type associated with them: Leader, Warrior, Ship, or Monster, or monster
# Figures can be on land or in a fjord
from bloodrage.models.Config import FigureType, ClanTypes

class Figure:
    def __init__(self, type, str, cost, clan, terrain):
        assert(type > 0 and type < 6)
        assert(terrain == 1 or terrain == 2)
        assert(clan > 0 and clan < 5)
        self._type = type
        self._str = str
        self._cost = cost
        self._clan = clan
        self._terrain = terrain

    def __str__(self):
        return FigureType.toString(self._type) + " of the " + ClanTypes.toString(self._clan)\
               + " clan. STR = " + str(self._str) + " and COST = " + str(self._cost)