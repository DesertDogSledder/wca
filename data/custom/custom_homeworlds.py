from data.homeworlds import *

custom_homeworld_list = []
########################################
# DO NOT EDIT ANYTHING ABOVE THIS LINE #
########################################

#
# TEMPLATE
# To add your own homeworld, follow the example below:
#
# farmworld = Homeworld(
#     name='Farmworld',
#     strength=1,
#     agility=0,
#     endurance=0,
#     intuition=-1,
#     logic=0,
#     willpower=0,
#     charisma=0,
#     luck=0,
#     reputation=0,
#     available_skills=['farming', 'plowing'])
# custom_homeworld_list.append(farmworld)
#

########################################
# DO NOT EDIT ANYTHING BELOW THIS LINE #
########################################
custom_homeworld_list.sort(key=lambda x: x.name)
custom_homeworld_list.insert(0, homeworlds_new.homeworld_none)
for homeworld in custom_homeworld_list:
    homeworld.available_skills.sort()
