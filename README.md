# Phone Home

Our submission for the global game jam (2018)

A space themed RPG written in python


### Stat sheet API:

####Characters:

| Key       | Potential Values                                           |
|:---------:|:----------------------------------------------------------:|
|type       | character                                                  |
|subtype    | player, enemy, neutral                                     |
| name      | Whatever you want                                          |
| objectID  | Assigned at runtime                                        |
| imagePath | The path to the sprite to use                              |
| health    | Positive number, -1 for unkillable                         |
| speed     | speed multiplier                                           |
| credits   | Amount of currency the player starts with                  |
| items     | List of starting items                                     |

#####Items:

| Key       | Potential Values                                           |
|:---------:|:----------------------------------------------------------:|
|type       | item                                                       |
|subtype    | weapon, credits, objective, wearable, misc                 |
| name      | Whatever you want                                          |
| objectID  | Assigned at runtime                                        |
| imagePath | The path to the sprite to use                              |
| weaponType| Ranged, Melee, Thrown, Placed                              |
| effects   | A list of modifiers such as EMP, stun, smoke, etc.         |
| consumable| Whether or not the item is single use, 1 for yes, 0 for no |
| ammo      | Amount of starting ammo, -1 for infinite                   |
| damage    | Damage dealt on hit, negative numbers will heal            |

####Environment:

| Key       | Potential Values                                           |
|:---------:|:----------------------------------------------------------:|
|type       | environemt                                                 |
|subtype    | really just anything here                                  |
| name      | Whatever you want                                          |
| objectID  | Assigned at runtime                                        |
| imagePath | The path to the sprite to use                              |
|destructable| Whether it can be destroyed, 1 for yes, 0 for no          |
| items     | Items available after the object is destroyed              |
| cover     | Whether or not the characters can use object as cover      |
| health    | Amount of damage taken before object is destroyed          |

