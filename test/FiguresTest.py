#!/usr/bin/env python

#
#   Author: Michael E Sanders
#



from bloodrage.models import Figure, ClanTypes, TerrainType,FigureType

def testFigures():
    leader = Figure(FigureType.LEADER, 3, 0, ClanTypes.WOLF, TerrainType.LAND)
    assert(leader._type == FigureType.LEADER)
    assert(leader._str == 3)
    assert(leader._cost == 0)
    assert(leader._clan == ClanTypes.WOLF)
    assert(leader._terrain == TerrainType.LAND)

    print(leader)


testFigures()