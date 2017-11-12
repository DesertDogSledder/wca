from lib.character import Race

# OLD races
race_old_grand_elf = Race(
    name='Grand Elf',
    desc='''Grand elves are an ancient race. Masters of gunpowder, there is nothing more awe-inspiring than the sight of ranks of grand elves lined up with their muskets in the driving rain, felling row after row of charging goblin hordes. Tall, pale, and serious, grand elves are strong believers in the good of the community being more important than that of the individual.

Grand elves are slightly taller and slimmer than humans, with a grave, stoic bearing. Their ears are pointed, and their faces tend towards the angular. They are immortal, and do not age past middle-age, although can still be slain by accident, illness, or violence.

Music is important to grand elves. Most are able to play one or more musical instruments, and singing comes naturally to them. Their music is beautiful and ethereal.

Grand elf adventurers tend to be musketeers, alchemists, and sailors.

Typical names (male and female): Nimrothor, Anduilas, Galmoth, Earros, Mabborn, Celelas, Mirairë, Glorgolfin, Lúfindel, Arwë.''',
    size='medium',
    agility=2, logic=2, luck=-2, magic=3,
    available_skills=['[musical]', 'alchemy', 'intimidate', 'law', 'leadership', 'muskets',
                      'pistols', 'sailing', 'swords'],
    exploits=[{'Name': 'Fey', 'Desc': '''Elves of all types are considered Fey.'''},
              {'Name': 'Magic sense', 'Desc': '''Grand elves can sense magic within 10' of them. They can intuitively sense the presence of magic, but not the power level, type, direction, or exact location.'''},
              {'Name': 'Meditation', 'Desc': '''Grand elves do not need to sleep. They may sometimes choose to meditate, instead, while their non-elven companions are sleeping, but this is not necessary.'''},
              {'Name': 'Naturally magical', 'Desc': '''Grand elves begin play with one free spell-path.'''},
              {'Name': 'Cultural weapon', 'Desc': '''Grand elves begin play with a free musket or pistol.'''},
              {'Name': 'Long-lived', 'Desc': '''When creating a Grand Elf character, multiply their career lengths by 5.'''},
              {'Name': 'Magical', 'Desc': '''Grand Elves are noted for their magic. When taking a new career, a Grand Elf may optionally exchange one of the listed four attribute increases for MAG, as long as it doesn't result in a duplicate attribute advancement.'''}])

race_old_human = Race(
    name='Human',
    desc='''There's a reasonably strong chance that you, the reader, are Human. You might be a little extra-human, with mechanical improvements (glasses, a hearing aid, maybe some genuine replacement parts) but when things boil down, you are a homo sapiens. This isn’t to say that Humans are not diverse—there is a wide range of cultures and peoples across the worlds of O.L.D., N.O.W., and N.E.W. —but all of them have 10 toes, two eyes, and so on. Where you are from and who raised you influence your outlook on life more than anything else.

Human adventurers are extremely varied, from private eyes to blackhats, from knights to starship captains, from martial artists to doctors, from wizards to space marines — the world, indeed the universe, is at your fingertips!''',
    size='medium',
    luck=2,
    available_skills=['sport', 'climbing', 'swimming', 'running', '[crafting]', '[trivia]', '[gaming]',
                      '[scientific]', 'engineering'],
    exploits=[{'Name': 'Varied', 'Desc': '''Humans boast more variation within their species than most. Add 2 to any attribute, and add a further +1 to one other attribute (noted above).'''},
              {'Name': 'Explorers', 'Desc': '''Driven by an inquisitive, exploratory nature, Humans recharge their LUC pool every time they take a wilderness journey of more than one week's length.'''},
              {'Name': 'Enduring', 'Desc': '''Humans may not be the fastest or the strongest, but they are known for their resilience. Humans get +1 to their 1d6 die roll to shake off a temporary condition.'''}])

race_old_mountain_dwarf = Race(
    name='Mountain Dwarf',
    desc='''Mountain dwarves are a sturdy folk who live in great mountain strongholds. They have a love of treasure, and great skill at mining and engineering. Sometimes gruff, they can be very serious about their work, but are amongst the world's greatest carousers.

An honorable race, mountain dwarves tend towards the serious-minded, although their reputation for sometimes excessive pride is not undeserved. Craftsmen, engineers, miners, metalworkers, stoneworkers – mountain dwarves are skilled with their hands, and most are equally skilled using weapons reminiscent of the tools of their trade. Hammers and axes, therefore, are common dwarven weapons.

Mountain dwarves, like most dwarves, are stocky and broad. They stand about 4 feet tall; the males almost invariably sport beards, while the females do not. They are stronger and tougher than humans, though they lack grace and agility. Mountain dwarves are mortal; they live for about 250 years on average.

A reputation for greed follows all mountain dwarves. Almost every member of the race is born with an innate appreciation of precious metals and rare gems, and much of their industry has historically been based around these things.

Mountain dwarf adventurers are usually warriors. They tend to shun magic, and have no innate natural ability.

Typical names (male and female): Kibur, Bruebur, Finor, Donor, Bomnor, Toin, Barin, Dwali, Gimlin, Babur.''',
    size='small',
    endurance=2, willpower=2,
    available_skills=['[crafting]', 'alchemy', 'appraisal', 'axes', 'engineering', 'carousing',
                      'hammers', 'mining'],
    exploits=[{'Name': 'Darksight', 'Desc': '''Mountain Dwarves can see in the dark to a distance of 60'.'''},
              {'Name': 'Iron constitution', 'Desc': '''Mountain Dwarves are not affected by non-magical poisons, with the exception of alcohol'''},
              {'Name': 'Sturdy', 'Desc': '''With a low center of gravity, it is hard to knock a dwarf down. Any attempt to do so suffers a -2d6 die penalty.'''},
              {'Name': 'Earthy', 'Desc': '''Mountain Dwarves automatically know the secret of earth, although Dwarves with MAGIC attributes are rare.'''},
              {'Name': 'Long-lived', 'Desc': '''When creating a Mountain Dwarf character, multiply their career lengths by 3.'''},
              {'Name': 'Stubborn', 'Desc': '''Mountain Dwarves are noted for their stubborn demeanour. When taking a new career, a Mountain Dwarf may optionally exchange one of the listed four attribute increases for WIL, as long as it doesn't result in a duplicate attribute advancement.'''}])

race_old_ogre = Race(
    name='Ogre',
    desc='''Ogres stand 7' tall. Towering masses of muscle, accompanied by green skin and bestial tusks, ogres have a well-earned reputation for stupidity.

Ogres have greasy, lice-ridden black hair, and are often covered in warts and other blemishes. They smell terrible, and an indescribable odor reminiscent of a mixture of stale sweat and rotting food.

Ogres are technically goblinoids, distantly related to orcs and goblins, but some giant blood was added in the long past. They are brutish, prone to violence, and tend to act on instinct.

Ogre adventurers tend to be mercenaries and soldiers. Tribal in nature, those which have joined adventuring outfits tend to curb their worst instincts and possess slightly higher intelligence than their wilder brethren.

Typical names (male and female): Lúrbag, Lugog, Gorrat, Ugbug, Bolglúk, Maudush, Radhur, Ugdush, Grishog.''',
    size='large',
    strength=3, endurance=3,
    available_skills=['brawling', 'bravery', 'carrying', 'hardy', 'intimidate', '[melee weapons]'],
    exploits=[{'Name': 'Thick hide', 'Desc': '''Ogres are extremely tough, with leathery skin. They gain 2 natural SOAK to physical attacks'''},
              {'Name': 'Smelly', 'Desc': '''No matter what they do, ogrons smell bad. They take a permanent -1d6 penalty to any attempts at stealth.'''},
              {'Name': 'Darksight', 'Desc': '''Ogres can see in the dark as though it were normal daylight.'''},
              {'Name': 'Acid blood', 'Desc': '''Ogres have acidic blood. In addition to gaining an additional 5 SOAK (acid), melee attackers which cause more than 10 slashing or piercing damage in a single blow take 1d6 acid damage from the blood splash.'''},
              {'Name': 'Strong', 'Desc': '''Ogres are noted for their strength. When taking a new career, an Ogre may optionally exchange one of the listed four attribute increases for STR, as long as it doesn’t result in a duplicate attribute advancement.'''}])

race_old_orc = Race(
    name='Orc',
    desc='''Orcs are tribal, aggressive, violent, quick to anger and easy to offend. Strong and tough, orcs can be a little slow on the uptake.

The warlike orcs have a barbaric, strength-based society. Orcs venerate warriors to the extreme, and include violence in most social rituals. Orcs believe that those who die gloriously in battle are guaranteed an afterlife of drinking, carousing, and fighting.

Orcs tend to be slightly taller, stronger, and broader than humans, with green skin and black hair. Their ears are pointed, and some historians claim they are an ancient corrupted mockery of the elves. Like ogres, they are goblinoids, perhaps with elven lineage in the distant past.

Orcs tend to be crafty and cunning, both on the battlefield and elsewhere. They are adept at crafting weapons, and wield many custom blades with unusual shapes. Equally, they are at home underground.

Orcs excel as soldiers and other warriors.

Typical names (male and female): Kevak, Deshe, Bra-el, G'Vera, Dracla, K'Ehleyr, Kellein, Kargan, Kalan, Adjur''',
    size='medium',
    strength=2, agility=2, intuition=3,
    available_skills=['[melee weapons]', 'blacksmithing', 'carousing', 'hunting', 'intimidation', 'mining',
                      'running', 'tactics', 'tracking'],
    exploits=[{'Name': 'Glory', 'Desc': '''Orcs take pleasure in battle, and pride in their wounds. When reduced to below half HEALTH, they gain a +1d6 die bonus to attack rolls.'''},
              {'Name': 'Darksight', 'Desc': '''Orcs can see clearly in the dark as though it were daylight. However, bright sunlight hurts their eyes, inflicting a -2 DEFENSE penalty.'''},
              {'Name': 'Bloodlust', 'Desc': '''Once per day an orc can drink fresh blood to recover 2d6 HEALTH. This takes an action. The blood must come from a creature slain in the last hour.'''}])

race_old_smallfolk = Race(
    name='Smallfolk',
    desc='''Smallfolk are welcome in most places. Standing at about 3' in height, with ruddy cheeks and simple clothing, they have a reputation for good cheer and friendliness. Homebodies, smallfolk are agile and resilient, and are good with their hands. They make excellent farmers and shopkeepers.

Smallfolk favor simple clothes in bright colors. They tend towards the stout (though not nearly so much as dwarves), and live to over 100 years of age. They boast pointed ears, although not as pronounced as those of the elves, and frequently hidden by their curly hair.

Jovial in nature, it can be hard to make a smallfolk take offence. Smallfolk will put a positive spin on almost anything, a trait which endears them to many. They are as generous as they are jovial, and always happy to welcome others to their homes: indeed, entertaining others is a prime instinct for the smallfolk.

Many view the smallfolk as weak, sometimes even cowardly. While it is true that the race does not tend towards violence, a cornered smallfolk will defend his or her friends to the death. In truth, smallfolk are the most courageous of all races.

Typical names (male and female): Dobur, Thrari, Kirin, Borin, Boli, Filin, Gimnor, Thrarin, Dwain, Dolo, Kibur.''',
    size='small',
    agility=2, charisma=2, luck=2, magic=1,
    available_skills=['[crafting]', 'farming', 'fishing', 'appraisal', 'cooking', 'brewing', 'slings', 'stealth',
                      'diplomacy', 'bluffing'],
    exploits=[{'Name': 'Stubborn', 'Desc': '''Smallfolk are difficult to enchant. They gain a +5 bonus to their MENTAL DEFENSE.'''},
              {'Name': 'Evasion', 'Desc': '''Smallfolk are nimble and adept at dodging. They gain a +5 bonus to their DEFENSE.'''}])

race_old_sylvan_elf = Race(
    name='Sylvan Elf',
    desc='''Wild, fierce, and at one with nature, sylvan elves live in the woodlands and forests, armed with bow and spear. Sylvan elves can be xenophobic at times, and are well-trained in the arts of both war and nature.

Sylvan elves are slim, like their grand elf cousins, but much shorter, at about 5-feet in height. With pointed ears, their skin tones tend to be dark, their hair brown, black, or sometimes with a greenish tinge. Unlike the grand elves, sylvan elves are not immortal. However, they have extremely long life spans of up to two-thousand years.

Naturally magical, sylvan elves know the words and spells of the forest. They are known to talk to plants, or to command animals. At home in the branches of trees, sylvan elves are also adept at hiding their presence, and more than a few unwary intruders have found themselves ambushed upon entering sylvan woodlands.

Sylvan elf adventurers tend to be priests, rangers, and druids.

Typical names (male and female): Ashonn, Branmer, Kozain, Kalier, Tereval, Rathell, Sinehan, Nerrat, Dukhon, Deerenn, Delon, Mayen.''',
    size='medium',
    agility=2, endurance=2, magic=3,
    available_skills=['climbing', 'running', 'survival', 'tracking', 'animal handling', 'herbalism', 'bows', 'nature',
                      'stealth'],
    exploits=[{'Name': 'Fey', 'Desc': '''Elves of all types are considered Fey.'''},
              {'Name': 'Nature affinity', 'Desc': '''All sylvan elves know either the secret of plants or the secret of beasts.'''},
              {'Name': 'Unimpeded', 'Desc': '''Sylvan elves are not affected or slowed by difficult terrain while outdoors.'''},
              {'Name': 'Tree-dwellers', 'Desc': '''Sylvan elves gain a climb speed equal to their regular speed.'''},
              {'Name': 'Trance', 'Desc': '''Sylvan elves do not need to sleep. They may choose to meditate, instead, while their non-elven companions are sleeping, but this is not necessary.'''},
              {'Name': 'Healthy', 'Desc': '''Sylvan elves are completely immune to illness and disease of a non-magical nature.'''},
              {'Name': 'Long-lived', 'Desc': '''When creating a Sylvan Elf character, multiply their career lengths by 4.'''},
              {'Name': 'Agile', 'Desc': '''Sylvan Elves are noted for their dexterity. When taking a new career, a Sylvan Elf may optionally exchange one of the listed four attribute increases for AGI, as long as it doesn’t result in a duplicate attribute advancement.'''}])

race_old_list = [race_old_grand_elf, race_old_human, race_old_mountain_dwarf, race_old_ogre, race_old_orc,
                 race_old_smallfolk, race_old_sylvan_elf]


for race in race_old_list:
    race.available_skills.sort()
    race.exploits.sort(key=lambda x: x['Name'])
