from lib.character import Career

career_ma_aikido = Career(
    name='Aikido',
    career_time='1d6',
    career_time_unit='years',
    prereq='martial arts',
    agility=1, intuition=1, willpower=1, chi=1,
    available_skills=['acrobatics', 'escape artist', 'reactions', 'martial arts'],
    desc='''Blending the force of your attacker with your own movements, you have mastered the art of redirecting a foe’s movement to your advantage, placing them in disadvantageous positions with joint locks and a chilling understanding of functional anatomy.''',
    available_exploits=[{'Name': '''Curriculum exploits''', 'Desc': '''Choose any three soft exploits from the Universal Exploits for Martial Artists sidebar.'''},
                        {'Name': '''Improved throw''', 'Desc': '''(requires Throw) Your throwing distance increases by 5' and deals +1d6 damage.'''},
                        {'Name': '''Reactive lock''', 'Desc': '''(requires Arm Lock) You may may use the Arm Lock exploit to make an attack as a reaction when an attacker misses you with a melee attack.'''},
                        {'Name': '''Paralyzing strike''', 'Desc': '''Spend 2 actions to make a precise strike that both deals damage and immobilizes the target until they shake the condition off.'''},
                        {'Name': '''Aikido weapons''', 'Desc': '''You may use your martial arts skill with swords, knives, and staves.'''}])

career_ma_brazilian_jujutsu = Career(
    name='Brazilian Jujutsu',
    career_time='1d6',
    career_time_unit='years',
    prereq='martial arts',
    strength=1, agility=1, endurance=1, reputation=1,
    available_skills=['acrobatics', 'meditation', 'martial arts'],
    desc='''Taking your opponents down with expert technique and leverage, you take them to the ground, where you are a master combatant.''',
    available_exploits=[{'Name': '''Ground fighter''', 'Desc': '''Opponents do not gain a bonus to hit you in melee when you are prone.'''},
                        {'Name': '''Momentous knockdown''', 'Desc': '''(requires Knockdown)  You do not pay a dice cost to perform the Knockdown exploit; however both you and the target are prone after a successful attempt.'''},
                        {'Name': '''Forced submission''', 'Desc': '''(requires Arm Lock)  If both you and your target are prone, and you have successfully applied an Arm Lock, you may make a melee attack against his MENTAL DEFENSE to force him to submit. If successful, your target is reduced to zero HEALTH but does not fall unconscious.'''},
                        {'Name': '''Escape''', 'Desc': '''When pinned, locked, or held by another combatant, you may use a reaction to make an immediate attempt to escape the pin.'''}])

career_ma_capoeira = Career(
    name='Capoeira',
    career_time='1d6',
    career_time_unit='years',
    prereq='dancing, martial arts',
    agility=1, intuition=1, luck=1, chi=1,
    available_skills=['acrobatics', 'dancing', 'jumping', 'reactions', 'martial arts'],
    desc='''Training with a capoeira master, you’ve become more adept at the acrobatic martial art, able to tumble, cartwheel, and flip around your enemies with ease.''',
    available_exploits=[{'Name': '''Curriculum exploits''', 'Desc': '''Choose any three hard exploits from the Universal Exploits for Martial Artists sidebar.'''},
                        {'Name': '''Ginga''', 'Desc': '''You gain +2 to your DEFENSE attribute against melee attacks.'''},
                        {'Name': '''Asymmetric advantage''', 'Desc': '''If you are engaged in melee with two or more opponents, you gain +1d6 to attack for every two opponents actively engaging you in melee combat. In other words, if you are being attacked by four foes, you gain +2d6 to attack.'''},
                        {'Name': '''Rasteira''', 'Desc': '''(requires Trip) If an adjacent enemy makes a movement action, you may take a trip attack against them as a reaction.'''},
                        {'Name': '''Asymmetric adept''', 'Desc': '''(requires Asymmetric advantage) For every foe past the first, you gain +1 MELEE DEFENSE.'''},
                        {'Name': '''Roda''', 'Desc': '''Capoeira works better to music. When music is playing publicly, you can make an additional unarmed attack per round as a free action. You cannot attach any exploit to this attack.'''},
                        {'Name': '''Capoeira weapons''', 'Desc': '''You may use your martial arts skill with knives.'''}])

career_ma_gun_fu = Career(
    name='Gun Fu',
    career_time='1d6',
    career_time_unit='years',
    prereq='pistols',
    agility=1, intuition=1, luck=1, chi=1,
    available_skills=['pistols', 'reactions', 'running', 'tactics', 'martial arts', 'jumping'],
    desc='''You have mastered the synthesis of modern weaponry with ancient martial arts, able to maximize the power and accuracy of firearms by integrating the forms of various styles into one terrifying dance of explosive death. ''',
    available_exploits=[{'Name': '''Rapid reload''', 'Desc': '''You may fire firearms with the single trait twice per round instead of once.'''},
                        {'Name': '''Sliding fusillade''', 'Desc': '''For two actions, you can take your full movement in a straight line and make up to two attack actions.'''},
                        {'Name': '''Firing forms''', 'Desc': '''By spending all of your actions, you can take as many attack actions as there are targets, up to your INT attribute. You may only fire at a given target once, and each cumulative shot beyond the first takes a -1d6 penalty.'''},
                        {'Name': '''Leaping ballistics''', 'Desc': '''When you perform a jump, you may make one gun attack for free.'''},
                        {'Name': '''Curved bullet''', 'Desc': '''You may spend a LUC die to curve a bullet round a corner once per round, effectively negating your target's cover. You must still have line of sight; this ability negates cover, but does not create new lines of sight.'''},
                        {'Name': '''Cover me!''', 'Desc': '''Any sidearm you use automatically gains the auto trait, making it especially suitable for suppressive fire.'''},
                        {'Name': '''Dual pistols''', 'Desc': '''You are considered to have the ambidextrous trait while holding two sidearms, even if you do not have that trait.'''},
                        {'Name': '''When doves fly''', 'Desc': '''Once per day you can cause a number of white doves to fly across the background.'''}])

career_ma_gun_kata = Career(
    name='Gun Kata',
    career_time='1d6',
    career_time_unit='years',
    prereq='pistols',
    agility=1, intuition=1, willpower=1, chi=1,
    available_skills=['pistols', 'martial arts', 'acrobatics', 'reactions', 'dancing'],
    desc='''You have learned the unusual but beautiful art of melee gun combat, where the gun is considered a total weapon and katas are performed which statistically inflict the maximum damage on the largest number of targets while avoiding statistically likely trajectories of return fire.''',
    available_exploits=[{'Name': '''Gunpunch''', 'Desc': '''Once per round, while holding a sidearm, your martial arts attack does the damage of your gun.'''},
                        {'Name': '''Multipunch''', 'Desc': '''(requires Gunpunch) If you are dual-wielding pistols, all of your martial arts attacks do the damage of your gun.'''},
                        {'Name': '''Closedown''', 'Desc': '''When attacked by somebody with a gun 10' or less away from you, you immediately move adjacent to them and perform a martial arts attack as a reaction.'''},
                        {'Name': '''Bulletcatcher''', 'Desc': '''Once per turn as a reaction you can catch a single bullet fired at you as long as you are aware of the attack. This does not help against weapons with the auto trait.'''},
                        {'Name': '''Return trajectories''', 'Desc': '''Your skill in pistols can be used as part of your DEFENSE pool against firearms.'''},
                        {'Name': '''Statistical pose''', 'Desc': '''You are able to adopt positions statistically most unlikely to be struck by gunfire. You gain +4 RANGED DEFENSE against firearms.'''}])

career_ma_jujutsu = Career(
    name='Jujutsu',
    career_time='1d6',
    career_time_unit='years',
    prereq='martial arts',
    strength=1, agility=1, endurance=1, chi=1,
    available_skills=['meditation', 'melee weapon', 'stealth', 'martial arts'],
    desc='''Trained in fighting an armed opponent with your feet and fists, you are a fluid warrior in combat, adapting to best use your enemy’s movements against them.''',
    available_exploits=[{'Name': '''Curriculum exploits''', 'Desc': '''Choose any two hard or soft exploits from the Universal Exploits for Martial Artists sidebar.'''},
                        {'Name': '''Breaking fall''', 'Desc': '''You take half damage from falls, throws, and trips.'''},
                        {'Name': '''Fluid resistance''', 'Desc': '''Once per turn, after taking damage from a melee attack, you automatically make a counterattack as a reaction.'''},
                        {'Name': '''Reactive disarm''', 'Desc': '''(requires Disarm) Once per turn, after a melee attack misses you, you automatically make a reactive attack which, if successful, disarms your attacker.'''},
                        {'Name': '''Reactive takedown''', 'Desc': '''(requires Trip) Once per turn, after a melee attack misses you, you automatically make a reactive attack which, if successful, trips your attacker.'''},
                        {'Name': '''Jujutsu weapons''', 'Desc': '''You may use your martial arts skill with swords, spears, polearms, and staves.'''}])

career_ma_karate = Career(
    name='Karate',
    career_time='1d6',
    career_time_unit='years',
    prereq='martial arts',
    strength=1, agility=1, willpower=1, chi=1,
    available_skills=['meditation', 'martial arts'],
    desc='''You learned a striking art which focuses on punches, kicks, and knee and able strikes, as well as open hand strikes.''',
    available_exploits=[{'Name': '''Curriculum exploits''', 'Desc': '''Choose any three hard exploits from the Universal Exploits for Martial Artists sidebar.'''},
                        {'Name': '''Wax On, Wax Off''', 'Desc': '''You develop patience while performing rote training tasks. You gain +2 MELEE DEFENSE and MENTAL DEFENSE.'''},
                        {'Name': '''Knifehand strike''', 'Desc': '''You strike with the edge of your hand, stunning your foe with a successful it.'''},
                        {'Name': '''Crane stance''', 'Desc': '''You adopt a stance by spending an action. You cannot move while in this stance. If any foe attempts to engage you melee combat, you gain a free attack as a reaction against him. This attack takes place before your foe's attack. Once you have made this attack, your stance ends.'''},
                        {'Name': '''Double punch''', 'Desc': '''You may use one action to make two unarmed attacks against a single foe. You may not add additional exploits to these two attacks.'''},
                        {'Name': '''Conditioning''', 'Desc': '''Your unarmed attacks do +1d6 damage.'''},
                        {'Name': '''Karate weapons''', 'Desc': '''You may use your martial arts skill with swords, spears, polearms, and staves.'''}])

career_ma_krav_maga = Career(
    name='Krav Maga',
    career_time='1d6',
    career_time_unit='years',
    prereq='martial arts',
    strength=1, agility=1, endurance=1, chi=1,
    available_skills=['perception', 'reactions', 'throwing', 'martial arts'],
    desc='''Studying one of the newest and most practical martial arts has taught you to end a fight as soon as it starts (if it has to) and to make the most out of your attacks with the least effort.''',
    available_exploits=[{'Name': '''Curriculum exploits''', 'Desc': '''Choose any three hard exploits from the Universal Exploits for Martial Artists sidebar.'''},
                        {'Name': '''Know the arena''', 'Desc': '''In any location, you automatically note any non-hidden exits from the vicinity. You are easily able to improvise weapons using your surroundings–glasses, rocks, and so on; you always count as carrying a knife or club.'''},
                        {'Name': '''Brutal counter''', 'Desc': '''After an enemy makes a successful melee attack on you, you gain +1d6 damage in melee against that foe. If any other enemy strikes you, your bonus damage switches to that target.'''},
                        {'Name': '''Weak points''', 'Desc': '''You are adept at targeting weak or vulnerable points in your foes, and can ignore SOAK by spending one LUC die.'''},
                        {'Name': '''Impromptu weapon''', 'Desc': '''No matter the size of an impromptu weapon (so long as it is tiny or larger), you can deal slashing, blunt, piercing, or blunt damage with it by making a thrown ranged attack. This does not count as an improvised weapon.'''}])

career_ma_kung_fu = Career(
    name='Kung Fu',
    career_time='1d6',
    career_time_unit='years',
    prereq='martial arts',
    agility=1, endurance=1, willpower=1, chi=1,
    available_skills=['acrobatics', 'meditation', 'perception', 'reactions', 'staves', 'martial arts'],
    desc='''Through intense and dedicated training, you've begun to unlock the secrets of the ancient martial arts of China. You can sense and feel the essence of your being and are able to manipulate not only that life energy, but also your body, to its maximum effect. With these skills at your disposal, you are a fearsome opponent in combat and able to perform feats of finesse and strength that dazzle your peers.''',
    available_exploits=[{'Name': '''Curriculum exploits''', 'Desc': '''Choose any two hard or soft exploits from the Universal Exploits for Martial Artists sidebar.'''},
                        {'Name': '''One-inch punch''', 'Desc': '''When pinned or grappled, you may make an unarmed attack against your foe as a free action and gain +1d6 damage to it.'''},
                        {'Name': '''Double strike''', 'Desc': '''With one action you may strike two opponents with a melee attack each. You cannot add additional exploits to these attacks.'''},
                        {'Name': '''Sticking hands''', 'Desc': '''You remain in constant contact with your foe's arms and hands, allowing you to easily deflect attacks and counter. You gain +2 MELEE DEFENSE against one adjacent opponent, and may counterstrike with a basic (no additional exploits) unarmed attack against that foe as a reaction to any missed attack.'''},
                        {'Name': '''Active resistance''', 'Desc': '''Once per day, spend an action to prepare and gain SOAK to one type of damage equal to your CHI for one minute. This resistance stacks with any others you or your equipment possess.'''},
                        {'Name': '''Kung Fu weapons''', 'Desc': '''You may use your martial arts skill with any Eastern melee weapon.'''}])

career_ma_muay_thai = Career(
    name='Muay Thai',
    career_time='1d6',
    career_time_unit='years',
    prereq='martial arts',
    strength=1, endurance=1, willpower=1, chi=1,
    available_skills=['acrobatics', 'climbing', 'jumping', 'reactions', 'martial arts'],
    desc='''Dedicated conditioning is a part of your daily routine, and you cannot count the number of times you’ve struck out against a tree trunk with your leg, but it doesn’t matter: your body truly is a living weapon. You have mastered the art of Thai boxing.''',
    available_exploits=[{'Name': '''Curriculum exploits''', 'Desc': '''Choose any three hard exploits from the Universal Exploits for Martial Artists sidebar.'''},
                        {'Name': '''Mae maei''', 'Desc': '''You gain +2 natural SOAK.'''},
                        {'Name': '''Thip''', 'Desc': '''You make a devastating kick; on a successful hit, instead of dealing damage the target is dazed until they shake the condition off.'''},
                        {'Name': '''Chok-te''', 'Desc': '''Gain a cumulative +1d6 to attack every time you make an unarmed attack which misses. Once an attack hits, your bonus resets to zero.'''},
                        {'Name': '''Ti khao and sok''', 'Desc': '''You leap quickly (up to your jump distance) and drive the momentum of your jump into a knee or elbow strike that ignores a target’s SOAK; you take an amount of damage equal to half of what you deliver to the target.'''}])

career_ma_northern_shaolin = Career(
    name='Northern Shaolin',
    career_time='1d6',
    career_time_unit='years',
    prereq='martial arts',
    agility=1, endurance=1, willpower=1, chi=1,
    available_skills=['hardy', 'melee weapon', 'nature', 'running', 'martial arts'],
    desc='''Focusing on the use of your legs and staying quick on your feet, you practice styles like Baguazhang, Eagle Claw, Northern Praying Mantis, or Chángquán.''',
    available_exploits=[{'Name': '''Curriculum exploits''', 'Desc': '''Choose any three soft exploits from the Universal Exploits for Martial Artists sidebar.'''},
                        {'Name': '''Fast feet''', 'Desc': '''You gain a +2 SPEED bonus.'''},
                        {'Name': '''Shifting forms''', 'Desc': '''You gain a +2 MELEE DEFENSE bonus.'''},
                        {'Name': '''Rolling defense''', 'Desc': '''(requires Roll With It) When you use the Roll With It combat exploit you finish the maneuver standing.'''},
                        {'Name': '''CHI healing''', 'Desc': '''Once per day you may roll your CHI dice pool and recover that much HEALTH. This takes one minute.'''}])

career_ma_pankration = Career(
    name='Pankration',
    career_time='1d6',
    career_time_unit='years',
    prereq='martial arts or boxing',
    strength=1, endurance=1, willpower=1, luck=1,
    available_skills=['acrobatics', 'climbing', 'reactions', 'running', 'boxing'],
    desc='''The truest expression of a person’s fighting ability, some would say, is the ancient art of wrestling—you count yourself among their number. After hundreds of matches, you know exactly the best way to grapple and pin an opponent in any situation.''',
    available_exploits=[{'Name': '''Curriculum exploits''', 'Desc': '''Choose any three soft exploits from the Universal Exploits for Martial Artists sidebar.'''},
                        {'Name': '''Olympic stance''', 'Desc': '''Spend 1 action to enter an Olympic stance. While in an Olympic stance your movement is halved, but you gain +4 MELEE DEFENSE.'''},
                        {'Name': '''Straight kick''', 'Desc': '''You make a devastating kick; on a successful hit, instead of dealing damage the target is sickened until they shake the condition off.'''},
                        {'Name': '''Great bear''', 'Desc': '''(requires Bear Hug) If you choose not to move in a round when applying a bear hug, you do double damage to your target.'''},
                        {'Name': '''Takedown''', 'Desc': '''(requires Knockdown) You may use the Knockdown exploit with no die penalty.'''}])

career_ma_savate = Career(
    name='Savate',
    career_time='1d6',
    career_time_unit='years',
    prereq='martial arts',
    agility=1, endurance=1, luck=1, chi=1,
    available_skills=['acrobatics', 'climbing', 'jumping', 'running', 'martial arts'],
    desc='''Training with a champion of the sport or learning the hard way on the meaner streets in Marseille or Paris, you’ve studied the martial art of France and can put it to great use.''',
    available_exploits=[{'Name': '''Curriculum exploits''', 'Desc': '''Choose any three hard exploits from the Universal Exploits for Martial Artists sidebar.'''},
                        {'Name': '''Assault savate''', 'Desc': '''Increase your jump distance by 50%. With a successful attack you may feint an opponent, just barely touching them and steal or place one small item, like a playing card or wallet, on their person without their notice.'''},
                        {'Name': '''Pre-combat savate''', 'Desc': '''Any turn that you jump, add +2d6 damage to any attack you make as you land. You must jump more than 5’ to gain this bonus.'''},
                        {'Name': '''Combat savate''', 'Desc': '''When you take damage from a melee attack, you may take the blow’s momentum and use it to your advantage, gaining an attack bonus equal to the damage caused to the next melee attack you make.'''},
                        {'Name': '''Long kick''', 'Desc': '''Once per turn you may kick a target 10' from you with a lunge.'''},
                        {'Name': '''Heavy shoe''', 'Desc': '''A heavy shin kick immobilizes your foe until they shake the condition off.'''}])

career_ma_southern_shaolin = Career(
    name='Southern Shaolin',
    career_time='1d6',
    career_time_unit='years',
    prereq='martial arts',
    agility=1, endurance=1, willpower=1, chi=1,
    available_skills=['climbing', 'hardy', 'melee weapon', 'nature', 'martial arts'],
    desc='''Your body is a weapon, and your hands are deadly indeed. Using styles like Fujian White Crane, Wing Chun, Southern Praying Mantis, Bak Mei and Dragon, you are a master of Nanquan—the Southern Fist.''',
    available_exploits=[{'Name': '''Curriculum exploits''', 'Desc': '''Choose any three hard exploits from the Universal Exploits for Martial Artists sidebar.'''},
                        {'Name': '''Empty hand''', 'Desc': '''Whenever you successfully perform a Disarm combat exploit, instead of the target dropping its weapon, you take it in hand and may make one free attack with it on the target.'''},
                        {'Name': '''Godfist''', 'Desc': '''(requires Knockback) When you use the Knockback combat exploit, you double the distance a target is moved. The target becomes stunned until they shake the condition off.'''},
                        {'Name': '''Flowing attacker''', 'Desc': '''For each 5’ you travel during a turn, you may make one attack. For every attack after the first, you take a cumulate -1d6 to the attack roll. Once you miss, your attack streak ends. This uses all of your actions for the turn.'''}])

career_ma_list = [career_ma_aikido, career_ma_brazilian_jujutsu, career_ma_capoeira, career_ma_gun_fu,
                  career_ma_gun_kata, career_ma_jujutsu, career_ma_karate, career_ma_krav_maga,
                  career_ma_kung_fu, career_ma_muay_thai, career_ma_northern_shaolin, career_ma_pankration,
                  career_ma_savate, career_ma_southern_shaolin]

for career in career_ma_list:
    career.available_skills.sort()
