custom_race_list = []
########################################
# DO NOT EDIT ANYTHING ABOVE THIS LINE #
########################################

#
# TEMPLATE
# To add your own races, follow the example below:
#
# slugpeople = Race(
#     name='Slugpeople',
#     desc='''These creatures look like giant slugs.  Slimy!''',
#     size='medium',
#     strength=0, agility=0, endurance=2, intuition=2, logic=0, willpower=1, charisma=-1, luck=0, reputation=0, power=0,
#     available_skills=['[trivia]', '[gaming]', '[scientific]', 'engineering', 'slithering'],
#     exploits=[{'Name': '''Slippery''',
#                'Desc': '''Slugpeople are so slimy they are hard to grab. Attackers must pay an extra 1d6 when attempting to grab you.'''},
#               {'Name': '''Slime trail''',
#                'Desc': '''Slugpeople leave a trail of slime wherever they go. Every square you move through on your turn counts as difficult terrain for anyone but other slugpeople until the beginning of your next turn.'''}])
# custom_race_list.append(slugpeople)
#

########################################
# DO NOT EDIT ANYTHING BELOW THIS LINE #
########################################
custom_race_list.sort(key=lambda x: x.name)
for race in custom_race_list:
    race.available_skills.sort()
    race.exploits.sort(key=lambda x: x['Name'])
