from lib.character import Career

career_new_academy = Career(
    name='Academy',
    career_time='3',
    career_time_unit='years',
    prereq='none',
    agility=1, logic=1, willpower=1, charisma=1,
    available_skills=['carrying', 'pistols', 'rifles', 'leadership', 'law', '[scientific]', '[technical]', 'tactics', 'leadership', 'starship tactics'],
    desc='''You joined the military and completed basic military training. Some programs send recruits to college to gain degrees before returning to cadet assignments. The Military Academy is the basic training location for both Naval and Marine officers, and as such covers a wide curriculum along with an opportunity to specialize early in a science, medicine, or engineering career.The Military Academy is regarded as a top-quality institution, easily the equal of many highly placed universities. The Academy is a three-year course, and is widely regarded as the equivalent of a Bachelor's degree.''',
    available_exploits=[{'Name': 'Basic training', 'Desc': '''You gain all of the following skills at 1 rank (1d6); this does not increase an existing skill beyond 1 rank. Tactics (marines) or piloting (navy); computers; law; one [scientific] skill (navy) or survival (marines).'''},
                        {'Name': 'Command school', 'Desc': '''(requires Basic training) A second stint in the Academy prepares you for command. You automatically gain a military rank and the leadership skill at 1 rank if you do not already have it. You gain +2 REP. Make a Challenging [13] CHA check before advancing any attributes. If you succeed, you automatically gain a second military rank.'''},
                        {'Name': 'Branch specialization', 'Desc': '''(requires Basic training; one [scientific] skill) You can choose to spend an additional stint at Engineering, Medical, or Science Branch School. This is regarded as the equivalent of a doctorate. You gain one bonus [scientific] or [technical] skill.'''},
                        {'Name': 'Academy tutor', 'Desc': '''(requires Basic training) You spent time teaching at the Academy. While not exciting, teaching is a great way to improve your connections and reputation, and many graduates opt to do so after basic training. You gain 2 REP points. You also gain a permanent +1d6 bonus to social interactions involving military personnel as you share common acquaintances, students, or colleagues.'''},
                        {'Name': 'Academy professor', 'Desc': '''(requires Academy Tutor) A paper or book you wrote has become required reading at the Academy. Naval graduates will automatically recognize your name. You gain a further 2 REP points and an automatic promotion of one rank.'''}])

career_new_assassin = Career(
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

career_new_athlete = Career(
    name='Athlete',
    career_time='1d6',
    career_time_unit='years',
    prereq='[sport] or [physical]',
    strength=1, agility=1, endurance=1, reputation=1,
    available_skills=['[physical]', '[sporting]', 'carousing', 'flirtation', '[unarmed combat]'],
    desc='''You are a professional athlete, whether that be in a team sport or a track and field event.''',
    available_exploits=[{'Name': 'Athletic', 'Desc': '''Choose four [physical] skills. You gain these four skills at 1 rank (1d6). This does not increase the rank of an existing skill.'''},
                        {'Name': 'Runner', 'Desc': '''You gain a +2 SPEED bonus.'''},
                        {'Name': 'Fit', 'Desc': '''You gain a +5 HEALTH bonus.'''},
                        {'Name': 'Signing bonus', 'Desc': '''You are signed to a team and gain a 1,000 credit signing bonus. You may repeat this Exploit, signing to a new team each time.'''}])

career_new_bartender = Career(
    name='Bartender',
    career_time='1d6',
    career_time_unit='years',
    prereq='none',
    endurance=1, intuition=1, charisma=1, luck=1,
    available_skills=['[social]', 'carousing', 'perception', 'brewing', 'cooking', 'brawling', 'clubs'],
    desc='''Bartending is a great way to pay the bills. Some make a lifelong career of it.''',
    available_exploits=[{'Name': 'Bouncer', 'Desc': '''You are used to dealing with drunkards. You gain a +1d6 bonus to all checks vs. an intoxicated creature.'''},
                        {'Name': 'Fake ID', 'Desc': '''Years of checking for fake ID mean that you can spot the telltale signs. You gain a +1d6 bonus to detect forgeries.'''},
                        {'Name': 'Gossip', 'Desc': '''You can gather local gossip and information simply by spending an hour in a bar or other watering hole, effectively giving you the local knowledge skill wherever you go as long as you are able to refresh your knowledge at a local bar weekly.'''}])

career_new_battlepsyche = Career(
    name='Battlepsyche',
    career_time='1d6',
    career_time_unit='years',
    prereq='concentration',
    endurance=1, willpower=1, psionics=2,
    available_skills=['[psionic]', '[combat]', 'concentration', 'meditation'],
    desc='''Battlepsychs are trained for wartime psionic combat. They specialize in brute-force mental offense.''',
    available_exploits=[{'Name': 'Psi-blast', 'Desc': '''You can use an action and make a PSI vs. MENTAL DEFENSE attack to blast an opponent with a mental burst which does 3d6 psionic damage and has a range increment of 10'.'''},
                        {'Name': 'Telekinetic shield', 'Desc': '''You gain +4 RANGED DEFENSE from a permanent telekinetic shield. This does not stack with any other equipment DEFENSE bonuses, such as shields, and it has no effect when used in cover.'''},
                        {'Name': 'Psychic cone', 'Desc': '''You gain the ability to once per day spend 1d6 HEALTH to project a 30' of psychic energy which causes psychic damage equal to your PSI check to all in the area of effect. If the 1d6 HEALTH causes you to fall to zero HEALTH, the power fails.'''},
                        {'Name': 'Electrokinetic blast', 'Desc': '''You blast an opponent with a range increment of 20' with a bolt of focused electricity. Make a PSI vs. DEFENSE attack; if you succeed, you do 2d6 electricity damage. You may repeat this Exploit once, incresing the damage to 3d6.'''}])

career_new_biopsychic = Career(
    name='Biopsychic',
    career_time='1d6',
    career_time_unit='years',
    prereq='medicine',
    endurance=1, willpower=1, charisma=1, psionics=1,
    available_skills=['[psionic]', 'medicine', 'biology', 'psychology', 'concentration', 'meditation'],
    desc='''Biopsychics are dedicated to healing. Known by a variety of names – energy healer, faith healers, psychic surgeons, and more they channel psionic energy into others in order to heal injuries and sickness.''',
    available_exploits=[{'Name': 'Psychic healing', 'Desc': '''You can heal 1d6 HEALTH by touch. Any given creature can only benefit from this power once per day. You may repeat this Exploit once, increasing the healing to 2d6 HEALTH.'''},
                        {'Name': 'Adrenalize', 'Desc': '''Once per day you can channel positive energy into somebody, granting them a +1d6 die bonus to all physical attribute checks for five minutes.'''},
                        {'Name': 'Psychic resuscitation', 'Desc': '''You may stabilize a dying creature by touch by spending two actions. Any given creature can only beneft from this power once per day.'''}])

career_new_bounty_hunter = Career(
    name='Bounty Hunter',
    career_time='1d6',
    career_time_unit='years',
    prereq='none',
    agility=1, intuition=1, logic=1, reputation=1,
    available_skills=['tracking', 'piloting', 'stealth', 'computers', 'perception', 'intimidate', '[combat]', 'law'],
    desc='''As a bounty hunter you spent time tracking down and capturing wanted criminals.''',
    available_exploits=[{'Name': 'Prey', 'Desc': '''You may choose a target species. You gain a +1d6 bonus to attempts to track targets of that species.'''},
                        {'Name': 'Datamining', 'Desc': '''You are able to locate a target's current location down to a specific planet by accessing credit, criminal, customs, and other records if you have access to a computer link.'''}])

career_new_burglar = Career(
    name='Burglar',
    career_time='1d6',
    career_time_unit='years',
    prereq='stealth',
    agility=1, intuition=1, luck=1, reputation=1,
    available_skills=['climbing', 'jumping', 'acrobatics', 'escape artist', 'computers', 'stealth', 'thievery', 'appraisal'],
    desc='''You become a master thief, able to infiltrate the most secure of locations. Some cat burglars work for hire and conduct industrial espionage, while others prefer to steal valuable artifacts and jewels from museums and high security vaults.''',
    available_exploits=[{'Name': 'Locksmith', 'Desc': '''You gain an exceptional quality lockpicking kit.'''},
                        {'Name': 'Catburglar', 'Desc': '''An expert at climbing, you do not take any die penalties in combat while climbing.'''},
                        {'Name': 'Sixth sense', 'Desc': '''You have a sixth sense when it comes to traps, and gain a +2d6 bonus to spot them and a +1d6 bonus to avoid or disarm them.'''},
                        {'Name': 'Climber', 'Desc': '''(requires Catburglar) Your climbing speed becomes equal to your regular SPEED.'''},
                        {'Name': 'Grand heist', 'Desc': '''You achieve a great robbery that will be remembered for years to come. Gain a bonus 3d6 x 100cr. You may repeat this Exploit, gaining 3d6x100cr each time.'''}])

career_new_college = Career(
    name='College',
    career_time='4',
    career_time_unit='years',
    prereq='none',
    logic=1, willpower=1, charisma=1, reputation=1,
    available_skills=['computers', '[scientific]', '[artistic]', '[sporting]', '[social]', '[technical]', '[academic]'],
    desc='''You attended a civilian college or university and gained formal qualifications in a chosen area of study.Choose a subject, which can be any skill, but is typically a [scientific], [technical], [academic], or [artistic] skill. You can restart this career at any time to gain degrees in additional subjects.''',
    available_exploits=[{'Name': 'Bachelor', 'Desc': '''After a four-year course, you gained a Bachelor's degree or equivalent at university. Improve your skill ranks in your chosen subject to 3. Your research skills are developed. If you have access to a library or data network, you gain a +1d6 bonus to attempts to learn information about a subject. Make a Challenging [13] LOG check before advancing any attributes. If you succeed, you pass this degree with honors and gain 1 bonus REP attribute point.'''},
                        {'Name': 'Masters', 'Desc': '''(requires Bachelor) You remain in college and gain a Masters degree in your subject. You gain 1 bonus skill rank in your chosen subject. Make a Difficult [16] LOG check before advancing any attributes. If you succeed, you pass this degree with honors and gain 1 bonus REP attribute point.'''},
                        {'Name': 'Doctorate', 'Desc': '''(requires Masters) After further studies, you gained a Doctorate at university. You may now call yourself a Doctor. But not THE Doctor. Gaining a doctorate requires not just an expert knowledge of a subject, but also rigorous skills of analysis and evaluation and critical achievement. Improve your skill ranks in your chosen subject to 6. Make a Demanding [21] LOG check before advancing any attributes. If you succeed, you pass this degree with honors and have also made a minor breakthrough in your chosen subject, and are known amongst peers for it, gaining you a bonus 2 points to your REP attribute. Choose the nature of your breakthrough.'''}])

career_new_con_artist = Career(
    name='Con Artist',
    career_time='1d6',
    career_time_unit='years',
    prereq='bluffing',
    intuition=1, logic=1, charisma=1, luck=1,
    available_skills=['[social]', 'disguise', 'bribery', 'forgery', '[gaming]', 'appraisal'],
    desc='''You honed your skills and learned how to trick others out of their money with charm, lies, bluffs, disguise, and more. Many career criminals combine the craft of the con man with the skills of the burglar.''',
    available_exploits=[{'Name': 'Grifter', 'Desc': '''In a bar or other crowded social situation, you can automatically make credits equal to a CHA check x 10 in the space of an hour using only the gift of the gab. You can only do this once per day. This Exploit cannot be used during downtime.'''},
                        {'Name': 'Impersonate', 'Desc': '''You are easily able to impersonate any job role which you have had opportunity to observe within the past day, even briefly. You gain a +1d6 bonus if you have been able to observe and mimic an example.'''},
                        {'Name': 'Quick change', 'Desc': '''You are able to don a quick disguise in one round instead of five minutes. This must be a disguise you've successfully used before.'''},
                        {'Name': 'Beguiling', 'Desc': '''You are able to temporarily beguile and captivate a target with your words as a CHA vs. MENTAL DEFENSE check. A successful check charms the target until they shake off the condition. The target must be able to understand you and have a LOGIC attribute of at least 2.'''}])

career_new_craftsman = Career(
    name='Craftsman',
    career_time='1d6',
    career_time_unit='years',
    prereq='[crafting] or [technical]',
    strength=1, agility=1, logic=1, charisma=1,
    available_skills=['[technical]', '[artistic]', '[crafting]'],
    desc='''You made your living by practising your craft as a carpenter, electrician, mechanic, or other professional skilled worker. You are the backbone of society, representative of all those billions like you who lead ordinary lives.''',
    available_exploits=[{'Name': 'Handyman', 'Desc': '''Choose four [crafting] skills. You gain these four skills at 1 rank (1d6). This does not increase the rank of an existing skill.'''},
                        {'Name': 'Toolkit', 'Desc': '''You gain a set of high quality tools.'''},
                        {'Name': 'Tradesman', 'Desc': '''You can make 3d6 x 10 Cr per week by plying your trade. This Exploit cannot be used during downtime.'''},
                        {'Name': 'Builder', 'Desc': '''Assuming raw materials are available, you can make an item of equipment in one day by rolling a LOG check vs. the item's value.'''},
                        {'Name': 'Fixer', 'Desc': '''You gain a +1d6 bonus to any attempt to repair something.'''}])

career_new_detective = Career(
    name='Detective',
    career_time='1d6',
    career_time_unit='years',
    prereq='none',
    agility=1, intuition=2, charisma=1,
    available_skills=['interrogation', 'pistols', 'driving', 'bureaucracy', 'perception', 'intimidate', 'stealth', 'tracking', 'law'],
    desc='''You become a detective, expert at spotting clues and finding your man. Even if you leave the profession, you still retain enough contacts to call in favors and request information.''',
    available_exploits=[{'Name': 'Clues', 'Desc': '''If there are any clues to find at a crime scene, you automatically find them within 5 minutes.'''},
                        {'Name': 'Criminal record', 'Desc': '''You can freely access police databanks and automatically discover any information held on file about a suspect.'''},
                        {'Name': 'Hull number', 'Desc': '''You can request a starship hull number lookup, and automatically determine the registered owner and port of registration of a starship.'''}])

career_new_diplomat = Career(
    name='Diplomat',
    career_time='1d6',
    career_time_unit='years',
    prereq='[social]',
    intuition=1, charisma=2, reputation=1,
    available_skills=['[social]', 'bureaucracy', 'law', 'politics', 'local knowledge'],
    desc='''You have represented your planet elsewhere.''',
    available_exploits=[{'Name': 'Diplomatic', 'Desc': '''Choose four [social] skills. You gain these four skills at 1 rank (1d6). This does not increase the rank of an existing skill.'''},
                        {'Name': 'Diplomatic pouch', 'Desc': '''You have a diplomatic pouch in which any small sized item can be carried through customs without inspection.'''},
                        {'Name': 'Embassy', 'Desc': '''You have access to your home planet's ambassadorial embassy and residences on any planet (if there are any), which can provide food, shelter, basic equipment, and medical care.'''},
                        {'Name': 'Diplomatic immunity', 'Desc': '''You gain diplomatic immunity to very low-level and petty crimes on any planet which contains an embassy.'''}])

career_new_drifter = Career(
    name='Drifter',
    career_time='1d6',
    career_time_unit='years',
    prereq='none',
    endurance=1, intuition=1, charisma=1, luck=1,
    available_skills=['carousing', 'gaming', 'flirtation', 'performing', 'bluffing', 'appraisal', 'thievery'],
    desc='''Somehow you lost your way. Drinking, gambling, with no clear objective, you drifted through the fringes of society.''',
    available_exploits=[{'Name': 'Unseen', 'Desc': '''You know how to blend in so that nobody pays any attention to you. You gain a +1d6 bonus when attempting to do so.'''}])

career_new_engineer = Career(
    name='Engineer',
    career_time='1d6',
    career_time_unit='years',
    prereq='engineering',
    strength=1, agility=1, logic=1, luck=1,
    available_skills=['computers', '[technical]', 'zero-g', 'bureaucracy'],
    desc='''You became an engineer, proficient at manipulating technology and repairing devices and engines.''',
    available_exploits=[{'Name': 'Technical knowledge base', 'Desc': '''Choose four [technical] skills. You gain these four skills at 1 rank (1d6). This does not increase the rank of an existing skill.'''},
                        {'Name': 'Jury-rig', 'Desc': '''You can temporarily repair and jury-rig a broken item of size Medium or smaller by spending five minutes with it. The item will operate for a number of minutes equal to your LOG check. If you spend one hour with it, it will operate for a number of hours equal to your LOG check. If you spend a day with it, it will operate for a number of days equal to your LOG check.'''},
                        {'Name': 'Upgrade', 'Desc': '''You can modify a piece of electronic equipment of size Small or smaller to upgrade it permanently to a high quality item. This process takes one hour, but the item can only be used by you due to unfamiliar and jury-rigged controls, and renders it monetarily worthless.'''},
                        {'Name': 'Engine-tuner', 'Desc': '''A starship in which you are an engineer increases its maximum FTL speed by 1 factor. This does not stack with other engineers should others be present.'''},
                        {'Name': 'Engine-master', 'Desc': '''(requires Engine-tuner) You can increase your starship's FTL speed by 2 factors for a number of hours equal to your LOG check, after which the FTL engines cannot be used for 24 hours. This does not stack with other engineers should others be present.'''},
                        {'Name': 'Explosives', 'Desc': '''You can create explosives from common items and surroundings. The explosive takes 30 minutes to make, and causes 3d6 heat damage to all within 5'. The explosive can be stored, but only for up to two hours.'''},
                        {'Name': 'Saboteur', 'Desc': '''You are able to disable any mechanical or electronic device to which you have access. This Exploit does not open a locked door (disabling the lock just means it remains stuck in whatever configuration it is currently in). This takes you five minutes.'''},
                        {'Name': 'Android repair', 'Desc': '''By using basic engineering equipment, you can heal 1d6 points of HEALTH to an adjacent mechanoid as a single action. Any given mechanoid can only benefit from your repairing in this way once per day.'''},
                        {'Name': 'Exceptional android repair (requires Android Repair)', 'Desc': '''Your Android Repair ability increases to 2d6 points of HEALTH.'''}])

career_new_gambler = Career(
    name='Gambler',
    career_time='1d6',
    career_time_unit='years',
    prereq='[gaming]',
    intuition=1, charisma=1, luck=2,
    available_skills=['[gaming]', '[social]', 'thievery'],
    desc='''You became an expert gambler, proficient at games of skill and chance.''',
    available_exploits=[{'Name': 'Lucky streak', 'Desc': '''Roll 3d6 and multiply by 100. You gain that many credits. You may repeat this Exploit, gaining 3d6x100 credits each time.'''},
                        {'Name': 'Cheat', 'Desc': '''You know a couple of tricks. In a game of chance, you may reroll any 1s in your dice pool.'''},
                        {'Name': 'Chancer', 'Desc': '''You may spend 5 minutes once per day to replenish your LUCK pool an additional time.'''}])

career_new_gangster = Career(
    name='Gangster',
    career_time='1d6',
    career_time_unit='years',
    prereq='intimidate',
    strength=1, intuition=1, charisma=1, reputation=1,
    available_skills=['intimidation', 'thievery', 'driving', 'pistols'],
    desc='''Eventually your life of crime led you to better things as you fell into a gang or crew.''',
    available_exploits=[{'Name': 'Intimidating', 'Desc': '''Intimidation is your way of life, especially in the criminal underworld. When attempting to intimidate a criminal, you gain a +1d6 bonus.'''},
                        {'Name': 'Protection racket', 'Desc': '''A protection racket is a lucrative and steady stream of income. Within your REP sphere you have a route. You gain your REP x 100 Cr each week. This Exploit cannot be used during downtime.'''}])

career_new_intelligence_officer_spy = Career(
    name='Intelligence Officer/Spy',
    career_time='1d6',
    career_time_unit='years',
    prereq='none',
    agility=1, intuition=1, charisma=1, luck=1,
    available_skills=['interrogation', '[subterfuge skills]', 'computers', 'pistols', '[social]', '[gaming]', 'law'],
    desc='''You're a spy. This may be Navy Intelligence or some other force. You have a wide remit, dealing with both domestic and external threats, and perform undercover investigations into military and civilian issues.''',
    available_exploits=[{'Name': 'False identify', 'Desc': '''You are able to create a false identity, complete with background records, in one day.'''},
                        {'Name': 'Off the grid', 'Desc': '''You know how to disappear without trace, dropping off the grid completely. No location discerning checks or abilities can find you unless you want them to.'''},
                        {'Name': 'Safe house', 'Desc': '''You can use a safe house on any populated planet to grant your off the grid ability to your entire party.'''},
                        {'Name': 'Monologue', 'Desc': '''Once per day you can make a CHA vs. MENTAL DEFENSE attack against an enemy. If successful, your target explains their plan with a short monologue.'''},
                        {'Name': 'Miraculous escape', 'Desc': '''Once per day you may automatically succeed in one attempt to escape handcuffs or other restraints.'''}])

career_new_marine_cadet_assignment = Career(
    name='Marine Cadet Assignment',
    career_time='2',
    career_time_unit='years',
    prereq='none',
    strength=1, endurance=1, intuition=1, luck=1,
    available_skills=['carrying', '[unarmed fighting]', 'pistols', 'rifles', 'hardy', 'survival', 'leadership', 'tactics'],
    desc='''You completed your cadet assignment in the Star Marines, which gave you a rude awakening after the comparative luxury that was the Academy. Assigned menial tasks in hostile conditions and climates, you endured two years before being approved by your Sergeant.''',
    available_exploits=[{'Name': 'Light sleeper', 'Desc': '''You gain a Kevlar vest and a rifle. You also gain the ability to sleep lightly, and are not disadvantaged by perception check made while asleep.'''}])

career_new_marine_tour = Career(
    name='Marine Tour',
    career_time='1d6',
    career_time_unit='years',
    prereq='none',
    strength=1, endurance=1, willpower=1, reputation=1,
    available_skills=['carrying', '[combat skills]', 'hardy', 'survival', 'leadership', 'carousing', 'bravery', 'perception'],
    desc='''A tour of duty in the Star Marines means a deployment to a probably dangerous environment where you engaged enemy forces in infantry based ground battles or boarded hostile starships. Star Marines pride themselves on their sense of duty and their courage, and consider themselves the most professional soldiers in known space.With each tour, roll 1d6. On a roll of 6, you gain a medal and a bonus +1 REP.''',
    available_exploits=[{'Name': 'Battle scars', 'Desc': '''You've received so many battle scars that you sometimes don't notice injury. You gain a SOAK bonus of 2.'''},
                        {'Name': 'Quick naps', 'Desc': '''You've learned to manage with little sleep. As long as you get 4 hours, you count as fully rested.'''},
                        {'Name': 'Get on with it', 'Desc': '''Your platoon doesn't have much patience for whining about minor injuries. Once per day you can pause for two actions and recover 2d6 HEALTH.'''},
                        {'Name': 'Shake it off', 'Desc': '''You gain a +1d6 bonus when attempting to shake off a condition.'''},
                        {'Name': 'Platoon leader', 'Desc': '''You are able to grant your entire party a +1d6 INITIATIVE bonus as long as they are within 30' of you.'''}])

career_new_medic = Career(
    name='Medic',
    career_time='1d6',
    career_time_unit='years',
    prereq='medicine',
    agility=1, intuition=1, logic=1, charisma=1,
    available_skills=['computers', 'medicine', 'bureaucracy', 'psychology'],
    desc='''You enter the medical profession. If you have gained a doctorate at college, you do so as a doctor; otherwise you are referred to as a nurse or medic.''',
    available_exploits=[{'Name': 'Medical knowledge base', 'Desc': '''Choose four [medical] skills. You gain these four skills at 1 rank (1d6). This does not increase the rank of an existing skill.'''},
                        {'Name': 'Bedside manner', 'Desc': '''You gain a medical pouch and a medical scanner. Your long-term care is of such quality that your patient gains an additional 1d6 HEALTH per day. You may only have one patient under your long-term care at a time.'''},
                        {'Name': 'Ward management', 'Desc': '''(requires Bedside Manner) You are an expert at running and managing a ward or sickbay. The number of patients you can have under your long-term care is increased to the value of your LOG attribute.'''},
                        {'Name': 'Diagnosis', 'Desc': '''You gain +1d6 bonus to all scans made with a medical scanner, and a +1d6 bonus to identify or treat diseases. Make a Difficult [16] LOG check before advancing any attributes. If you succeed, you discovered a new disease or illness which is named after you; you also gain 1 bonus REP attribute point.'''},
                        {'Name': 'Healing hands', 'Desc': '''Using basic medical equipment, you can heal 1d6 points of HEALTH to an adjacent creature as a single action. Any given creature can only benefit from your healing in this way once per day.'''},
                        {'Name': 'Exceptional healing hands', 'Desc': '''(requires Healing Hands) Your Healing Hands ability increases to 2d6 points of HEALTH.'''},
                        {'Name': 'Resuscitation', 'Desc': '''(requires Exceptional Healing Hands) You can revive a seemingly dead creature with a LOG check. The creature must have “died” within the last five minutes, and the difficulty value of the check is 20 + the damage of the attack that killed it. The creature wakes up with 1 HEALTH.'''},
                        {'Name': 'Medical officer', 'Desc': '''On board a starship, your vessel's daily sickbay capacity for restoring casualties to active duty is increased by 10% as long as you are in charge of the medical facilities.'''},
                        {'Name': 'Emergency response', 'Desc': '''(requires Medical Officer) When starship casualties are rolled for a ship on which you are in charge of the medical facilities, roll the casualty amount twice and take the lowest value.'''}])

career_new_miner = Career(
    name='Miner',
    career_time='1d6',
    career_time_unit='years',
    prereq='none',
    strength=1, endurance=1, willpower=1, luck=1,
    available_skills=['carrying', 'climbing', 'survival', '[technical]', 'mining', 'appraising', 'carousing', 'picks', 'hammers'],
    desc='''There's nothing like a few years spent down a tritanium mine to build character.''',
    available_exploits=[{'Name': 'Underground sense', 'Desc': '''When underground you can always determine direction and depth and pick a route to the surface.'''},
                        {'Name': 'Darksight', 'Desc': '''You have spent so much time below ground that you've developed darksight to a distance of 30'.'''},
                        {'Name': 'Mining hazards', 'Desc': '''You gain a +2d6 bonus to spot underground hazards and traps.'''},
                        {'Name': 'Toxic gases', 'Desc': '''The underground is full of toxic fumes, and you've become used to them. You gain a poison SOAK of 5.'''},
                        {'Name': 'Identify substance', 'Desc': '''You can identify by sight any mineral or metal based substance automatically.'''}])

career_new_navy_cadet_cruise = Career(
    name='Navy Cadet Cruise',
    career_time='1',
    career_time_unit='years',
    prereq='none',
    agility=1, willpower=1, charisma=1, luck=1,
    available_skills=['piloting', 'computers', 'leadership'],
    desc='''You completed your cadet cruise and are now a Navy Officer! The cadet cruise is a year long, and spent on a starship; those who successfully complete the cadet cruise and evaluation are then able to proceed to a Navy Tour or to Navy Command School. The exact assignment of the cadet cruise varies, but a cadet will typically carry out a range of non-specialized duties under the supervision of an evaluating officer.''',
    available_exploits=[{'Name': 'Ship rat', 'Desc': '''You gain an overall familiarity with naval vessels and starships, and get a +1d6 bonus to checks related to them.'''}])

career_new_navy_tour = Career(
    name='Navy Tour',
    career_time='1d6',
    career_time_unit='years',
    prereq='none',
    agility=1, intuition=1, willpower=1, reputation=1,
    available_skills=['piloting', 'computers', 'leadership', 'pistols', 'rifles', 'engineering', '[scientific]', 'tactics', 'starship tactics'],
    desc='''A navy tour is a regular military assignment; tours constitute the bulk of a military character's career. Tours in the Navy can encompass any and all of these duties. A crewman will typically specialize in one of several career branches – medical, security, engineering, science, operations, pilot – and carry out his tour of duty in that area of specialization, often with a long-term aim of becoming chief of that department. For example, if you are already a medic, your tour will be as a medical officer; if you are already a scientist, it will be as a science officer or similar role. The same goes for pilots, security personnel, engineers, and so on.''',
    available_exploits=[{'Name': 'Starship familiarity', 'Desc': '''. Your familiarity with naval starships is such that you can automatically navigate to any location inside one.'''},
                        {'Name': 'Brace yourself', 'Desc': '''(requires Starship Familiarity) You are so accustomed to the starship environment, instinctively knowing how to brace yourself, that you never take damage from external starship fire.'''},
                        {'Name': 'Acclimatized', 'Desc': '''Missions into hostile environments make you used to changes in gravity. You do not suffer penalties (but still gain bonuses) for high or low gravity environments.'''},
                        {'Name': 'Bridge officer', 'Desc': '''If you are commanding a starship, all bridge officers gain a +1d6 bonus to starship operations from your presence.'''},
                        {'Name': 'You have the conn', 'Desc': '''(requires Bridge Officer) You may donate LUCK dice to allies while on the bridge.'''},
                        {'Name': 'First contact', 'Desc': '''You were involved in a first contact mission, discovering a new alien species. Decide on the nature of the species (with your GM's approval). You gain a bonus +1 REP and 1 rank in linguistics.'''}])

career_new_performer = Career(
    name='Performer',
    career_time='1d6',
    career_time_unit='years',
    prereq='[performance]',
    charisma=2, luck=1, reputation=1,
    available_skills=['carousing', '[performance]'],
    desc='''You became a musician or other performer, and made your way working bars, clubs, and theaters.''',
    available_exploits=[{'Name': 'Triple-threat', 'Desc': '''You gain the skills singing, dancing, and acting at 1 rank (1d6). This does not increase the rank of an existing skill.'''},
                        {'Name': 'Gigs', 'Desc': '''You can make money by playing at bars and doing local performances. You can automatically make an amount equal to a CHA check x 10 Cr per day by doing this. This Exploit cannot be used during downtime.'''},
                        {'Name': 'Captivating', 'Desc': '''You have the ability to captivate people with your musical ability. While using your musical instrument or voice, all those who can hear you become beguiled (unable to attack you) until you stop. This requires a CHA vs. MENTAL DEFENSE check and a full two actions each turn.'''},
                        {'Name': 'Lullaby', 'Desc': '''Your music and make people drowsy. While using your musical instrument or voice, all those who can hear you become weary (-1d6 to all physical attribute checks and -1 SPEED) until you stop. This requires a CHA vs. MENTAL DEFENSE check and a full two actions each turn.'''},
                        {'Name': 'Fearful', 'Desc': '''You can use voice or music to instil fear in those who hear it. While using your musical instrument or voice, all those who can hear you become nervous (-1d6 to all interactions with you or with a target or object of your choice) until you stop. This requires a CHA vs. MENTAL DEFENSE check and a full two actions each turn.'''}])

career_new_pilot = Career(
    name='Pilot',
    career_time='1d6',
    career_time_unit='years',
    prereq='piloting',
    agility=1, intuition=1, logic=1, luck=1,
    available_skills=['reactions', 'piloting', 'computers', 'astronomy', 'gunnery', 'navigation', 'starship tactics'],
    desc='''You became a pilot or starship helm officer, learning to fly shuttles, fighters, freighters, or starships.''',
    available_exploits=[{'Name': 'Push the limits', 'Desc': '''You can exceed a ship's normal maximum FTL speed by one factor (as long as it has FTL capability).'''},
                        {'Name': 'Evasive flying', 'Desc': '''A ship which you pilot gains a DEFENSE bonus equal to your AGI attribute dice pool.'''},
                        {'Name': 'Evasive maneuver', 'Desc': '''(requires Evasive Flying) As an action, you may designate one incoming missile per round and gain an additional +5 DEFENSE against it.'''},
                        {'Name': 'Stay on target', 'Desc': '''(requires Evasive Flying) While in the rear arc of a target ship, you negate any bonus it gets from Evasive Flying.'''},
                        {'Name': 'Cruise control', 'Desc': '''You are able to easily navigate in-system at subluminal speeds without an attribute check.'''},
                        {'Name': 'Full stop', 'Desc': '''As an action, you can bring a starship to an immediate stop without needing to decelerate. This causes 1d6 damage to the ship's superstructure.'''},
                        {'Name': 'Astrogator', 'Desc': '''You are a great navigator, able to plot FTL journeys with ease. The travel increment on a starship you are piloting is increased by 2 days.'''},
                        {'Name': 'Sideslip', 'Desc': '''You can move your ship in a sideslip maneuver. This moves it one hex forward and one hex sideways for the cost of two hex moves.'''}])

career_new_police_officer = Career(
    name='Police Officer',
    career_time='1d6',
    career_time_unit='years',
    prereq='none',
    agility=1, intuition=1, logic=1, reputation=1,
    available_skills=['interrogation', 'pistols', 'driving', 'bureaucracy', 'perception', 'intimidate', 'law'],
    desc='''You join the police or other security force and begin a career as a uniformed officer.''',
    available_exploits=[{'Name': 'Troublesense', 'Desc': '''You are easily able to spot trouble before it happens. You gain a +1d6 bonus to initiative checks.'''},
                        {'Name': 'Out of place', 'Desc': '''You know the signs of suspicious behavior. You gain a +1d6 bonus to checks made to spot unusual or criminal activity.'''},
                        {'Name': 'Freeze!', 'Desc': '''You can compel a target to “freeze!” with a CHA vs. MENTAL DEFENSE check. If successful, the target stops in his tracks and is stunned for one round. The target must be able to understand you and have an INT attribute of 2 or more. You can only do this to a given target once.'''},
                        {'Name': 'Backup', 'Desc': '''In an allied urban environment, you can call for backup once per day in the form of 1d6 police officers who arrive within 5 minutes and who will follow your orders.'''},
                        {'Name': 'Anti-surveillance', 'Desc': '''You are so familiar with surveillance devices, blind spots, and avoidance techniques that, by moving half your speed, you can render yourself invisible to electronic monitoring equipment.'''}])

career_new_priest = Career(
    name='Priest',
    career_time='1d6',
    career_time_unit='years',
    prereq='religion',
    intuition=1, willpower=1, charisma=1, luck=1,
    available_skills=['perception', 'crafting', 'bureaucracy', 'cryptology', 'linguistics', '[trivia]', 'meditation', 'leadership', 'performing', 'religion'],
    desc='''You joined the clergy and practised religion, tending to your flock.''',
    available_exploits=[{'Name': 'Confessional', 'Desc': '''Your insights into the morality of living things enables you to draw confessions from others. Given an hour of conversation, you gain a +2d6 bonus to checks designed to gain information from another creature.'''},
                        {'Name': 'Unshakeable faith', 'Desc': '''You have faith, a peace of mind and an inner tranquillity which is hard to penetrate. You gain +5 to your MENTAL DEFENSE.'''},
                        {'Name': 'Respect', 'Desc': '''Your position in the clergy grants you a certain reverence from others. Sentient opponents able to recognise your occupation take a -1d6 penalty to attack you on their first attack as long as you have not attacked them first.'''}])

career_new_prisoner = Career(
    name='Prisoner',
    career_time='2d6',
    career_time_unit='years',
    prereq='none',
    strength=1, endurance=1, intuition=1, reputation=1,
    available_skills=['intimidation', 'survival', '[subterfuge skills]', '[unarmed fighting]', 'knives'],
    desc='''Your life of crime ended you up in prison where you served time; or perhaps you were a political prisoner or a prisoner-of-war. It was a tough environment and you spent most of your time just trying to survive, although you did make one or two lifelong contacts.''',
    available_exploits=[{'Name': 'Prison tough', 'Desc': '''You are mentally and physically toughened. Each time you go to prison you gain a permanent +1 bonus to your DEFENSE and MENTAL DEFENSE.'''},
                        {'Name': 'Shiv', 'Desc': '''You are easily able to improvise weapons using your surroundings – glasses, rocks, and so on. You always count as carrying a knife or club.'''}])

career_new_psi_cop = Career(
    name='Psi-cop',
    career_time='1d6',
    career_time_unit='years',
    prereq='law',
    intuition=1, charisma=1, reputation=1, psionics=1,
    available_skills=['[psionic]', 'intimidation', 'concentration', 'meditation', 'law', 'pistols', 'perception'],
    desc='''A Psi-Cop is a specialist investigative law-enforcement individual with psionic training, and usually works alongside police – or occasionally Navy Security or Intelligence – in a consulting role. Psi-Cops aren't usually trained in direct psionic combat skills; their area of expertise is in the teasing out of information from suspects and crime scenes, although higher ranking Psi-Cops known as Inquisitors do receive potent combat training.''',
    available_exploits=[{'Name': 'Speak-with-dead', 'Desc': '''You have the ability to interrogate a dead body which has been dead for less than a day. It will truthfully answer three yes/no questions with no PSI check needed.'''},
                        {'Name': 'Psychic interrogation', 'Desc': '''You can make a special PSI attack vs. a suspect's MENTAL DEFENSE. Success means that they must answer three yes/no questions truthfully.'''},
                        {'Name': 'Sense motive', 'Desc': '''You are able to sense strong emotions within 30', although you cannot necessarily pinpoint their location.'''},
                        {'Name': 'Psychic torture', 'Desc': '''You use an unethical technique of mental torture to force a suspect to speak, gaining +2d6 to an intimidation check.'''}])

career_new_psychic = Career(
    name='Psychic',
    career_time='1d6',
    career_time_unit='years',
    prereq='none',
    intuition=1, luck=1, reputation=1, psionics=1,
    available_skills=['[psionic]', 'negotiation', 'bluffing', 'hypnotism', 'concentration', 'meditation'],
    desc='''You used your psionic abilities in a career of professional psychic work. Your skills are commercial and generalist in nature.''',
    available_exploits=[{'Name': 'Empathy', 'Desc': '''You can automatically sense strong emotions in others within 30'.'''},
                        {'Name': 'Ghostly advice', 'Desc': '''Once per day you may receive advice from “ghosts” (really lingering consciousness artifacts) which gives you a +2d6 die bonus to the next attribute check you make within 1 minute.'''},
                        {'Name': 'Precog', 'Desc': '''Your natural precognition gives you a +1d6 bonus to INITIATIVE checks as well as checks to access the ambush turn.'''},
                        {'Name': 'Fair trade', 'Desc': '''You are able to monitor a negotiation or bargaining situation with the agreement of both parties. You immediately sense any falsehood or deception on either part.'''}])

career_new_scientist = Career(
    name='Scientist',
    career_time='1d6',
    career_time_unit='years',
    prereq='[scientific]',
    intuition=1, logic=1, willpower=1, reputation=1,
    available_skills=['computers', '[scientific]', '[technical]', 'survival', 'perception'],
    desc='''You take your science with you as investigate phenomena in strange locations. Field scientists are viewed by academia as adventurous types, and include archaeologists, meteorologists, zoologists, oceanographers, geologists, botanists, astrophysicists, and much more. Scientists on starships are usually known as science officers.''',
    available_exploits=[{'Name': 'Scientific knowledge base', 'Desc': '''Choose four [scientific] skills. You gain these four skills at 1 rank (1d6). This does not increase the rank of an existing skill.'''},
                        {'Name': 'Analytical eye', 'Desc': '''You are able to identify the resistances, immunities, and vulnerabilities of any creature you can see with a Difficult [16] LOG check; if you use a hand-scanner, it is only a Challenging [13] LOG check. This requires two full actions of observation.'''},
                        {'Name': 'Improviser', 'Desc': '''In the field, you need to improvise. Using your scientific know-how, you can create a crude object or device from your surroundings. This requires a LOG check, with a difficulty value equal to the purchase value of the object, and takes 30 minutes.'''},
                        {'Name': 'Modify', 'Desc': '''You may modify the output of any energy weapon or device to any other energy type of your choice. This takes one minute. The device operates for five minutes, but breaks permanently when this time is up.'''}])

career_new_scout_special_forces = Career(
    name='Scout/Special Forces',
    career_time='1d6',
    career_time_unit='years',
    prereq='stealth or [combat]',
    strength=1, agility=1, endurance=1, intuition=1,
    available_skills=['[combat]', 'stealth', 'thievery', 'escape arts', 'acrobatics', 'climbing', 'survival', 'tracking', 'running'],
    desc='''The pinnacle of special operations, either police, military or freelance, the infiltrator aptly describes the occupation of many men and women whose job it is to infiltrate enemy locations and accomplish dangerous missions, and specialized soldiers able to operate alone and perform reconnaissance. A scout needs a range of skills beyond the mere ability to kill that is the hallmark of the assassin.''',
    available_exploits=[{'Name': 'Quick-hide', 'Desc': '''You are able to disappear while in plain sight. You can make a stealth check even while under observation to move your speed and become effectively invisible for a round. You may then make regular stealth checks as normal, but cannot repeat this feat against the same observer.'''},
                        {'Name': 'Hustle', 'Desc': '''Your SPEED increases by 2.'''},
                        {'Name': 'Hostile terrain', 'Desc': '''You do not suffer penalties for moving across difficult terrain.'''},
                        {'Name': 'Swimmer', 'Desc': '''You gain a SWIM speed equal to your regular SPEED.'''},
                        {'Name': 'Climber', 'Desc': '''You gain a CLIMB speed equal to your regular SPEED.'''}])

career_new_smuggler = Career(
    name='Smuggler',
    career_time='1d6',
    career_time_unit='years',
    prereq='piloting',
    agility=1, charisma=1, luck=1, reputation=1,
    available_skills=['thievery', 'astrogation', 'carousing', 'piloting', 'bluffing', 'appraisal', 'pistols'],
    desc='''You spent time as a smuggler, moving stolen or illegal goods from one planetary system to another.''',
    available_exploits=[{'Name': 'Smuggle', 'Desc': '''You know how to hide objects, either about your person or in a location. You gain a +2d6 bonus to attempts to hide items.'''},
                        {'Name': 'Secret routes', 'Desc': '''You know all the secret – if dangerous – trade routes. If you navigate a starship, you may reduce the journey distance (in parsecs) by 2d6%.'''},
                        {'Name': 'Haggler', 'Desc': '''You're a born haggler, and can reduce the cost of any purchase by 3d6%.'''},
                        {'Name': 'Fence', 'Desc': '''In an urban environment, you can sell goods for 75% of normal cost rather than 50%.'''},
                        {'Name': 'Seat of your pants', 'Desc': '''Smugglers rely a lot on old-fashioned luck and bravado. They can recharge their LUCK pool one extra time per day.'''}])

career_new_sniper = Career(
    name='Sniper',
    career_time='1d6',
    career_time_unit='years',
    prereq='stealth, rifles',
    endurance=1, intuition=1, willpower=1, luck=1,
    available_skills=['rifles', 'stealth', 'perception', 'concentration', 'climbing'],
    desc='''You mastered the art of lying very still for long periods of time and shooting people a long way away. Sniping is a job which requires great endurance, patience, and accuracy.''',
    available_exploits=[{'Name': 'Vantage point', 'Desc': '''You gain an additional +1d6 to attack with a ranged weapon if you are at least 30' higher than your target. This stacks with the regular +1d6 bonus for high ground.'''},
                        {'Name': 'Steady eye', 'Desc': '''All weapon range increments increase by 50%.'''},
                        {'Name': 'Good position', 'Desc': '''You cannot be pinned down in combat.'''},
                        {'Name': 'Perfect aim', 'Desc': '''. The bonus you gain for the Aim Exploit increases to +2d6.'''}])

career_new_socialite = Career(
    name='Socialite',
    career_time='1d6',
    career_time_unit='years',
    prereq='[social]',
    charisma=2, reputation=2,
    available_skills=['[social]'],
    desc='''You aim be famous for being famous, and have mastered the art of networking.''',
    available_exploits=[{'Name': 'High class', 'Desc': '''You are at home when in high-class social gatherings. In such environments, you gain a +1d6 bonus to all attribute checks. Unfortunately, you are less comfortable – or welcome - in lower-class environments, and suffer a -1d6 penalty to all social interactions in such situations.'''}])

career_new_space_jockey = Career(
    name='Space Jockey',
    career_time='1d6',
    career_time_unit='years',
    prereq='none',
    agility=1, endurance=1, logic=1, luck=1,
    available_skills=['zero-g', 'engineering', 'carousing', 'piloting', 'computers'],
    desc='''You got a commission on a civilian ship – a merchant vessel or miner. As a general dogsbody, you learned a variety of skills, and you feel truly at home aboard a vessel travelling between the stars.''',
    available_exploits=[{'Name': 'Zero-g monkey', 'Desc': '''You gain an effective fly speed equal to your regular SPEED in zero-g environments.'''},
                        {'Name': 'Mr. Fixit', 'Desc': '''You gain a +1d6 bonus to rolls made to repair starships.'''},
                        {'Name': 'Hitch-hiker', 'Desc': '''You can get free passage for yourself and your party on civilian vessels.'''},
                        {'Name': 'Used market', 'Desc': '''You know many starship dealers and merchants. You can save 10% on the cost of starship components.'''}])

career_new_spartan_battle_school = Career(
    name='Spartan Battle School',
    career_time='1d6',
    career_time_unit='years',
    prereq='Spartan',
    strength=2, agility=1, endurance=1,
    available_skills=['[combat]', 'survival', 'tactics', 'bravery'],
    desc='''Spartan education is brutal and militaristic.''',
    available_exploits=[{'Name': 'Swordsman', 'Desc': '''You gain a high quality Spartan sword.'''},
                        {'Name': 'Bred for war', 'Desc': '''You gain 3 points of natural SOAK. You also gain a distinctive scar.'''}])

career_new_starbase_assignment = Career(
    name='Starbase Assignment',
    career_time='1d6',
    career_time_unit='years',
    prereq='none',
    logic=1, charisma=1, reputation=2,
    available_skills=['carousing', 'computers', 'engineering', '[scientific]'],
    desc='''You were assigned to a Starbase or space station.''',
    available_exploits=[{'Name': 'Starbase layout', 'Desc': '''You become accustomed to the layout of starbases and outposts, and can navigate them without need for reference.'''}])

career_new_star_knight = Career(
    name='Star Knight',
    career_time='1d6',
    career_time_unit='years',
    prereq='concentration or meditation; law',
    agility=1, intuition=1, willpower=1, psionics=1,
    available_skills=['[psionic]', 'swords', 'reactions', 'meditation', 'concentration', 'law', '[physical]'],
    desc='''An elite order of warriors, the Star knights are respected throughout the galaxy. Star knights rarely use ranged weapons, engaging the enemy with their laser swords.''',
    available_exploits=[{'Name': 'Enhanced attributes', 'Desc': '''You gain +2 SPEED and +5' to both vertical and horizontal jump distances.'''},
                        {'Name': 'Psionic attributes', 'Desc': '''(requires Enhanced attributes) Once per round you may use your PSI attribute in place of any STR, AGI, or END check.'''},
                        {'Name': 'Laser sword', 'Desc': '''You build your own standard quality laser sword. Every time the Star Knight gains a grade, roll 1d6. On a 6, the laser sword increases quality by one category.'''},
                        {'Name': 'Missile deflection', 'Desc': '''(requires Laser Sword) You are able to deflect incoming ranged attacks with your laser sword. This allows you to use your laser sword for DEFENSE against ranged attacks as well as from melee attacks.'''},
                        {'Name': 'Throw sword', 'Desc': '''(requires Laser Sword) You can throw a laser sword as a ranged weapon with a range increment of 10'. The sword returns to your hand.'''},
                        {'Name': 'Sense psionics', 'Desc': '''You can sense the presence of psionics within 30' of you.'''},
                        {'Name': 'Foresight', 'Desc': '''You always gain access to the ambush turn.'''},
                        {'Name': 'Recover', 'Desc': '''You can meditate for five minutes to recover full HEALTH once per day.'''},
                        {'Name': 'Refocus', 'Desc': '''(requires Recover) Once per day you can focus and recover HEALTH equal to your PSI attribute check. This takes two actions.'''},
                        {'Name': 'Summon', 'Desc': '''You can telekinetically call a Small or smaller object within 10' to your hand by using two actions. If the object is held by someone else, it will require an opposed PSI vs. STR check.'''},
                        {'Name': 'Telekinesis', 'Desc': '''(requires Summon) You can freely telekinetically move and manipulate single objects of Small size or smaller within 30' of you. You may only manipulate one such object at a time.'''},
                        {'Name': 'Psychic choke', 'Desc': '''(requires Telekinesis) You can squeeze the breath from a victim within 30' with a PSI vs. DEFENSE check, causing 3d6 blunt damage.'''},
                        {'Name': 'Psychic push', 'Desc': '''(requires Telekinesis) Once per round you can, as an action, make a PSI vs. DEFENSE attack to push a single creature of size Medium or smaller a distance in feet equal to your PSI check.'''},
                        {'Name': 'Telepathic message', 'Desc': '''You develop the ability to freely send short telepathic messages to other intelligent creatures with whom you have spent time.'''},
                        {'Name': 'Psychic suggestion', 'Desc': '''(requires Telepathic Message) You can momentarily influence the thoughts and actions of another creature within 30' by making a PSI vs. MENTAL DEFENSE check.'''},
                        {'Name': 'Destiny', 'Desc': '''You may meditate for 5 minutes once per day to replenish your LUCK pool.'''}])

career_new_street_thug = Career(
    name='Street Thug',
    career_time='1d6',
    career_time_unit='years',
    prereq='none',
    strength=1, endurance=1, charisma=1, luck=1,
    available_skills=['intimidation', 'running', 'brawling', 'clubs', 'knives', 'pistols'],
    desc='''You fell into the fringes of society and ended up as a thug on the street, committing petty crimes for small amounts of money.''',
    available_exploits=[{'Name': 'The filth!', 'Desc': '''You have developed an uncanny ability to detect cops. When attempting to sniff out a police officer or similar authority figure, you gain a +1d6 bonus.'''},
                        {'Name': 'Street tough', 'Desc': '''Life on the streets is tough. You gain a natural +2 SOAK.'''}])

career_new_systems_upgrade = Career(
    name='Systems Upgrade',
    career_time='1d6',
    career_time_unit='months',
    prereq='Android; computers, engineering',
    available_skills=[],
    desc='''You spent time upgrading your software or hardware.''',
    available_exploits=[{'Name': 'Modification', 'Desc': '''Choose one modification from the Android species Exploits list. You may repeat this Exploit.'''}])

career_new_trader = Career(
    name='Trader',
    career_time='1d6',
    career_time_unit='years',
    prereq='none',
    intuition=1, charisma=1, luck=1, reputation=1,
    available_skills=['appraisal', '[social]', 'carousing', '[crafting]', 'bureaucracy', 'accounting', 'law', 'local knowledge', 'bribery', 'forgery'],
    desc='''Life as a trader can mean profit, but it can also bring ruin.''',
    available_exploits=[{'Name': 'Sale of the century', 'Desc': '''You worked hard on a great deal, and it netted you 1,000Cr. You may repeat this Exploit, gaining 1,000Cr each time.'''},
                        {'Name': 'Trade routes', 'Desc': '''You know the best, most profitable trade routes. Your starship fuel costs are reduced by 20%.'''},
                        {'Name': 'Haggler', 'Desc': '''You know how to get a good deal. You reduce the cost of any purchase by 2d6%.'''}])

career_new_venetian_retreat = Career(
    name='Venetian Retreat',
    career_time='4d6',
    career_time_unit='years',
    prereq='Venetian',
    logic=2, willpower=1, psionics=1,
    available_skills=['[artistic]', '[psionic]', '[crafting]', 'concentration', 'meditation'],
    desc='''The long-lived Venetians often retire to their own kind for a decade or more in order to contemplate their place in the universe, and train their minds.''',
    available_exploits=[{'Name': 'Fortified', 'Desc': '''You gain a +5 bonus to MENTAL DEFENSE.'''}])

career_new_list = [career_new_athlete, career_new_bartender, career_new_battlepsyche, career_new_biopsychic,
                   career_new_bounty_hunter, career_new_burglar, career_new_college, career_new_con_artist,
                   career_new_craftsman, career_new_detective, career_new_diplomat, career_new_engineer,
                   career_new_gambler, career_new_gangster, career_new_intelligence_officer_spy,
                   career_new_marine_cadet_assignment, career_new_marine_tour, career_new_medic, career_new_miner,
                   career_new_navy_cadet_cruise, career_new_navy_tour, career_new_performer, career_new_pilot,
                   career_new_police_officer, career_new_priest, career_new_prisoner, career_new_psi_cop,
                   career_new_psychic, career_new_scientist, career_new_scout_special_forces, career_new_smuggler,
                   career_new_sniper, career_new_socialite, career_new_space_jockey, career_new_spartan_battle_school,
                   career_new_starbase_assignment, career_new_star_knight, career_new_street_thug,
                   career_new_systems_upgrade, career_new_trader, career_new_venetian_retreat]

for career in career_new_list:
    career.available_skills.sort()
