#!/usr/bin/env python

#
#   Author: Michael E Sanders
#
# Might need more information for a figure; however for now the following in the blocks below should be
# ample enough description to get started.

# A figure is a "model" or piece that a player has in reserve.
# Figures have a STR rating { Which usually equals what their cost is to play }
# FIgures have a Cost of rage to play: Leaders are Free, Warriors cost one and Ships cost two.
# Figures can have upgrades that allow them to do cool stuff
# Figures have a type associated with them: Leader, Warrior, Ship, or Monster, or monster
# Figures can be on land or in a fjord
from bloodrage.models.Config import FigureType, ClanTypes, TerrainType

class Figure:
    def __init__(self, type, str, cost, clan, terrain):
        self._type = type
        self._str = str
        self._cost = cost
        self._clan = clan
        self._terrain = terrain

    def __str__(self):
        return FigureType.toString(self._type) + " of the " + ClanTypes.toString(self._clan)\
               + " clan. STR = " + str(self._str) + " and COST = " + str(self._cost)

    def eventHandler(self):
        pass

    def getStr(self):
        return self._str

def FigureFactory(Figure):
    @staticmethod
    def getShip(clan):
        return Figure(FigureType.SHIP, 2, 2, clan, TerrainType.SEA)

    @staticmethod
    def getLeader(clan):
        return Figure(FigureType.LEADER, 3, 0, clan, TerrainType.LAND)

    @staticmethod
    def getWarrior(clan):
        return Figure(FigureType.WARRIOR, 1, 1, clan, TerrainType.LAND)

    ############################
    ##### 9 Monster Upgrades
    ############################
    @staticmethod
    def getDarkElf(clan):
        return Figure(FigureType.MONSTER, 1, 1, clan, TerrainType.LAND)

    @staticmethod
    def getSeaSerpent(clan):
        return Figure(FigureType.MONSTER, 3, 3, clan, TerrainType.SEA)

    @staticmethod
    def getFireGiant(clan):
        fireGiant = Figure(FigureType.MONSTER, 4, 4, clan, TerrainType.LAND)
        return fireGiant

    @staticmethod
    def getDwarfKing(clan):
        return Figure(FigureType.MONSTER, 2, 0, clan, TerrainType.LAND)

    @staticmethod
    def getTroll(clan):
        return Figure(FigureType.MONSTER, 2, 2, clan, TerrainType.LAND)