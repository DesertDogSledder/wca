from lib.character import Race

# OLD races
race_old_clockman = Race(
    name='Clockman',
    desc='''These sentient clockwork people tick quietly, an unnerving noise which can be heard by those who stand '''
         '''close to them. Made completely of clockwork, their bodies are filled with cogs and gears, and they move '''
         '''with a certain stiffness, their faces stuck in a single expression.\n\n'''
         '''A technically proficient scavenger race, clockmen have the unnerving ability to use their surroundings '''
         '''to repair themselves. Damage a clockman, and it might pick up a nearby knife or fork, spare part, or '''
         '''random trinket and use it to replace a damaged component. They can even use organic components, meaning '''
         '''that many of them look particularly gruesome.\n\n'''
         '''Clockmen need order and routine; they despise chaos and disorder. In a hierarchy, they need to know the '''
         '''exact structure and their place within it, and will not deviate from that chain, for good or ill. Even '''
         '''simply entering an untidy room will distress a clockman, who will likely being tiding it up immediately. '''
         '''If they find broken objects, they feel the need to repair them.''',
    size='medium',
    strength=1, logic=2, willpower=2,
    available_skills=['engineering', 'astronomy', 'law', 'history', 'medicine'],
    exploits=[{'Name': 'Clockwork',
               'Desc': '''As clockwork automatons, clockmen do not need to eat or breathe. They do, however, need to '''
               '''sleep, in a fashion, as their gears wind down. Like other automatons they are vulnerable '''
               '''(1d6) to electricity and in sci-fi settings (2d6) to ion damage. They are immune to attacks which ''' 
               '''use MENTAL DEFENSE. Like most automatons, clockmen cannot have a MAG (or PSI or CHI) score, and '''
               '''cannot spend LUC dice.'''},
              {'Name': 'Repair',
               'Desc': '''Once per day clockmen can repair themselves in a patchwork fashion to the amount half '''
               '''their normal maximum HEALTH by spending two actions and resources from their environment.'''},
              {'Name': 'Wind-up',
               'Desc': '''Clockmen can spend two actions winding themselves up. For the next minute, they move at a '''
               '''faster speed (making a rapid clockwork ticking noise while they do so), gaining an extra action '''
               '''each turn, but at the end of the minute they wind down and cannot act or move for one hour.'''},
              {'Name': 'Internal clock',
               'Desc': '''Clockmen track the passage of time accurately, to the very second.'''}])

race_old_danuki = Race(
    name='Danuki',
    desc='''Danuki are spirit animals, at home in brush, hills, and ditches. Danuki are a small and very cowardly '''
         '''race. They are peerless shapechangers but rarely have an agenda with their change of forms; pranks '''
         '''and laughter are often enough for them.\n\n'''
         '''Danuki are small, about 2’7”, furred humanoids that are very animal-like, looking like a Japanese '''
         '''raccon-dog walking on its hind legs. Their bodies appear rotund and short limbed; much of it is '''
         '''actually fur. They have fluffy tails, and when a Danuki fails a disguise attempt, the first sign of is '''
         '''often that their tail starts poking out.''',
    size='small',
    agility=2, logic=2, luck=2, magic=2,
    available_skills=['bluffing', 'disguise', 'insight', 'stealth', 'thievery', 'alchemy'],
    exploits=[{'Name': 'Masterful shapechanger',
               'Desc': '''A Danuki can assume the form of another creature. The new form must be small-sized and '''
               '''have a Maximum Dice Pool equal to or lower than the Danuki. It takes the Danuki a full round to '''
               '''change shape, and it can only do so once per day. The transformation lasts until the Danuki ends '''
               '''it, or until it suffers the Afraid condition (Danuki cannot maintain a shape when feeling fear). '''
               '''The Danuki retains its own mental attributes, and its own Maximum Dice Pool, but gains any other '''
               '''physical characteristics of the new shape.'''},
              {'Name': 'Cowardly',
               'Desc': '''Danuki are natural cowards. They must roll a 6 to shake off the Afraid condition. All '''
               '''danuki have a phobia, usually against a type of predator animal , but sometimes against a natural '''
               '''phenomenon. In addition, all danuki are phobic against getting caught; this triggers when '''
               '''grappled, entangled, cuffed, bound, or locked up. When in the presence of their phobia, danuki '''
               '''become Afraid. You should randomly select a phobia, or choose one with the GM’s approval.'''}])

race_old_deepling = Race(
    name='Deepling',
    desc='''Deeplings are a race of cursed beings, corrupted grand elves crossed with demonic ancestry. Hailing from '''
         '''a magically-bereft nation, Deepling society is science-focused. In addition to the obvious horns and '''
         '''tails, a Deepling's eyes are a deep solid yellow. Skin color varies from tan to a reddish hue.\n\n'''
         '''Deeplings are widely envied for their progress in industry and technology. Their country has a fully '''
         '''functioning steam railroad, powerful steam-powered ships, and is known for its statesmen, inventors, '''
         '''and scholars.\n\n'''
         '''Deeplings are fiercely opposed to superstition. Magic left them long ago, and they have turned their '''
         '''back on old beliefs and religion. Deeplings believe that technology can achieve anything that magic - '''
         '''either mortal or divine - can.''',
    size='medium',
    agility=2, charisma=2, logic=2, magic=-99,
    available_skills=['[crafting]', 'bluffing', 'engineering', 'sailing', 'rapiers', 'rifles', 'pistols'],
    exploits=[{'Name': 'Natural weapons',
               'Desc': '''A Deepling's horns and tail make for dangerous natural weapons. A Deepling's natural '''
               '''damage is 2d6 rather than the 1d6 its size would normally allow, and becomes piercing damage.'''},
              {'Name': 'Superior darksight',
               'Desc': '''Deeplings can see in the dark as though it were daylight.'''},
              {'Name': 'Fire resistance',
               'Desc': '''Deeplings have a natural SOAK 5 (fire). At old age, this increases to 10.'''},
              {'Name': 'Antimagic',
               'Desc': '''So averse to magic are they, Deeplings actually naturally suppress magic in their '''
               '''presence. Deeplings get +4 DEFENSE against any magical attacks. However, they can never have a '''
               '''MAG attribute.'''}])

race_old_earth_nymph = Race(
    name='Earth Nymph',
    desc='''These nymphs arise from stone and soil in their many forms. The most common clan are the oreads, who '''
         '''embody mountains and caves. Earth nymphs can just as easily hail from valleys, particular stones, or '''
         '''underground mineral structures. Some even purport to be born of the stars.''',
    size='medium',
    endurance=2, willpower=1, magic=3,
    available_skills=['nature', 'religion', '[magical]', 'dancing', 'singing'],
    exploits=[{'Name': "Stone's fortitude",
               'Desc': '''You have natural SOAK 5 to slashing damage.'''},
              {'Name': 'Stone step',
               'Desc': '''Once per day you may pass through up to 30’ of natural stone. Worked stone blocks this '''
               '''ability.'''},
              {'Name': 'Voice of nature',
               'Desc': '''You know the secret of earth.'''},
              {'Name': 'Fey',
               'Desc': '''As a fey creature, you can sense the presence of (but not the location or type of) magic '''
               '''within 10’, and are vulnerable (1d6) to cold iron.'''},
              {'Name': 'Fey grace',
               'Desc': '''You are immune to the Charmed condition.'''}])

race_old_forest_nymph = Race(
    name='Forest Nymph',
    desc='''Forest nymphs occur from woodlands and vegetation. Hamadryads are the spirits of individual trees, '''
         '''and dryads are their aggregate forests. Whether they are distinct from or identical with the fey '''
         '''creature that shares their name is anyone’s guess. Similar clans include flowers (anthousai), groves '''
         '''(alseides), winds and breezes (aurae), and even the cardinal directions.''',
    size='medium',
    intuition=1, agility=2, magic=3,
    available_skills=['nature', 'religion', '[magical]', 'stealth', 'climbing', 'dancing', 'singing'],
    exploits=[{'Name': 'Tree stride',
               'Desc': '''Once per turn, you can use an action to step magically into one adjacent living tree '''
               '''and emerge from a second living tree within 60 feet of the first, appearing in an unoccupied space '''
               '''within 5 feet of the second tree. Both trees must be large-sized or bigger.'''},
              {'Name': 'Voice of nature',
               'Desc': '''You know the secret of plants.'''},
              {'Name': 'Fey',
               'Desc': '''As a fey creature, you can sense the presence of (but not the location or type of) magic '''
               '''within 10’, and are vulnerable (1d6) to cold iron.'''},
              {'Name': "Fey's grace",
               'Desc': '''You are immune to the Charmed condition.'''},
              {'Name': "Nature's step",
               'Desc': '''You are not affected by difficult terrain caused by forest, brush, undergrowth, or similar '''
               '''natural features; neither do you leave tracks or trace of your passing.'''}])

race_old_goblin = Race(
    name='Goblin',
    desc='''Goblins are small goblinoids. Nasty, cunning, and scrappy, with poor hygiene, these creatures are looked '''
         '''down upon by most sentient races. Goblins come from the deep, living underground in dark caverns in '''
         '''large packs. They stand about 3 feet tall, with green skin and scrawny bodies. Their jagged, yellow '''
         '''teeth are suited to tearing meat apart, and their yellow eyes are suited to seeing in the darkness of '''
         '''deep caverns and caves.''',
    size='small',
    agility=2, intuition=2,
    available_skills=['thievery', 'climbing', 'stealth', 'survival', 'mining', 'running', 'knives'],
    exploits=[{'Name': 'Pack attack',
               'Desc': '''Goblins work best in groups, using numbers to compensate for their small size. Goblins '''
               '''gain +1d6 to attack a target for every ally also adjacent to the target.'''},
              {'Name': 'Darksight',
               'Desc': '''Goblins can see in darkness as though it were normal light. They are vulnerable to bright '''
               '''light, however, and lose their Natural Cunning ability in direct sunlight, and cannot shake off '''
               '''the Blind status if it is caused by bright light (note that temporary conditions automatically '''
               '''end after 5 minutes).'''},
              {'Name': 'Natural cunning',
               'Desc': '''Although not known for their intellect, goblins do possess a natural instinct. They gain '''
               '''+1d6 to INITIATIVE checks.'''},
              {'Name': 'Scavengers',
               'Desc': '''Goblins can use any organic material as food, no matter how strange or rotten, and as such '''
               '''are immune to poisons.'''},
              {'Name': 'Snatch',
               'Desc': '''Using a melee attack, a goblin can steal a small-sized or smaller item from an adjacent '''
               '''target, even in combat.'''},
              {'Name': 'Between the legs',
               'Desc': '''A goblin can freely move through the squares of large sized or larger creatures which have '''
               '''two or more legs.'''}])

race_old_grand_elf = Race(
    name='Grand Elf',
    desc='''Grand elves are an ancient race. Masters of gunpowder, there is nothing more awe-inspiring than the '''
         '''sight of ranks of grand elves lined up with their muskets in the driving rain, felling row after row of '''
         '''charging goblin hordes. Tall, pale, and serious, grand elves are strong believers in the good of the '''
         '''community being more important than that of the individual.\n\n'''
         '''Grand elves are slightly taller and slimmer than humans, with a grave, stoic bearing. Their ears are '''
         '''pointed, and their faces tend towards the angular. They are immortal, and do not age past middle-age, '''
         '''although can still be slain by accident, illness, or violence.\n\n'''
         '''Music is important to grand elves. Most are able to play one or more musical instruments, and singing '''
         '''comes naturally to them. Their music is beautiful and ethereal.\n\n'''
         '''Grand elf adventurers tend to be musketeers, alchemists, and sailors.\n\n'''
         '''Typical names (male and female): Nimrothor, Anduilas, Galmoth, Earros, Mabborn, Celelas, Mirairë, '''
         '''Glorgolfin, Lúfindel, Arwë.''',
    size='medium',
    agility=2, logic=2, luck=-2, magic=3,
    available_skills=['[musical]', 'alchemy', 'intimidate', 'law', 'leadership', 'muskets',
                      'pistols', 'sailing', 'swords'],
    exploits=[{'Name': 'Fey',
               'Desc': '''Elves of all types are considered Fey.'''},
              {'Name': 'Magic sense',
               'Desc': '''Grand elves can sense magic within 10' of them. They can intuitively sense the presence '''
               '''of magic, but not the power level, type, direction, or exact location.'''},
              {'Name': 'Meditation',
               'Desc': '''Grand elves do not need to sleep. They may sometimes choose to meditate, instead, while '''
               '''their non-elven companions are sleeping, but this is not necessary.'''},
              {'Name': 'Naturally magical',
               'Desc': '''Grand elves begin play with one free spell-path.'''},
              {'Name': 'Cultural weapon',
               'Desc': '''Grand elves begin play with a free musket or pistol.'''},
              {'Name': 'Long-lived',
               'Desc': '''When creating a Grand Elf character, multiply their career lengths by 5.'''},
              {'Name': 'Magical',
               'Desc': '''Grand Elves are noted for their magic. When taking a new career, a Grand Elf may '''
               '''optionally exchange one of the listed four attribute increases for MAG, as long as it doesn't '''
               '''result in a duplicate attribute advancement.'''}])

race_old_human = Race(
    name='Human',
    desc="There's a reasonably strong chance that you, the reader, are Human. You might be a little extra-human, "
         "with mechanical improvements (glasses, a hearing aid, maybe some genuine replacement parts) but when things "
         "boil down, you are a homo sapiens. This isn’t to say that Humans are not diverse—there is a wide range of "
         "cultures and peoples across the worlds of O.L.D., N.O.W., and N.E.W. —but all of them have 10 toes, two "
         "eyes, and so on. Where you are from and who raised you influence your outlook on life more than anything "
         "else.\n\n"
         "Human adventurers are extremely varied, from private eyes to blackhats, from knights to starship captains, "
         "from martial artists to doctors, from wizards to space marines — the world, indeed the universe, is at "
         "your fingertips!",
    size='medium',
    luck=2,
    available_skills=['any'],
    exploits=[{'Name': 'Varied',
               'Desc': '''Humans boast more variation within their species than most. Add 2 to any attribute, and '''
               '''add a further +1 to one other attribute (noted above).'''},
              {'Name': 'Explorers',
               'Desc': '''Driven by an inquisitive, exploratory nature, Humans recharge their LUC pool every time '''
               '''they take a wilderness journey of more than one week's length.'''},
              {'Name': 'Enduring',
               'Desc': '''Humans may not be the fastest or the strongest, but they are known for their resilience. '''
               '''Humans get +1 to their 1d6 die roll to shake off a temporary condition.'''}])

race_old_flint_dwarf = Race(
    name='Flint Dwarf',
    desc='''Crafted from an adaptable, yet flaky stone, Flint Dwarves are physically strong but emotionally '''
         '''volatile. Flint Dwarves now dwell in isolated pockets of wilderness not claimed by anyone else and have '''
         '''come to be known as “wild dwarves.”\n\n'''
         '''The Flint Dwarves were instilled with the spirit of adaptability and survivability. They were given a '''
         '''jovial temperament to serve as the mediators between dwarven tribes, but their mistreatment at the '''
         '''hands of their kin has made the flint dwarves volatile and wild. While they are leaner and less sturdy '''
         '''than other dwarves, they are still strong and stout-hearted. Yet, some dwarves were wary of their '''
         '''slim-featured cousins, and decided they did not want the odd-looking, talkative flint dwarves to be '''
         '''their emissaries to human lands, and banished them.\n\n'''
         '''Today, Flint Dwarves can be found living in small stone huts in the wild areas of the world, and their '''
         '''unkempt appearance suggests they have adapted well to their new homes.''',
    size='small',
    strength=2, willpower=1, charisma=1,
    available_skills=['navigation', 'carousing', 'survival', 'negotiating', 'linguistics', 'farming'],
    exploits=[{'Name': 'Darksight',
               'Desc': '''Like most dwarves, Flint Dwarves can see in the dark to a distance of 60'.'''},
              {'Name': 'Survivalist',
               'Desc': '''It's hard to kill a Flint Dwarf. They do not fall unconscious when at negative HEALTH '''
               '''(although they still form a death pool as normal) and are do not suffer conditions from '''
               '''environmental effects. Additionally, they are immune to all diseases.'''},
              {'Name': 'Inner fire',
               'Desc': '''Flint Dwarves gain +5 to all DEFENSEs against magical effects.'''}])

race_old_jade_dwarf = Race(
    name='Jade Dwarf',
    desc='''In many lands, jade is valued as protection against corruption and disease. Jade Dwarves were created '''
         '''from this stone as personification of this ability to withstand foul energies. Sometimes called '''
         '''“celestial” or “exalted,” Dade Dwarves are rare and their holds are always found bordering regions that '''
         '''are cursed, overrun with undead or fiends, or tainted in some other way. They are almost otherworldly '''
         '''in nature and consider themselves the supreme guardians of civilization and all that is good.\n\n'''
         '''Beautiful is not a word commonly associated with dwarves, but it is embodied in the Jade Dwarves and '''
         '''everything they create. Whilst most craftsdwarves’ art favors functionality over form, Jade Dwarves '''
         '''approach all their creations with an equal measure of beauty. Jade Dwarf halls are immense structures '''
         '''of unparalleled splendor.\n\n'''
         '''Jade Dwarves view the people of the world as members of their clan, and they are willing to lay down '''
         '''their lives for their family. Their society teaches that even the most depraved mortal can be redeemed, '''
         '''but that monsters and beasts are beyond salvation.\n\n'''
         '''A Jade Dwarf's skin can range from mint green to green-grey, and their dark eyes have no pupils. Their '''
         '''hair varies from brown to grey, but can also be streaked with green, or totally dark green if they are '''
         '''member of a noble house.''',
    size='small',
    charisma=2, logic=1, willpower=1,
    available_skills=['swords', '[social]', 'religion', 'medicine', '[artistic]', 'appraisal'],
    exploits=[{'Name': 'Darksight',
               'Desc': '''Like most dwarves, Jade Dwarves can see in the dark to a distance of 60'.'''},
              {'Name': 'Incorruptible body',
               'Desc': '''Jade Dwarves are immune to non-magical diseases.'''},
              {'Name': 'Exalted',
               'Desc': '''Jade Dwarves can sense the presence of (but not the direction or exact location of the '''
               '''Evil virtue within 60'.'''},
              {'Name': 'Healing touch',
               'Desc': '''A Jade Dwarf can heal by touch, automatically granting 2d6 HEALTH with a single action. '''
               '''This same touch can be used to do 2d6 holy damage to the undead, a spirit, or any creature with '''
               '''the Evil virtue.'''}])

race_old_minotaur = Race(
    name='Minotaur',
    desc='''Imposing figures with the head of a bull and the body of a man, minotaurs are powerful, proud creatures. '''
         '''Typically the size and build of a tall, powerful human, minotaurs are incredible sailors, using their '''
         '''innate navigation prowess to sail the high seas. Minotaur pirates are feared, and Grand Elves '''
         '''traditionally have an enmity with the race, hunting down and bringing such pirates to justice.\n\n'''
         '''Minotaurs are arrogant, certain of their own superiority. However, they are also loyal - a minotaur will '''
         '''never break its word. Minotaurs are fond of tridents and nets, although many also choose to wield large '''
         '''and powerful axes. A minotaur will traditionally wear a kilt and a breastplate of iron or bronze.''',
    size='medium',
    strength=2, intuition=2, endurance=1, reputation=1,
    available_skills=['navigation', 'sailing', 'brawling', 'axes', 'polearms', 'tracking', 'scent'],
    exploits=[{'Name': 'Horns',
               'Desc': '''A minotaur has horns which can be used in combat. The minotaur’s unarmed (natural) damage '''
               '''increases by +1d6 and becomes piercing damage.'''},
              {'Name': 'Charge',
               'Desc': '''Minotaurs gain the Charge exploit for free.'''},
              {'Name': 'Direction sense',
               'Desc': '''A minotaur always knows which direction is which, and how deep it is below ground or how '''
               '''far it is above ground. A minotaur never becomes lost when travelling.'''},
              {'Name': 'Stoic',
               'Desc': ''' Minotaurs are honor-bound and brought up to never show pain. When taking a new career, a '''
               '''Minotaur may optionally exchange one of the listed four attribute increases for END, as long as it '''
               '''doesn’t result in a duplicate attribute advancement.'''}])

race_old_mountain_dwarf = Race(
    name='Mountain Dwarf',
    desc='''Mountain dwarves are a sturdy folk who live in great mountain strongholds. They have a love of treasure, '''
         '''and great skill at mining and engineering. Sometimes gruff, they can be very serious about their work, '''
         '''but are amongst the world's greatest carousers.\n\n'''
         '''An honorable race, mountain dwarves tend towards the serious-minded, although their reputation for '''
         '''sometimes excessive pride is not undeserved. Craftsmen, engineers, miners, metalworkers, stoneworkers – '''
         '''mountain dwarves are skilled with their hands, and most are equally skilled using weapons reminiscent of '''
         '''the tools of their trade. Hammers and axes, therefore, are common dwarven weapons.\n\n'''
         '''Mountain dwarves, like most dwarves, are stocky and broad. They stand about 4 feet tall; the males '''
         '''almost invariably sport beards, while the females do not. They are stronger and tougher than humans, '''
         '''though they lack grace and agility. Mountain dwarves are mortal; they live for about 250 years on '''
         '''average.\n\n'''
         '''A reputation for greed follows all mountain dwarves. Almost every member of the race is born with an '''
         '''innate appreciation of precious metals and rare gems, and much of their industry has historically been '''
         '''based around these things.\n\n'''
         '''Mountain dwarf adventurers are usually warriors. They tend to shun magic, and have no innate natural '''
         '''ability.\n\n'''
         '''Typical names (male and female): Kibur, Bruebur, Finor, Donor, Bomnor, Toin, Barin, Dwali, Gimlin, '''
         '''Babur.''',
    size='small',
    endurance=2, willpower=2,
    available_skills=['[crafting]', 'alchemy', 'appraisal', 'axes', 'engineering', 'carousing',
                      'hammers', 'mining'],
    exploits=[{'Name': 'Darksight',
               'Desc': '''Mountain Dwarves can see in the dark to a distance of 60'.'''},
              {'Name': 'Iron constitution',
               'Desc': '''Mountain Dwarves are not affected by non-magical poisons, with the exception of alcohol'''},
              {'Name': 'Sturdy',
               'Desc': '''With a low center of gravity, it is hard to knock a dwarf down. Any attempt to do so '''
               '''suffers a -2d6 die penalty.'''},
              {'Name': 'Earthy',
               'Desc': '''Mountain Dwarves automatically know the secret of earth, although Dwarves with MAGIC '''
               '''attributes are rare.'''},
              {'Name': 'Long-lived', 'Desc': '''When creating a Mountain Dwarf character, multiply their career '''
               '''lengths by 3.'''},
              {'Name': 'Stubborn', 'Desc': '''Mountain Dwarves are noted for their stubborn demeanour. When taking '''
               '''a new career, a Mountain Dwarf may optionally exchange one of the listed four attribute increases '''
               '''for WIL, as long as it doesn't result in a duplicate attribute advancement.'''}])

race_old_night_elf = Race(
    name='Night Elf',
    desc='''Their pale white skin reflects the moonlight. Their eyes are full of cruelty and deceit. They stalk the '''
         '''night, the face of treachery, at one with the darkness - assassins, necromancers and foul priests. The '''
         '''night elves are rightly feared in all civilized lands, and their spired citadels given wide berth.\n\n'''
         '''Night elves are steeped in treachery; lies and deception are, to them, as natural as breathing. Life '''
         '''itself has little value, and the lives of inferior races have none. Night elves, like their grand elf '''
         '''cousins, were once no different to the sylvan elves of the woods and forests. When the sorcery and '''
         '''gunpowder cities of the grand elves arose, the night elves were but a prominent house. Politics, '''
         '''divisions, and rivalries took their course, and night elves today live apart from their cousins, feared '''
         '''and hated.\n\n'''
         '''Lovers of darkness, worshipers of the moon, night elves are tall, thin, and have pale, white skin the '''
         '''color of milk. Their eyes are coal-black, and their hair - when not decorated or dyed - is the purest '''
         '''white.''',
    size='medium',
    agility=1, intuition=1, charisma=1, magic=1,
    available_skills=['stealth', 'alchemy', 'thievery', 'bluffing', 'insight', 'swords', 'herbalism', 'creation'],
    exploits=[{'Name': 'Darksight',
               'Desc': '''Night Elves have superior darksight, able to see in darkness as though it were daylight.'''},
              {'Name': 'Night affinity',
               'Desc': '''All Night Elves know the secret of shadow. In dim light or darker, Night Elves can become '''
               '''invisible for one minute once per day.'''},
              {'Name': 'Deceitful',
               'Desc': '''When night elves make CHA checks to deceive, the dice pool is considered an exploding dice '''
               '''pool.'''},
              {'Name': 'Poisoners',
               'Desc': '''Accustomed to handling poison, night elves have a natural SOAK 10 (poison). Additionally, '''
               '''at-will, they can add the poison damage type to their melee weapons, as long as they are wielding '''
               '''the weapon themself.'''}])

race_old_obsidian_dwarf = Race(
    name='Obsidian Dwarf',
    desc='''The extremely tough and durable obsidian dwarves were created with hearts of basalt and magma flowing '''
         '''through their veins. They were the first dwarves, but the Creator abandoned them in the primordial '''
         '''fires, considering them a failed experiment.\n\n'''
         '''All obsidian dwarves practice rituals that humans would call cannibalism. In its purest form, the Rites '''
         '''of Consumption honor the fallen. Though the Rites are often misunderstood, obsidian dwarves do not eat '''
         '''the flesh of intelligent creatures as an act of evil or intimidation; it is their way of honoring life, '''
         '''death, and rebirth. Obsidian dwarves have no grave sites; family members are consumed by their clan and '''
         '''their stony bones are displayed in their hall.\n\n'''
         '''An obsidian dwarf's black skin is perfectly smooth and glassy, and flickers beautifully in firelight. '''
         '''Their eyes reflect their fiery heritage, like black coals or scarlet embers. Their hair may be wild and '''
         '''tangled, but can be dreadlocked, singed by fire, or ritually burned away.''',
    size='small',
    intuition=2, logic=2,
    available_skills=['religion', 'history', 'intimidation', 'knives', 'alchemy'],
    exploits=[{'Name': 'Darksight',
               'Desc': '''Like most dwarves, obsidian dwarves can see in the dark to a distance of 60'.'''},
              {'Name': 'Magma born',
               'Desc': '''Obsidian dwarves are immune to fire and are immune to the effects of hot environments.'''},
              {'Name': 'Obsidian skin',
               'Desc': '''An obsidian's dwarf's glassy skin is surprisingly hard, giving the dwarf +4 natural SOAK.'''},
              {'Name': 'Secret of fire',
               'Desc': '''Obsidian dwarves automatically know the secret of fire.'''},
              {'Name': 'Cold sensitivity',
               'Desc': '''Obsidian dwarves suffer from vulnerability 1d6 (cold).'''}])

race_old_ogre = Race(
    name='Ogre',
    desc='''Ogres stand 7' tall. Towering masses of muscle, accompanied by green skin and bestial tusks, ogres have '''
         '''a well-earned reputation for stupidity.\n\n'''
         '''Ogres have greasy, lice-ridden black hair, and are often covered in warts and other blemishes. They '''
         '''smell terrible, and an indescribable odor reminiscent of a mixture of stale sweat and rotting food.\n\n'''
         '''Ogres are technically goblinoids, distantly related to orcs and goblins, but some giant blood was added '''
         '''in the long past. They are brutish, prone to violence, and tend to act on instinct.\n\n'''
         '''Ogre adventurers tend to be mercenaries and soldiers. Tribal in nature, those which have joined '''
         '''adventuring outfits tend to curb their worst instincts and possess slightly higher intelligence than '''
         '''their wilder brethren.\n\n'''
         '''Typical names (male and female): Lúrbag, Lugog, Gorrat, Ugbug, Bolglúk, Maudush, Radhur, Ugdush, '''
         '''Grishog.''',
    size='large',
    strength=3, endurance=3,
    available_skills=['brawling', 'bravery', 'carrying', 'hardy', 'intimidate', '[melee weapons]'],
    exploits=[{'Name': 'Thick hide',
               'Desc': '''Ogres are extremely tough, with leathery skin. They gain 2 natural SOAK to physical '''
               '''attacks'''},
              {'Name': 'Smelly',
               'Desc': '''No matter what they do, ogres smell bad. They take a permanent -1d6 penalty to any '''
               '''attempts at stealth.'''},
              {'Name': 'Darksight',
               'Desc': '''Ogres can see in the dark as though it were normal daylight.'''},
              {'Name': 'Acid blood',
               'Desc': '''Ogres have acidic blood. In addition to gaining an additional 5 SOAK (acid), melee '''
               '''attackers which cause more than 10 slashing or piercing damage in a single blow take 1d6 acid '''
               '''damage from the blood splash.'''},
              {'Name': 'Strong',
               'Desc': '''Ogres are noted for their strength. When taking a new career, an Ogre may optionally '''
               '''exchange one of the listed four attribute increases for STR, as long as it doesn’t result in a '''
               '''duplicate attribute advancement.'''}])

race_old_orc = Race(
    name='Orc',
    desc='''Orcs are tribal, aggressive, violent, quick to anger and easy to offend. Strong and tough, orcs can be '''
         '''a little slow on the uptake.\n\n'''
         '''The warlike orcs have a barbaric, strength-based society. Orcs venerate warriors to the extreme, and '''
         '''include violence in most social rituals. Orcs believe that those who die gloriously in battle are '''
         '''guaranteed an afterlife of drinking, carousing, and fighting.\n\n'''
         '''Orcs tend to be slightly taller, stronger, and broader than humans, with green skin and black hair. '''
         '''Their ears are pointed, and some historians claim they are an ancient corrupted mockery of the elves. '''
         '''Like ogres, they are goblinoids, perhaps with elven lineage in the distant past.\n\n'''
         '''Orcs tend to be crafty and cunning, both on the battlefield and elsewhere. They are adept at crafting '''
         '''weapons, and wield many custom blades with unusual shapes. Equally, they are at home underground.\n\n'''
         '''Orcs excel as soldiers and other warriors.\n\n'''
         '''Typical names (male and female): Kevak, Deshe, Bra-el, G'Vera, Dracla, K'Ehleyr, Kellein, Kargan, Kalan, '''
         '''Adjur''',
    size='medium',
    strength=2, agility=2, intuition=3,
    available_skills=['[melee weapons]', 'blacksmithing', 'carousing', 'hunting', 'intimidation', 'mining',
                      'running', 'tactics', 'tracking'],
    exploits=[{'Name': 'Glory',
               'Desc': '''Orcs take pleasure in battle, and pride in their wounds. When reduced to below half '''
               '''HEALTH, they gain a +1d6 die bonus to attack rolls.'''},
              {'Name': 'Darksight',
               'Desc': '''Orcs can see clearly in the dark as though it were daylight. However, bright sunlight '''
               '''hurts their eyes, inflicting a -2 DEFENSE penalty.'''},
              {'Name': 'Bloodlust',
               'Desc': '''Once per day an orc can drink fresh blood to recover 2d6 HEALTH. This takes an action. The '''
               '''blood must come from a creature slain in the last hour.'''}])

race_old_smallfolk = Race(
    name='Smallfolk',
    desc='''Smallfolk are welcome in most places. Standing at about 3' in height, with ruddy cheeks and simple '''
         '''clothing, they have a reputation for good cheer and friendliness. Homebodies, smallfolk are agile and '''
         '''resilient, and are good with their hands. They make excellent farmers and shopkeepers.\n\n'''
         '''Smallfolk favor simple clothes in bright colors. They tend towards the stout (though not nearly so much '''
         '''as dwarves), and live to over 100 years of age. They boast pointed ears, although not as pronounced as '''
         '''those of the elves, and frequently hidden by their curly hair.\n\n'''
         '''Jovial in nature, it can be hard to make a smallfolk take offence. Smallfolk will put a positive spin on '''
         '''almost anything, a trait which endears them to many. They are as generous as they are jovial, and always '''
         '''happy to welcome others to their homes: indeed, entertaining others is a prime instinct for the '''
         '''smallfolk.\n\n'''
         '''Many view the smallfolk as weak, sometimes even cowardly. While it is true that the race does not tend '''
         '''towards violence, a cornered smallfolk will defend his or her friends to the death. In truth, smallfolk '''
         '''are the most courageous of all races.\n\n'''
         '''Typical names (male and female): Dobur, Thrari, Kirin, Borin, Boli, Filin, Gimnor, Thrarin, Dwain, '''
         '''Dolo, Kibur.''',
    size='small',
    agility=2, charisma=2, luck=2, magic=1,
    available_skills=['[crafting]', 'farming', 'fishing', 'appraisal', 'cooking', 'brewing', 'slings', 'stealth',
                      'diplomacy', 'bluffing'],
    exploits=[{'Name': 'Stubborn',
               'Desc': '''Smallfolk are difficult to enchant. They gain a +5 bonus to their MENTAL DEFENSE.'''},
              {'Name': 'Evasion',
               'Desc': '''Smallfolk are nimble and adept at dodging. They gain a +5 bonus to their DEFENSE.'''}])

race_old_sylvan_elf = Race(
    name='Sylvan Elf',
    desc='''Wild, fierce, and at one with nature, sylvan elves live in the woodlands and forests, armed with bow and '''
         '''spear. Sylvan elves can be xenophobic at times, and are well-trained in the arts of both war and '''
         '''nature.\n\n'''
         '''Sylvan elves are slim, like their grand elf cousins, but much shorter, at about 5-feet in height. With '''
         '''pointed ears, their skin tones tend to be dark, their hair brown, black, or sometimes with a greenish '''
         '''tinge. Unlike the grand elves, sylvan elves are not immortal. However, they have extremely long life '''
         '''spans of up to two-thousand years.\n\n'''
         '''Naturally magical, sylvan elves know the words and spells of the forest. They are known to talk to '''
         '''plants, or to command animals. At home in the branches of trees, sylvan elves are also adept at hiding '''
         '''their presence, and more than a few unwary intruders have found themselves ambushed upon entering sylvan '''
         '''woodlands.\n\n'''
         '''Sylvan elf adventurers tend to be priests, rangers, and druids.\n\n'''
         '''Typical names (male and female): Ashonn, Branmer, Kozain, Kalier, Tereval, Rathell, Sinehan, Nerrat, '''
         '''Dukhon, Deerenn, Delon, Mayen.''',
    size='medium',
    agility=2, endurance=2, magic=3,
    available_skills=['climbing', 'running', 'survival', 'tracking', 'animal handling', 'herbalism', 'bows', 'nature',
                      'stealth'],
    exploits=[{'Name': 'Fey',
               'Desc': '''Elves of all types are considered Fey.'''},
              {'Name': 'Nature affinity',
               'Desc': '''All sylvan elves know either the secret of plants or the secret of beasts.'''},
              {'Name': 'Unimpeded',
               'Desc': '''Sylvan elves are not affected or slowed by difficult terrain while outdoors.'''},
              {'Name': 'Tree-dwellers',
               'Desc': '''Sylvan elves gain a climb speed equal to their regular speed.'''},
              {'Name': 'Trance',
               'Desc': '''Sylvan elves do not need to sleep. They may choose to meditate, instead, while their '''
               '''non-elven companions are sleeping, but this is not necessary.'''},
              {'Name': 'Healthy',
               'Desc': '''Sylvan elves are completely immune to illness and disease of a non-magical nature.'''},
              {'Name': 'Long-lived',
               'Desc': '''When creating a Sylvan Elf character, multiply their career lengths by 4.'''},
              {'Name': 'Agile',
               'Desc': '''Sylvan Elves are noted for their dexterity. When taking a new career, a Sylvan Elf may '''
               '''optionally exchange one of the listed four attribute increases for AGI, as long as it doesn’t '''
               '''result in a duplicate attribute advancement.'''}])

race_old_water_nymph = Race(
    name='Water Nymph',
    desc='''Numerous legends report water nymphs leading foolish men to early ends; indeed, they are the most '''
         '''spirited and mysterious. The kingdom of fresh water nymphs (naiads) include those who live in lakes '''
         '''(limnades), rivers (potameides), streams, and fountains. Various salt water kingdoms include the oceans '''
         '''(oceanids) and the seas (nereids), each with clans unknown to landborne races. There are also clans of '''
         '''frozen water nymphs (icebergs, glaciers, snow) and airborne water nymphs (humidity, mist, stormclouds).''',
    size='medium',
    intuition=1, charisma=2, magic=3,
    available_skills=['nature', 'religion', '[magical]', '[social]', 'dancing', 'singing'],
    exploits=[{'Name': 'Aquatic',
               'Desc': '''You can breathe underwater. You also have a SWIM speed equal to your regular SPEED.'''},
              {'Name': 'Nautral allure',
               'Desc': '''ou can spend two actions making a MAG mental attack at a humanoid creature within 30’. If '''
               '''successful, the target gains the Charmed condition. If unsuccessful, you may not try again with '''
               '''the same target.'''},
              {'Name': 'Voice of nature',
               'Desc': '''You know the secret of water.'''},
              {'Name': 'Fey',
               'Desc': '''As a fey creature, you can sense the presence of (but not the location or type of) '''
               '''magic within 10’, and are vulnerable (1d6) to cold iron.'''},
              {'Name': 'Fey grace',
               'Desc': '''You are immune to the Charmed condition.'''},
              {'Name': 'Watery step',
               'Desc': '''You can walk on water and other liquids.'''}])

race_old_list = [race_old_clockman, race_old_danuki, race_old_deepling, race_old_earth_nymph, race_old_forest_nymph,
                 race_old_goblin, race_old_grand_elf, race_old_human, race_old_flint_dwarf, race_old_jade_dwarf,
                 race_old_minotaur, race_old_mountain_dwarf, race_old_night_elf, race_old_obsidian_dwarf,
                 race_old_ogre, race_old_orc, race_old_smallfolk, race_old_sylvan_elf, race_old_water_nymph]

for race in race_old_list:
    race.available_skills.sort()
    race.exploits.sort(key=lambda x: x['Name'])
