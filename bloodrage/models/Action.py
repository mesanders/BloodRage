#!/usr/bin/env python

#
#   Author: Michael E Sanders
#

# At the beginning of the action phase, set the curent rage of each clan to the current Rage Stat.
# Each player takes turn performing one action at a time, paying the rage cost associated to each action.
#Players with 0 rage cannot take actions.
# Continue until all players have 0 rage or all provinces are pillaged.

# The actions a player can take:
#   INVADE: Pay rage equal to figure's str to move from reserve to empty village. Ships Invade Fjords, and no one can invade Yggdrasil, except dark elf
#   MARCH: Pay 1 Rage to move any # of figures from ONE province to another provicnce, ships can't march
#   UPGRADE, Pay Rage equal to the STR of an Upgrade Card in hand to place it on your clan sheet. Upgrade monster may immediately invade.
#   QUEST: Costs 0 rage to play, add quest to clann sheet when played
#   PILLAGE: At no rage cost, choose an un-pillaged province with at least one of your fiugres in it or supportin fjord. to attempt o pillarge it.
#          Starting with the player to the left may move for free figures from adjacent provnnces into empty villages of the province being pillaged
#           All players with figures in the battle choose and revewal one card, add str bonus to your figures to total str.
#           All losing players return all played cards to their hands. All of their participating figures are destoryed. 
