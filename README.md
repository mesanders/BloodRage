# BloodRage
This project is mainly to help me learn to use python using a structured rule set in place. This is not an attempt to make a full blown game or anything of that nature. What it is intented to do is help me grow as a Software Craftsman in developing complex data models while doing it towards something that I enjoy and can relate to.

##Structure
I don't really have one yet, but I will attempt to do more as I go. Normally, I would love to do this in Java or Scala. Using python will give me an opportunity to learn the language better.

###Game Board
The board divides the land into nine provinces, the center province is Yggdrasil, the tree of life. There are eight outer provinces around it. The Eight provinces are divided into three regions: Manheim, Alfheim, and Jotunheim. 

Each province has three to five villages. Each village can hold one model with the exception of Yggdrasil, there can be an unlimited amount there. 

There are four fjords situated between pairs of outer provinces. 

The last component is the Glory track, which keeps track of each clan's progress on glory.

###Age Track
This is a sheet that keeps track of the various phases discussed below of a phase. This also keeps track of which  Province will be destroyed during the ragnorak phase.

###Clan Sheet
The clan sheet keeps track of upgrades, rage available, Stats, and has the basic actions that are available during the game. 

####Upgrade Slots 
* One Leader Upgrade Slots
* Three Clan Upgrade Slots
* One Ship Upgrade Slot
* One Warrior Upgrade Slot
* Two Monster Upgrade Slots

####Stats
* Rage: Default 6 -> How much Rage is available at the beginning of each round.
* Axes: Default 3 -> How much Glory gained for winning battles.
* Horns: Default 4 -> How many figures can occupy the board at a given time. 

###Figures
Each figure: Leader, Warrior, Ship, Monsters have a STR rating. Some figures have special abilities. Upgrades can give warriors special abilities later. When a figure is destroyed it goes to Valhalla.

###Cards
Decks of cards represent gifts of the gods. Each game round has a draft where players can pull cards to bolster their armies. 

####Types of Cards
* Quest cards: represent divine quests vgiven to the clan. They have tasks that must be completed by the end of the age and give glory and raise stats.
* Upgrade cards: represent upgrades available as discussed above
* Battle cards: Add strength and have special abilities in battle.

###Phases of Play
1. God's Gifts
2. Action
3. Discard
4. Quest
5. Ragnarok
6. Release Valhalla
