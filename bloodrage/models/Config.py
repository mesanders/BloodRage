#!/usr/bin/env python

#
#   Author: Michael E Sanders
#
# The following three classes are essentially ENUMs with toString methods.
# FigureType is the Type of Figure it is, this might be useful for upgrades.
# As the time of this writing not sure how the Upgrades will be applied, because
# The player can have a Leader upgrade. Not sure which entity should handle the upgrade at this point
# But I want to at least have a trail of my thought process. Cheers!

class FigureType:
    LEADER = 1
    SHIP = 2
    WARRIOR = 3
    MONSTER = 4
    MYSTIC = 5

    _figureMap = { 1 : "LEADER", 2 : "SHIP", 3: "WARRIOR", 4: "MONSTER", 5: "MYSTIC"}

    @staticmethod
    def toString(figureType):
        return str(FigureType._figureMap[figureType])

class TerrainType:
    LAND = 1
    SEA = 2

    _terrainMap = {1: "LAND", 2: "SEA" }

    @staticmethod
    def toString(terrainType):
        return str(TerrainType._terrainMap[terrainType])

class ClanTypes:
    WOLF = 1
    BEAR = 2
    SERPENT = 3
    RAVEN = 4

    _clanmap = {1: "WOLF", 2: "BEAR", 3: "SERPENT", 4: "RAVEN"}

    @staticmethod
    def toString(clanType):
        return str(ClanTypes._clanmap[clanType])