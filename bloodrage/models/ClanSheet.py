#!/usr/bin/env python

#
#   Author: Michael E Sanders
#
# In the physical game there is a Clan Sheet that keeps track of a players resources, stats and upgrades
#
# In the middle of the sheet it has the player's current rage, which defaults to 6
#
# The base stats are Rage, Axes, and Horns. Rage defaults to 6, Axes to 3 and Horns to 4
# Rage is the amount of points per age a player can spend on actions: 6, 7, 8, 9, 12, 12
# Axes are the amount of points for winning battles. 3, 4, 5, 6, 8, 8
# Horns are the number of figures that can be on a map. 4, 5, 6, 7, 10, 10
#
# The number of clan upgrades a character can have is 3 and monster upgrades is 2
#
# At the end of the game, players get an extra 10 glory if they are in 4th slot for any of the stats, and 20 glory for the 6th slot


''' TO DO: NEED TO FIGURE OUT HOW TO HANDLE UPGRADES, THEY SHOULD PROBABLY BE THEIR OWN CLASS WITH THEIR OWN ABILITIES.
    NEED TO LOOK AT ALL POSSIBLE UPGRADES. MONSTER UPGRADES SHOULD BE STRAIGHT FOWARD, BUT NEED TO CHECK
'''
class ClanSheet(object):
    RAGE_SLOTS = {1 : 6, 2 : 7, 3 : 8, 4 : 9, 5 : 12, 6 : 12}
    AXES_SLOTS = {1 : 3, 2 : 4, 3 : 5, 4 : 6, 5 : 8, 6 : 8}
    HORNS_SLOTS = {1 : 4, 2 : 5, 3 : 6, 4 : 7 , 5 : 10, 6 : 10}


    def __init__(self, clan):
        self._leader_upgrade =  None
        self._warrior_upgrade = None
        self._ship_upgrade = None
        self._clan_upgrade = []
        self._monster_upgrade = []
        self._clan = clan
        self._current_rage = 6
        self._current_rage_slot = 1
        self._current_axes_slot = 1
        self._current_horns_slot = 1


    def upgrade_rage(self):
        if self._current_rage_slot < 6:
            self._current_rage_slot += 1
            return True
        return False

    def upgrade_axes(self):
        if self._current_axes_slot < 6:
            self._current_axes_slot += 1
            return True
        return False

    def upgrade_horns(self):
        if self._current_horns_slot < 6:
            self._current_horns_slot += 1
            return True
        return False

    def getEndGlory(self):
        return  self._getEndGlory(self._current_horns_slot) \
                + self._getEndGlory(self._current_rage_slot) + self._getEndGlory(self._current_axes_slot)

    def _getEndGlory(self, slot):
        if slot == 4 or slot == 5:
            return 10
        elif slot == 6:
            return 20
        else:
            return 0


