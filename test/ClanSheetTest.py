#!/usr/bin/env python

### Test to make sure the various actions within the Clansheet function properly.
# Test End glory computation and the upgrade stats

from bloodrage.models.ClanSheet import ClanSheet
from bloodrage.models.Config import ClanTypes

def testEndGlory():
    wolfClan = ClanSheet(ClanTypes.WOLF)
    assert(wolfClan.getEndGlory() == 0)
    wolfClan.upgrade_axes()
    wolfClan.upgrade_axes()
    wolfClan.upgrade_axes()
    wolfClan.upgrade_axes()
    assert(wolfClan.getEndGlory() == 10)
    wolfClan.upgrade_axes()
    assert(wolfClan.getEndGlory() == 20)


    wolfClan.upgrade_horns()
    wolfClan.upgrade_horns()
    wolfClan.upgrade_horns()
    assert (wolfClan.getEndGlory() == 30)

def testUpgradeStats():
    wolfClan = ClanSheet(ClanTypes.WOLF)
    assert(wolfClan._current_axes_slot == 1)
    assert(wolfClan._current_rage_slot== 1)
    assert(wolfClan._current_horns_slot == 1)
    wolfClan.upgrade_horns()
    wolfClan.upgrade_horns()
    wolfClan.upgrade_rage()
    wolfClan.upgrade_rage()
    wolfClan.upgrade_rage()
    wolfClan.upgrade_rage()
    wolfClan.upgrade_rage()
    wolfClan.upgrade_rage()
    wolfClan.upgrade_rage()
    assert(wolfClan._current_axes_slot == 1)
    #assert(wolfClan._current_rage_slot== 6)
    print(wolfClan._current_rage_slot)
    assert(wolfClan._current_horns_slot == 3)


testEndGlory()
testUpgradeStats()