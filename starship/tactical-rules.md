# Tactical Rules

When simulating close encounters in space, Star5er uses a set of rules that are different than the rules used for ground combat. While most of the details about [starship combat](combat.md) are explained in a further chapter, this section introduces some basic elements that will also help you understand how to [build starships](build.md) effectively.

## Local Space Maps: Position and Speed

Starship combat is played on a grid of hexes with figures representing the starship combatants. The hexes don’t represent a specific distance, as Star5er’s portrayal of movement and combat in three-dimensional space is more fluid and narrative than realistic. Unless otherwise specified, each ship occupies 1 hex, regardless of its size. No two starships are allowed to occupy the same hex. 

Occasionally maps may contain other elements beside starships that may occupy one or more hexes, like asteroids, space stations, wormholes, etc. There are no pre-established rules for those elements here, so the GM is free to determine their effects.

## Starship orientation

Unlike ground combat, orientation of the starships is significant. Tactical use of orientation is key for engaging enemies effectively. The ship orientation affects the following aspects:

* Movement: it's generally easier to go forward than to change direction
* Offense: Most weapons are mounted in a given direction, and will be able to fire at targets in that direction. Some weapons may be able to fire at a wider arc, or installed on a mobile turret with a 360⁰ arc. You'll want to keep your enemies towards the direction were you have most firepower, and they will want to evade.
* Defense: Ships have shields that can hold different charge towards different directions (which can be rebalanced tactically during combat). Attacks coming from a given direction will affect different shields, and you'll likely want to put your strongest shield towards your most dangerous attackers.

Starships on the grid have a specific orientation in their hex, with the bow of the ship always aiming to one of the six hex sides, and never towards a corner:

![Ship Orientation](../img/orientation.png)

For each ship, its orientation determines four quadrants, called "arcs", as seem in the diagram below. The place (**firing arc**)were weapons are mounted (and some special qualities) will determine which arcs it may shoot, and enemies in a given arc will affect shields in that arc (**shield quadrant**).

![Ship Quadrants](../img/arcs.png)

 Hexes marked in blue in the diagram can be assigned to two different arcs. Each round, characters on that ship must decided which arc corresponds to each one of those hexes, if relevant. 

## Movement

### Speed

In tactical situation, the **speed** of ships and other objects (like missiles) are measured in hexes. A speed will be a number that indicates how many hexes an object can move (going from one hex to one of the six adjacent ones). All starships have a speed.

In normal conditions, a pilot can move a ship up to its speed or less hexes. This movement is in a straight line in the orientation the starship is facing, though a starship’s facing can be altered while it moves by making turns (see below).

### Maneuverability

While moving, a starship can make turns, altering its orientation, firing arcs, and shield quadrants. One turn changes a starship’s forward facing by 60 degrees, or one side of a hex. Every round in which a starship turns, it must move a certain number of hexes before each turn, determined by its **maneuverability**. A ship's maneuverability can be computed by following the rules for [building starhips](build.md), and it indicates the distance a ship must move in a straight line before changing direction. A ship’s maneuverability also provides a modifier for Dexterity (Piloting) checks made by its pilot:

|Maneuverability|Distance Between Turns|Piloting Check Modifier|
|---------------|:--------------------:|:---------------------:|
|Clumsy|4|–2|
|Poor|3|–1|
|Average|2|0|
|Good|1|+1|
|Perfect|0 (see below) |+2|

 For example, a ship with average maneuverability(distance between turns 2) making two turns in a round must move at least 2 hexes before turning for the first time in a round, and at least 2 more hexes before its turning again. If a starship has perfect maneuverability (the distance between turns is 0), the ship can make two turns (120⁰, or 2 hex sides) for each hex that it moves (allowing it to take a full turn around a single point). 
 
 ![Maneuverability](../img/maneuverability.png)

The number of turns per round a starship can take is limited only by its speed and maneuverability. Turns don’t count against a starship’s movement speed. If a ship with average maneuverability (distance between turns 2) has a speed of 8, it can usually turn up to a total of four times during a single round; the last turn would be after doing all its movement.

## Ship defenses


* size?
* stats: ac, tl, pd
* shield and hp basics, destruction
* 