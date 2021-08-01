# Building Starships

From the smallest transport shuttles to the largest, battleready dreadnoughts, starships are an important part of Star5er. They defend orbital stations from raids by space pirates, engage enemy fleets during massive interstellar conflicts, and explore the deepest reaches of space. But at their simplest, they allow the characters to travel the stars in search of adventure. The following section outlines the process of building a starship from scratch and customizing it to perfectly fit your needs.

## Understanding Starships

Most starships are built around _frames_ that give a ship its role and basic characteristics. Different _frames_ are available to cover for varied ship roles, from fighters and shuttles, to freighters and destroyers, or even carriers and dreadnoughts.

Starships and their base frames are described using stat blocks that include information about how they move, the size of their crews, and more. When you’re reading a starship or base frame stat block, the statistics and definitions below define its capabilities. A starship sheet is provided at the end of this book.

* **Name and Tier:** This is the designation of the starship and its power level. Tiers go from 1 to 20 and frequently follow the level of the characters in their crew.
* **Size Category and Frame:** This describes the overall size of the vessel. A starship’s size provides a modifier to its Armor Class and Target Lock (see below). This entry also notes the base frame of the starship.
* **Speed:** This is the number of hexes the starship can move using most pilot actions.
* **Maneuverability:** A starship’s maneuverability is rated clumsy, poor, average, good, or perfect. This is generally tied to the mass and size of the starship, and it both indicates how agile the starship is in space and determines the minimum number of hexes the starship must move before it can turn.
* **Drift:** This is a starship’s Drift engine rating. When determining how long it takes a starship to travel to a location through the Drift, divide the die roll by this number (see [Drift Navigation](navigation.md#drift-navigation) rules). If this entry is absent, the starship can’t travel into the Drift.
* **Armor Class (AC):** This value is used when determining whether direct-fire weapons (like lasers and railguns) hit a starship. AC is calculated based on the ship’s size, maneuverability, and physical armor, as well as the pilot’s proficiency bonus.
* **Target Lock (TL):** This value is used when determining whether tracking weapons (like missiles and torpedoes) hit a starship. TL is calculated based on the starship’s size, maneuverability, and defensive countermeasures, plus the pilot’s proficiency bonus.
* **Passive Defense (PD):** This value is used when determining success of some actions that try to scan or target electronic systems in a ship.
* **Hull Points (HP):** This is the total amount of damage a starship can take before it becomes inoperative. A starship with 0 Hull Points isn’t destroyed, though many of its systems are no longer functioning and it is no longer a threat to its enemies. In a base frame stat block, the Hull Points entry also lists the HP increment, which is the number of Hull Points a starship with that frame automatically gains when its tier increases to 4 (and every 4 tiers thereafter).
* **Damage Threshold (DT):** If an attack deals less damage less than this value, that damage isn’t counted against the ship’s total Hull Points. Only Huge or larger ships have a Damage Threshold, and it matters only when such a starship’s shields are depleted.
* **Critical Threshold (CT):** Whenever the total amount of damage that has been dealt to a starship’s Hull Points reaches a multiple of this value, one of its systems takes critical damage. This value is always one-fifth of the starship’s maximum number of Hull Points.
* **Shields:** In a starship stat block, this lists the ship’s shield system and the Shield Points (SP), which represent the damage shields can take before they’re depleted. Shield Points are assigned to particular quadrants (forward, port, starboard, or aft). These quadrants correspond in orientation to the firing arcs.
* **Attacks:** A starship has four firing arcs: forward, port, starboard, and aft. Most non-turret weapons can fire only in the firing arc where they’re mounted; turret weapons can be fired in any arc. The attack entries list the various weapons mounted on the ship that can fire in each of the arcs. Each weapon also lists its damage, range, and other special properties.
* **Mounts:** In a base frame stat block, this entry lists the class of weapon that can be mounted on the starship.
* **Power Core:** This lists a starship’s power core or cores and the power core units (PCU) it produces.
* **Drift Engine:** The starship’s Drift engine, if any, is listed here.
* **Systems:** This entry lists a starship’s major systems, such as armor, defensive countermeasures, sensors, and weapons.
* **Expansion Bays:** This entry lists any expansion bays—cargo spaces that can be used for special purposes.
* **Modifiers:** This entry lists the bonuses (or penalties) to certain skill checks during starship combat gained from a starship’s speed and maneuverability, as well as from some starship systems.
* **Minimum and Maximum Crew:** In a base frame stat block, these entries note the minimum and maximum number of characters who can take actions on that vessel during starship combat. Larger starships use teams that report to a higher officer who performs an assigned role in starship combat. A starship without its minimum crew can’t be operated.
* **Complement:** In a starship stat block, this section lists the total size of the crew aboard that ship.
* **Crew:** In a starship stat block, this section lists those filling various roles in combat, as well as their bonuses to skills used during starship combat. Any modifiers listed earlier in the stat block are accounted for here. If a starship has teams supporting officers who fill roles, this entry also lists the number and size of teams. This section is listed only for ships under the GM’s control—PCs can perform their own actions aboard starships they control; for more on these actions, see [Starship Combat](combat.md).
* **Special Abilities:** Any unique actions or qualities a starship has due to its crew or its equipment are listed here.
* **Cost:** In a base frame stat block, this lists the frame’s Build Point cost. Build Points (BP) are an abstract resource used for creating and upgrading starships.

## Step by step build

Regardless of starships’ size and purpose, they’re all created using the same process. GMs and players alike can use the following steps to create an incredibly diverse array of vessels, from sleek science ships and nimble skirmishers to heavily armored combat frigates. Alternatively, you can use the prebuilt [sample starships](samples.md).

While it’s possible to run a Star5er game that doesn’t involve starships at all, the game assumes that PCs have access to a starship. Whether it was built from scrap, received from a generous benefactor, or purchased with an exorbitant loan, the PCs’ starship serves as a mobile base of operations, a means of reaching distant stars, and a defense against hostile alien vessels. Often, the PCs’ first starship is designed by the GM and can be upgraded or even replaced as the characters gain experience. However, some GMs might allow the PCs free reign over their starship’s creation, letting them feel a sense of true ownership over the starship that will accompany them throughout the campaign. Either way, a starship’s power level is based on the PCs’ average character level. See [Refitting and Upgrading](#refitting-and-upgrading) for information on how to adjust a starship’s capabilities when the characters level up.

When creating a starship, follow these steps.

1. **Conceptualize.** Start by deciding what type of starship you are designing, with a general idea of its purpose and required crew size. If you are creating a starship to be used by PCs, make sure that all the PCs can fit within the vessel! Some of the choices you make later might depend on your overall concept.
2. **Determine tier and Build Points.** If you are creating a PC starship, determine the characters’ average level by adding together the characters’ levels and dividing by the number of characters. That number is their ship’s tier. If designing enemy starships, decide the difficulty of the encounter and choose the enemy ship’s tier. Once you know the tier of the ship, consult the table below to determine the number of Build Points you can spend to create the starship. Note that a starship receives a boost to its Hull Points equal to its HP increment at tiers 4, 8, 12, 16, and 20.
3. **Select a frame.** Each starship is built upon one of a variety of frames that determines its size, maneuverability, crew complement, weapon mounts, and other basic statistics. Each frame costs a certain number of Build Points; see [Base Frame](#base-frame) below for more information.
4. **Select a power core.** A starship’s power core determines its overall power available (listed in power core units, or PCU), so you should spend Build Points on it first. This amount of power can be used as a kind of budget when installing other systems, such as thrusters and weapons.
5. **Select thrusters.** A starship without a means of propulsion is nothing more than a floating target (or an inert hunk of metal on a planet’s surface), so spending Build Points on the starship’s thrusters should be your next priority. On the [Thrusters](#thrusters) section there's a list by starship size and speed (in hexes) during combat.
6. **Select other systems.** Next, spend your remaining Build Points on all the other systems you wish to have on your starship. To be effective in combat, a starship needs armor, defensive countermeasures, shields, and weapons. If you wish to travel to locations outside of your home star system, it also needs a Drift engine. Other, more optional purchases include upgrades to the starship’s computers, expansion bays, security, and sensors.
7. **Add details.** Finally, once all these choices have been made, you should give your starship a name, determine its relevant statistics (such as its AC and TL), and add any other details (such as quirks, physical description, and so on).

|Tier|Starship Build Points|Special|
|---:|--------------------:|-------|
|¼ |   25|—|
|⅓ |   30|—|
|½ |   40|—|
|1 |   55|—|
|2 |   75|—|
|3 |   95|—|
|4 |  115|HP increase|
|5 |  135|—|
|6 |  155|—|
|7 |  180|—|
|8 |  205|HP increase|
|9 |  230|—|
|10|  270|—|
|11|  310|—|
|12|  350|HP increase|
|13|  400|—|
|14|  450|—|
|15|  500|—|
|16|  600|HP increase|
|17|  700|—|
|18|  800|—|
|19|  900|—|
|20|1,000|HP increase|

### Minimum proficiency bonus for starship

A starship has a proficiency bonus equivalent to a character with the same level as the ship tier. This bonus is used in some checks and rolls for autonomous actions made by the ship or its systems. Characters with a lower proficiency bonus can not add their proficiency bonus when rolling for checks to operate the ship.

## Base Frame

Each starship has a base frame that determines its size, maneuverability, starting weapon mounts, hull strength, room for expansion, and other capacities. Although two ships that use the same frame might look radically different, they both have some of these base statistics in common. The frame of a starship includes all life support and artificial gravity systems necessary to keep the crew (and any passengers) alive and comfortable. The starship’s frame is also built with a transponder that is essentially the ship’s “address” for standard system-wide and unlimited-range communications; this transponder can be turned off, during which time the starship can’t send or receive messages, but neither can it be tracked down by conventional means.

The base frames below are organized by size (from smallest to largest) and cost in Build Points (with less expensive frames coming first within a size). In general, the size and expansion bay capacities of a base frame can’t be changed without a great deal of time and money (and the GM’s permission), so it can be more effective to just start over with a different base frame when upgrading those aspects of a starship.

Note that some of the stats provided in a base frame will later be adjusted by the ship equipment of loadout. For example, each frame lists a maneuverability, but adding armor to the ship may result in a penalty to the final value.

<div class="statblock">

# Racer
_Tiny starship_

**Maneuverability** perfect (+2 piloting, turn 0)    
**HP** 20 (increment 5); **DT** —; **CT** 4    
**Mounts** forward arc (1 light), aft arc (1 light)    
**Expansion Bays** —    
**Minimum Crew** 1; **Maximum Crew** 1    
**Cost** 4

</div>

<div class="statblock">

# Interceptor
_Tiny starship_

**Maneuverability** perfect (+2 piloting, turn 0)    
**HP** 30 (increment 5); **DT** —; **CT** 6    
**Mounts** forward arc (2 light)    
**Expansion Bays** —    
**Minimum Crew** 1; **Maximum Crew** 1    
**Cost** 6

</div>

<div class="statblock">

# Shuttle
_Small starship_

**Maneuverability** perfect (+2 piloting, turn 0)    
**HP** 35 (increment 5); **DT** —; **CT** 7    
**Mounts** forward arc (1 light)    
**Expansion Bays** 3 (usually cargo holds or passenger seating)    
**Minimum Crew** 1; **Maximum Crew** 2    
**Cost** 8

</div>

<div class="statblock">

# Fighter
_Tiny starship_

**Maneuverability** good (+1 piloting, turn 1)    
**HP** 35 (increment 5); **DT** —; **CT** 7    
**Mounts** forward arc (2 light [1 must be a tracking weapon]), aft arc (1 light)    
**Expansion Bays** —    
**Minimum Crew** 1; **Maximum Crew** 2    
**Cost** 8

</div>


<div class="statblock">

# Light Freighter
_Small starship_

**Maneuverability** good (+1 piloting, turn 1)    
**HP** 40 (increment 10); **DT** —; **CT** 8    
**Mounts** forward arc (2 light), port arc (1 light), starboard arc (1 light)    
**Expansion Bays** 3    
**Minimum Crew** 1; **Maximum Crew** 6    
**Cost** 10

</div>

<div class="statblock">

# Explorer
_Medium starship_

**Maneuverability** good (+1 piloting, turn 1)    
**HP** 55 (increment 10); **DT** —; **CT** 11    
**Mounts** forward arc (2 light), port arc (1 light), starboard arc (1 light), turret (1 light)    
**Expansion Bays** 4    
**Minimum Crew** 1; **Maximum Crew** 6    
**Cost** 12

</div>

<div class="statblock">

# Transport
_Medium starship_

**Maneuverability** average (+0 piloting, turn 2)    
**HP** 70 (increment 15); **DT** —; **CT** 14    
**Mounts** forward arc (1 heavy, 1 light), aft arc (1 light), turret (2 light)    
**Expansion Bays** 5    
**Minimum Crew** 1; **Maximum Crew** 6    
**Cost** 15

</div>

<div class="statblock">

# Destroyer
_Large starship_

**Maneuverability** average (+0 piloting, turn 2)    
**HP** 150 (increment 20); **DT** —; **CT** 30    
**Mounts** forward arc (2 heavy), port arc (1 light), starboard arc (1 light), aft arc (1 light), turret (1 light)    
**Expansion Bays** 4    
**Minimum Crew** 6; **Maximum Crew** 20    
**Cost** 30

</div>

<div class="statblock">

# Heavy Freighter
_Large starship_

**Maneuverability** average (+0 piloting, turn 2)    
**HP** 120 (increment 20); **DT** —; **CT** 24    
**Mounts** forward arc (1 heavy, 2 light), port arc (1 heavy), starboard arc (1 heavy)    
**Expansion Bays** 8    
**Minimum Crew** 6; **Maximum Crew** 20    
**Cost** 40

</div>

<div class="statblock">

# Bulk Freighter
_Huge starship_

**Maneuverability** poor (-1 piloting, turn 3)    
**HP** 160 (increment 20); **DT** 5; **CT** 32    
**Mounts** forward arc (1 heavy), aft arc (1 heavy), turret (2 light)    
**Expansion Bays** 10    
**Minimum Crew** 20; **Maximum Crew** 50    
**Cost** 55

</div>

<div class="statblock">

# Cruiser
_Huge starship_

**Maneuverability** average (+0 piloting, turn 2)    
**HP** 180 (increment 25); **DT** 5; **CT** 36    
**Mounts** forward arc (1 capital), port arc (1 light), starboard arc (1 light), turret (1 heavy)    
**Expansion Bays** 6    
**Minimum Crew** 20; **Maximum Crew** 100    
**Cost** 60

</div>

<div class="statblock">

# Carrier
_Gargantuan starship_

**Maneuverability** poor (-1 Piloting, turn 3)    
**HP** 240 (increment 30); **DT** 10; **CT** 48    
**Mounts** forward arc (1 capital), port arc (3 heavy), starboard arc (3 heavy), turret (2 light)    
**Expansion Bays** 10 (at least 1 must be a hanger bay)    
**Minimum Crew** 75; **Maximum Crew** 200    
**Cost** 120
</div>

<div class="statblock">

# Battleship
_Gargantuan starship_

**Maneuverability** average (+0 piloting, turn 2)    
**HP** 280 (increment 40); **DT** 10; **CT** 56    
**Mounts** forward arc (1 capital, 2 heavy), port arc (2 heavy, 1 light), starboard arc (2 heavy, 1 light), aft arc (1 light), turret (2 heavy)    
**Expansion Bays** 8    
**Minimum Crew** 100; **Maximum Crew** 300    
**Cost** 150
</div>


<div class="statblock">

# Dreadnought
_Colossal starship_

**Maneuverability** clumsy (-2 piloting, turn 4)    
**HP** 400 (increment 50); **DT** 15; **CT** 80    
**Mounts** forward arc (2 capital, 2 heavy), port arc (1 capital, 3 heavy), starboard arc (1 capital, 3 heavy), turret (4 light)    
**Expansion Bays** 20    
**Minimum Crew** 125; **Maximum Crew** 500    
**Cost** 200
</div>

## Power Core

The power core is the most important system on a ship, as it provides power to every other system. The table below lists the ship size each core is designed for, as well as the PCU it provides and its cost. Each Large and smaller ship has room for only a single power core by default, but Medium and Large starships can be fitted with an extra power core housing (see [Expansion Bays](#expansion-bays)). Huge starships can have up to two power cores, Gargantuan starships can have up to three, and Colossal starships can have up to four. Though some ships are exceptions to this standard, they are rare in design. A power core typically has a backup battery system for use in emergencies that can provide limited power—enough for life support, gravity, and comms, but no other systems—for 2d6 days.

|Core|Size|PCU|Cost (in BP)|
|----|:--:|--:|-----------:|
|Micron Light|T|50|4|
|Micron Heavy|T|70|6|
|Micron Ultra|T|80|8|
|Arcus Light|T, S|75|7|
|Pulse Brown|T, S|90|9|
|Pulse Black|T, S|120|12|
|Pulse White|T, S|140|14|
|Pulse Gray|T, S, M|100|10|
|Arcus Heavy|T, S, M|130|13|
|Pulse Green|T, S, M|150|15|
|Pulse Red|T, S, M|175|17|
|Pulse Blue|T, S, M|200|20|
|Arcus Ultra|S, M, L|150|15|
|Arcus Maximum|S, M, L|200|20|
|Pulse Orange|S, M, L|250|25|
|Pulse Prismatic|S, M, L|300|30|
|Nova Light|M, L, H|150|15|
|Nova Heavy|M, L, H|200|20|
|Nova Ultra|M, L, H|300|30|
|Gateway Light|L, H, G|300|30|
|Gateway Heavy|L, H, G|400|40|
|Gateway Ultra|H, G, C|500|50|

## Thrusters

Ships rely on conventional thrusters to move between locations in a system, to navigate the reaches of the Drift once they arrive there, to explore, and to engage in combat They are designed for ships of a specific size (specified in the Size column of the table below), and they can’t be installed in a ship of an incorrect size. The maximum speed of a starship’s thrusters either grants a bonus or imparts a penalty to Dexterity (Piloting) checks to fly the vessel, as noted on the table below.

Thrusters are also used when landing on and taking off from a planet. Large and smaller Starships generally have little difficulty landing on and taking off from a planet with low gravity or standard gravity (unless there are atmospheric conditions such as high winds or storms). The GM determines whether or not a starship’s pilot must attempt a Dexterity (Piloting) check to land a starship with a speed lower than 8 on a planet with high gravity, with failure meaning it might crash. Due to their sheer size, Huge and larger starships can’t land on planets, and must use shuttles or other means to ferry crew and goods to a planet and back.

|Thruster     |Size|Speed (in Hexes)|Piloting Modifier|PCU |Cost (in BP)|
|:-----------:|:--:|---------------:|----------------:|---:|-----------:|
|T6 Thrusters | T  |              6 |               +1| 20 |           3|
|T8 Thrusters | T  |              8 |                0| 25 |           4|
|T10 Thrusters| T  |             10 |                0| 30 |           5|
|T12 Thrusters| T  |             12 |               -1| 35 |           6|
|T14 Thrusters| T  |             14 |               -2| 40 |           7|
|S6 Thrusters | S  |              6 |               +1| 30 |           3|
|S8 Thrusters | S  |              8 |                0| 40 |           4|
|S10 Thrusters| S  |             10 |                0| 50 |           5|
|S12 Thrusters| S  |             12 |               -1| 60 |           6|
|M4 Thrusters | M  |              4 |               +2| 40 |           2|
|M6 Thrusters | M  |              6 |               +1| 50 |           3|
|M8 Thrusters | M  |              8 |                0| 60 |           4|
|M10 Thrusters| M  |             10 |                0| 70 |           5|
|M12 Thrusters| M  |             12 |               -1| 80 |           6|
|L4 Thrusters | L  |              4 |               +2| 60 |           4|
|L6 Thrusters | L  |              6 |               +1| 80 |           6|
|L8 Thrusters | L  |              8 |                0| 100|           8|
|L10 Thrusters| L  |             10 |                0| 120|          10|
|H4 Thrusters | H  |              4 |               +2| 80 |           4|
|H6 Thrusters | H  |              6 |               +1| 120|           6|
|H8 Thrusters | H  |              8 |                0| 140|           8|
|H10 Thrusters| H  |             10 |                0| 160|          10|
|G4 Thrusters | G  |              4 |               +2| 120|           8|
|G6 Thrusters | G  |              6 |               +1| 180|          12|
|G8 Thrusters | G  |              8 |                0| 240|          16|
|C4 Thrusters | C  |              4 |               +2| 200|           8|
|C6 Thrusters | C  |              6 |               +1| 300|          12|
|C8 Thrusters | C  |              8 |                0| 400|          16|

## Other Systems

There are many other systems that may be present in starships to customize them and enhance their capabilities. Some of these have restrictions on the ship size, and requirements in terms of Build Points (BP) and power (PCU)

### Armor

Available ship armors go from Mk 1 to Mk 8. Armor protects a ship from direct-fire weapons, deflecting their energy and preventing damage to critical ship systems. It grants an armor bonus to a ship’s AC. Armor’s cost depends on the bonus it grants and the ship’s size category (for the purpose of this calculation, Tiny = 1, Small = 2, Medium = 3, Large = 4, etc.). Armor is a passive system and does not require any PCU to remain functional. It provides protection primarily through mass, which can affect a ship’s maneuverability (making it harder to turn) and make it easier for opponents using tracking weapons to lock on to the ship—these effects are listed in the Special column of the table below.
 

|Name|AC Bonus|Special|Cost in BP|
|----|-------:|:-----:|---------:|
|Mk 1 Armor|+1|—|2 × size category|
|Mk 2 Armor|+2|—|5 × size category|
|Mk 3 Armor|+3|-1 TL|9 × size category|
|Mk 4 Armor|+4|-1 TL|15 × size category|
|Mk 5 Armor|+5|-2 TL, +1 turn distance|21 × size category|
|Mk 6 Armor|+6|-3 TL, +2 turn distance|30 × size category|
|Mk 7 Armor|+7|-3 TL, +2 turn distance|40 × size category|
|Mk 8 Armor|+8|-4 TL, +3 turn distance|50 × size category|

### Computer

A computer system functions in many ways as a ship’s brain. Most computers aboard starships have at least a rudimentary artificial personality, and while they can’t fully perform the duties of a crew member, they can assist crew members in various tasks. However, many spacefarers claim that over time, a starship’s computers can develop temperaments and personality quirks that set them apart from identical computers in other ships. A starship has a basic computer of a tier of ¼ the ship tier (see the [Computers](../equipment/computers.md) section for information about upgrading or hacking a computer).

While a starship’s computer is responsible for operating and managing a wide variety of starship systems at any given point in time, only a starship with an integrated control module (ICM) can aid the crew in starship combat (the basic computer listed on the table below is the only option that lacks an ICM).

In general, an ICM adds a bonus die to one or more starship combat checks, decided just after the check is attempted but before the results are resolved. An ICM has a number of nodes; each node grants, as a reaction, its bonus to one crewman performing starship combat check. Once the node has been used, it has to be reinitialized by the engineer to be used again
ICMs can be purchased only with Build Points, not with credits.

|Name       |Bonus|Nodes|PCU|BP cost|
|-----------|:---:|----:|--:|------:|
|Basic computer|   0| 0 |  0|   0|
|Mk 1 mononode | 1d4| 1 | 10|   2|
|Mk 1 duonode  | 1d4| 2 | 15|   4|
|Mk 1 trinode  | 1d4| 3 | 15|   8|
|Mk 1 tetranode| 1d4| 4 | 15|  12|
|Mk 1 pentanode| 1d4| 5 | 15|  16|
|Mk 1 hexanode | 1d4| 6 | 15|  20|
|Mk 2 duonode  | 1d6| 2 | 25|  16|
|Mk 2 trinode  | 1d6| 3 | 25|  32|
|Mk 2 tetranode| 1d6| 4 | 25|  48|
|Mk 2 pentanode| 1d6| 5 | 25|  64|
|Mk 2 hexanode | 1d6| 6 | 25|  80|
|Mk 3 duonode  | 1d8| 2 | 35|  36|
|Mk 3 trinode  | 1d8| 3 | 35|  72|
|Mk 3 tetranode| 1d8| 4 | 35| 108|
|Mk 3 pentanode| 1d8| 5 | 35| 144|
|Mk 4 duonode  |1d10| 2 | 45|  64|
|Mk 4 trinode  |1d10| 3 | 45| 128|
|Mk 4 tetranode|1d10| 4 | 45| 192|
|Mk 5 duonode  |1d12| 2 | 55| 100|
|Mk 5 trinode  |1d12| 3 | 55| 200|

### Crew Quarters

Most starships larger than Tiny have places where their crew can eat, sleep, and bathe during long journeys through space. These quarters can range from hammocks strung between cargo containers to cozy chambers with custom furnishings and private bathrooms. Crew quarters consume a negligible amount of PCU, though amenities in fancier quarters require an operational power core to function.

#### Common

**BP Cost** 0    
Common crew quarters are the most basic type. They consist of simple bunks (sometimes folding out from the side of a hallway) or other similarly austere places to rest. Crew members who sleep in common quarters usually keep their personal possessions in a footlocker. Common crew quarters also include a communal bathroom (which includes a military-style shower) and a tiny galley (big enough to prepare only the most basic of meals). Starships with crews numbering in the dozens or hundreds often have massive barracks where crew members sleep in shifts.

#### Good

**BP Cost** 2    
Good crew quarters are a bit more upscale than common crew quarters. They consist of dormitory-style rooms that can hold one or two small beds (larger starships usually require lower-ranking crew members to share these quarters) and sometimes a personal closet or drawer space for each occupant. Good crew quarters also include one or two shared bathrooms with multiple sinks and shower stalls, and a dining space with an attached galley. Crews of larger starships eat in this dining space in shifts.

#### Luxurious

**BP Cost** 5    
Luxurious crew quarters are the pinnacle of comfort. They consist of private rooms for each crew member, with personal bathrooms (including showers with high water pressure) and furnishings that match the resident’s tastes. Some luxurious crew quarters also feature a kitchenette, gaming areas, or intimate meeting spaces.

### Defensive Countermeasures

Defensive countermeasures systems protect a ship from tracking weapons such as missiles, and they make it difficult for enemies using sensors to get a solid reading on the ship. They do this via a complicated suite of electronic sensors and broadcasting equipment that’s designed to jam enemy sensors and create false readings. These systems grant a bonus to a ship’s TL; the bonus, PCU usage, and cost are listed in the table below.

|Name|TL Bonus|PCU|Cost in BP|
|----|-------:|--:|---------:|
|Mk 1 defenses|+1|1|3|
|Mk 2 defenses|+2|3|6|
|Mk 3 defenses|+3|5|11|
|Mk 4 defenses|+4|9|18|
|Mk 5 defenses|+5|13|27|
|Mk 6 defenses|+6|20|40|
|Mk 7 defenses|+7|32|65|
|Mk 8 defenses|+8|50|100|

### Drift Engines

These engines let you travel to and from the Drift (see [Navigation](navigation.md)). The better the engine rating, the faster you can reach distant destinations. Drift engines have a PCU requirement and a maximum frame size. The cost in Build Points is based on the starship’s size category (for the purposes of this calculation, Tiny = 1, Small = 2, Medium = 3, Large = 4, and so on). See the table below for the statistics of the various Drift engines.

|Drift Engine|Engine Rating|Minimum PCU|Maximum Size|Cost (in BP)|
|------------|------------:|----------:|------------|------------|
|Signal Basic|1|75|—|2 x size category|
|Signal Booster|2|100|Huge|5 x size category|
|Signal Major|3|150|Large|10 x size category|
|Signal Superior|4|175|Large|15 x size category|
|Signal Ultra|5|200|Medium|20 x size category|

### Expansion Bays

Most starships have room within their hull for one or more expansion bays, each of which can be converted to function in a wide variety of roles. Unfilled, these bays are simply storage space (and count as cargo holds), and for many large transport vessels, they remain this way. If a starship’s bays are instead used for guest quarters, the ship can serve as a transport vessel for soldiers, travelers, or refugees. If its bays are filled with medical bays and guest quarters, the ship becomes a mobile hospital.

The following options are available for most ships that have available expansion bays. If an option requires multiple bays, this is noted in its description; if it must consume PCU to function, the amount is listed in the table below. An entire expansion bay must be used for a single purpose, even if it gives you multiple instances of that option. For example, if you select escape pods, that expansion bay gains all six escape pods—you can’t combine three escape pods and one life boat.

The PCU requirement and the Build Point costs of the expansion bay options are as follows:

|Name|PCU|Cost (in bp)|
|----|--:|-----------:|
|[Arcane Laboratory](#arcane-laboratory)|1|1|
|[Brig](#brig)|1|1|
|[Cargo Hold](#cargo-hold)|0|0|
|[Escape Pods](#escape-pods)|2|1|
|[Guest Quarters](#guest-quarters)|1|1|
|[Hangar Bay](#hangar-bay)|30|10|
|[Life Boats](#life-boats)|5|3|
|[Medical Bay](#medical-bay)|4|8|
|[Passenger Seating](#passenger-seating)|0|0|
|[Recreation Suite, Gym](#recreation-suite)|0|1|
|[Recreation Suite, HAC](#recreation-suite)|3|1|
|[Recreation Suite, Trivid Den](#recreation-suite)|1|1|
|[Science Lab](#science-lab)|2|1|
|[Sealed Environment Chamber](#sealed-environment-chamber)|2|1|
|[Shuttle Bay](#shuttle-bay)|10|4|
|[Smuggler Compartment](#smuggler-compartment)|4|2|
|[Synthesis Bay](#synthesis-bay)|2|1|
|[Tech Workshop](#tech-workshop)|3|1|

#### Arcane Laboratory

An arcane laboratory contains all the tools and space necessary to craft magic items, though the crafter must still provide the necessary raw materials. Such a laboratory reduces the crafting time by half.

#### Brig

A brig contains all the necessary restraints and security systems to incarcerate up to eight Medium creatures.

#### Cargo Hold

Unconverted expansion bays count as cargo holds. A cargo hold can contain approximately 25 tons of goods, with no item being larger than Large. A starship with multiple cargo holds can hold larger objects; usually 4 contiguous cargo holds are required to hold Huge objects and 8 for Gargantuan objects. These size restrictions can be overridden at the GM’s discretion.

#### Escape Pods

Escape pods give the crew of a severely damaged or destroyed starship a way to avoid imminent death. An escape pod fits one Medium or smaller creature and has enough supplies and life-support capacity for that creature to survive for 7 days. It is also fitted with a distress beacon that is easily identified by long-range scanners. An escape pod has heat shields that allow it to crash-land on a planet with an atmosphere, but no means of propulsion. A single expansion bay can be converted into six escape pods.

#### Guest Quarters

Starships that function as passenger vessels require spaces apart from their crew quarters for their guests to sleep. A single expansion bay can be converted into common quarters (usually simple bunks or hammocks) for six passengers, good quarters (usually a comfortable bed, a desk with a chair, and a small set of drawers) for four passengers, or luxurious quarters (usually a large bed, a wardrobe, a couch, a desk with a nice chair, and a private washroom) for two passengers.

#### Hangar Bay

A hangar bay can be installed only in a Gargantuan or larger starship and takes up 4 expansion bays. A hangar bay provides a place for up to 8 Tiny starships to dock.

#### Life Boats

A life boat is a more sophisticated version of an escape pod. It has room for one Large creature, or two Medium or smaller creatures, and enough supplies to last those passengers 15 days (or 30 days of supplies for one Medium or smaller creature). While it has the same kind of distress beacon as an escape pod, a life boat also has an on-board computer that automatically detects the nearest hospitable celestial body and minimal thrusters to get the craft there (though a life boat can’t participate in starship combat). A single expansion bay can be converted into two life boats.

#### Medical Bay

A medical bay functions as a [medical lab](../equipment/other.md#medical-lab)

#### Passenger Seating

An expansion bay can be converted into rows of seating for passengers at no cost. A single expansion bay can hold seating for 16 Medium passengers (though seats can be built for larger creatures). This upgrade is appropriate only for taking many passengers on short trips; starships on journeys lasting multiple days should instead have guest quarters installed.

#### Recreation Suite

A recreation suite includes entertainments that help the crew (or passengers) relax and blow off steam. These diversions can be wide-ranging, with some consuming more PCU than others. Example recreation suites include a gym, sparring arena, or other exercise area; a trivid den or other comfortable space in which to consume passive entertainment; or a holographic amusement chamber (or HAC), vidgame arcade, or other high-tech interactive entertainment center.

#### Science Lab

A science lab contains scientific apparatuses and other laboratory equipment to aid in the research of certain topics. A general science lab provides a bonus to Life Science and Physical Science checks equal to half the ship minimum proficiency (and is called a general science lab), a life science lab provides a bonus to Life Science checks equal to the ship bonus, and a physical science lab provides a bonus to Physical Science checks equal to the ship bonus. The lab type is chosen when the expansion bay is converted.

#### Sealed Environment Chamber

Occasionally, a starship will need to host an alien or other creature whose biology is radically different from that of the crew. The passenger might be able to breathe only methane gas or can survive in only below-freezing temperatures. In such a case, a sealed environment chamber is required for the passenger to remain comfortable (and alive).

#### Shuttle Bay

A shuttle bay can be installed only in a Huge or larger starship and takes up two expansion bays. A shuttle bay provides a place for a Small or smaller starship to dock.

#### Smuggler Compartment

Smuggler compartments are cargo holds hidden behind false bulkheads and are shielded from most scanning, allowing a starship equipped with them to haul illegal goods without detection. A smuggler compartment can contain 10 tons of goods, with no item being larger than Medium. A creature on the starship must succeed at a DC 15 Wisdom (Perception) check to detect a basic smuggler compartment on the starship. A creature scanning the starship must succeed at a DC 15 Intelligence (Computers) check to detect one (this additional check is part of the science officer’s scan action in [starship combat](combat.md)). For each Build Point spent over the base cost, these DCs increase by 5 (maximum DC 30), though the amount of power the compartment uses also increases by 1.

#### Synthesis Bay

A synthesis bay contains all the space and tools required to craft drugs, medicine, or poison, though the crafter must still provide the necessary raw materials. A synthesis bay reduces the crafting time by half.

#### Tech Workshop

A tech workshop contains all the space and tools necessary to craft technological items, though the crafter must still provide the necessary raw materials. Such a workshop reduces the crafting time by half.

### Security

The additions below help to prevent unwanted scoundrels from absconding with a starship. Security systems require an operational power core to function, but they consume a negligible amount of PCU. The cost of each option is listed in the table below.

|Name|Cost (in BP)|
|----|:----------:|
|Anti-Hacking Systems|5|
|Antipersonnel Weapon, Heavy|4 × weapon min proficiency + 1|
|Antipersonnel Weapon, Longarm|4 × weapon min proficiency - 4|
|Biometric Locks|5|
|Computer Countermeasures|Tier of computer × 2|
|Self-Destruct System|5 × size category|

#### Anti-Hacking Systems

By increasing the security of the starship’s computer, these systems increase the DC to hack into it by 2. This upgrade can be purchased once.

#### Antipersonnel Weapon, Heavy

It's possible to install a modified version of a hand-held heavy weapon (not a ship weapon) on the outer hull of a ship to defend it against potential intruders. The weapon is typically mounted close to the entrance and can be operated while the ship is landed. As an action, anyone with computer access can activate or deactivate the weapon, and flag targets as hostile (flagging targets and activate it can be done in the same action). while activated it fires once per round at the closest hostile creature within normal range of the weapon, until it's ammunition is depleted or all targets in range are incapacitated. Reloading the weapon must be done from outside the ship and requires standard ammo.

This weapon can not have a minimum proficiency larger than the minimum proficiency of the ship. The weapon that gets installed is a modified weapon that can not be used by a character. It's attack bonus is the ship's minimum proficiency bonus, and it does not add any ability modifier to the damage.

#### Antipersonnel Weapon, Longarm

This works as the Heavy Antipersonal Weapon, but using a long arm instead of a heavy weapon. These have a lower BP cost.

#### Biometric Locks

The systems of a starship with biometric locks can only be used by certain creatures, designated when the locks are installed; this list can be updated by any creature who can gain access to the ship’s computer systems. A successful Intelligence (Computers) check (DC = 10 + 2 × the ship's proficiency bonus) can bypass these locks.

#### Computer Countermeasures

When a foe attempts to hack a starship’s computers and fails, a set of countermeasures can punish the would-be hacker. The crew can install one computer countermeasure, following the normal [rules for countermeasures](../equipment/computers.md#countermeasures). Each countermeasure costs a number of Build Points equal to half the starship’s tier.

#### Self-Destruct System

Used most often as a last resort, a self-destruct system completely destroys the starship on which it is installed (as if the ship had taken damage equal to twice its Hull Points), often killing everyone on board. A starship in a hex adjacent to a starship that self-destructs takes an amount of damage equal to half the destroyed starship’s maximum Hull Points; this damage can be mitigated by shields. A self-destruct system can be activated only by creatures on the starship (by turning a set of keys, typing in a specific passcode, or other physical means known only to high-ranking members of the crew) and can’t be activated remotely via hacking. The activating creatures set a time delay for the destruction (at least 1 round of starship combat). The cost of a self-destruct system depends on the size category of the ship (for the purposes of this calculation, Tiny = 1, Small = 2, Medium = 3, Large = 4, and so on).

### Sensors

Sensors function as a starship’s eyes and ears, allowing a crew to see what’s in the space around the ship, whether planetary bodies, other ships, a dangerous asteroid field, or some monstrosity from the depths of space. Sensors are a combination of video cameras, multispectrum scanners, radar arrays, signal interceptors, and optical telescopes. In starship combat, short-range sensors have a range of 5 hexes, medium-range sensors have a range of 10 hexes, and long-range sensors have a range of 20 hexes. All sensors have a skill modifier that applies to any skill used in conjunction with them. Sensors require an operational power core to function, but they consume a negligible amount of PCU.

Sensors operate in two modes: passive or active. In passive mode, sensors automatically scan the ship’s surroundings. Passive sensors detect visible or unhidden objects in a 360-degree field around the ship at a range of up to twice the sensors’ range category while in space or in the Drift (no skill check required), though local conditions may affect their range. However, gravitational forces and atmospheric conditions limit starship sensors to a range of 250 feet on most planets, and their range might be further limited by terrain, at the GM’s discretion.

Active sensors are far more discerning, and they are required if the science officer wishes to scan enemy vessels and learn details about them during starship combat. The modifier listed in the table below applies to some checks attempted by the science officer in starship combat as specified in the science officer’s actions. Active sensors can discern information about a target up to four times the sensors’ range away from the ship, but such checks are done at disadvantage if made beyond the stated range. For example, if short-range sensors (range = 5 hexes) were used against a target 12 hexes away, the check would be at disadvantage.

Outside of starship combat, a crew member can use sensors to scan a planet the starship is orbiting, attempting an Intelligence (Computers) check (applying the sensors’ modifier) to learn basic information about the planet’s composition and atmosphere. The DC for this check is usually 15, but it can be altered at the GM’s discretion to account for mitigating factors or complications. A crew member can also use the starship’s active sensors to attempt Wisdom (Perception) checks to examine the surrounding area as if she were standing outside the starship, using her own senses (such as darkvision), but adding the sensors’ modifier as a circumstance bonus to the check.

|Sensors               |Range |Modifier|Cost (in BP)|
|----------------------|:----:|-------:|-----------:|
|Cut-Rate              |Short |      -2|           1|
|Budget Short-Range    |Short |       0|           2|
|Basic Short-Range     |Short |      +2|           3|
|Advanced Short-Range  |Short |      +4|           4|
|Budget Medium-Range   |Medium|       0|           3|
|Basic Medium-Range    |Medium|      +2|           5|
|Advanced Medium-Range |Medium|      +4|           8|
|Budget Long-Range     |Long  |       0|           6|
|Basic Long-Range      |Long  |      +2|          10|
|Advanced Long-Range   |Long  |      +4|          14|

### Shields

While almost every ship has simple navigational shielding to prevent damage from tiny bits of debris, this protection does little to stop a starship from being damaged by lasers, missiles, and larger impacts. To defend against such threats, a ship has energy shields. Projectors mounted around the ship create a barrier that absorbs damage from attacks. Each attack reduces the number of Shield Points (SP) in a given arc until that arc’s shields are depleted, after which point all further damage in that arc reduces the ship’s Hull Points. See [Starship Damage](combat.md#damage) for more information. Shield Points regenerate over time and can eventually be used again, but this regeneration occurs only when the ship is not in combat or otherwise taking damage. Shields must be attached to a functional power core in order to regenerate; the rate of regeneration is listed in the table below.

The value listed under Total SP in the table below is the total number of Shield Points provided to the ship. At the start of combat, when the starship’s crew takes up battle stations and the shields are activated, the Shield Points must be divided up between the four quadrants of the ship. No quadrant can be assigned less than 10% of the total number of Shield Points available at the start of combat, or available at the time the shields are balanced again using the _balance_ science officer action.

The table also lists rate of regeneration, PCU needed, and cost.

|Shield Name|Total SP|Regeneration|PCU|Cost (in BP)|
|-----------|-------:|-----------:|--:|-----------:|
|Basic Shields 10|10|1/min.|5|2|
|Basic Shields 20|20|1/min.|10|3|
|Basic Shields 30|30|1/min.|15|4|
|Basic Shields 40|40|1/min.|15|5|
|Light Shields 50|50|2/min.|20|6|
|Light Shields 60|60|2/min.|20|8|
|Light Shields 70|70|2/min.|25|10|
|Light Shields 80|80|2/min.|30|12|
|Medium Shields 90|90|4/min.|30|13|
|Medium Shields 100|100|4/min.|30|15|
|Medium Shields 120|120|4/min.|35|17|
|Medium Shields 140|140|8/min.|40|18|
|Medium Shields 160|160|8/min.|45|20|
|Medium Shields 200|200|8/min.|50|22|
|Heavy Shields 240|240|16/min.|55|23|
|Heavy Shields 280|280|16/min.|60|25|
|Heavy Shields 320|320|16/min.|70|27|
|Heavy Shields 360|360|32/min.|80|28|
|Heavy Shields 420|420|32/min.|90|30|
|Heavy Shields 480|480|32/min.|110|32|
|Superior Shields 540|540|64/min.|130|35|
|Superior Shields 600|600|64/min.|160|40|

## Weapons

Whether the PCs are in the Vast or near a Pact Worlds planet, space is a dangerous place, plagued with hostile aliens, raiders, and worse. As a result, most ships protect themselves with a variety of weapons, ranging from laser cannons to solar torpedoes.

Weapons must be installed on special mounts on a ship, specified in the ship’s [base frame](#base-frame). These mounts are designed for optimal firing and are placed so that they can be easily tied into the ship’s power and control systems. They also prevent the weapon from affecting the course or speed of a ship when fired.

### Weapon Attributes

Weapons are classified using the following key statistics.

* **Name**: The name of the weapon
* **Class**: Weapons belong to one of three classifications. [Light weapons](#light-weapons) can be mounted on any ship but are most typically found on smaller fighters and bombers. While dangerous, light weapons do not have the firepower necessary to damage very large starships. [Heavy weapons](#heavy-weapons) are a serious threat to any vessel but can be mounted only on Medium or larger starships. [Capital weapons](#capital-weapons) can be mounted only on Huge or larger starships. Capital weapons can’t be brought to bear against Tiny or Small targets and are typically used only against other large vessels.
* **Type**: Starship weapons are one of two types. _Direct-fire weapons_ fire projectiles or beams at amazing speed, targeting the opposing vessel’s AC. _Tracking weapons_’ projectiles are slower and must home in using a target’s TL. A tracking weapon’s projectile has a listed speed; once fired, it moves that number of hexes toward its target. Each subsequent round during the gunnery phase, it must succeed at a gunnery check against the target’s TL to continue to move its speed toward its target. On a failure, the projectile is lost. If the projectile reaches the target’s hex, it deals the listed damage.
* **Range**: Weapons have one of three ranges: short range (5 hexes), medium range (10 hexes), or long range (20 hexes). As with character scale ranged attacks, an attack with a starship weapon has disadvantage when shooting out of the normal range. The maximum range of a starship weapon is 5 times its normal range. A gunner firing a tracking weapon has this disadvantage only on her first gunnery check, when the target is first acquired.
* **Speed**: This is the distance in hexes a tracking weapon moves toward its target each round during the gunnery phase. Projectiles from a tracking weapon have perfect maneuverability, and as such, they have a minimum turn distance of 0.
* **Damage**: This is the amount of damage (in Hull Points) the weapon deals when it successfully hits a target. See [Shooting Starships](combat.md#shooting-starships) for guidelines on how starship weapons can affect characters. You never add an ability bonus to starship weapon damage.
* **PCU**: This is the amount of PCU consumed by the weapon. It uses this amount continuously whenever the weapon is powered up and ready to fire.
* **Cost**: This is the cost of the weapon in Build Points.

### Weapon Special Properties

Some weapons have one or multiple of the following special properties

#### Array

An array weapon fires at all targets within a single firing arc. The gunner attempts a single gunnery check at disadvantage against each target in the firing arc, starting with those closest to her starship. Roll damage only once for all targets. Critical damage is determined by each target’s Critical Threshold. The gunner can’t avoid shooting at allies in the firing arc, nor can she shoot any target more than once. An array weapon uses two weapon mounts.

#### Broad Arc

A weapon with this special property can fire in an arc adjacent to the one in which it was installed with disadvantage. A broad arc weapon can fire at only one target at a time.

#### EMP

A weapon with this special property emits a beam of electromagnetic energy that does not deal damage to ships or shields, but plays havoc with a ship’s electronic systems. On a hit, an EMP weapon scrambles one of the target starship’s systems, determined randomly. This causes that system to act as if it had the glitching condition for 1d4 rounds. A system glitching in this way can be patched as normal, but if it takes critical damage, its glitching condition becomes constant until the system is patched or repaired (or takes further critical damage). Functioning shields are unaffected by EMP weapons and completely block an EMP weapon’s effects.

#### Irradiate

A weapon with this special property creates a wave of harmful [radiation](../rules/environment.md#radiation) that penetrates shields and starship hulls. Living creatures on a starship struck by an irradiating weapon are subjected to the level of radiation noted in parentheses for 1d4 rounds of starship combat.

#### Limited Fire

A weapon with this special property can fire only the listed number of times in a starship combat encounter before it requires a brief period of time (10 minutes outside of starship combat) to recharge and rebuild the weapon’s inherent ammunition. A weapon with this special property is often a tracking weapon.

#### Line

A weapon with this special property fires a beam in a straight line that can pierce through multiple targets. The gunner attempts a single gunnery check and compares the result to the AC of all ships in a line originating from her starship and extending to the weapon’s range. Roll the weapon’s damage once and apply it to each target with an AC equal to or lower than the gunner’s result, starting with the closest. If any of that damage is negated due to a ship’s Damage Threshold, the beam is stopped and the attack doesn’t deal damage to targets farther away.

#### Point

A weapon with this special property is always short range and can’t be fired against targets that are outside the listed weapon range. If a tracking weapon would hit a ship in an arc that contains a weapon with the point special property, the gunner of the targeted starship can use her reaction to make a gunnery check with the point weapon against the incoming tracking projectile adding the bonus listed in parentheses in the weapon’s Special entry. The DC for this gunnery check is equal to 10 + the tracking weapon’s speed. If the attack hits, the tracking weapon is destroyed before it can damage the ship. A point weapon can be used to attempt only one such free gunnery check each round, but this usage potentially allows a point weapon to be fired twice in a single round.

#### Quantum

Once a gunner fires a quantum weapon, he can reroll one gunnery check for that weapon after its launch if the result would be a miss. Only tracking weapons have this special property.

#### Ripper

Firing a blast of metal shards, a weapon with this special property deals terrific damage to a ship’s hull but is almost entirely negated by functioning shields. Halve all damage dealt by ripper weapons to shields. Ripper weapons are always short range.

#### Tractor Beam

A weapon with this special property can generate a stable beam of gravitons, creating a tractor beam that can move other ships. In addition to dealing damage, a hit with a tractor beam prevents the target ship from moving normally. The gunner can push or pull the target ship (at a rate of 2 hexes per round, resolved at the beginning of the helm phase), or hold the target ship in place. The pilot of the targeted starship can attempt a Dexterity (Piloting) check with a DC of 18 to break free of the tractor beam as her action in a round. When a tractor beam weapon is locked on to a starship, it can’t be used as a regular weapon. A tractor beam is effective only against ships of the same size as the firing ship or smaller; larger ships are unaffected by the tractor beam.

#### Vortex

A weapon with this special property creates a spiraling cyclone of gravitons that tears, crushes, and twists everything in its path, reducing a target ship’s speed by half and reducing its maneuverability by one step for 1d4 rounds on a hit. A ship protected by functioning shields takes no damage from a vortex weapon, but the target ship’s pilot must succeed at a Dexterity (Piloting) check with a DC of 18 or the hit depletes all Shield Points in that arc.

### Light Weapons

|Weapon|Type|Range|Speed|Damage|PCU|Cost (BP)|Special Properties|
|------|:--:|:---:|----:|:----:|--:|--------:|------------------|
|Chain Cannon|Direct-Fire|Short|—|6d4|15|15|Ripper|
|Coilgun|Direct-Fire|Long|—|4d4|10|6|—|
|Flak Thrower|Direct-Fire|Short|—|3d4|10|5|Point (+2)|
|Gyrolaser|Direct-Fire|Short|—|1d8|10|3|Broad Arc|
|Laser Net|Direct-Fire|Short|—|2d6|10|9|Point (+4)|
|Light EMP Cannon|Direct-Fire|Short|—|Special|10|8|EMP|
|Light Laser Cannon|Direct-Fire|Short|—|2d4|5|2|—|
|Light Particle Cannon|Direct-Fire|Medium|—|3d6|10|10|—|
|Light Plasma Cannon|Direct-Fire|Short|—|2d12|10|12|—|
|High Explosive Missile Launcher|Tracking|Long|12|4d8|10|4|Limited Fire 5|
|Light Plasma Torpedo Launcher|Tracking|Long|14|3d8|5|5|Limited Fire 5|
|Light Torpedo Launcher|Tracking|Long|16|2d8|5|4|—|
|Micromissile Battery|Tracking|Long|10|2d6|10|3|Array, Limited Fire 5|
|Tactical Nuclear Missile Launcher|Tracking|Long|10|5d8|10|5|Irradiate (low), Limited Fire 5|

### Heavy Weapons

|Weapon|Type|Range|Speed|Damage|PCU|Cost (BP)|Special Properties|
|------|:--:|:---:|----:|:----:|--:|--------:|------------------|
|Graser|Direct-Fire|Short|—|7d10|40|35|Irradiate (medium)|
|Gravity Gun|Direct-Fire|Medium|—|6d6|40|30|Tractor Beam|
|Heavy EMP Cannon|Direct-Fire|Medium|—|Special|30|24|EMP|
|Heavy Laser Array|Direct-Fire|Short|—|6d4|15|10|Array|
|Heavy Laser Cannon|Direct-Fire|Medium|—|4d8|10|8|—|
|Heavy Laser Net|Direct-Fire|Short|—|5d6|15|12|Point (+6)|
|Maser|Direct-Fire|Long|—|6d10|35|22|—|
|Particle Beam|Direct-Fire|Long|—|8d6|25|15|—|
|Persistent Particle Beam|Direct-Fire|Long|—|10d6|40|25|—|
|Plasma Cannon|Direct-Fire|Medium|—|5d12|30|20|—|
|Railgun|Direct-Fire|Long|—|8d4|20|15|—|
|Twin Laser|Direct-Fire|Long|—|5d8|15|12|—|
|X-Laser Cannon|Direct-Fire|Long|—|8d6|40|35|Line|
|Heavy Antimatter Missile Launcher|Tracking|Long|8|10d10|15|12|Limited Fire 5|
|Heavy Nuclear Missile Launcher|Tracking|Long|10|10d8|15|10|Irradiate (medium), Limited Fire 5|
|Heavy Plasma Torpedo Launcher|Tracking|Long|12|5d10|10|10|Limited Fire 5|
|Heavy Torpedo Launcher|Tracking|Long|14|5d8|10|8|Limited Fire 5|

### Capital Weapons

|Weapon|Type|Range|Speed|Damage|PCU|Cost (BP)|Special Properties|
|------|:--:|:---:|----:|:----:|--:|--------:|------------------|
|Gravity Cannon|Direct-Fire|Long|—|2d6 × 10|40|50|Tractor Beam|
|Mass Driver|Direct-Fire|Long|—|2d6 × 10|25|25|—|
|Particle Beam Cannon|Direct-Fire|Long|—|3d4 × 10|30|30|—|
|Persistent Particle Beam Cannon|Direct-Fire|Long|—|2d10 × 10|50|40|—|
|Super EMP Cannon|Direct-Fire|Long|—|Special|45|45|EMP|
|Super Plasma Cannon|Direct-Fire|Medium|—|3d6 × 10|45|35|—|
|Supergraser|Direct-Fire|Medium|—|2d8 × 10|50|60|Irradiate (high)|
|Superlaser|Direct-Fire|Long|—|2d4 × 10|20|20|—|
|Supermaser|Direct-Fire|Long|—|2d8 × 10|40|35|—|
|Vortex Cannon|Direct-Fire|Medium|—|2d12 × 10|55|75|Vortex|
|Antimatter Mega-Missile Launcher|Tracking|Long|6|4d10 × 10|15|25|Limited Fire 5|
|Hellfire Torpedo Launcher|Tracking|Long|8|2d10 × 10|10|25|Limited Fire 5|
|Nuclear Mega-Missile Launcher|Tracking|Long|8|4d8 × 10|15|20|Limited Fire 5|
|Quantum Missile Launcher|Tracking|Long|12|2d8 × 10|15|20|Limited Fire 5, Quantum|
|Solar Torpedo Launcher|Tracking|Long|10|2d6 × 10|10|20|Limited Fire 5|


### Linking Weapons

If you install two of the same direct-fire weapon in the same firing arc, you can link them together so they fire as one. This costs a number of Build Points equal to half the cost of one of the weapons (rounded down) and consumes a negligible amount of PCU.


## Refitting and Upgrading

As the PCs go on adventures and gain experience, they need an increasingly powerful starship to face tougher challenges. When the characters’ average level increases, so does the tier of their starship. The PCs receive a number of Build Points equal to the Build Points listed for their starship’s new tier – those listed for its previous tier, which they can use to upgrade their starship. For example, a group whose level increases from 2 to 3 receives 20 BP that the PCs can use to upgrade their starship. This could represent salvage gathered during their exploits, an arrangement with a spacedock, or called-in favors from a wealthy patron. Some GMs might require PCs to visit a safe, inhabited world before they can spend these Build Points, but this shouldn’t be allowed to impact the campaign too much.

Also remember that at tier 4 and every 4 tiers thereafter, the starship gains an increase in Hull Points equal to the HP increment listed for its base frame.

### Refitting Systems

If the PCs want to alter their starship before receiving additional Build Points (for instance, replacing a weapon with one that costs fewer Build Points or consumes less PCU), they can do so at a friendly spaceport (or safe landing zone) given enough time. If they replace a system or option with one that costs fewer Build Points, they can immediately spend the excess Build Points. Refitting a single system or starship weapon usually takes 1d4 days.

### Upgrading Systems

PCs with Build Points to spare can replace a system or weapon with one that costs more Build Points by paying only the difference in cost between the two systems. If the cost is the same, the system can be upgraded for free, but the crew should keep the amount of PCU the starship’s power core produces in mind so they don’t exceed their power budget. When upgrading a weapon, remember that the starship’s frame starts with a certain number and type of weapon mounts (but see [New Weapon Mounts](#new-weapon-mounts) below). Installing a single upgrade usually takes 1d4 days.

PCs can’t upgrade the base frame of their starship. They can rebuild their starship with a new base frame if they so desire (within the limits of their budget of Build Points, of course), but that new starship will have a different look (and should probably have a different name). PCs can purchase Huge and larger base frames only at the GM’s discretion, as these usually require large crews and thus are normally reserved for NPC starships.

Buying a whole new starship is a process that can take between 1d4 days and 1d4 months, depending on whether the PCs are purchasing a used starship from a spacedock or having a custom vessel built from scratch.

### New Weapon Mounts

Greater dangers means the PCs will require more powerful weapons in order to survive and triumph. Unless they begin flying around with an escort of armed battlecruisers, the weapons they start with will eventually become inadequate. Bigger weapons require the correct weapon mounts, however.

By spending 4 BP, the crew can upgrade a light weapon mount in any of the aft, forward, port, or starboard arcs to a heavy weapon mount. By spending 6 BP, the crew can upgrade a light weapon mount on a turret to a heavy weapon mount. By spending 5 Build Points, the crew can upgrade a heavy weapon mount in any of the aft, forward, port, or starboard arcs to a capital weapon mount. Heavy weapons can be mounted on only Medium or larger starships. Capital weapons can be mounted on only Huge or larger starships and can’t be mounted on turrets.

By spending 3 BP, the crew can fit a new light weapon mount in any of the aft, forward, port, or starboard arcs with enough free space. By spending 5 BP, the crew can fit a new light weapon mount on a turret that has enough free space. Tiny and Small starships can have only two weapon mounts per arc (and per turret). Medium and Large starships can have only three weapon mounts per arc (and per turret). Huge and larger starships can have only four weapon mounts per arc (and per turret).

## Finishing details

Once you have built a starship, it's a good idea to precalculate the following to make combat easier

### Armor Class

A ship Armor Class (AC) is determined by the following formula:

AC = 10 + the pilot’s proficiency bonus + the ship’s armor bonus + modifier based on the ship’s size 

The pilot can only add their proficiency bonus if they are proficient in Piloting. Note that in combat some actions can temporarily increase or decrease this AC.

### Tracking Lock

The Tracking Lock (TL) of a ship is determined by the following Formula:

TL = 10 + the pilot’s proficiency bonus + the ship’s countermeasures bonus + modifier based on the ship’s size

The pilot can only add their proficiency bonus if they are proficient in Piloting. Note that in combat some actions can temporarily increase or decrease this TL.

### Passive defense

The passive defense of a ship (PD) is:

PD = 10 + the ship's minimum proficiency bonus + the ship’s countermeasures bonus

