# Phone Home

Our submission for the global game jam (2018)

A space themed RPG written in python


### Stat sheet API:

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

