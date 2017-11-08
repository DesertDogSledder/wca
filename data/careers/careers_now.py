from lib.character import Career

career_now_actor = Career(
    name='Actor',
    career_time='1d6',
    career_time_unit='years',
    prereq='none',
    logic=1, intuition=1, charisma=1, reputation=1,
    available_skills=['swords', 'acting', 'singing', 'dancing', 'flirtation', 'carousing', 'bluffing', 'linguistics', 'movie trivia', 'celebrity trivia', 'theater trivia', 'disguise'],
    desc='''A star of screen or stage, you make your living pretending to be somebody else. Each time you take this career, roll 1d6. If you roll a 6, you win an award. Roll again: (1) BAFTA, (2) Emmy, (3) Tony, (4) Soap Opera Digest, (5) Razzie, (6) Oscar. An award gives you +1 REP.''',
    available_exploits=[{'Name': 'Box-office star', 'Desc': '''(requires B-movie) You were in a blockbuster movie. You gain reputation=2 and begin play with an extra $1,000. You also learned one new skill of your choice at 1 rank (1d6). Name your movie.'''},
                                         {'Name': 'Method actor', 'Desc': '''You immerse yourself into your roles. Increase your acting skill to 6 ranks.'''},
                                         {'Name': 'Stage-fright', 'Desc': '''You learned to overcome your nerves on the stage. Once per day you may ignore a fear-based effect.'''},
                                         {'Name': 'Costumer', 'Desc': '''You are used to wearing costumes in your roles. Gain the disguise skill at 6 ranks.'''},
                                         {'Name': 'B-movie', 'Desc': '''You were in a classic B-movie. You gain reputation=1 and and begin play with an extra $500. You also learned one new skill of your choice at 1 rank (1d6). Name your movie.'''},
                                         {'Name': 'Catchphrase', 'Desc': '''You are associated with a catchphrase. Once per day you can use your catchphrase and gain +1d6 on any roll. Write down your catchphrase.'''}])

career_now_archaeologist = Career(
    name='Archaeologist',
    career_time='1d6',
    career_time_unit='years',
    prereq='none',
    intuition=1, logic=1, willpower=1, luck=1,
    available_skills=['literature', 'history', 'art', 'linguistics', 'theology', 'geography', 'climbing', 'archeology', 'cryptology', 'appraisal'],
    desc='''As an archeologist, you explored dark caves, tracked down lost treasures, and dug a lot of holes.''',
    available_exploits=[{'Name': 'Not another trap', 'Desc': '''You can spend a LUC die to automatically avoid a trap.'''},
                        {'Name': 'Great discovery', 'Desc': '''You discovered something incredible – the Holy Grail, the Ark of the Covenant, or something equally impressive. You gain +2 REP.'''},
                        {'Name': 'Antique', 'Desc': '''You start play with an antique weapon, which is of exceptional quality.'''},
                        {'Name': 'Direction sense', 'Desc': '''You always know where you are, and you never get lost.'''},
                        {'Name': 'Linguist.', 'Desc': '''You can speak and understand any language, although it might sometimes take you a moment to figure it out.'''}])

career_now_assassin = Career(
    name='Assassin',
    career_time='1d6',
    career_time_unit='years',
    prereq='stealth, tracking, [combat]',
    strength=1, agility=1, intuition=1, reputation=1,
    available_skills=['[combat]', 'stealth', 'thievery', 'perception', 'intimidate', 'disguise'],
    desc='''A killer for hire, you mastered the skills of assassination.''',
    available_exploits=[{'Name': 'Killing blow', 'Desc': '''Any attack you make during the ambush turn gains a +2d6 bonus to attack.'''},
                        {'Name': 'Ambush', 'Desc': '''You gain +2d6 to rolls made to access the ambush turn.'''},
                        {'Name': 'Weak point', 'Desc': '''Once per enemy you may ignore any SOAK score he possesses by targeting a weak spot.'''},
                        {'Name': 'Sneak', 'Desc': '''If nobody is actively looking for you, you are able to move silently and unseen at half your normal speed. You are effectively invisible. However, if anybody is actually looking for you, they may make INT checks as normal to spot you.'''}])

career_now_astronaut = Career(
    name='Astronaut',
    career_time='1d6',
    career_time_unit='years',
    prereq='[scientific] or piloting',
    endurance=1, intuition=1, logic=1, reputation=1,
    available_skills=['piloting', 'zero-g', 'engineering', 'physics', 'medicine', 'astronomy'],
    desc='''You trained to become an astronaut and travelled into space, either into orbit or to the moon or a similar body.''',
    available_exploits=[{'Name': 'G-forces', 'Desc': '''You are trained to resist g-forces. You gain SOAK 5 to crushing damage.'''},
                        {'Name': 'Space sickness', 'Desc': '''Nearly every astronaut gets sick. You learn to ignore it. You become immune to sickness conditions.'''},
                        {'Name': 'Spacewalker', 'Desc': '''You gain a zero-g SPEED equal to your regular speed.'''}])

career_now_athlete = Career(
    name='Athlete',
    career_time='1d6',
    career_time_unit='years',
    prereq='[sport] or [physical]',
    strength=1, agility=1, endurance=1, reputation=1,
    available_skills=['[physical]', '[sporting]', 'carousing', 'flirtation', '[unarmed combat]'],
    desc='''You are a professional athlete, whether that be in a team sport or a track and field event.''',
    available_exploits=[{'Name': 'Athletic', 'Desc': '''Choose four [physical] skills. You gain these four skills at 1 rank (1d6). This does not increase the rank of an existing skill.'''},
                        {'Name': 'Runner', 'Desc': '''You gain a +1 SPEED bonus.'''},
                        {'Name': 'Fit', 'Desc': '''You gain a +5 HEALTH bonus.'''},
                        {'Name': 'Signing bonus', 'Desc': '''You are signed to a team and gain a $1,000 signing bonus.'''}])

career_now_bartender = Career(
    name='Bartender',
    career_time='1d6',
    career_time_unit='years',
    prereq='none',
    endurance=1, intuition=1, charisma=1, luck=1,
    available_skills=['[social]', 'carousing', 'perception', 'brewing', 'cooking', 'brawling', 'clubs'],
    desc='''Bartending is a great way to pay the bills. Some make a lifelong career of it.''',
    available_exploits=[{'Name': 'Bouncer', 'Desc': '''You gain a +1d6 bonus to checks vs. an intoxicated creature.'''},
                        {'Name': 'Fake ID', 'Desc': '''Years of checking for fake ID mean that you can spot the telltale signs. You gain a +1d6 bonus to detect forgeries.'''},
                        {'Name': 'Gossip', 'Desc': '''You can gather local gossip and information simply by spending an hour in a bar or other watering hole, effectively giving you the local knowledge skill wherever you go as long as you are able to refresh your knowledge at a local bar weekly.'''}])

career_now_boot_camp = Career(
    name='Boot Camp',
    career_time='1',
    career_time_unit='years',
    prereq='none',
    agility=1, logic=1, willpower=1, charisma=1,
    available_skills=['carrying', 'pistols', 'rifles', 'leadership', 'tactics', 'survival'],
    desc='''You joined the military and completed basic military training. Some programs send recruits to college to gain degrees before returning to cadet assignments.''',
    available_exploits=[{'Name': 'Basic training', 'Desc': '''. You gain a uniform which incorporates a kevlar vest. You also gain one rank in tactics, law, rifles, and survival.'''},
                        {'Name': 'Officer training [requires Basic Training]', 'Desc': '''A second stint in the Academy prepares you for command. You automatically gain a military rank and the leadership skill at 1 rank if you do not already have it. You gain +2 REP. Make a Challenging [13] CHA check before advancing any attributes. If you succeed, you automatically gain a second military rank.'''}])

career_now_bouncer = Career(
    name='Bouncer',
    career_time='1d6',
    career_time_unit='years',
    prereq='none',
    strength=1, endurance=1, intuition=1, charisma=1,
    available_skills=['hardy', 'insight', 'perception', 'brawling', 'reactions', 'carousing', 'law'],
    desc='''You stood guard at the door to a bar, club, or other private venue.''',
    available_exploits=[{'Name': 'Immovable object', 'Desc': '''You know how to plant yourself in place and refuse to budge. You may spend a LUC die to negate any forced movement from a creature of your size or smaller.'''},
                        {'Name': 'Quick-search', 'Desc': '''You are adept at spotting concealed weapons, drugs, and other things. You automatically spot hidden items concealed about somebody's person.'''},
                        {'Name': 'Age-check', 'Desc': '''Not only can you discern somebody's age at a glance, you can see through disguises.'''},
                        {'Name': 'Fake-ID', 'Desc': '''You can spot forgeries, whether that be a driver's license or the Mona Lisa.'''},
                        {'Name': 'Pin', 'Desc': '''You know how to pin somebody in place. Make a melee attack against an adjacent target your size or smaller. On a success, the target is pinned in place unless they escape with a melee attack against you. You may move at half-speed, taking your pinned target with you. A pinned target may not make any attacks other than an attempt to escape.'''}])

career_now_bounty_hunter = Career(
    name='Bounty Hunter',
    career_time='1d6',
    career_time_unit='years',
    prereq='none',
    agility=1, intuition=1, logic=1, reputation=1,
    available_skills=['tracking', 'piloting', 'stealth', 'law', 'computers', 'perception', 'intimidate', '[combat]'],
    desc='''As a bounty hunter you spent time tracking down and capturing wanted criminals.''',
    available_exploits=[{'Name': 'Prey', 'Desc': '''You may choose a target species or heritage. You gain a +1d6 bonus to attempts to track targets of that species.'''},
                        {'Name': 'Datamining', 'Desc': '''You are able to locate a target's current location down to a specific city by accessing credit, criminal, customs, and other records if you have access to a computer link.'''}])

career_now_boxer = Career(
    name='Boxer',
    career_time='1d6',
    career_time_unit='years',
    prereq='boxing',
    strength=1, endurance=1, willpower=1, reputation=1,
    available_skills=['boxing', 'hardy', 'reactions', 'intimidate'],
    desc='''The ring is your king. You have been in scores of fights (both sanctioned and otherwise), endured countless days and nights of strenuous physical training, and your body is a shrine to thousands of jabs, hooks, and hastily landed strikes.''',
    available_exploits=[{'Name': 'One-two', 'Desc': '''Once per turn, you may make a quick second boxing attack for free. This second attack may not have any exploits attached to it.'''},
                        {'Name': 'Haymaker', 'Desc': '''With a wild swing, you pool all your attack potential into one mighty blow. The attack costs two actions, suffers a -2d6 penalty to hit, but deals double damage. If you miss, however, you put yourself at a disadvantage, allowing your opponent an immediate free attack at you.'''},
                        {'Name': 'Beat the count', 'Desc': '''Once per day, when reduced to 0 health, you may spend two actions to recover 2d6 health and stand up.'''},
                        {'Name': 'Rope-a-dope', 'Desc': '''You allow your enemy to attack you, fooling him into believing he is winning. You allow the enemy's next two attacks to strike home, choosing to receive the damage; after the second attack, you respond with a counterattack which does bonus damage equal to the damage he dealt you.'''},
                        {'Name': 'K.O.', 'Desc': '''(requires Haymaker)  A mighty blow fells your opponent, knocking him to the ground and stunning him until he shakes that condition off.'''},
                        {'Name': 'Bare Knuckles', 'Desc': '''Not every fight is in a well-lit ring with ropes, medical staff, or even gloves—and you know that better than anyone. People have been tangling with you in back alleys, bars, and maybe even prison yards, fist for fist, for years. Your boxing damage increases by 1d6 when not using gloves.'''},
                        {'Name': 'Battered', 'Desc': '''Cauliflower ears and broken nose you may have, but you can take a hit without flinching. You gain SOAK 5 (blunt).'''}])

career_now_burglar = Career(
    name='Burglar',
    career_time='1d6',
    career_time_unit='years',
    prereq='stealth',
    agility=1, intuition=1, luck=1, reputation=1,
    available_skills=['climbing', 'jumping', 'acrobatics', 'escape artist', 'computers', 'stealth', 'thievery', 'appraisal'],
    desc='''You become a master thief, able to infiltrate the most secure of locations. Some cat burglars work for hire and conduct industrial espionage, while others prefer to steal valuable artifacts and jewels from museums and high security vaults.''',
    available_exploits=[{'Name': 'Locksmith', 'Desc': '''You gain a exceptional quality lockpicking kit.'''},
                        {'Name': 'Catburglar', 'Desc': '''An expert at climbing, you do not take any die penalties in combat while climbing.'''},
                        {'Name': 'Sixth sense', 'Desc': '''You have a sixth sense when it comes to traps, and gain a +2d6 bonus to spot them and a +1d6 bonus to avoid or disarm them.'''},
                        {'Name': 'Climber', 'Desc': '''(requires Catburglar) Your climbing speed becomes equal to your regular SPEED.'''},
                        {'Name': 'Grand heist', 'Desc': '''You achieve a great robbery that will be remembered for years to come. Gain a bonus 3d6 x $100. You may repeat this exploit, gaining 3d6 x $100 each time.'''}])

career_now_chef = Career(
    name='Chef',
    career_time='1d6',
    career_time_unit='years',
    prereq='cooking',
    agility=1, intuition=1, logic=1, reputation=1,
    available_skills=['cooking', 'brewing', 'gardening', 'knives'],
    desc='''You know how to cook, to prepare amazing meals, and to run a kitchen.''',
    available_exploits=[{'Name': 'Cooking knives', 'Desc': '''You are an expert at cutting flesh with a blade. When using a knife, you do +1d6 damage.'''},
                        {'Name': 'Poison resistance', 'Desc': '''You often have to taste your food, and you have developed SOAK 5 vs. poisons.'''},
                        {'Name': 'Poisoner', 'Desc': '''You know how to make a poison. It takes you five minutes, and lasts for one hour before becoming ineffective. Your poison does poison damage equal to your LOG dice pool when ingested.'''},
                        {'Name': 'Kitchen management', 'Desc': '''Running a kitchen is a gruelling job. You know how to get the most out of your underlings, even if you have to shout profanities at them. One per day you may spend two actions to give all allies within 30' one immediate free action.'''},
                        {'Name': 'A good meal', 'Desc': '''Once per day you can spend an hour preparing a good meal for a number of people equal to your LOG score. The meal restores 1d6 HEALTH to all who eat it, or it removes one stage of the Tiredness status track.'''}])

career_now_college = Career(
    name='College',
    career_time='4',
    career_time_unit='years',
    prereq='none',
    logic=1, willpower=1, charisma=1, reputation=1,
    available_skills=['computers', '[scientific]', '[artistic]', '[sporting]', '[social]', '[technical]'],
    desc='''You attended a civilian college or university and gained formal qualifications in a chosen area of study. Choose a subject, which can be any skill, but is typically a [scientific], [technical], or [artistic] skill. You can restart this career at any time to gain degrees in additional subjects.''',
    available_exploits=[{'Name': 'Bachelor', 'Desc': '''After a four-year course, you gained a Bachelor's degree or equivalent at university. Improve your skill ranks in your chosen subject to 3. Your research skills are developed. If you have access to a library or computer network, you gain a +1d6 bonus to attempts to learn information about a subject. Make a Challenging [13] LOG check before advancing any attributes. If you succeed, you pass this degree with honors and gain 1 bonus REP attribute point.'''},
                        {'Name': 'Masters [requires Bachelor]', 'Desc': '''You remain in college and gain a Masters degree in your subject. You gain 1 bonus skill rank in your chosen subject. Make a Difficult [16] LOG check before advancing any attributes. If you succeed, you pass this degree with honors and gain 1 bonus REP attribute point.'''},
                        {'Name': 'Doctorate [requires Masters]', 'Desc': '''After further studies, you gained a Doctorate at university. You may now call yourself a Doctor. But not THE Doctor. Gaining a doctorate requires not just an expert knowledge of a subject, but also rigorous skills of analysis and evaluation and critical achievement. Improve your skill ranks in your chosen subject to 6. Make a Demanding [21] LOG check before advancing any attributes. If you succeed, you pass this degree with honors and have also made a minor breakthrough in your chosen subject, and are known amongst peers for it, gaining you a bonus 2 points to your REP attribute. Choose the nature of your breakthrough.'''}])

career_now_con_artist = Career(
    name='Con Artist',
    career_time='1d6',
    career_time_unit='years',
    prereq='bluffing',
    intuition=1, logic=1, charisma=1, luck=1,
    available_skills=['[social]', 'disguise', 'bribery', 'forgery', '[gaming]', 'appraisal'],
    desc='''You honed your skills and learned how to trick others out of their money with charm, lies, bluffs, disguise, and more. Many career criminals combine the craft of the con man with the skills of the burglar.''',
    available_exploits=[{'Name': 'Grifter', 'Desc': '''In a bar or other crowded social situation, you can automatically make money equal to a CHA check x $10 in the space of an hour using only the gift of the gab. You can only do this once per day. This exploit cannot be used during downtime.'''},
                        {'Name': 'Impersonate', 'Desc': '''You are easily able to impersonate any job role which you have had opportunity to observe within the past day, even briefly. You gain a +1d6 bonus if you have been able to observe and mimic an example.'''},
                        {'Name': 'Quick change', 'Desc': '''You are able to don a quick disguise in one round instead of five minutes. This must be a disguise you've successfully used before.'''},
                        {'Name': 'Beguiling', 'Desc': '''You are able to temporarily beguile and captivate a target with your words as a CHA vs. MENTAL DEFENSE check. A successful check charms the target until they shake off the condition. The target must be able to understand you and have a LOGIC attribute of at least 3.'''}])

career_now_craftsman = Career(
    name='Craftsman',
    career_time='1d6',
    career_time_unit='years',
    prereq='[crafting] or [technical]',
    strength=1, agility=1, logic=1, charisma=1,
    available_skills=['[technical]', '[artistic]', '[crafting]'],
    desc='''You made your living by practising your craft as a carpenter, electrician, mechanic, or other professional skilled worker.''',
    available_exploits=[{'Name': 'Handyman', 'Desc': '''Choose four [crafting] skills. You gain these four skills at 1 rank (1d6). This does not increase the rank of an existing skill.'''},
                        {'Name': 'Toolkit', 'Desc': '''You gain a set of high quality tools.'''},
                        {'Name': 'Tradesman', 'Desc': '''You can make 3d6 x $10per week by plying your trade.'''},
                        {'Name': 'Builder', 'Desc': '''Assuming raw materials are available, you can make an item of equipment in one day by rolling a LOG check vs. the item's value (up to $20).'''},
                        {'Name': 'Fixer', 'Desc': '''You gain a +1d6 bonus to any attempt to repair something.'''}])

career_now_cultist = Career(
    name='Cultist',
    career_time='1d6',
    career_time_unit='years',
    prereq='religion',
    agility=1, intuition=1, logic=1, charisma=1,
    available_skills=['religion', 'history', 'politics', 'philosophy', 'knives', 'meditation', 'disguise', '[social]', 'hypnotism', 'occult', 'astrology'],
    desc='''You were either part of a cult, or you studied cults or the occult.''',
    available_exploits=[{'Name': 'Devotion', 'Desc': '''You are utterly devoted to your cause. Your single-mindedness grants you +4 MENTAL DEFENSE.'''},
                        {'Name': 'Occultist', 'Desc': '''You have knowledge of the paranormal; things that were not meant to be known.'''},
                        {'Name': 'Sacrificial dagger', 'Desc': '''You start play with a high quality dagger with either the Serrated Blade or the Sharpened customization.'''},
                        {'Name': 'Poison resistance', 'Desc': '''Part of your cult's observances involve drinking poison. You gain SOAK 5 (poison).'''},
                        {'Name': 'Fanatic', 'Desc': '''You may be slightly unhinged; you are completely immune to the Fear status track.'''}])

career_now_dark_crusader = Career(
    name='Dark Crusader',
    career_time='1d6',
    career_time_unit='years',
    prereq='stealth',
    agility=1, intuition=1, willpower=1, reputation=1,
    available_skills=['stealth', 'climbing', 'jumping', 'acrobatics', 'intimidation', 'thievery', '[combat]'],
    desc='''You prowl the streets at night. More than just a vigilante, you are a symbol. You have learned how to instill fear into the hearts of criminals, and the very mention of your name is enough to make the most hardened of gangs look nervously over their shoulders.''',
    available_exploits=[{'Name': 'Dark knight', 'Desc': '''You operate best at night, knowing how to use the shadows to your advantage. Once per day, during the hours of darkness, you gain a +1d6 bonus to all dice pools for one minute.'''},
                        {'Name': 'Fearful legend', 'Desc': '''Criminals fear you, and rightly so. You may make a REP vs. MENTAL DEFENSE attack to inflict the frightened condition on a target until they shake it off.'''},
                        {'Name': 'Vanish.', 'Desc': '''You are renowned for your ability to simply disappear; some even believe it to be supernatural. Once per day, during the hours of darkness, you may effectively turn invisible until you attack.'''},
                        {'Name': 'Utility belt', 'Desc': '''You gain one gadget of your choice.'''},
                        {'Name': 'Costume.', 'Desc': '''You gain a costume which acts as armor with SOAK 8. This special costume does not require armor training to use effectively even when it is of high quality or better, and can be upgraded one stage by taking this exploit again, become high quality, exceptional, and so on. You may repeat this exploit up to five times, upgrading your costume each time.'''}])

career_now_detective = Career(
    name='Detective',
    career_time='1d6',
    career_time_unit='years',
    prereq='none',
    agility=1, intuition=2, charisma=1,
    available_skills=['interrogation', 'pistols', 'driving', 'bureaucracy', 'perception', 'intimidate', 'stealth', 'tracking', 'law'],
    desc='''You become a detective, expert at spotting clues and finding your man. Even if you leave the profession, you still retain enough contacts to call in favors and request information.''',
    available_exploits=[{'Name': 'Clues', 'Desc': '''If there are any clues to find at a crime scene, you automatically find them within 5 minutes.'''},
                        {'Name': 'Criminal record', 'Desc': '''You can freely access police databanks and automatically discover any information held on file about a suspect.'''},
                        {'Name': 'Plate number', 'Desc': '''You can request a registration plate number lookup, and automatically determine the registered owner and address of a vehicle.'''}])

career_now_diplomat = Career(
    name='Diplomat',
    career_time='1d6',
    career_time_unit='years',
    prereq='[social]',
    intuition=1, charisma=2, reputation=1,
    available_skills=['[social]', 'bureaucracy', 'law', 'politics', 'local knowledge'],
    desc='''You have represented your planet elsewhere.''',
    available_exploits=[{'Name': 'Diplomatic', 'Desc': '''Choose four [social] skills. You gain these four skills at 1 rank (1d6). This does not increase the rank of an existing skill.'''},
                        {'Name': 'Diplomatic pouch', 'Desc': '''You have a diplomatic pouch in which any small sized item can be carried through customs without inspection.'''},
                        {'Name': 'Embassy', 'Desc': '''You have access to your home country's ambassadorial embassy and residences in any country (if there are any), which can provide food, shelter, basic equipment, and medical care.'''},
                        {'Name': 'Diplomatic immunity', 'Desc': '''You gain diplomatic immunity to very low-level and petty crimes in any country which contains an embassy for your country.'''}])

career_now_diver = Career(
    name='Diver',
    career_time='1d6',
    career_time_unit='years',
    prereq='swimming',
    strength=1, agility=1, endurance=1, intuition=1,
    available_skills=['swimming', 'perception', 'hardy', 'oceanography', 'sailing'],
    desc='''Whether it was a commercial job, or for the military or police, you feel most at home in a wetsuit. You became a diver, able to explore the ocean depths.''',
    available_exploits=[{'Name': 'Like a fish', 'Desc': '''You gain a SWIM speed equal to your regular SPEED.'''},
                        {'Name': 'Hold breath', 'Desc': '''You can hold your breath for a number of minutes equal to your END dice pool.'''},
                        {'Name': 'Murky depths', 'Desc': '''You can see well underwater and in other dark environments, gaining darksight to a distance of 5' per point of INT.'''},
                        {'Name': 'High diver', 'Desc': '''You never take damage when falling into water from any height.'''}])

career_now_drifter = Career(
    name='Drifter',
    career_time='1d6',
    career_time_unit='years',
    prereq='none',
    endurance=1, intuition=1, charisma=1, luck=1,
    available_skills=['carousing', 'gaming', 'flirtation', 'performing', 'bluffing', 'appraisal', 'thievery'],
    desc='''Somehow you lost your way. Drinking, gambling, with no clear objective, you drifted through the fringes of society. Perhaps you never fitted in; or perhaps you are a war veteran who found home was no longer home.''',
    available_exploits=[{'Name': 'Unseen', 'Desc': '''You know how to blend in so that nobody pays any attention to you. You gain a +1d6 bonus when attempting to do so.'''}])

career_now_driver = Career(
    name='Driver',
    career_time='1d6',
    career_time_unit='years',
    prereq='driving',
    agility=1, intuition=1, luck=1, reputation=1,
    available_skills=['driving', 'engineering', 'reactions'],
    desc='''You became a driver. Either a racing driver, such as Formula 1 or NASCAR, or a getaway driver. You may even have been a military driver.''',
    available_exploits=[{'Name': 'Getaway', 'Desc': '''If a vehicle is within one move increment of you, you can move to it, start the engine, and move away at the vehicle's SPEED all with just two actions (one turn).'''},
                        {'Name': 'Racer', 'Desc': '''You can push a vehicle to extreme speeds, increasing its SPEED by 2.'''},
                        {'Name': 'Evasive driving', 'Desc': ''' When you are driving a vehicle, it gains +4 DEFENSE.'''},
                        {'Name': 'Shoot n drive', 'Desc': '''While driving, you may take a free sidearm shot once per round.'''}])

career_now_engineer = Career(
    name='Engineer',
    career_time='1d6',
    career_time_unit='years',
    prereq='engineering',
    strength=1, agility=1, logic=1, luck=1,
    available_skills=['computers', '[technical]', 'bureaucracy'],
    desc='''You became an engineer, proficient at manipulating technology and repairing vehicles, devices and engines. ''',
    available_exploits=[{'Name': 'Technical knowledge base', 'Desc': '''Choose four [technical] skills. You gain these four skills at 1 rank (1d6). This does not increase the rank of an existing skill.'''},
                        {'Name': 'Jury-rig', 'Desc': '''You can temporarily repair and jury-rig a broken item of size Medium or smaller by spending five minutes with it. The item will operate for a number of minutes equal to your LOG check. If you spend one hour with it, it will operate for a number of hours equal to your LOG check. If you spend a day with it, it will operate for a number of days equal to your LOG check.'''},
                        {'Name': 'Upgrade', 'Desc': '''You can modify a piece of electronic equipment of size Small or smaller to upgrade it permanently to a high quality item. This process takes one hour, but the item can only be used by you due to unfamiliar and jury-rigged controls, and renders it monetarily worthless.'''},
                        {'Name': 'Engine-tuner', 'Desc': '''A vehicle to which you have an hour's access increases its maximum speed by 1. This does not stack with other engineers should others be present.'''},
                        {'Name': 'Engine-master [requires Engine-tuner]', 'Desc': '''You can increase your vehicle's speed by 2 for a number of hours equal to your LOG check, after which the engine cannot be used for 24 hours. This does not stack with other engineers should others be present.'''},
                        {'Name': 'Explosives', 'Desc': '''You can create explosives from common items and surroundings. The explosive takes 30 minutes to make, and causes 3d6 heat damage to all within 5'. The explosive can be stored, but only for up to two hours.'''},
                        {'Name': 'Saboteur', 'Desc': '''You are able to disable any mechanical or electronic device to which you have access. This exploit does not open a locked door (disabling the lock just means it remains stuck in whatever configuration it is currently in). This takes you five minutes.'''}])

career_now_explosives_expert = Career(
    name='Explosives Expert',
    career_time='1d6',
    career_time_unit='years',
    prereq='none',
    agility=1, intuition=1, logic=1, luck=1,
    available_skills=['explosives', 'hardy', 'perception', 'reactions', 'electronics', 'thievery'],
    desc='''You were either a bomb disposal or a demolitions expert.You just love the smell of napalm in the morning. Something about the smell of explosives, or maybe the very loud boom they make, is very pleasing to you. Of course, you can't discount the whiz of shrapnel, oh, and the display, the coruscating fireballs...''',
    available_exploits=[{'Name': 'Home-cooking', 'Desc': '''You can make an explosive out of regular household items (a minimum of 4 components) with a minute of work. This explosive deals 2d6 heat damage to all within 5'. The explosives can be stored, but only up to four hours.'''},
                        {'Name': 'Booby-trapping', 'Desc': '''Using a home-cooked device (made as above), a grenade, or similar explosive, you can rig a door, trunk, or object to explode when opened or at a specific time. This takes 2 actions and is obvious. By spending 5 minutes you can hide it; anyone activating it gets an opposed check (their INT vs. your AGI) to notice the trap before it is set off.'''},
                        {'Name': 'Boom-boom', 'Desc': '''Explosive devices, such as grenades, do +!d6 damage when you use them.'''},
                        {'Name': 'Shaped charge', 'Desc': '''You know exactly how to target explosives. You may direct any area of effect attack with a radius so that it explodes in a cone in a single direction. The cone size is equal to the diameter (not radius) of the original explosion, so a 5' radius explosion can be directed into a 10' cone.'''},
                        {'Name': 'Disarm bomb', 'Desc': '''If you have a minute to spare, you can disarm any explosive device. If it is timed, it dramatically happens at the last second.'''},
                        {'Name': 'Duck-and-cover', 'Desc': '''You know how to avoid damage from explosives and similar effects. You take half damage from area of effect attacks.'''},
                        {'Name': '''Don't step there!''', 'Desc': '''You always notice explosive devices and traps within 10' of you, even if an attribute check would normally be required.'''}])

career_now_firefighter = Career(
    name='Firefighter',
    career_time='1d6',
    career_time_unit='years',
    prereq='none',
    agility=1, endurance=1, intuition=1, luck=1,
    available_skills=['climbing', 'carrying', 'jumping', 'carousing', 'explosives', 'local knowledge'],
    desc='''Fighting fires is a noble calling, putting yourself at risk to help others.''',
    available_exploits=[{'Name': 'Fire-resistant', 'Desc': '''You've been through many fires, and have developed a resistance to it. You gain natural SOAK 5 (heat).'''},
                        {'Name': 'Ladder-climber', 'Desc': '''You spend a lot of time climbing ladders, broken stairs, even drainpipes and walls. You gain a CLIMB speed equal to your regular SPEED.'''},
                        {'Name': '''Fireman's lift''', 'Desc': '''When carrying another person, you are not encumbered or slowed in any way.'''},
                        {'Name': 'Door breaker', 'Desc': '''Your dice pool explodes when you are breaking down a door.'''},
                        {'Name': 'Hold breath', 'Desc': '''Like a swimmer, you have learned to hold your breath; in your case it's so that you do not inhale noxious fumes or smoke. You can hold your breath for one minute per point of INT.'''},
                        {'Name': 'Extinguish', 'Desc': '''You can extinguish flames in an adjacent square by spending one action.'''},
                        {'Name': 'Drop and roll', 'Desc': '''You can completely remove the Fire status track from yourself or an adjacent creature by spending two actions.'''}])

career_now_gambler = Career(
    name='Gambler',
    career_time='1d6',
    career_time_unit='years',
    prereq='[gaming]',
    intuition=1, charisma=1, luck=1, reputation=1,
    available_skills=['[gaming]', '[social]', 'thievery'],
    desc='''You became an expert gambler, proficient at games of skill and chance.''',
    available_exploits=[{'Name': 'Good game', 'Desc': '''Make a LUC attribute check and multiply by $100. You win that much money.'''},
                        {'Name': 'Lucky streak', 'Desc': '''You may replenish your LUCK attribute an extra time each day.'''},
                        {'Name': 'Cheat', 'Desc': '''You know a couple of tricks. In a game of chance, you may reroll any 1s in your dice pool.'''}])

career_now_gangster = Career(
    name='Gangster',
    career_time='1d6',
    career_time_unit='years',
    prereq='intimidate',
    strength=1, intuition=1, charisma=1, reputation=1,
    available_skills=['intimidation', 'thievery', 'driving', 'pistols'],
    desc='''Eventually your life of crime led you to better things as you fell into a gang or crew.''',
    available_exploits=[{'Name': 'Intimidating', 'Desc': '''Intimidation is your way of life, especially in the criminal underworld. When attempting to intimidate a criminal, you gain a +1d6 bonus.'''},
                        {'Name': 'Protection racket', 'Desc': '''A protection racket is a lucrative and steady stream of income. Within your REP sphere you have a route. You gain your REP x $100 each week. This exploit cannot be used during downtime.'''}])

career_now_guerrilla_fighter = Career(
    name='Guerrilla Fighter',
    career_time='1d6',
    career_time_unit='years',
    prereq='survival',
    endurance=1, intuition=1, luck=1, reputation=1,
    available_skills=['bravery', 'pistols', 'rifles', 'stealth', 'tactics', 'survival', 'perception', 'disguise'],
    desc='''Either as a dangerous lone wolf or as part of an organized resistance, you're experienced with waging war on the go, mounting military strikes that melt away quickly afterward. After taking a grade in this career, roll 1d6; on a 2 or less, the next career you take must be Prison.''',
    available_exploits=[{'Name': 'Ambush expert', 'Desc': '''During an ambush turn you can take a second action.'''},
                        {'Name': 'Blend in', 'Desc': '''If you are a wanted fugitive or actively being pursued by someone, you can disappear into a crowd twice per day.'''},
                        {'Name': 'Hit-and-run', 'Desc': '''You can move from out of line of sight, into firing position, make an attack action, and then back to out of line of sight twice per day.'''},
                        {'Name': 'Always read', 'Desc': '''Sleep in armor with no penalty. Anyone sneaking up on you while you sleep must make a Difficult [16] AGI check to do so.'''},
                        {'Name': 'Sabotage', 'Desc': '''You can prepare booby-traps using home-made devices as an explosives expert. There is no duration for how long one of your home-cooked devices remains potent, and it may be rigged to go off at any time.'''}])

career_now_hacker = Career(
    name='Hacker',
    career_time='1d6',
    career_time_unit='years',
    prereq='computers',
    logic=1, intuition=1, luck=1, reputation=1,
    available_skills=['computers', 'reactions', 'cryptology', 'appraisal', 'forgery', 'linguistics', 'electronics', 'bureaucracy'],
    desc='''Hacking into computer systems to find information or manipulate events comes easily to you.''',
    available_exploits=[{'Name': 'Hacking rig', 'Desc': '''You gain a high quality laptop or portably computer designed for hacking on the move.'''},
                        {'Name': 'Red lights', 'Desc': '''(requires Hacking Rig) You can use your hacking rig to change traffic lights to any configuration you wish.'''},
                        {'Name': 'Bank job', 'Desc': '''A virtual bank job gains you $1,000 and +1 REP.'''},
                        {'Name': 'City hall', 'Desc': '''You can hack into security agencies, including the police and intelligence agencies, to gain information about any individual whose name you know, assuming those agencies have that information. This takes you one hour.'''},
                        {'Name': 'Security override', 'Desc': '''You can remotely unlock an electronic lock for up to one minute.'''},
                        {'Name': 'CCTV', 'Desc': '''You are able to access the CCTV cameras of a given location. This gives you poor quality video, and no audio.'''}])

career_now_heavy_gunner = Career(
    name='Heavy Gunner',
    career_time='1d6',
    career_time_unit='years',
    prereq='heavy weapons.',
    strength=1, endurance=1, intuition=1, willpower=1,
    available_skills=['carrying', 'hardy', 'heavy weapons', 'running', 'gunnery', 'engineering'],
    desc='''A real weapon is the kind that requires a strap, and if it doesn't kick like a mule when you fire it, the gun just isn't for you. Whether a specialist for a security team or mercenary group, or party of a a heavy weapons team in the military, you've spent plenty of time around big guns.''',
    available_exploits=[{'Name': 'Lay down fire', 'Desc': '''You can spray an area 15'x15' (3 squares by 3 squares), doing 1d6 damage to every target within that area when using a heavy weapon designated auto.'''},
                        {'Name': '''This ain't heavy.''', 'Desc': '''Choose one heavy weapon; when you carry one of these weapons, it does not count against your carrying capacity.'''},
                        {'Name': 'Long range', 'Desc': '''Increase the range of heavy weapons you wield by 10'.'''},
                        {'Name': 'Heavy specialty', 'Desc': '''You deal +1d6 damage with your chosen weapon for the This Ain't Heavy ability. You can repair it if broken (it takes 1 minute), and draw it as a free action.'''}])

career_now_infiltrator = Career(
    name='Infiltrator',
    career_time='1d6',
    career_time_unit='years',
    prereq='stealth, [combat]',
    strength=1, agility=1, endurance=1, intuition=1,
    available_skills=['[combat skills]', 'stealth', 'thievery', 'escape arts', 'acrobatics', 'climbing'],
    desc='''The pinnacle of special operations, either police, military or freelance, the infiltrator aptly describes the occupation of many men and women whose job it is to infiltrate enemy locations and accomplish dangerous missions. An infiltrator needs a range of skills beyond the mere ability to kill that is the hallmark of the assassin.''',
    available_exploits=[{'Name': 'Quick-hide', 'Desc': '''You are able to disappear while in plain sight. You can make a stealth check even while under observation to move your speed and become effectively invisible for a round. You may then make regular stealth checks as normal, but cannot repeat this feat against the same observer.'''}])

career_now_laborer = Career(
    name='Laborer',
    career_time='1d6',
    career_time_unit='years',
    prereq='none',
    strength=1, endurance=1, charisma=1, luck=1,
    available_skills=['[crafting]', 'carousing', 'hardy', 'computers', '[outdoor]', 'bureacracy', 'engineering', '[vehicle]'],
    desc='''You did a regular physical job, whether skilled or unskilled, performing manual work for a fair wage. You may have been in construction, a gravedigger, even a street-sweeper or cleaner; or perhaps a delivery person, baker, brewer or other worker.''',
    available_exploits=[{'Name': 'Jack-of-all-trades', 'Desc': '''You gain three skills from your skill choices list above at rank 3 (2d6). This does not increase a skill above 3 ranks.'''},
                        {'Name': 'Danger pay', 'Desc': '''Some work is dangerous. Perhaps you worked high on a skyscraper or cleaned toxic waste. You gain $1,000 bonus money and +1 REP.'''},
                        {'Name': 'Union', 'Desc': '''You were a member of a union. Your pay is higher (gain +2 REP) and you gain 1 rank (1d6) in law and bureaucracy.'''},
                        {'Name': '''Worker's clothes''', 'Desc': '''Over the years you have patched together a "uniform" of sorts which protects you from hazards - hardhat, goggles, high strength clothing, gloves, sturdy boots, and so on. This constitutes light armor with a SOAK of 5, but is a custom piecemeal outfit which can only be worn by you. The uniform also includes a engineer's toolkit, hearing protection, a respirator, and it protects you from non-extreme environmental effects.'''}])

career_now_lawyer = Career(
    name='Lawyer',
    career_time='1d6',
    career_time_unit='years',
    prereq='law',
    logic=1, willpower=1, charisma=1, reputation=1,
    available_skills=['law', 'interrogation', 'bluffing', 'bureaucracy', 'local knowledge', 'negotiating'],
    desc='''You became a lawyer, learning the complexities of the legal system, and how to get yourself and others out of (or into!) trouble.''',
    available_exploits=[{'Name': 'Get out of jail free', 'Desc': '''When arrested for a minor offence, you are able to use legal techniques to keep yourself out of jail.'''},
                        {'Name': 'Court records', 'Desc': '''You have access to court records, and can look up the criminal record of any named individual given an hour's notice and a computer connection (or physical access to the courthouse).'''},
                        {'Name': 'Orator', 'Desc': '''You can be very persuasive, and know how to bend a jury or other group of people to your point of view. You can influence up to 12 people within 30' with a 15-minute speech. Make a CHA mental attack; if successful, the group moves one stage along the Charm status track.'''},
                        {'Name': 'Ambulance-chaser', 'Desc': '''You spent time making money the only way you could. You start play with $1,000 extra money.'''},
                        {'Name': 'Crusader.', 'Desc': '''A principled public defender or prosecutor, you're in it for the ideals. You'll make the world a better place using the power of law. You gain the following skills at 1 rank (1d6): intimidation, bureaucracy, conviction. This does not increase a skill beyond one rank.'''}])

career_now_medic = Career(
    name='Medic',
    career_time='1d6',
    career_time_unit='years',
    prereq='medicine',
    agility=1, intuition=1, logic=1, charisma=1,
    available_skills=['computers', 'medicine', 'bureaucracy', 'psychology'],
    desc='''You enter the medical profession. If you have gained a doctorate at college, you do so as a doctor; otherwise you are referred to as a nurse or medic.''',
    available_exploits=[{'Name': 'Medical knowledge base', 'Desc': '''Choose four [medical] skills. You gain these four skills at 1 rank (1d6). This does not increase the rank of an existing skill.'''},
                        {'Name': 'Bedside manner', 'Desc': '''You gain a medical kit. Your long-term care is of such quality that your patient gains an additional 1d6 HEALTH per day. You may only have one patient under your long-term care at a time.'''},
                        {'Name': 'Consultant (requires Doctorate', 'Desc': '''. You are a highly paid consultant doctor. Your REP increases by 2 and you start play with a bonus $1,000.'''},
                        {'Name': 'Ward management [requires Bedside Manner].', 'Desc': '''You are an expert at running and managing a ward or sickbay. The number of patients you can have under your long-term care is increased to the value of your LOG attribute.'''},
                        {'Name': 'Diagnosis', 'Desc': '''You gain +1d6 bonus to identify or treat diseases. Make a Difficult [16] LOG check before advancing any attributes. If you succeed, you discovered a new disease or illness which is named after you; you also gain 1 bonus REP attribute point.'''},
                        {'Name': 'Healing hands', 'Desc': '''Using basic medical equipment, you can heal 1d6 points of HEALTH to an adjacent creature as a single action. Any given creature can only benefit from your healing in this way once per day.'''},
                        {'Name': 'Exceptional healing hands [requires Healing Hands]', 'Desc': '''Your Healing Hands ability increases to 2d6 points of HEALTH.'''},
                        {'Name': 'Psychologist', 'Desc': '''An expert in matters of the mind, you gain +2 MENTAL DEFENSE and once per day you can automatically remove a mental (WIL-based) status track from yourself or an adjacent ally by spending two actions.'''},
                        {'Name': 'Resuscitation [requires Exceptional Healing Hands].', 'Desc': '''You can revive a seemingly dead creature with a LOG check. The creature must have “died” within the last five minutes, and the difficulty value of the check is 20 + the damage of the attack that killed it. The creature wakes up with 1 HEALTH.'''}])

career_now_miner = Career(
    name='Miner',
    career_time='1d6',
    career_time_unit='years',
    prereq='none',
    strength=1, endurance=1, willpower=1, luck=1,
    available_skills=['carrying', 'climbing', 'survival', '[technical]', 'mining', 'appraising', 'carousing', 'picks', 'hammers'],
    desc='''There's nothing like a few years spent down a coalmine to build character.''',
    available_exploits=[{'Name': 'Underground sense', 'Desc': '''When underground you can always determine direction and depth and pick a route to the surface.'''},
                        {'Name': 'Darksight', 'Desc': '''You have spent so much time below ground that you've developed darksight to a distance of 30'.'''},
                        {'Name': 'Mining hazards', 'Desc': '''You gain a +2d6 bonus to spot underground hazards and traps.'''},
                        {'Name': 'Toxic gases', 'Desc': '''The underground is full of toxic fumes, and you've become used to them. You gain a poison SOAK of 5.'''},
                        {'Name': 'Identify substance', 'Desc': '''You can identify by sight any mineral or metal based substance automatically.'''}])

career_now_ninja = Career(
    name='Ninja',
    career_time='1d6',
    career_time_unit='years',
    prereq='martial arts',
    agility=1, endurance=1, intuition=1, power=1,
    available_skills=['acrobatics', 'climbing', 'disguise', 'perception', 'stealth', 'martial arts'],
    desc='''The skills and tactics of Japan's warriors of subterfuge, sabotage, and deception are known to you, either through a Ninja master that took you in as an apprentice, or by traveling to the ancestral homeland and earning the right to train among those who still practice ninjutsu.''',
    available_exploits=[{'Name': 'Poison', 'Desc': '''With one minute of preparation, you can craft poison and apply it to one weapon; for one minute, that weapon deals +1d6 poison damage; you must deal enough damage to bypass a target's SOAK to deal this poison damage.'''},
                        {'Name': 'Fast climb', 'Desc': '''You gain a CLIMB speed equal to your regular SPEED.'''},
                        {'Name': 'Gas poison (requires Poison).', 'Desc': '''By spending an action, you can deliver your poison as a dust or small burst of gas that ignores the target's SOAK. You can throw this with a range increment of 2.'''},
                        {'Name': 'Weapon master', 'Desc': '''. You can draw and sheathe a sword, staff, club, spear, naginata, kusarigama, and shuriken as a free action. Choose one of these weapons; you receive a +1d6 to damage with this weapons.'''},
                        {'Name': 'Death strike', 'Desc': '''Once per day you may strike a creature that is not aware of your presence or does not realize you are an enemy with surprising, lethal force. Make an attack roll using your CHI attribute; if you hit, you deal double damage.'''},
                        {'Name': 'Shadow warrior', 'Desc': '''You may move at full SPEED while hidden if you succeed in your AGI (stealth) check.'''}])

career_now_performer = Career(
    name='Performer',
    career_time='1d6',
    career_time_unit='years',
    prereq='[performance]',
    charisma=2, luck=1, reputation=1,
    available_skills=['carousing', '[performance]'],
    desc='''You became a musician or other performer, and made your way working bars, clubs, and theaters.''',
    available_exploits=[{'Name': 'Triple-threat', 'Desc': '''You gain the skills singing, dancing, and acting at 1 rank (1d6). This does not increase the rank of an existing skill.'''},
                        {'Name': 'Gig', 'Desc': '''. You can make money by playing at bars and doing local performances. You can automatically make an amount equal to a CHA check x $10 per day by doing this. This exploit cannot be used during downtime.'''},
                        {'Name': 'Captivating', 'Desc': '''You have the ability to captivate people with your musical ability. While using your musical instrument or voice, all those who can hear you become beguiled (unable to attack you) until you stop. This requires a CHA vs. MENTAL DEFENSE check and a full two actions each turn.'''},
                        {'Name': 'Lullaby', 'Desc': '''Your music and make people drowsy. While using your musical instrument or voice, all those who can hear you become weary (-1d6 to all physical attribute checks and -1 SPEED) until you stop. This requires a CHA vs. MENTAL DEFENSE check and a full two actions each turn.'''},
                        {'Name': 'Fearful', 'Desc': '''You can use voice or music to instill fear in those who hear it. While using your musical instrument or voice, all those who can hear you become nervous (-1d6 to all interactions with you or with a target or object of your choice) until you stop. This requires a CHA vs. MENTAL DEFENSE check and a full two actions each turn.'''}])

career_now_pilot = Career(
    name='Pilot',
    career_time='1d6',
    career_time_unit='years',
    prereq='piloting',
    agility=1, intuition=1, logic=1, luck=1,
    available_skills=['reactions', 'piloting', 'computers', 'astronomy', 'gunnery', 'navigation'],
    desc='''You became a pilot, learning to fly aircraft big or small.''',
    available_exploits=[{'Name': 'Push the limits', 'Desc': '''You can exceed an aircraft's normal maximum SPEED by 2.'''},
                        {'Name': 'Evasive flying', 'Desc': '''An aircraft which you pilot gains a DEFENSE bonus equal to your AGI attribute dice pool.'''},
                        {'Name': 'Cruise control', 'Desc': '''You are able to easily navigate without an attribute check.'''},
                        {'Name': 'Evasive maneuver [requires Evasive Flying]', 'Desc': '''As an action, you may designate one incoming missile per round and gain an additional +5 DEFENSE against it.'''},
                        {'Name': 'Stay on target [requires Evasive Flying]', 'Desc': '''While in the rear arc of a target ship, you negate any bonus it gets from Evasive Flying.'''}])

career_now_police_officer = Career(
    name='Police Officer',
    career_time='1d6',
    career_time_unit='years',
    prereq='none',
    agility=1, intuition=1, logic=1, reputation=1,
    available_skills=['interrogation', 'pistols', 'law', 'driving', 'bureaucracy', 'perception', 'intimidate'],
    desc='''You join the police or other security force and begin a career as a uniformed officer.''',
    available_exploits=[{'Name': 'Troublesense', 'Desc': '''You are easily able to spot trouble before it happens. You gain a +1d6 bonus to INITIATIVE checks.'''},
                        {'Name': 'Out of place', 'Desc': '''You know the signs of suspicious behavior. You gain a +1d6 bonus to checks made to spot unusual or criminal activity.'''},
                        {'Name': 'Freeze!', 'Desc': '''You can compel a target to “freeze!” with a CHA vs. MENTAL DEFENSE check. If successful, the target stops in his tracks and is stunned until he shakes that condition off. The target must be able to understand you and have an INT attribute of 3 or more. You can only do this to a given target once.'''},
                        {'Name': 'Backup', 'Desc': '''In an allied urban environment, you can call for backup once per day in the form of 1d6 police officers who arrive within 5 minutes and who will follow your orders.'''},
                        {'Name': 'Anti-surveillance', 'Desc': '''You are so familiar with surveillance devices, blind spots, and avoidance techniques that, by moving half your speed, you can render yourself invisible to electronic monitoring equipment.'''}])

career_now_politician = Career(
    name='Politician',
    career_time='1d6',
    career_time_unit='years',
    prereq='local knowledge',
    logic=1, willpower=1, charisma=1, reputation=1,
    available_skills=['[social]', 'politics', 'economics', 'geography', 'history', 'local knowledge'],
    desc='''You entered politics at a local level and started to rise through the ranks.''',
    available_exploits=[{'Name': 'Corruption', 'Desc': '''Not all politicians are corrupt, but you succumbed to temptation. You start play with $2,000 bonus money, but your next career much be the Prisoner career. You may not return to the Politician career after taking this exploit. You may only take this exploit during character creation, and only if this is not your last career.'''},
                        {'Name': 'Idealist', 'Desc': '''You have a platform of ideology, and this gives you great mental strength. You gain +2 MENTAL DEFENSE. Decide what you ideological platform is.'''},
                        {'Name': 'Local elections', 'Desc': '''You won a local election and started representing your community. You gain +1 REP. You can make a REP mental attack against a target within 30' to push them one stage down the Charm status track.'''},
                        {'Name': 'Regional elections (requires Local Elections).', 'Desc': '''You won a regional election and represented the greater community. You gain +2 REP. Your REP attack to influence people can now affect a number of people equal to your CHA score.'''},
                        {'Name': 'Public speaker', 'Desc': '''You are able to sway and influence crowds. You can spend 5 minutes talking to a crowd and make a REP check equal to 1% the size of the crowd (so for a crowd of 2,000 you must beat 20 in your check). If successful, you influence the crowd in some manner, pushing it one stage along the Charm or Anger tracks.'''}])

career_now_priest = Career(
    name='Priest',
    career_time='1d6',
    career_time_unit='years',
    prereq='religion',
    intuition=1, willpower=1, charisma=1, luck=1,
    available_skills=['perception', 'crafting', 'bureaucracy', 'cryptology', 'linguistics', '[trivia]', 'meditation', 'leadership', 'performing', 'religion'],
    desc='''You joined the clergy and practised religion, tending to your flock.''',
    available_exploits=[{'Name': 'Confessional.', 'Desc': '''Your insights into the morality of living things enables you to draw confessions from others. Given an hour of conversation, you gain a +2d6 bonus to checks designed to gain information from another creature.'''},
                        {'Name': 'Unshakeable faith', 'Desc': '''You have faith, a peace of mind and an inner tranquillity which is hard to penetrate. You gain +5 to your MENTAL DEFENSE.'''},
                        {'Name': 'Respect', 'Desc': '''Your position in the clergy grants you a certain reverence from others. Sentient opponents take a -1d6 penalty to attack you on their first attack as long as you have not attacked them first.'''}])

career_now_prisoner = Career(
    name='Prisoner',
    career_time='2d6',
    career_time_unit='years',
    prereq='none',
    strength=1, endurance=1, intuition=1, reputation=1,
    available_skills=['intimidation', 'survival', '[subterfuge skills]', '[unarmed fighting]', 'knives'],
    desc='''Your life of crime ended you up in prison where you served time; or perhaps you were a political prisoner, a hostage, or a prisoner-of-war. It was a tough environment and you spent most of your time just trying to survive, although you did make one or two lifelong contacts.''',
    available_exploits=[{'Name': 'Prison tough', 'Desc': '''You are mentally and physically toughened. Each time you go to prison you gain a permanent +1 bonus to your DEFENSE and MENTAL DEFENSE.'''},
                        {'Name': 'Shiv', 'Desc': '''You are easily able to improvise weapons using your surroundings – glasses, rocks, and so on. You always count as carrying a knife or club and can use the brawling skill with knives and clubs.'''}])

career_now_private_eye = Career(
    name='Private Eye',
    career_time='1d6',
    career_time_unit='years',
    prereq='none',
    intuition=1, charisma=1, luck=1, reputation=1,
    available_skills=['pistols', 'bluffing', 'bribery', 'perception', 'insight', 'tracking', 'intimidate', '[subterfuge]'],
    desc='''You snoop, bribe, tail, and occasionally get socked a few times a month in order to pay the bills. You know all the shady spots in town.''',
    available_exploits=[{'Name': 'Snoop', 'Desc': '''You've got a good sense of when something just isn't quite right; once per day when you roll a check to determine if someone is lying to you, reroll all results of 1 and 2.'''},
                        {'Name': 'Contacts', 'Desc': '''You have a contact in the police force who can conduct routine checks (background, number plates, etc.) for you.'''},
                        {'Name': 'Great detective', 'Desc': '''You are used as an informal consultant by authorities who recognize your expertise. You are permitted access to crime scenes and evidence, and are often called upon.'''},
                        {'Name': 'Hardboiled', 'Desc': '''Cynical and rumpled, you gain a+4 bonus to MENTAL DEFENSE.'''}])

career_now_reporter = Career(
    name='Reporter',
    career_time='1d6',
    career_time_unit='years',
    prereq='none',
    intuition=1, logic=1, charisma=1, reputation=1,
    available_skills=['insight', 'perception', 'linguistics', 'literature', 'law', 'politics', 'economics', 'geography', 'journalism', 'interrogation', 'carousing'],
    desc='''As an intrepid reporter, you are skilled at getting to the truth.''',
    available_exploits=[{'Name': 'Discern lie', 'Desc': '''You always know when somebody is lying to you.'''},
                        {'Name': 'Ask the right question', 'Desc': '''You may spend a LUC die to ask an NPC a yes/no question. The GM will answer truthfully as the NPC gives away the answer either verbally or in some more subtle way.'''},
                        {'Name': 'Research skills', 'Desc': '''You gain 3 ranks in computers, journalism, and one skill from a choice of law, politics, or economics.'''},
                        {'Name': 'Big scoop', 'Desc': '''You uncovered a big secret, and revealed it in the news. Decide what this scoop was. You gain +2 REP. Roll 1d6; on a 6 you won a Pulitzer Prize for it. You may take this exploit mltiple times.'''},
                        {'Name': 'Contact', 'Desc': '''You have a contact in the police force, mayor's office, or similar body. You can call on this contact for information once per month. You may take this exploit multiple times, gaining a new contact each time.'''},
                        {'Name': 'Tabloid hack', 'Desc': '''You worked as the lowest of the low, a tabloid journalist interested only in shocking your readers. Sadly, it's a profitable job, and you start play with $1,000 extra money. However, if you take this exploit, you lose any contacts you had from the Contact exploit, and may not take that exploit in future.'''}])

career_now_sailor = Career(
    name='Sailor',
    career_time='1d6',
    career_time_unit='years',
    prereq='none',
    agility=1, intuition=1, luck=1, endurance=1,
    available_skills=['carousing', 'climbing', 'clubs', 'fishing', 'knives', 'leadership', 'navigation', 'sailing', 'swimming'],
    desc='''At home on the sea, you spent time aboard a ship mastering the art of sailing.''',
    available_exploits=[{'Name': 'Any Port', 'Desc': '''You may take this exploit multiple times. Each time you take it, you may designate an additional port town. At that location, you will have one contact upon whom you can (generally) rely, and one bar at which you can drink for free.'''},
                        {'Name': 'Grog', 'Desc': '''While you may well enjoy a drink, you never suffer any penalties from intoxication via alcohol.'''},
                        {'Name': 'Hold Breath', 'Desc': '''(requires Swimmer) You gain two additional countdown dice when holding your breath.'''},
                        {'Name': 'Lookout', 'Desc': '''Lookout duty is a mandatory part of a sailor's life. You gain +1d6 to perception checks.'''},
                        {'Name': 'Sea Legs', 'Desc': '''You adapt to the motion of a ship; this makes you very hard to knock down. When you are knocked prone, you may make a Challenging [13] AGI check; if you succeed, you remain standing.'''},
                        {'Name': 'Seasick', 'Desc': '''You are immune to the Nausea status track.'''},
                        {'Name': 'Sea Weather', 'Desc': '''You are able to ignore the effects of rain, wind, mist, and fog.'''},
                        {'Name': 'Swimmer', 'Desc': '''You gain a SWIM speed equal to your regular SPEED.'''}])

career_now_scientist = Career(
    name='Scientist',
    career_time='1d6',
    career_time_unit='years',
    prereq='one [scientific] skill',
    intuition=1, logic=1, willpower=1, reputation=1,
    available_skills=['computers', '[scientific]', '[technical]', 'survival', 'perception'],
    desc='''You take your science with you as investigate phenomena in strange locations. Field scientists are viewed by academia as adventurous types, and include archaeologists, meteorologists, zoologists, oceanographers, geologists, botanists, astrophysicists, and much more.''',
    available_exploits=[{'Name': 'Scientific knowledge base', 'Desc': '''Choose four [scientific] skills. You gain these four skills at 1 rank (1d6). This does not increase the rank of an existing skill.'''},
                        {'Name': 'Analytical eye', 'Desc': '''You are able to identify the resistances, immunities, and vulnerabilities of any creature you can see with a Difficult [16] LOG check. This requires two full actions of observation.'''},
                        {'Name': 'Improviser', 'Desc': '''In the field, you need to improvise. Using your scientific know-how, you can create a crude object or device from your surroundings. This requires a LOG check, with a difficulty value equal to the purchase value of the object, and takes 30 minutes.'''},
                        {'Name': 'Experimental device', 'Desc': '''You may produce an experimental device once per day which allows you to use your LOG attribute in place of any other attribute for one attribute check. The device breaks permanently after use.'''}])

career_now_scout = Career(
    name='Scout',
    career_time='1d6',
    career_time_unit='years',
    prereq='stealth, tracking',
    agility=1, endurance=1, intuition=1, willpower=1,
    available_skills=['stealth', 'perception', 'survival', 'tracking', 'climbing', 'running'],
    desc='''You became a scout – a specialized special forces soldier able to operate alone and perform reconnaissance.''',
    available_exploits=[{'Name': 'Ambusher', 'Desc': '''You gain a +1d6 bonus to access the ambush turn.'''},
                        {'Name': 'Hustle', 'Desc': '''Your SPEED increases by 2.'''},
                        {'Name': 'Hostile terrain', 'Desc': '''You do not suffer penalties for moving across difficult terrain.'''},
                        {'Name': 'Swimmer', 'Desc': '''You gain a SWIM speed equal to your regular SPEED.'''},
                        {'Name': 'Climber', 'Desc': '''You gain a CLIMB speed equal to your regular SPEED.'''}])

career_now_sensei_sifu = Career(
    name='Sensei/Sifu',
    career_time='1d6',
    career_time_unit='years',
    prereq='martial arts 3 ranks',
    agility=1, intuition=1, willpower=1, reputation=1,
    available_skills=['martial arts', 'philosophy', 'tactics', 'insight', 'leadership', 'teaching', 'local knowledge'],
    desc='''You run a dojo, wu kwan, or kwoon, teaching others the martial arts.''',
    available_exploits=[{'Name': 'Inspiring', 'Desc': '''You inspire respect in your students. Those within 30' of can claim a +1d6 bonus to any attribute roll once per day.'''},
                        {'Name': 'Teacher', 'Desc': '''You are able to "lend" somebody one rank in a skill for up to one day. Only one person at a time can benefit from this ability.'''},
                        {'Name': 'Heirloom weapon', 'Desc': '''You gain one high quality Eastern weapon.'''},
                        {'Name': 'Protégé', 'Desc': '''(requires Inspiring and Teacher) You gain a protégé. This is a martial artist who has half your grade. The protégé accompanies you and assists you. If your protégé dies, you must take this exploit again in order to replace him or her. You may only have one protégé at a time.'''},
                        {'Name': 'First-aid', 'Desc': '''Used to injuries in the dojo, you are able to heal an adjacent ally 1d6 HEALTH by using one action. Any given creature can only benefit from this ability once per day.'''}])

career_now_smuggler = Career(
    name='Smuggler',
    career_time='1d6',
    career_time_unit='years',
    prereq='piloting or sailing',
    agility=1, charisma=1, luck=1, reputation=1,
    available_skills=['thievery', 'navigation', 'carousing', 'piloting', 'sailing', 'bluffing', 'appraisal', 'pistols'],
    desc='''You spent time as a smuggler, moving stolen or illegal goods from one country to another.''',
    available_exploits=[{'Name': 'Smuggle', 'Desc': '''You know how to hide objects, either about your person or in a location. You gain a +2d6 bonus to attempts to hide items.'''},
                        {'Name': 'Haggler.', 'Desc': '''You're a born haggler, and can reduce the cost of any purchase by 3d6%. This does not stack with any other exploits which reduce purchase costs.'''},
                        {'Name': 'Fence', 'Desc': '''In an urban environment, you can sell goods for 75% of normal cost rather than 50%.'''},
                        {'Name': 'Seat of your pants', 'Desc': '''Smugglers rely a lot on old-fashioned luck and bravado. They can recharge their LUCK pool an extra time per day.'''}])

career_now_sniper = Career(
    name='Sniper',
    career_time='1d6',
    career_time_unit='years',
    prereq='stealth, rifles',
    endurance=1, intuition=1, willpower=1, luck=1,
    available_skills=['rifles', 'stealth', 'perception', 'concentration', 'climbing'],
    desc='''You mastered the art of lying very still for long periods of time and shooting people a long way away. Sniping is a job which requires great endurance, patience, and accuracy.''',
    available_exploits=[{'Name': 'Vantage point', 'Desc': '''You gain an additional 1d6 to attack with a ranged weapon if you are at least 30' higher than your target. This stacks with the regular bonus for high ground.'''},
                        {'Name': 'Steady eye', 'Desc': '''All weapon range increments increase by 50%.'''},
                        {'Name': 'Good position', 'Desc': '''You cannot be pinned down in combat.'''}])

career_now_socialite = Career(
    name='Socialite',
    career_time='1d6',
    career_time_unit='years',
    prereq='[social]',
    charisma=2, reputation=2,
    available_skills=['[social]'],
    desc='''You aim be famous for being famous, and mastered the art of networking.''',
    available_exploits=[{'Name': 'High class', 'Desc': '''You are at home when in high-class social gatherings. In such environments, you gain a +1d6 bonus to all attribute checks. Unfortunately, you are less comfortable – or welcome - in lower-class environments, and suffer a -1d6 penalty to all social interactions in such situations.'''}])

career_now_soldier = Career(
    name='Soldier',
    career_time='1d6',
    career_time_unit='years',
    prereq='must have completed one year in Boot Camp',
    strength=1, endurance=1, willpower=1, reputation=1,
    available_skills=['carrying', '[combat]', 'hardy', 'survival', 'leadership', 'carousing', 'bravery', 'perception'],
    desc='''A tour of duty in the army means a deployment to a probably dangerous environment where you engaged enemy forces in infantry based ground battles. The army prides itself on their sense of duty and their courage. With each tour, roll 1d6. On a roll of 6, you gain a medal and a bonus +1 REP.''',
    available_exploits=[{'Name': 'Battle scars', 'Desc': '''You've received so many battle scars that you sometimes don't notice injury. You gain a natural SOAK bonus of 2.'''},
                        {'Name': 'Quick naps', 'Desc': '''You've learned to manage with little sleep. As long as you get 4 hours, you count as fully rested.'''},
                        {'Name': 'Get on with it.', 'Desc': '''Your platoon doesn't have much patience for whining about minor injuries. Once per day you can pause for two actions and recover 2d6 HEALTH.'''},
                        {'Name': 'Shake it off.', 'Desc': '''You gain a +1d6 bonus when attempting to shake off a condition.'''},
                        {'Name': 'Platoon leader', 'Desc': '''You grant your entire party a +1d6 INITIATIVE bonus as long as they are within 30' of you.'''}])

career_now_spy = Career(
    name='Spy',
    career_time='1d6',
    career_time_unit='years',
    prereq='none',
    agility=1, intuition=1, charisma=1, luck=1,
    available_skills=['interrogation', 'law', '[subterfuge]', 'computers', 'pistols', '[social]', '[gaming]'],
    desc='''You're a spy. This may be MI6, CIA, KGB, or some other force. You have a wide remit, dealing with both domestic and external threats, and perform undercover investigations into military and civilian issues.''',
    available_exploits=[{'Name': 'False identify', 'Desc': '''You are able to create a false identity, complete with background records, in one day. This identity is good enough that people can look you up on various databases, and the details will match.'''},
                        {'Name': 'Off the grid', 'Desc': '''You know how to disappear without trace, dropping off the grid completely. No location discerning checks or abilities can find you unless you want them to.'''},
                        {'Name': 'Safe house', 'Desc': '''(requires Off the Grid) You can use a safe house on any populated planet to grant your off the grid ability to your entire party.'''},
                        {'Name': 'Monologue', 'Desc': '''Once per day you can make a CHA vs. MENTAL DEFENSE attack against an enemy. If successful, your target explains their plan with a short monologue.'''},
                        {'Name': 'Miraculous escape', 'Desc': '''Once per day you may automatically succeed in one attempt to escape handcuffs or other restraints.'''},
                        {'Name': 'Q-Branch', 'Desc': '''You start play with one gadget from the equipment chapter of your choice.'''},
                        {'Name': 'Golden Gun', 'Desc': '''You gain a high quality pistol of your choice. This pistol already has the extra damage upgrade (+1d6 damage). It is not actually golden.'''}])

career_now_street_thug = Career(
    name='Street Thug',
    career_time='1d6',
    career_time_unit='years',
    prereq='none',
    strength=1, endurance=1, charisma=1, luck=1,
    available_skills=['intimidation', 'running', 'brawling', 'clubs', 'knives', 'pistols'],
    desc='''You fell into the fringes of society and ended up as a thug on the street, committing petty crimes for small amounts of money.''',
    available_exploits=[{'Name': 'The filth', 'Desc': '''You have developed an uncanny ability to detect cops. When attempting to sniff out a police officer or similar authority figure, you gain a +1d6 bonus.'''},
                        {'Name': 'Street tough', 'Desc': '''Life on the streets is tough. You gain a natural +2 SOAK.'''}])

career_now_student = Career(
    name='Student',
    career_time='1',
    career_time_unit='years',
    prereq='18 years of age or under',
    intuition=1, logic=1, charisma=1, luck=1,
    available_skills=['[academic]', '[scientific]', '[sporting]'],
    desc='''High School, or its equivalent, is a place of learning... and sometimes of adventure!''',
    available_exploits=[{'Name': 'Walker', 'Desc': '''Before you learned to drive you had to walk everywhere. You gain SPEED +1.'''},
                        {'Name': 'Mentor', 'Desc': '''One of your teachers is a mentor to you. Choose one skill. He or she has 10 ranks (4d6) in that skill and will use it to assist you.'''},
                        {'Name': 'Wrong crowd', 'Desc': '''You got in with the wrong crowd. You gain 1 rank (1d6) in carousing, intimidation, and thievery. This does not increase a skill beyond 1 rank.'''},
                        {'Name': 'Chess club', 'Desc': '''You joined the Chess Club, or a similar club. Gain logic=1, and 3 ranks (2d6) in chess (or a similar subject).'''},
                        {'Name': 'Wheels', 'Desc': '''You got given a car at an early age. It's not a great car, but it's a car. Gain a car with a value of up to $1,000.'''}])

career_now_stuntman = Career(
    name='Stuntman',
    career_time='1d6',
    career_time_unit='years',
    prereq='none',
    agility=1, endurance=1, luck=1, reputation=1,
    available_skills=['[physical]', '[vehicle]', 'hardy'],
    desc='''You've rolled cars, jumped off buildings, jumped open drawbridges, even set yourself on fire in the name of entertainment.''',
    available_exploits=[{'Name': 'Broken every bone', 'Desc': '''You've broken most every bone in your body at one time or the other. You gain natural SOAK 5.'''},
                        {'Name': 'Fast-healer', 'Desc': '''You need to heal fasts to make it in the stuntman business. When you roll for natural healing each day, add an extra 2d6.'''},
                        {'Name': 'Patched up', 'Desc': '''Once per day you can patch yourself up, recovering 2d6 HEALTH. This takes two actions.'''},
                        {'Name': 'Resilient', 'Desc': '''You have an extra 2d6 HEALTH.'''},
                        {'Name': 'Jumping off buildings', 'Desc': '''You take half normal falling damage.'''},
                        {'Name': 'Grit your teeth', 'Desc': '''You are immune to the Pain status track. It's not that you don't feel pain, it's that you're so used to it.'''}])

career_now_survivalist = Career(
    name='Survivalist',
    career_time='1d6',
    career_time_unit='years',
    prereq='any [outdoor] skill',
    endurance=1, intuition=1, willpower=1, luck=1,
    available_skills=['geography', 'reactions', '[crafting]', 'fishing', 'hunting', 'climbing', 'swimming', 'carrying', 'medicine', 'survival', 'cooking', 'animal handling', 'tracking', 'navigation'],
    desc='''Some choose to spend time in the wild, testing their mind and body against nature, living off the land, and existing with animals.''',
    available_exploits=[{'Name': 'Spot poison', 'Desc': '''A survivalist needs to know what to eat and what not to. By sniffing and taking very tiny tastes, you are able to detect the presence of poison.'''},
                        {'Name': 'Poison resistance', 'Desc': '''You gain SOAK (5) to poison. If you take this exploit a second time it increases to SOAK 10. A third time, you become immune to poisons.'''},
                        {'Name': 'Animal knowledge', 'Desc': '''You know a lot about animals. You automatically know the vulnerabilities and abilities of any creature of the beast creature type.'''},
                        {'Name': 'Move without trace', 'Desc': '''You know how not to leave tracks. You gain +1d6 to stealth checks related to tracking and the avoidance of it, and to avoid non-visual animal senses such as scent.'''},
                        {'Name': 'Improvised weapon', 'Desc': '''You can craft a spear, knife, or bow from your natural surroundings. This takes you five minutes, and the item does not count as an improvised weapon when you use it.'''}])

career_now_teacher = Career(
    name='Teacher',
    career_time='1d6',
    career_time_unit='years',
    prereq='any [academic], [artistic], [performance] or [scientific skill], or linguistics',
    intuition=1, logic=1, charisma=1, luck=1,
    available_skills=['teaching', 'insight', 'leadership', 'linguistics', '[scientific]', '[academic]', '[artistic]'],
    desc='''Your calling is teaching others. You are a mentor figure, a font of learning, and a source of inspiration.''',
    available_exploits=[{'Name': 'Advice', 'Desc': '''You may freely donate your LUC dice to anybody within 30'. The dice must be used immediately.'''},
                        {'Name': 'Role-model', 'Desc': '''Allies within 30' of you gain +2 MENTAL DEFENSE.'''},
                        {'Name': 'Textbook', 'Desc': '''You may choose any skill. You have a textbook about that subject on you. You have that skill at the same number of ranks as your LUC score. You may change your textbook and switch to a different skill by visiting a library, bookstore, or other source of books. This may not be a skill you use a physical attribute (STR, AGI, END) with.'''},
                        {'Name': 'Professor', 'Desc': '''You became a professor. You gain +1 REP and you have a textbook out. Name your textbook. When dealing with people in that field of study, your REP dice explode.'''}])

career_now_trader = Career(
    name='Trader',
    career_time='1d6',
    career_time_unit='years',
    prereq='none',
    intuition=1, charisma=1, luck=1, reputation=1,
    available_skills=['appraisal', '[social]', 'carousing', '[crafting]', 'bureaucracy', 'accounting', 'law', 'local knowledge', 'bribery', 'forgery'],
    desc='''Life as a trader can mean profit, but it can also bring ruin.''',
    available_exploits=[{'Name': 'Sale of the century', 'Desc': '''You worked hard on a great deal, and it netted you $1,000. You may repeat this exploit gaining $1,000 each time.'''},
                        {'Name': 'Trade route', 'Desc': '''You know the best, most profitable trade routes. Your fuel costs are reduced by 20%.'''},
                        {'Name': 'Haggler', 'Desc': ''' You know how to get a good deal. You reduce the cost of any purchase by 2d6%.'''}])

career_now_vigilante = Career(
    name='Vigilante',
    career_time='1d6',
    career_time_unit='years',
    prereq='none',
    agility=1, endurance=1, intuition=1, reputation=1,
    available_skills=['[subterfuge]', '[combat]', 'intimidation'],
    desc='''Something about the world calls to you, asking—no, demanding—that you rise above the law to accomplish some task. You might battle crime, fight against a corrupt corporation, or work to clean the world of dirty politicians, but you are often at odds with the law, using measures they're unable to utilize to get the job done.''',
    available_exploits=[{'Name': 'Inside contacts', 'Desc': '''You know people who know people who know people. You might have a reliable ear in the underworld, a police detective neighbor that talks too much, or a wiretap to the commissioner's phone. Regardless of your exact source, you can spend 4 hours to make a Challenging [13] INT check to learn valuable information about a specific target. For every stage you exceed the minimum check, you learn one more piece of information about the target; for example, an INT check result of 16 would tell you two pieces of information, an INT check result of 21 would tell you three pieces of information, and so on.'''},
                        {'Name': 'My city', 'Desc': '''Choose a city or other area. In that area, you receive +1d6 on checks made to hide or move quietly while there.'''},
                        {'Name': 'Iconic vehicle', 'Desc': '''If you possess a vehicle, it gains two enhancements. If you don't yet have one, you receive a vehicle with one enhancement.'''},
                        {'Name': 'Signature weapon', 'Desc': '''Choose one melee weapon. You gain a high quality version of that weapon, and you do +1d6 damage with it.'''}])

career_now_warrior_monk = Career(
    name='Warrior-Monk',
    career_time='1d6',
    career_time_unit='years',
    prereq='religion or martial arts',
    agility=1, endurance=1, willpower=1, power=1,
    available_skills=['[artistic]', 'acrobatics', 'dancing', 'martial arts', 'philosophy', 'religion', 'staves'],
    desc='''You became a member of a martial monastic order, and were trained in philosophy and martial arts. You should also take grades in a martial arts career.''',
    available_exploits=[{'Name': 'Defensive Stance.', 'Desc': '''You gain +4 to your MELEE DEFENSE as long as you are unarmed and not wielding a shield or wearing armor. This does not stack with Drunken Fist.'''},
                        {'Name': 'Drunken Fist', 'Desc': '''When intoxicated through alcohol, you gain +4 to both your MELEE and RANGED DEFENSE. This does not stack with Defensive Stance.'''},
                        {'Name': 'Elemental Fist', 'Desc': '''(requires Iron Fist, CHI 2+) Your fist is surrounded by the glow of elemental energy. The damage type becomes heat, and does an additional +1d6 damage.'''},
                        {'Name': 'Iron Fist', 'Desc': '''Your unarmed damage increases by 1d6. This does not stack with other exploits or equipment which increase your unarmed damage, except for Elemental Fist.'''},
                        {'Name': 'Iron Skin', 'Desc': '''Your training grants you +2 natural SOAK.'''},
                        {'Name': 'Martial Leap', 'Desc': '''Increase both your vertical and horizontal Jump distances by 5'.'''},
                        {'Name': 'Martial Technique Base', 'Desc': '''You gain two of the following universal exploits: Trip, Throw, Sidestep, Flying Kick. You may take this exploit again to gain the remaining two exploits.'''},
                        {'Name': 'Mountain Stance', 'Desc': '''(requires Defensive Stance) You become as immobile as a mountain. No knockdown or knockback attempt by a creature of your size or smaller will work against you.'''},
                        {'Name': 'Weapon Synthesis', 'Desc': '''When using any Eastern weapon, you gain one free unarmed melee attack whenever you make two weapon attacks.'''},
                        {'Name': 'Zen Mind', 'Desc': '''You gain +4 to your MENTAL DEFENSE.'''}])

career_now_list = [career_now_actor, career_now_archaeologist, career_now_assassin, career_now_astronaut,
                   career_now_athlete, career_now_bartender, career_now_boot_camp, career_now_bouncer,
                   career_now_bounty_hunter, career_now_boxer, career_now_burglar, career_now_chef, career_now_college,
                   career_now_con_artist, career_now_craftsman, career_now_cultist, career_now_dark_crusader,
                   career_now_detective, career_now_diplomat, career_now_diver, career_now_drifter, career_now_driver,
                   career_now_engineer, career_now_explosives_expert, career_now_firefighter, career_now_gambler,
                   career_now_gangster, career_now_guerrilla_fighter, career_now_hacker, career_now_heavy_gunner,
                   career_now_infiltrator, career_now_laborer, career_now_lawyer, career_now_medic, career_now_miner,
                   career_now_ninja, career_now_performer, career_now_pilot, career_now_police_officer,
                   career_now_politician, career_now_priest, career_now_prisoner, career_now_private_eye,
                   career_now_reporter, career_now_sailor, career_now_scientist, career_now_scout,
                   career_now_sensei_sifu, career_now_smuggler, career_now_sniper, career_now_socialite,
                   career_now_soldier, career_now_spy, career_now_street_thug, career_now_student, career_now_stuntman,
                   career_now_survivalist, career_now_teacher, career_now_trader, career_now_vigilante,
                   career_now_warrior_monk]

for career in career_now_list:
    career.available_skills.sort()
