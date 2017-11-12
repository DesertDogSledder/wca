from lib.character import Career

# OLD/NOW
career_woin_origin_acoloyte = Career(
    name='Acoloyte',
    career_time='2d6+6',
    career_time_unit='years',
    prereq='none',
    intuition=1, willpower=1, charisma=1, luck=1,
    available_skills=['[artistic]', '[magical]', 'herbalism', 'intuition', 'linguistics', 'mediation', 'medicine', 'religion'],
    desc='''A childhood spent in a monastery taught you well for a life of piety.''',
    available_exploits=[{'Name': '''Daily Worship''', 'Desc': '''Once per day, you may pray to your deity and refresh your LUCK (or "faith" as you view it) dice pool.'''}])

career_woin_origin_acrobat = Career(
    name='Acrobat',
    career_time='2d6+6',
    career_time_unit='years',
    prereq='none',
    strength=1, agility=1, charisma=1, reputation=1,
    available_skills=['running', 'jumping', 'climbing', 'throwing', 'acrobatics'],
    desc='''You've been trained in acrobatics, taught to flip and cartwheel with ease to entertain spectators. Perhaps you grew up in a circus or travelling show.''',
    available_exploits=[{'Name': '''Slippery''', 'Desc': '''It isn't easy to hit you. You receive a +2 to DEFENSE when you are aware of an incoming attack, and you reduce falling damage by 1d6.'''}])

# NEW
career_woin_origin_borian_apprentice = Career(
    name='Borian Apprentice',
    career_time='2d6+6',
    career_time_unit='years',
    prereq='Borian',
    strength=1, agility=1, logic=1, reputation=1,
    available_skills=['[crafting]', '[technical]', '[outdoor]'],
    desc='''Growing up on the Borian Homeworld often involves an apprenticeship in a trade or craft.''',
    available_exploits=[{'Name': '''Artisan''', 'Desc': '''Choose a [crafting] skill. You gain 3 ranks in that skill.'''}])

career_woin_origin_everyman = Career(
    name='Everyman',
    career_time='2d6+6',
    career_time_unit='years',
    prereq='none',
    endurance=1, logic=1, charisma=1, luck=1,
    available_skills=['[scientific]', '[outdoor]', 'computers', 'carousing', '[performance]'],
    desc='''Your childhood was characterized only by its unremarkability. A normal childhood and High School experience, reasonable grades, and a typical teenaged social life, perhaps youdreamed of being something more.''',
    available_exploits=[{'Name': '''Ordinary''', 'Desc': '''Your very nondescript nature makes you easily able to blend in unnoticed, giving you a +1d6 bonus to attempts to bluff, disguise, or otherwiseremain visible but unremarked upon.'''}])

career_woin_origin_experiment = Career(
    name='Experiment',
    career_time='1d6',
    career_time_unit='years',
    prereq='none',
    strength=1, agility=1, endurance=1, logic=1,
    available_skills=['[physical]'],
    desc='''You were the subject of tests and experiments by scientists and doctors, whether created or merely altered. Your childhood was spent in a lab.''',
    available_exploits=[{'Name': '''Programming''', 'Desc': '''You have been specifically bred and engineered for a purpose. At the start of a fight your ‘programming' kicks in, granting you a +2d6 INITIATIVE bonus.'''}])

# OLD
career_woin_origin_farmhand_old = Career(
    name='Farmhand, archaic',
    career_time='2d6+6',
    career_time_unit='years',
    prereq='none',
    strength=1, endurance=1, luck=1,
    available_skills=['animal handling', 'farming', 'fishing', 'herbalism', 'nature', 'survival'],
    desc='''You grew up on a farm, learning how to manage crops and livestock.''',
    available_exploits=[{'Name': '''Outdoorsman''', 'Desc': '''You know the secret of plants.'''}])

# NEW
career_woin_origin_farmhand_new = Career(
    name='Farmhand, future',
    career_time='2d6+6',
    career_time_unit='years',
    prereq='none',
    strength=1, endurance=1, intuition=1, willpower=1,
    available_skills=['[outdoor]', '[vehicle]', '[physical]', '[crafting]', '[technical]'],
    desc='''You grew up on a farm – a wheat farm, a moisture farm, or similar.''',
    available_exploits=[{'Name': '''Dreamer''', 'Desc': '''You may replenish your LUCK pool once per day by spending five minutes daydreaming about wonderful possibilities.'''}])

career_woin_origin_felan_scavenger = Career(
    name='Felan Scavenger',
    career_time='1d6',
    career_time_unit='years',
    prereq='Felan',
    agility=1, intuition=1, luck=2,
    available_skills=['perception', 'stealth', 'survival', '[local knowledge]'],
    desc='''With their short lifespans and rapid growth to maturity, the Felan do not form strong family bonds. A youngster is soon left to fend for itself.''',
    available_exploits=[{'Name': '''Scavenge''', 'Desc': '''Once per day, given an hour in an urban environment, you can scavenge one item worth up to 100Cr. This exploit cannot be used during downtime.'''}])

# NOW
career_woin_origin_geek = Career(
    name='Geek',
    career_time='2d6+6',
    career_time_unit='years',
    prereq='none',
    intuition=1, logic=1, willpower=1, luck=1,
    available_skills=['[trivia]', '[gaming]'],
    desc='''You were obsessed with geek culture; you can recite lines from your favorite movies, rules from your favorite tabletop games, or obscure facts from your favorite video games.''',
    available_exploits=[{'Name': '''What Would Luke Do?''', 'Desc': '''Once per day you can be inspired by a pop culture character: you may spend all of your LUC dice on a check without reducing your LUC pool.'''}])

career_woin_origin_hacker = Career(
    name='Hacker',
    career_time='2d6+6',
    career_time_unit='years',
    prereq='none',
    logic=2, luck=1, reputation=1,
    available_skills=['computers', 'bureaucracy', 'cryptology', 'gaming', '[scientific]'],
    desc='''You were obsessed with computer systems in your adolescent years.''',
    available_exploits=[{'Name': '''White-hat''', 'Desc': '''You are practised at hacking and anti-hacking techniques. You can actively provide a starship control computer with a +4ELECTRONIC DEFENSE score, and gain a +1d6 bonus to electronic attacks.'''}])

career_woin_origin_jock = Career(
    name='Jock',
    career_time='15',
    career_time_unit='years',
    prereq='none',
    strength=1, agility=1, endurance=1, charisma=1,
    available_skills=['[sporting]', '[physical]', 'carousing', 'intimidation'],
    desc='''You were a football player (or other sportsman) in High School. You developed your physical and social skills, but your academic skills fell slightly behind.''',
    available_exploits=[{'Name': '''Athlete''', 'Desc': '''You are able to either throw objects with a +50% to their range increment, OR gain a +2 to your SPEED.'''}])

career_woin_origin_martial_artist = Career(
    name='Martial Artist',
    career_time='2d6+6',
    career_time_unit='years',
    prereq='none',
    agility=1, endurance=1, willpower=1, chi=1,
    available_skills=['martial arts', 'acrobatics', 'religion', '[artistic]', 'staves', 'polearms'],
    desc='''The story of your youth involves disciplined, regimented schooling in a traditional style of fighting, typically at a dojo in a remote location.''',
    available_exploits=[{'Name': '''Training.''', 'Desc': '''Your training proves that the old ways are often the best, for more reasons than one. You receive a +1 bonus to all three DEFENSEs.'''}])

career_woin_origin_military_brat = Career(
    name='Military Brat',
    career_time='2d6+6',
    career_time_unit='years',
    prereq='none',
    endurance=1, logic=1, willpower=1, luck=1,
    available_skills=['[vehicle]', 'pistols', 'rifles', 'carousing', 'survival'],
    desc='''You spent time getting shuffled around from military base to military base or otherwise learning from modern soldiers.''',
    available_exploits=[{'Name': '''Tactical''', 'Desc': '''You gain 3 ranks (2d6) in the tactics skill.'''}])

career_woin_origin_moisture_farmer = Career(
    name='Moisture Farmer',
    career_time='2d6+6',
    career_time_unit='years',
    prereq='none',
    agility=1, intuition=1, logic=1, luck=1,
    available_skills=['driving', 'farming', 'negotiating', 'engineering', 'pilot'],
    desc='''You grew up on a desert world, eking out a living harvesting moisture from the atmosphere.''',
    available_exploits=[{'Name': '''Technician''', 'Desc': '''You are adept at maintaining and repairing old equipment, persuading it to function for far longer than it is designed to. You can make any non-functioning Medium or smaller electronic item work for up to one hour, although it will be permanently broken thereafter.'''}])

career_woin_origin_navy_brat = Career(
    name='Navy Brat',
    career_time='2d6+6',
    career_time_unit='years',
    prereq='none',
    agility=1, endurance=1, luck=1, reputation=1,
    available_skills=['[vehicle]', 'computers', 'leadership', 'military trivia', 'brawling'],
    desc='''You were brought up on starships, starbases, and military installations.''',
    available_exploits=[{'Name': '''Petrolhead''', 'Desc': '''You have a familiarity with vehicles of military design. When driving or piloting a military vehicle (but not a starship), you gain a +1d6 bonus to checks to operate it.'''}])

career_woin_origin_nerd = Career(
    name='Nerd',
    career_time='2d6+6',
    career_time_unit='years',
    prereq='none',
    logic=2, luck=1, reputation=1,
    available_skills=['[computers]', 'bureaucracy', 'cryptology', 'gaming', '[scientific]'],
    desc='''You've been obsessed with computer systems.''',
    available_exploits=[{'Name': '''White-hat''', 'Desc': '''You are practiced at hacking and antihacking techniques. You can actively provide a computer system with a +4 e-DEFENSE score and gain a +1d6 bonus to electronic attacks.'''}])

career_woin_origin_noble = Career(
    name='Noble, archaic',
    career_time='2d6+6',
    career_time_unit='years',
    prereq='none',
    logic=1, charisma=1, luck=1, reputation=1,
    available_skills=['[artistic]', '[gaming]', 'carousing', 'linguistics', 'leadership', 'religion', 'swords'],
    desc='''You had a privilieged upbriging, surrounded by luxury.''',
    available_exploits=[{'Name': '''Silver Spoon''', 'Desc': '''Your wealthy upbringing means that you start play with 1,000 bonus gold coins and a superior quality set of clothing.'''}])

career_woin_origin_novice = Career(
    name='Novice',
    career_time='2d6+6',
    career_time_unit='years',
    prereq='none',
    endurance=1, intuition=1, willpower=1, psionics=1,
    available_skills=['religion', '[artistic]', '[crafting]', 'linguistics', 'martial arts', 'concentration', 'meditation'],
    desc='''You were brought up in a monastic or religious order.''',
    available_exploits=[{'Name': '''Confidant''', 'Desc': '''Being brought up in a monastery has given you a certain perception. You can discern a lie through a mix of intuition and experience. You gain a +1d6 bonus to discern lies and deceptions.'''}])

career_woin_origin_orphan = Career(
    name='Orphan',
    career_time='2d6 +6',
    career_time_unit='years',
    prereq='none',
    agility=1, intuition=1, charisma=1, luck=1,
    available_skills=['brawling', 'stealth', 'thievery', 'running', 'bluffing', '[performance]'],
    desc='''Your childhood was not a happy one.''',
    available_exploits=[{'Name': '''Urchin''', 'Desc': '''You are very familiar with urban backgrounds, and are able to blend in easily. With a one-hour period in a new city, you are able to name local crime figures.'''}])

career_woin_origin_page = Career(
    name='Page',
    career_time='2d6+6',
    career_time_unit='years',
    prereq='none',
    agility=1, intuition=1, charisma=1, reputation=1,
    available_skills=['[artistic]', '[gaming]', 'heraldry', 'history', 'linguistics', 'running', 'riding'],
    desc='''You spent years in the service of a lord or lady, learning the ways of court, running messages, cleaning, and serving a noble.''',
    available_exploits=[{'Name': '''Page Gear''', 'Desc': '''You start play with a superior set of clothing and a high-quality musical instrument.'''}])

career_woin_origin_primitive = Career(
    name='Primitive',
    career_time='2d6+6',
    career_time_unit='years',
    prereq='none',
    strength=1, agility=1, endurance=1, intuition=1,
    available_skills=['[outdoor]', 'herbalism'],
    desc='''You grew up in a tribe where you knew little of civilization.''',
    available_exploits=[{'Name': '''Fleet''', 'Desc': '''You gain +2 to your SPEED when outdoors in a non-urban envirpnemnt This does not stack with other other exploits which grant a SPEED bonus.'''}])

career_woin_origin_prodigy = Career(
    name='Prodigy',
    career_time='2d6',
    career_time_unit='years',
    prereq='none',
    intuition=1, logic=1, luck=1, reputation=1,
    available_skills=['[scientific]', 'engineering', 'computers'],
    desc='''A veritable genius, years ahead of your classmates, you were fast-tracked through your academic career.''',
    available_exploits=[{'Name': '''Unorthodox''', 'Desc': '''You often have an unorthodox approach to things. Once per day you may substitute one of your mental attributes for another one for the purposes of making a single attribute check.'''}])

career_woin_origin_scion = Career(
    name='Scion',
    career_time='15',
    career_time_unit='years',
    prereq='none',
    intuition=1, charisma=1, reputation=2,
    available_skills=['[trivia]', '[social]', '[artistic]', '[gaming]', '[sporting]'],
    desc='''You had a privileged upbringing in a wealthy family, heir to old money. You have never known hardship.''',
    available_exploits=[{'Name': '''Privileged''', 'Desc': '''You gain two sets of exceptional quality clothing and 1,000 bonus credits.'''}])

career_woin_origin_scout_eagle = Career(
    name='Scout/Eagle',
    career_time='2d6+6',
    career_time_unit='years',
    prereq='none',
    agility=1, intuition=1, logic=1, willpower=1,
    available_skills=['[crafting]', '[miscellaneous hobby]', '[outdoor]'],
    desc='''Always prepared, you were a member of the Boy or Girl Scouts or a similar organization.''',
    available_exploits=[{'Name': '''Be Prepared''', 'Desc': '''Once per day you can produce a small object worth $10 or less from your pockets.'''}])

career_woin_origin_service_droid = Career(
    name='Service Droid',
    career_time='1d6',
    career_time_unit='years',
    prereq='Android',
    agility=1, logic=2, charisma=1,
    available_skills=['cooking', 'linguistics', 'engineering', 'computers', 'driving', 'accounting', 'navigation', 'astrogation'],
    desc='''You were created to perform a specific service – perhaps as a repair droid, domestic bot, astromech, or a translator.''',
    available_exploits=[{'Name': '''Unsuspicious''', 'Desc': '''Everybody trusts a service droid; it doesn't even occur to them that one might lie or attack. You gain a +1d6 bonus to all attempts to bluff or deceive or to access anambush turn.'''}])

career_woin_origin_slave = Career(
    name='Slave',
    career_time='2d6+6',
    career_time_unit='years',
    prereq='none',
    endurance=2, intuition=1, willpower=1,
    available_skills=['[crafting]', 'animal handling', 'farming', 'mining'],
    desc='''A lifetime of slavery and labor has toughned you both physically and mentally.''',
    available_exploits=[{'Name': '''Hardship''', 'Desc': '''A life of oppression has taught you to endure hardship; you gain an extra death/dying countdown die when reduced to below 0 HEALTH.'''}])

career_woin_origin_street_tough = Career(
    name='Street Tough',
    career_time='2d6+6',
    career_time_unit='years',
    prereq='none',
    agility=1, intuition=1, charisma=1, luck=1,
    available_skills=['intimidation', 'thievery', 'appraisal', 'brawling', 'knives', 'clubs'],
    desc='''You fell in with local gangs and the lower echelons of organized crime, looking up to gangsters as role models. You joined a gang, played truant, and engaged in petty crime.''',
    available_exploits=[{'Name': '''Fell Off a Truck''', 'Desc': '''You may acquire starting equipment at half cost. However, any items you acquire this way have been stolen.'''}])

career_woin_origin_survivor = Career(
    name='Survivor',
    career_time='2d6+6',
    career_time_unit='years',
    prereq='none',
    agility=1, endurance=1, intuition=1, willpower=1,
    available_skills=['[outdoors]', 'stealth', '[vehicle]', 'running'],
    desc='''The story of your childhood is one of hardship and warzones; you've grown a thick hide from countless conflicts or wars.''',
    available_exploits=[{'Name': '''Endurance''', 'Desc': '''You endured a lot, and have the scars to prove it. You gain +2 natural Soak.'''}])

career_woin_origin_talent = Career(
    name='Talent',
    career_time='2d6+6',
    career_time_unit='years',
    prereq='none',
    intuition=1, willpower=1, psionics=1,
    available_skills=['empathy', 'stealth', '[psionic]', '[performance]'],
    desc='''You manifested undisciplined psionic ability early in life, and struggled because of it.''',
    available_exploits=[{'Name': '''Empath''', 'Desc': '''You can sense strong emotions in those with whom you converse.'''}])

career_woin_origin_traveller = Career(
    name='Traveller',
    career_time='2d6+6',
    career_time_unit='years',
    prereq='none',
    endurance=1, intuition=1, luck=1, reputation=1,
    available_skills=['piloting', 'navigation', 'bureaucracy', 'computers', 'linguistics'],
    desc='''Your parents travelled a lot, which gave you great exposure to the wonders and goings on of the universe.''',
    available_exploits=[{'Name': '''Stargazer''', 'Desc': '''Your years of travelling the space lanes has heightened your sense of location. You can identify which system you are in if you are able to see the sky (as long as you are not in uncharted space).'''}])

career_woin_origin_urchin = Career(
    name='Urchin',
    career_time='2d6+6',
    career_time_unit='years',
    prereq='none',
    agility=1, intuition=1, endurance=1, luck=1,
    available_skills=['perception', 'running', 'stealth', 'survival', 'thievery'],
    desc='''A rough childhood on the streets taught you how to survive.''',
    available_exploits=[{'Name': '''Life on the Streets''', 'Desc': '''Accustomed to sleeping rough, you heal a bonus 1d6 HEALTH every day.'''}])

career_woin_origin_wizards_apprentice = Career(
    name='''Wizard's Apprentice''',
    career_time='2d6+6',
    career_time_unit='years',
    prereq='none',
    intuition=1, logic=1, magic=1, reputation=1,
    available_skills=['[artistic]', '[lore]', '[magical]', 'hypnotism'],
    desc='''Your childood was an academic one of study and lore.''',
    available_exploits=[{'Name': '''Prestidigitation''', 'Desc': '''You learned little magical tricks to help with your chores as an apprenstice. You are able to use small displays of magical presidigitation at-will to assist you with day-to-day inconveniences: cleaning clothes, keeping the rain or mud off, a tiny reading light, polishing silverware, and the like.'''}])

career_woin_origin_list = [career_woin_origin_acoloyte, career_woin_origin_acrobat,
                           career_woin_origin_borian_apprentice, career_woin_origin_everyman,
                           career_woin_origin_experiment, career_woin_origin_farmhand_old,
                           career_woin_origin_farmhand_new, career_woin_origin_felan_scavenger,
                           career_woin_origin_geek, career_woin_origin_hacker, career_woin_origin_jock,
                           career_woin_origin_martial_artist, career_woin_origin_military_brat,
                           career_woin_origin_moisture_farmer, career_woin_origin_navy_brat, career_woin_origin_nerd,
                           career_woin_origin_noble, career_woin_origin_novice, career_woin_origin_orphan,
                           career_woin_origin_page, career_woin_origin_primitive, career_woin_origin_prodigy,
                           career_woin_origin_scion, career_woin_origin_scout_eagle, career_woin_origin_service_droid,
                           career_woin_origin_slave, career_woin_origin_street_tough, career_woin_origin_survivor,
                           career_woin_origin_talent, career_woin_origin_traveller, career_woin_origin_urchin,
                           career_woin_origin_wizards_apprentice]

for career in career_woin_origin_list:
    career.available_skills.sort()
