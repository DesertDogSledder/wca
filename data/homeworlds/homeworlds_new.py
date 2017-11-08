from lib.character import Homeworld

# Homeworlds
homeworld_agricultural = Homeworld(name='Agricultural', endurance=1, logic=-1, available_skills=['farming'])
homeworld_arctic = Homeworld(name='Arctic', endurance=1, agility=-1, available_skills=['survival'])
homeworld_asteroid = Homeworld(name='Asteroid', agility=1, strength=-1, available_skills=['zero-g', 'mining'])
homeworld_barren = Homeworld(name='Barren', endurance=1, charisma=-1, available_skills=['survival'])
homeworld_city = Homeworld(name='City', charisma=1, endurance=-1, available_skills=['diplomacy', 'bureaucracy'])
homeworld_desert = Homeworld(name='Desert', endurance=1, agility=-1, available_skills=['navigation', 'survival'])
homeworld_jungle = Homeworld(name='Jungle', agility=1, endurance=-1, available_skills=['climbing'])
homeworld_ocean = Homeworld(name='Ocean', agility=1, intuition=-1, available_skills=['swimming', 'sailing'])
homeworld_volcanic = Homeworld(name='Volcanic', agility=1, strength=-1, available_skills=['dodging'])

homeworld_none = Homeworld(name='None')

homeworld_new_list = [homeworld_none, homeworld_agricultural, homeworld_arctic, homeworld_asteroid, homeworld_barren,
                      homeworld_city, homeworld_desert, homeworld_jungle, homeworld_ocean, homeworld_volcanic]
