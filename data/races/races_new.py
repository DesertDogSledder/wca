from lib.character import Race

# NEW races
race_new_android = Race(
    name='Android',
    desc='''Androids aren't technically a species, and can vary greatly in appearance.  Frequently, however, they look like humans.  While many philosophers will debate whether or not Androids have true consciousness, they have passed every test imaginable and are legally considered to be alive, with all the rights and responsibilities that entails.  Stronger and tougher than humans, with processors which can outpace the human mind, Androids aren't always the most popular in the room.

Androids make excellent scientists, engineers, and doctors.  

Typical names: KX-159, D.A.T.A., SL1A, TikTok, G.O.L.E.M., Watson, Jeeves, C.H.I.P., Robby, A.L.P.H.A., Mk XIV, B.R.A.I.N.''',
    size='small, medium, or large',
    strength=2, logic=2, psionics=-99,
    available_skills=['computers', 'engineering', 'running', 'linguistics', '[technical]'],
    exploits=[{'Name': 'Mindless', 'Desc': '''Androids are immune to any attacks which target MENTAL DEFENSE.'''},
              {'Name': 'Deterministic', 'Desc': '''An Android's PSI attribute can never rise above zero, and an Android cannot spend LUC dice to gain bonus dice when making attributes.'''},
              {'Name': 'Electronic vulnerability', 'Desc': '''As mechanoids, Androids are vulnerable (1d6) to electricity damage, vulnerable (2d6) to ion damage.'''},
              {'Name': 'Automaton', 'Desc': '''Androids do not need to eat, sleep, or breathe, and weigh 150% normal.'''},
              {'Name': 'Bonus modification exploit', 'Desc': '''Choose an android modification exploit.'''}])

race_new_borian = Race(
    name='Borian',
    desc='''Borians are welcome in most places. Standing at about 4' in height, with bright red or blue skin (depending on clan) and spiky, bony heads, they have a reputation for good cheer and friendliness. This, coupled with their naturally robust constitution, also makes them renowned drinkers, and it has been said that Borians make the most common bartender race in the universe.

Borians are good with their hands, and enjoy tinkering and building. They make excellent engineers and craftsmen.

Typical names (male and female): Dobur, Thrari, Kirin, Borin, Boli, Filin, Gimnor, Thrarin, Dwain, Dolo, Kibur.''',
    size='small',
    endurance=1, intuition=1, charisma=1, reputation=1,
    available_skills=['carousing', 'hardy', '[crafting]', 'engineering', 'appraisal'],
    exploits=[{'Name': 'Darksight', 'Desc': '''Borians can see in the dark to a distance of 10' per point of INT.'''},
              {'Name': 'Iron constitution', 'Desc': '''Borians are not affected by poisons, including alcohol. They are also immune to radiation damage and radiation sickness.'''},
              {'Name': 'Tinkerer', 'Desc': '''Borians may designate one item of equipment which they own. That item permanently gains one bonus quality level. If the item is lost or destroyed, the Borian may designate a new item after 24 hours.'''},
              {'Name': 'Long-lived', 'Desc': '''When creating a Borian character, multiply their career lengths by 3.'''},
              {'Name': 'Personable', 'Desc': '''Borians are noted for their cheerful demeanour and likability. When taking a new career, a Borian may optionally exchange one of the listed four attribute increases for CHA, as long as it doesn’t result in a duplicate attribute advancement.'''}])

race_new_felan = Race(
    name='Felan',
    desc='''Felans, unimaginatively named by the first human explorers to encounter them, are a cat-like species. Like their four-legged namesake, Felans are often beautiful to the eye, and move with a graceful, acrobatic purpose. Easily able to jump and climb, felans like to make use of their environment, and tend to sleep in precarious locations high above the ground.

Felans have a deserved reputation for being easily distracted, and often flit from career to career, unable to settle.

Typical names (male and female): Arhel, Infin, Elenrik, Makil, Crihel, Talik, Gimlek, Amaduil, Idthit, Ciraire.''',
    size='medium',
    agility=2, intuition=1, charisma=1, luck=1,
    available_skills=['acrobatics', 'climbing', 'jumping', '[unarmed fighting]', 'reactions',
                      'appraisal', 'bluffing', 'stealth', 'negotiating'],
    exploits=[{'Name': 'Fast', 'Desc': '''Felans are fast and nimble, adding 2 to their SPEED.'''},
              {'Name': 'Jumper', 'Decs': '''Felans are adept at jumping, adding 5' to both horizontal and vertical jump distances.'''},
              {'Name': 'Land on your feet', 'Desc': '''When falling, a Felan reduces the effective distance by 10'.'''},
              {'Name': 'Claws', 'Desc': '''Accurately slashing with their sharp claws, a Felan's unarmed damage is 2d6 slashing damage.'''},
              {'Name': 'Agile', 'Desc': '''Felans are noted for their dexterity. When taking a new career, a Felan may optionally exchange one of the listed four attribute increases for AGI, as long as it doesn’t result in a duplicate attribute advancement.'''}])

race_new_human = Race(
    name='Human',
    desc='''There's a reasonably strong chance that you, the reader, are Human. You might be a little extra-human, with mechanical improvements (glasses, a hearing aid, maybe some genuine replacement parts) but when things boil down, you are a homo sapiens. This isn’t to say that Humans are not diverse—there is a wide range of cultures and peoples across the worlds of O.L.D., N.O.W., and N.E.W. —but all of them have 10 toes, two eyes, and so on. Where you are from and who raised you influence your outlook on life more than anything else.

Human adventurers are extremely varied, from private eyes to blackhats, from knights to starship captains, from martial artists to doctors, from wizards to space marines — the world, indeed the universe, is at your fingertips!''',
    size='medium',
    luck=2,
    available_skills=['sport', 'climbing', 'swimming', 'running', '[crafting]', '[trivia]', '[gaming]',
                      '[scientific]', 'engineering'],
    exploits=[{'Name': 'Varied', 'Desc': '''Humans boast more variation within their species than most. Add 2 to any attribute, and add a further +1 to one other attribute (noted above).'''},
              {'Name': 'Explorers', 'Desc': '''Driven by an inquisitive, exploratory nature, Humans recharge their LUC pool every time they stand on a planet new to them.'''},
              {'Name': 'Enduring', 'Desc': '''Humans may not be the fastest or the strongest, but they are known for their resilience. Humans get +1 to their 1d6 die roll to shake off a temporary condition.'''}])

race_new_ogron = Race(
    name='Ogron',
    desc='''Ogrons stand 7' tall.  Towering masses of muscle, accompanied by green skin and bestial tusks, they so much resemble the ogres of fairytale and lore than humankind named them after the mythical creatures. Ogrons have a reputation for stupidity.  While it's certainly true that most of humankind outstrips the Ogron species in terms of intelligence and education, ogrons aren't quite as stupid as many expect – they, as a species, do manage to operate and build starships, after all.

Ogron adventurers tend to be mercenaries and soldiers.

Typical names (male and female): Lúrbag, Lugog, Gorrat, Ugbug, Bolglúk, Maudush, Radhur, Ugdush, Grishog.''',
    size='large',
    strength=2, endurance=2,
    available_skills=['carrying', 'hardy', 'bravery', 'intimidate'],
    exploits=[{'Name': 'Dull-witted', 'Desc': '''Although slow-witted, ogron minds are hard to penetrate. They gain a +4 bonus to MENTAL DEFENSE.'''},
              {'Name': 'Smelly', 'Desc': '''No matter what they do, Ogrons smell bad. They take a permanent -1d6 penalty to any attempts at stealth.'''},
              {'Name': 'Brawny', 'Desc': '''Ogrons increase their carrying capacity by 50%.'''},
              {'Name': 'Stronger with age', 'Desc': '''Unlike most species, Ogrons can continue to increase their STR attribute into old age.  Ancient Ogrons are incredibly strong.'''},
              {'Name': 'Strong', 'Desc': '''Ogrons are noted for their strength. When taking a new career, an Ogron may optionally exchange one of the listed four attribute increases for STR, as long as it doesn’t result in a duplicate attribute advancement.'''}])

race_new_spartan = Race(
    name='Spartan',
    desc='''Spartans were named after the mythological human legends because of their warrior-based culture. Aggressive, violent, quick to anger and easy to offend, a group of Spartans can empty a bar in minutes. Add in their love of heavy drinking and the sheer joy they get from combat, it's easy to see why Spartans are not the most popular of species. However, they do get frequently misunderstood – they are rarely bullies (indeed, they'd see it as cowardly to attack someone weaker).

Spartans excel as soldiers and other warriors. They abhor indirect conflict, and will tend to avoid careers which involve subterfuge or deception.

Typical names (male and female): Kevak, Deshe, Bra-el, G'Vera, Dracla, K'Ehleyr, Kellein, Kargan, Kalan, Adjur.''',
    size='medium',
    strength=1, agility=1, endurance=1,
    available_skills=['[combat]', 'intimidate', 'carousing'],
    exploits=[{'Name': 'Berserker', 'Desc': '''Spartans can enter a berserker rage by tasting their own blood when they are below half HEALTH. This grants them a +1d6 bonus to all attack rolls. The rage only ends when all foes are dead, or the Spartan is rendered unconscious or restored to above half HEALTH.'''},
              {'Name': 'Redundant organs', 'Desc': '''Spartans have a number of redundant organs and heal fairly rapidly. They can spend five minutes to heal 2d6 HEALTH once per day.'''},
              {'Name': 'Warlike', 'Desc': '''Spartans gain one bonus [combat] skill.'''}])

race_new_venetian = Race(
    name='Venetian',
    desc='''Venetians are a slim, hairless species, standing at roughly the same height as humans. They tend towards the ascetic, and, indeed, have a society which highly favors the monastic orders to which so many belong. The Venetian style of self-discipline and avoidance of indulgence gives the species a somewhat aloof demeanor which can be off-putting. Venetians are naturally psionic.

Many of the Venetian monastic orders, of which there are thousands, focus on the martial arts and self-discipline. For this reason, Venetians – while being pacifistic in nature – are often very skilled combatants.

Venetian adventurers tend to be priests, healers, and scientists.

Typical names (male and female): Ashonn, Branmer, Kozain, Kalier, Tereval, Rathell, Sinehan, Nerrat, Dukhon, Deerenn, Delon, Mayen.''',
    size='medium',
    agility=1, logic=2, luck=-2, psionics=3,
    available_skills=['reactions', 'acrobatics', 'perception', 'concentration', 'religion',
                      '[scientific]'],
    exploits=[{'Name': 'Naturally psionic', 'Desc': '''A society which integrates psionics from childhood, Venetians start play with one free psionic exploit.'''},
              {'Name': 'Acute hearing', 'Desc': '''Venetians have excellent hearing, and gain a +1d6 bonus to perception checks when sound is relevant.'''},
              {'Name': 'Learned', 'Desc': '''Venetians start with four species skills rather than three. The bonus (fourth) skill must be a [scientific] skill.'''},
              {'Name': 'Disciplined', 'Desc': '''The mental discipline of a venetian is such that they are completely immune to the Fatigued condition as long as they get 8 hours sleep per week. This is not a preferred situation, however.'''},
              {'Name': 'Long-lived', 'Desc': '''When creating a Venetian character, multiply their career lengths by 5.'''},
              {'Name': 'Logical', 'Desc': '''Venetians are noted for their intelligence and logic. When taking a new career, a Venetian may optionally exchange one of the listed four attribute increases for LOG, as long as it doesn’t result in a duplicate attribute advancement.'''}])

race_new_list = [race_new_android, race_new_borian, race_new_felan, race_new_human, race_new_ogron, race_new_spartan,
                 race_new_venetian]

for race in race_new_list:
    race.available_skills.sort()
    race.exploits.sort(key=lambda x: x['Name'])
