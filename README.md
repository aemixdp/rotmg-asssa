# rotmg-asssa
This simple script is intended to save your ass during gameplay.
Of course this is just for demonstration purpose *bla-bla-bla* don't use it or you could get banned if somebody cares.
Well, I actually think it's more fun to do this by hand, but now I'm extra hungry for fame, pots, and achievements.

## How it works
Basically this script just examines pixel colors on HP and MP (in priest mode) bars and sends keyboard presses to game window.

Regular mode: If target pixel on HP bar corresponds to low HP, try to drink HP potion (by sending keypress).
If after this HP is still low, it means there are no HP potions, so it's time to teleport to Nexus.

Priest mode: If target pixel on HP bar corresponds to low HP, check the MP. If MP is low too, try to drink MP potion.
If succeed, cast heal spell. Otherwise, try to drink HP potion. If there are no HP potions, teleport to Nexus.

## Usage
To run this script you should install [python](https://www.python.org/downloads/release/python-343/)
and corresponding version of [pywin32](http://sourceforge.net/projects/pywin32/files/pywin32/Build%20219/). Then just run from command line:
```
$ python .\rotmg_asssa.py
```

## In action
It should look like this:
```
$ python .\rotmg_asssa.py
(21:47:01) [init/info] Seeking for game window...
(21:47:01) [init/success] Game window found: 3409050
(21:48:40) [game/event] Low HP! Trying to cast heal...
(21:48:40) [game/success] Successfully healed!
(21:48:46) [game/event] Low HP! Trying to cast heal...
(21:48:46) [game/success] Successfully healed!
(21:48:51) [game/event] Low HP! Trying to cast heal...
(21:48:52) [game/success] Successfully healed!
(21:48:56) [game/event] Low HP! Trying to cast heal...
(21:48:56) [game/success] Successfully healed!
(21:49:02) [game/event] Low HP! Trying to cast heal...
(21:49:02) [game/event] Low MP! Trying to drink potion...
(21:49:02) [game/failure] There are no mana potions!
(21:49:02) [game/event] Low HP! Trying to drink potion...
(21:49:03) [game/failure] Nothing works! HP is still low! Teleporting to Nexus...
```
