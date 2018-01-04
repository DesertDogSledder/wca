from lib.character import Career

career_old_alchemist = Career(
    name='Alchemist',
    career_time='1d6',
    career_time_unit='years',
    prereq='herbalism, alchemy',
    logic=1, endurance=1, magic=1, reputation=1,
    available_skills=['cooking', 'brewing', 'alchemy', 'concentration', 'healing', 'animal handling'],
    desc="Alchemists mix potions and substances, and transforms substances from one to another. Creating elixirs of "
         "life in bubbling cauldrons and seeking the secrets of magical chemistry, alchemists are true creators. Many "
         "make a living selling their concoctions. Unlike herbalism, alchemy involves a touch of magic. For each "
         "alchemical concoction, you should roll and note down an Alchemical Science result. This describes the "
         "nature of the concoction, whether it requires you to dilute amber in a jade keg, or cool mercury in a ruby "
         "flute.",
    available_exploits=[{'Name': 'Explosive alchemy',
                         'Desc': "You can create an explosive concoction using your alchemy kit. This takes a full "
                                 "round (two actions), and the concoction can be thrown (range increment 3, "
                                 "radius 5', damage 3d6 fire). The concoction can only be stored for 5 minutes before "
                                 "it stops working."},
                        {'Name': 'Healing potion',
                         'Desc': "You can use your alchemy kit to heal 2d6 HEALTH in yourself or any creature you can "
                                 "touch. No creature may benefit from this more than once per day."},
                        {'Name': 'Gaseous concoction',
                         'Desc': "(requires Concoction, alchemy 5) Your concoction can be thrown in a glass bottle "
                                 "which breaks on inpact, causing a 10' radius area of gas."},
                        {'Name': 'Greater healing potion',
                         'Desc': "(requires Healing Potion, alchemy 3) Your healing ability using your alchemy kit "
                                 "improves. You may now restore 3d6 HEALTH."},
                        {'Name': 'Concoction',
                         'Desc': "Choose one status track. You can spend five minutes to create a concoction which, "
                                 "when drunk (and a MAG vs. the appropriate DEFENSE attack is made), "
                                 "moves the recipient one stage along that track. You may take this exploit multiple "
                                 "times, choosing a new status track each time."},
                        {'Name': 'Strong concoction',
                         'Desc': "(requires Concoction, alchemy 3) One concoction you can create using the Concoction "
                                 "exploit now moves targets two stages along that status track."},
                        {'Name': 'Sticky concoction',
                         'Desc': "(requires Concoction, alchemy 3) You may turn your concoction into a substance "
                                 "which can be delivered via a blade or an arrow. Apply an already-created concoction "
                                 "to an edged weapon. The next successful damaging attack made by that weapon will "
                                 "deliver the concoction to the target as though it had drunk it. This only lasts for "
                                 "one successful attack or for five minutes, whichever comes first."},
                        {'Name': 'Protective oil',
                         'Desc': "You may spend 5 minutes to create a an oil which, when smeared over a creature, "
                                 "grants it SOAK 2 against one damage type. This is enough to protect against "
                                 "climate-based effects."}])

career_old_archer = Career(
    name='Archer',
    career_time='1d6',
    career_time_unit='years',
    prereq='AGI 3+',
    strength=1, agility=1, luck=1, reputation=1,
    available_skills=['bows', 'perception', 'carousing', 'survival'],
    desc="You joined the army as an archer, manning walls and front lines in times of war.",
    available_exploits=[{'Name': 'Long shot',
                         'Desc': "You have an eye for distance. You can double the range increment of a bow by taking "
                                 "a -1d6 die penalty to damage."},
                        {'Name': 'Bowyer',
                         'Desc': "You know how to maintain your equipment. One standard quality bow becomes a high "
                                 "quality weapon, as long as you spend an hour maintaining it every day."},
                        {'Name': 'Careful aim', 'Desc': "When aiming, your bonus to hit increases to +2d6."},
                        {'Name': 'Rapid shot',
                         'Desc': "Your rate of fire increases; once per turn you can fire two shots instead of one."},
                        {'Name': 'Stand your ground',
                         'Desc': "As long as you do not move, you can plant arrows in the ground and loose two shots "
                                 "every action."},
                        {'Name': 'Double shot',
                         'Desc': "You notch two arrows and let both fly simultaneously. Each must be directed at a "
                                 "different target, and both targets must be within 10' of each other. You cannot "
                                 "combine this ability with any other exploits."},
                        {'Name': 'Intercepting shot',
                         'Desc': "(requires INT 8+; Rapid Shot) You can shoot another arrow out of the sky as a "
                                 "reaction. Roll an opposed attack roll against that of the attacker's arrow; if you "
                                 "succeed, the arrow is split and falls harmlessly to the ground."}])

career_old_assassin = Career(
    name='Assassin',
    career_time='1d6',
    career_time_unit='years',
    prereq='stealth',
    agility=1, intuition=1, willpower=1, reputation=1,
    available_skills=['stealth', 'thievery', 'perception', 'intimidate', 'disguise', '[melee weapon]',
                      '[ranged weapon]', 'herbalism'],
    desc="A killer for hire, you mastered the skills of assassination.",
    available_exploits=[{'Name': 'Surprise attack',
                         'Desc': "If you successfully hit a target before it becomes aware of you, you gain a +2d6 "
                                 "damage bonus."},
                        {'Name': 'Death blow',
                         'Desc': "(requires Surprise Attack) Your damage bonus for attacking unaware targets "
                                 "increases to +4d6."},
                        {'Name': 'Poison resistance',
                         'Desc': "You become resistant to poisons, gaining SOAK 5 poison and an additional die in "
                                 "your countdown die pool when poisoned."},
                        {'Name': 'Quiet kill',
                         'Desc': "You are a master of silent death. Any target you kill during the ambush turn dies "
                                 "silently and without obvious visible signs. Nobody will notice that the target is "
                                 "dead for one minute, and will require a Strenuous [21] INT check to realize it "
                                 "thereafter."},
                        {'Name': 'Weak point',
                         'Desc': "Once per enemy you may ignore any SOAK score it possesses by targeting a weak spot. "
                                 "You can never use this ability on the same enemy again."}])

career_old_barbarian = Career(
    name='Barbarian',
    career_time='1d6',
    career_time_unit='years',
    prereq='none',
    strength=1, endurance=1, agility=1, intuition=1,
    available_skills=['swords', 'axes', 'spears', '[physical]', '[outdoor]', 'hardy', 'herbalism'],
    desc="Tribal warriors from the very fringes of civilization, barbarians are wild and uncouth. Barbarians "
         "exemplify physical prowess and natural prowess, but can feel uncomfortable in enclosed spaces.",
    available_exploits=[
        {'Name': 'Fleet of foot', 'Desc': "In an outdoor environment, you gain a +2 bonus to your SPEED."},
        {'Name': 'Mighty leap', 'Desc': "Your horizontal free jump distance increases by 5' (one square)."},
        {'Name': 'Set in the old ways', 'Desc': "You gain +5 to your MENTAL DEFENSE."},
        {'Name': 'Primal charge',
         'Desc': "(requires Fleet of Foot) When charging, you howl and screech, moving twice your SPEED and gaining "
                 "+2d6 to damage."},
        {'Name': 'Hides &amp; skins',
         'Desc': "You know how to make the most out of basic gear. Hide armor worn by a barbarian counts as one "
                 "quality level higher than it actually is."},
        {'Name': 'Leathery skin', 'Desc': "You gain +2 natural SOAK from hard, conditioned, leathery skin."},
        {'Name': 'Iron skin', 'Desc': "(requires Leathery Skin) Your natural SOAK bonus increases to +4."},
        {'Name': 'Sacred terrain',
         'Desc': "Choose a terrain type, such as forest, plains, ocean, or mountains. When in that terrain, "
                 "you gain a +1d6 to all dice pools; however, when not in that terrain, you suffer a -1d6 penalty to "
                 "all dice pools."},
        {'Name': 'Beastly visage',
         'Desc': "You have modified your body in various ways (scars, tattoos, piercings) as to make yourself as "
                 "intimidating as possible. With a CHA vs. MENTAL DEFENSE attack, you can move a target who can see "
                 "and hear you one stage along the Fear status track."},
        {'Name': 'Scarred visage',
         'Desc': "(requires Beastly Visage, Leathery Skin) You are covered in scars. You are immune to the Bleeding "
                 "status track."},
        {'Name': 'Keen senses', 'Desc': "You gain +1d6 to perception checks."},
        {'Name': 'Trophy collection',
         'Desc': "(requires Set In The Old Ways) You collect gruesome trophies from your vanquished foes – teeth, "
                 "skills, bones, etc. Each trophy replenishes one LUCK die in your LUCK dice pool, and loses its "
                 "power once the LUCK die is spent. You may only claim a trophy if you delivered the killing blow to "
                 "a creature of Medium size or larger."},
        {'Name': 'Reap the whirlwind',
         'Desc': "You may spend two actions to make one melee attack against every adjacent foe. You cannot add "
                 "additional exploits to these attacks."},
        {'Name': 'Feral',
         'Desc': "You gain a bite attack; your natural damage increases by +1d6 and becomes piercing damage."},
        {'Name': 'Natural serenity',
         'Desc': "(requires Sacred Terrain) In your chosen sacred terrain, you may pause for five minutes once per "
                 "day, reflecting on nature and speaking to the Old Gods, to recover your full HEALTH."}])

career_old_berserker = Career(
    name='Berserker',
    career_time='1d6',
    career_time_unit='years',
    prereq='STR 6+, Feral exploit',
    strength=1, endurance=1, charisma=1, luck=1,
    available_skills=['sword', 'axe', 'spear', '[physical]', '[unarmed]', 'hardy'],
    desc="Some barbarians become berserkers – raging warriors of fury.",
    available_exploits=[{'Name': 'Frenzy',
                         'Desc': "You can fly into a berserk rage. When berserk, you must attack the closest enemy, "
                                 "and move on to the next closest thereafter. You gain SOAK +5 (even when wearing "
                                 "armor) and +1d6 damage. Each round you rage for, you take 1d6 damage; you do not "
                                 "stop raging until you pass out or until all enemies are dead."},
                        {'Name': 'One with nature',
                         'Desc': "(requires Frenzy) When frenzied and wearing no armor, you gain a +4 MELEE DEFENSE "
                                 "bonus."},
                        {'Name': 'Regenerate',
                         'Desc': "(requires Frenzy) Every time you deal a killing blow while frenzied you gain +1d6 "
                                 "HEALTH."},
                        {'Name': 'Fearless',
                         'Desc': "(requires Frenzy) While frenzied, you are completely immune to the Fear status "
                                 "track."}])

career_old_burglar = Career(
    name='Burglar',
    career_time='1d6',
    career_time_unit='years',
    prereq='stealth',
    agility=1, intuition=1, luck=1, reputation=1,
    available_skills=['climbing', 'jumping', 'acrobatics', 'escape artist', 'computers', 'stealth', 'thievery',
                      'appraisal'],
    desc="You become a master thief, able to infiltrate the most secure of locations. Some cat burglars work for hire "
         "and conduct industrial espionage, while others prefer to steal valuable artifacts and jewels from museums "
         "and high security vaults.",
    available_exploits=[{'Name': 'Locksmith',
                         'Desc': "You gain a exceptional quality lockpicking kit. You gain a +1d6 bonus to attempts "
                                 "to pick locks, combinations, guess passwords, or access security panels."},
                        {'Name': 'Catburglar',
                         'Desc': "An expert at climbing, you do not take any die penalties in combat while climbing."},
                        {'Name': 'Sixth sense',
                         'Desc': "You have a sixth sense when it comes to traps, and gain a +2d6 bonus to spot them "
                                 "and a +1d6 bonus to avoid or disarm them."},
                        {'Name': 'Climber',
                         'Desc': "(requires Catburglar) Your climbing speed becomes equal to your regular SPEED."},
                        {'Name': 'Grand heist',
                         'Desc': "You achieve a great robbery that will be remembered for years to come. Gain a bonus "
                                 "3d6 x 100gc. You may repeat this exploit, gaining 3d6x100gc each time."}])

career_old_cleric = Career(
    name='Cleric',
    career_time='1d6',
    career_time_unit='years',
    prereq='religion',
    willpower=1, logic=1, charisma=1, magic=1,
    available_skills=['healing', 'herbalism', 'religion', 'leadership', 'history', 'local knowledge', 'staves', 'maces',
                      '[magical]'],
    desc="The cleric devotes his or her life to a higher power, hoping to serve that power’s will. Whether the cleric "
         "serves a noble god or a vicious demon lord, he or she gains power from faith, and learns to wield powerful "
         "magic in the service of his or her deity. Clerics are also trained to be capable warriors, able to defend "
         "themselves physically if their spells fail them. Since clerics deal more in abstract realms of the soul and "
         "the spirit, their magic has a definite slant toward the intangible, generally eschewing direct offensive "
         "magic in favor of spells that affect creatures’ essence and behavior, or that make creatures more or less "
         "able to battle. Most clerics worship one specific deity from a pantheon, but still respect other members of "
         "that pantheon, even if they are not actual followers. The agendas of deities’ worshippers may conflict in "
         "the realm of mortals, but it is folly to defy even enemy deities. Thus, though a cleric may choose to "
         "change the deity he or she reveres, if the clerics truly abandons the pantheon, he or she will never be "
         "accepted by any deity, being forced to rely on mortal magic alone.",
    available_exploits=[{'Name': 'Beatification',
                         'Desc': "(requires religion 6) You gain the Virtue of your god. Additionally, all damage you "
                                 "do is damage of that Virtue type, whatever the delivery instrument."},
                        {'Name': 'Blessing/curse',
                         'Desc': "(requires Portfolio) You can issue a blessing or a curse. This takes one minute, "
                                 "lasts one hour, and affects one creature within 30'. A curse makes the target "
                                 "unable to access its LUC pool; a blessing grants it a bonus 3d6 to its LUC pool for "
                                 "the hour."},
                        {'Name': 'Divine touch',
                         'Desc': "(requires Portfolio) The potency of your touch increases. If you chose the secret "
                                 "of good, your touch can now heal 2d6 HEALTH. A creature can only be affected once "
                                 "by your healing touch per day. Alternatively, if you chose the secret of evil, "
                                 "your touch now also pushes your target one stage along the Nausea status track."},
                        {'Name': 'Portfolio',
                         'Desc': "Choose either the Good or the Evil virtue, plus one Elemental or Creature secret. "
                                 "If you choose the secret of good, your touch can heal 1d6 HEALTH as a single action "
                                 "(although any given creature can only benefit from this once per day). If you "
                                 "choose the secret of evil, it inflicts 1d6 evil damage beyond your natural damage. "
                                 "You may never learn the opposite Virtue secret to the one you chose."},
                        {'Name': 'Sense virtue',
                         'Desc': "(requires Portfolio) You are able to sense the presence of (but not the location "
                                 "of) any beings or objects within 60' with a Virtue opposite to that of the secret "
                                 "you chose."}])

career_old_diabolist = Career(
    name='Diabolist',
    career_time='1d6',
    career_time_unit='years',
    prereq='religion, secret of evil',
    willpower=1, charisma=1, luck=1, magic=1,
    available_skills=['[magical]', 'religion', 'alchemy', 'concentration', '[social]', 'linguistics', 'knives', 'law'],
    desc="A diabolist consorts with the infernal, and dabbles in the darkest and most dangerous of magical arts – he "
         "deals with demons and devils, risking his very soul in the process. A diabolist needs a strong will, "
         "for devils and demons know the powers of temptation, deceit, and the lure of pure evil. A diabolist knows "
         "how to summon infernal creatures and bind them to his will.",
    available_exploits=[{'Name': 'Blood magic',
                         'Desc': "(requires Faustian Pact) You are now able to cast spells for fewer MP by spilling "
                                 "your own blood. As an action, you may do either 1d6 or 2d6 damage to yourself; the "
                                 "MP cost of the next spell cast within one minute is reduced by the number of d6s "
                                 "damage you cause."},
                        {'Name': 'Demonic traits',
                         'Desc': "(requires Faustian Pact) You begin to take on the appearance of the infernal. You "
                                 "may take this exploit up to six times. Each time you take it, roll 1d6 to determine "
                                 "the trait you gain; if a trait is duplicated, roll again. 1. Horns. +1d6 Magic "
                                 "Points 2. Red eyes. Darkvision 60' 3. Claws. +1d6 to unarmed damage 4. Red skin. "
                                 "SOAK 5 (fire) 5. Hooves. +1 SPEED 6. Tail. +1 AGILITY"},
                        {'Name': 'Faustian pact',
                         'Desc': "Your Faustian pact begins; but power comes at a price. You gain 2d6 additional "
                                 "Magic Points. Whenever you cast a spell, you take damage equal to the number of MP "
                                 "placed in that spell. However, you know that true power comes later to those who "
                                 "are patient."},
                        {'Name': 'Infernal mysteries',
                         'Desc': "You learn the basics of diabolism. You gain the summoning, abjuration, and hexing "
                                 "skills at 1 rank (1d6) if you do not already have them, and learn the secret of "
                                 "demons."},
                        {'Name': 'Imp',
                         'Desc': "You gain an imp familiar which will do your bidding. It will undertake dangerous "
                                 "tasks, but to persuade it to do something suicidal (or near-so) requires a "
                                 "Difficult [16] CHA check; if you fail, your imp betrays you."}])

career_old_druid = Career(
    name='Druid',
    career_time='1d6',
    career_time_unit='years',
    prereq='nature',
    intuition=1, willpower=1, endurance=1, magic=1,
    available_skills=['[outdoor]', 'nature', 'healing', 'staves', '[crafting]', 'herbalism', '[magical]'],
    desc="Guardians of nature, druids are attuned with the natural forces of the world. Plants and animals are their "
         "allies, and druids frequently live in the wild, deep within forests. A druid typically wields a staff or "
         "sickle.",
    available_exploits=[{'Name': 'Animal affinity',
                         'Desc': "(requires Speak With Animals) With a successful CHA vs. MENTAL DEFENSE check, "
                                 "you can shift an animal one stage along the Charm status track for one hour."},
                        {'Name': 'Animal companion',
                         'Desc': "You gain an animal companion in the form of a wolf. This companion will accompany "
                                 "and defend you. If your companion dies, you attract a new companion in one month. "
                                 "However, if you abuse your companion (for example by sending it ahead to set off "
                                 "traps), it will leave you and you will never be able to replace the companion. The "
                                 "companion is bright for its species, but has no special intelligence or abilities. "
                                 "You may take this exploit multiple times, gaining an extra animal companion each "
                                 "time."},
                        {'Name': 'Ageless',
                         'Desc': "(requires Poison Immunity) You no longer age and become effectively immortal, "
                                 "saving accidental death."},
                        {'Name': 'Beast form',
                         'Desc': "You may transform into a small or medium-sized animal (and back again) once per day "
                                 "for up to one hour. You cannot speak in this form, and retain your own mental "
                                 "attributes, but otherwise use the animal's statistics."},
                        {'Name': 'Companion link',
                         'Desc': "(requires Animal Companion) You gain a telepathic link with your animal companion "
                                 "with a range of 1 mile; this enables you to send it instructions and to see through "
                                 "its eyes."},
                        {'Name': 'Elemental druid',
                         'Desc': "You gain any two of the secrets of air, earth, fire, and water."},
                        {'Name': 'Greater beast form',
                         'Desc': "(requires Beast form) You may now change into a large or tiny animal."},
                        {'Name': '''Nature's passage''',
                         'Desc': "You can move through woodland areas and thick undergrowth without any speed "
                                 "reduction, and leave no tracks or traces of your passing unless you choose to do "
                                 "so."},
                        {'Name': 'Nature priest', 'Desc': "You gain the secret of beasts and the secret of plants."},
                        {'Name': 'Poison immunity', 'Desc': "You become immune to all poisons and poison damage."},
                        {'Name': 'Speak with animals',
                         'Desc': "You may freely speak with animals, although they do not gain special intelligence "
                                 "or knowledge."}])

career_old_firemage = Career(
    name='Firemage',
    career_time='1d6',
    career_time_unit='years',
    prereq='secret of fire.',
    magic=1, agility=1, charisma=1, logic=1,
    available_skills=['[magical]', '[lore]', '[crafting]', 'bluffing', 'perception', 'reactions', 'knives'],
    desc="Firemages are fascinated by fire. They love the way it flickers and dances; they excel at creating flames, "
         "throwing fire, and delight in creating and controlling infernos and conflagrations. Firemages can sometimes "
         "be identified by a slight sent of sulfur.",
    available_exploits=[{'Name': 'Fiery affinity.',
                         'Desc': "Your focus on fire grants you +1d6 to any attribute which interacts with fire or "
                                 "heat."},
                        {'Name': 'Firebolt',
                         'Desc': "(requires Flaming Touch) You can throw a bolt of fire as a single ranged attack ("
                                 "using your MAG attribute) which has a range increment of 30' and does 2d6 fire "
                                 "damage."},
                        {'Name': 'Firebolt, greater',
                         'Desc': "(requires Firebolt) Your Firebolt's damage increases to 3d6 fire."},
                        {'Name': 'Fire immunity',
                         'Desc': "(requires Fire Resistance) You become completely immune to fire or heat damage. "
                                 "Your vulnerability to cold, however, increases to 2d6."},
                        {'Name': 'Fire resistance',
                         'Desc': "You permanently gain SOAK 5 (fire). However, you also suffer Vulnerability (1d6) to"
                                 " cold."},
                        {'Name': 'Firesculptor',
                         'Desc': "You can 'sculpt' fire easily; any non-magical flame within 30' can be shaped or "
                                 "enlarged as a single action and a mere effort of will as long as it remains within "
                                 "30' (things outside can catch fire as normal, but you have no control over them)."},
                        {'Name': 'Flaming aura',
                         'Desc': "(requires Flaming Touch) You gain an aura (based on your size as normal) of flame "
                                 "and heat, although you may suppress it easily. Creatures entering or starting a "
                                 "turn in this aura take 2d6 fire damage."},
                        {'Name': 'Flaming touch',
                         'Desc': "Your touch becomes hot enough to injure others, causing an additional 1d6 of heat "
                                 "damage beyond your natural damage."},
                        {'Name': 'Sticky fire',
                         'Desc': "Every time you damage a foe with fire, they are pushed one stage down the fire "
                                 "status track."}])

career_old_gladiator = Career(
    name='Gladiator',
    career_time='1d6',
    career_time_unit='years',
    prereq='none',
    agility=1, endurance=1, reputation=1, charisma=1,
    available_skills=['[combat]', 'reactions', 'storytelling', 'intimidation', 'dancing', 'acrobatics'],
    desc="You fought in an arena for money and fame with a flashy combat style and a few dirty tricks.",
    available_exploits=[{'Name': '''Gladiator's skills''',
                         'Desc': "You gain two of the following universal exploits: Disarm, Trip, Achilles Heel, "
                                 "Blinding Attack, Crippling Strike, Quickstand, Taunt. You may repeat this exploit "
                                 "to gain two more from the list."},
                        {'Name': 'Showman',
                         'Desc': "You can make a CHA vs. MENTAL DEFENSE attack in combat against a single target "
                                 "within 30' as a standard action to put on an intimidating and flashy display of "
                                 "prowess. If successful, the target is moved one stage down the Fear status track."},
                        {'Name': 'Exhibitionist',
                         'Desc': "Onlookers give you strength. If there are 6 or more non-participating people "
                                 "watching you fight, you replenish your LUCK pool by 1 die every time you defeat an "
                                 "opponent."},
                        {'Name': '''Crowd's worship''',
                         'Desc': "(requires Exhibitionist) You feed off the admiration of a crowd to the extent that "
                                 "if there are 6 or more non-participating people watching you fight, every time you "
                                 "defeat a foe, you gain 2d6 HEALTH as you bask in glory."},
                        {'Name': '''Gladiator's cut''',
                         'Desc': "Your successful strikes move your target one stage along the Bleeding status track."},
                        {'Name': 'Unusual weapon',
                         'Desc': "Choose one of the following weapons: trident, net, spear. Weapons of that type "
                                 "count as one quality level higher when you use them."},
                        {'Name': '''Signature move''',
                         'Desc': "(requires Gladiator's Skills) Choose one exploit that you have learned from the "
                                 "Gladiator's Skills list. This becomes your signature move. You gain a permanent "
                                 "+1d6 when using that move."},
                        {'Name': 'Fake wounds',
                         'Desc': "Once per day, you may use your expertise in faking injuries to turn an actual blow "
                                 "into a pretend one. Your opponent, and all onlookers, will believe you have "
                                 "suffered the damage inflicted by the attack, but in fact it causes no damage at "
                                 "all."},
                        {'Name': 'Surprise recovery',
                         'Desc': "(requires Fake Wounds) After using your Fake Wounds ability, you may make a single "
                                 "free melee attack at any point up until you make an actual regular melee attack. "
                                 "The free attack must be your first melee attack since using the Fake Wounds "
                                 "ability."}])

career_old_herbalist = Career(
    name='Herbalist',
    career_time='1d6',
    career_time_unit='years',
    prereq='INT 4+',
    logic=1, intuition=1, willpower=1, luck=1,
    available_skills=['cooking', 'brewing', 'herbalism', 'nature', 'perception', 'gardening', 'healing', 'survival'],
    desc="An herbalist knows how to gather, store, prepare, and administer herbs and herbal concoctions which have a "
         "wide variety of effects. An expert herbalist can, merely from gathering resources found in nature, "
         "create ointments and mixtures which protect, heal, or ward. For each herbal mixture, you should roll and "
         "note down an Herbal Science result. This describes the nature of the mixture, whether it is soup of the "
         "spirit-wood weed, or incense from the blue-vine nut.",
    available_exploits=[{'Name': 'Healing herbs',
                         'Desc': "As long as you have your herbalism kit on you, you can heal an ally by 1d6 of "
                                 "HEALTH as a single action. No creature can benefit from this healing more than once "
                                 "per day."},
                        {'Name': 'Alleviate condition',
                         'Desc': "You can automatically devise an herbal concoction to remove any condition instantly "
                                 "(stunned, blinded, and so on) by mixing the herbs you have on you and adding "
                                 "additional components from your surroundings as long as you have your herbalism kit "
                                 "on you. This takes two actions (a full turn) and reduces any status track by one "
                                 "stage automatically."},
                        {'Name': 'Herbal ward',
                         'Desc': "You can create a herbal abjuration effect (equal to a 0 MP spell) at-will. It takes "
                                 "you one minute to prepare the herbs, and they remain usable for five minutes. "
                                 "Choose one creature type; any time a creature of that type attempts to come within "
                                 "10' of you (or the recipient of your herbs), it is subject to a LOG vs. MENTAL "
                                 "DEFENSE attack. On a success, it may not come any closer for five minutes, "
                                 "at which point it may try again. The duration of the effect is 30 minutes."},
                        {'Name': 'Stimulant',
                         'Desc': "You can create a herbal mixture which increases the die pool of one attribute by "
                                 "1d6 for five minutes. You must choose the attribute when you select this exploit; "
                                 "you may select it multiple times and choose a different attribute each time. It "
                                 "takes one minute to create the mixture."},
                        {'Name': 'Depressant',
                         'Desc': "You can create a herbal mixture which decreases the die pool of one attribute by "
                                 "1d6 for five minutes. You must choose the attribute when you select this exploit; "
                                 "you may select it multiple times and choose a different attribute each time. It "
                                 "takes one minute to create the mixture."}])

career_old_inquisitor = Career(
    name='Inquisitor',
    career_time='1d6',
    career_time_unit='years',
    prereq='law, divination',
    endurance=1, intuition=1, willpower=1, magic=1,
    available_skills=['religion', 'law', 'interrogation', 'intimidation', 'tracking', 'divination', 'compulsion',
                      'abjuration', 'knives'],
    desc="Inquisitors are magical bodyguards and interrogators skilled in uncovering plots and opposing enemy magic. "
         "Inquisitorial magic is subtle in its effects, with few sensory cues, but very distinctive with regard to "
         "its caster. Inquisitors learn to use their force of will to intimidate foes, and so they typically growl "
         "their spells loudly and gesture clearly at their spell’s targets. They use few directly offensive spells, "
         "though many can create flaming barriers for defense or to trap foes. Inquisitors are easily recognized for "
         "their masks, which they claim protect their souls from enemy magic. Most Inquisitor masks are wood or stone "
         "carved in the shape of bearskulls, and many Inquisitors favor bearskin cloaks. They seldom arm themselves "
         "with more than a claw-shaped dagger. Inquisitors learn their spells from copies of old spellbooks, "
         "scribed by the founders of the Inquisitorial order centuries ago. These spellbooks are written in a "
         "civilized form of Orcish, and are closely protected by the order that owns them. Experienced Inquisitors "
         "also usually study the magic of other groups to be better able to counterspell it.",
    available_exploits=[{'Name': 'Dispel magic',
                         'Desc': "(requires Sense Magic) You are able to dispel magic within 30' as a single action "
                                 "by making a MAG vs. MAG check against the effect you are trying to dispel."},
                        {'Name': '''Inquisitor's mask''',
                         'Desc': "You can protect yourself from spells by hiding your soul behind a special mask. You "
                                 "create the mask yourself. While you wear that mask you gain a +4 MENTAL DEFENSE "
                                 "bonus. Also divination spells that directly target you take a -1d6 die "
                                 "penalty.&nbsp; You must make the mask yourself, and it must be specifically "
                                 "designed to protect your soul. You can take this exploit a second time to create a "
                                 "Greater Inquisitor's Mask, which gives you +6 MENTAL DEFENSE and inflicts a -2d6 "
                                 "penalty to divination spells targeting you."},
                        {'Name': '''Inquisitor's sight''',
                         'Desc': "You gain the secret of humanoids, and gain one rank in the compulsion, divination, "
                                 "and abjuration skills."},
                        {'Name': 'Magic resistance',
                         'Desc': "You gain SOAK 5 (magic). This applies to any damage caused directly by magic; it "
                                 "does not apply to indirect damage."},
                        {'Name': 'Sense magic', 'Desc': "You are able to sniff out magic within 60'."}])

career_old_knight = Career(
    name='Knight',
    career_time='1d6',
    career_time_unit='years',
    prereq='heraldry',
    strength=1, charisma=1, luck=1, reputation=1,
    available_skills=['lances', 'swords', 'heraldry', 'animal handling', 'riding', 'bravery', 'leadership', 'tactics',
                      'carousing', 'law'],
    desc="You became a knight – a mounted warrior proficient in lance, shield, and sword.",
    available_exploits=[{'Name': 'Bonded mount',
                         'Desc': "You gain a loyal warhorse. The warhorse is bonded to you, and gains +2 SPEED while "
                                 "you are riding it. If the warhorse dies, you can replace it after a week of "
                                 "mourning."},
                        {'Name': 'Jouster',
                         'Desc': "You can charge an enemy from horseback using your lance. This attack gains +2d6 to "
                                 "both attack and damage, and requires you to move on horseback at least 20' in a "
                                 "straight line."},
                        {'Name': 'Jumper',
                         'Desc': "Your horse's free JUMP distance increases by 5' horizontally, and 5' vertically."},
                        {'Name': 'Honorable',
                         'Desc': "Your courage and honor are such that you automatically succeed in attempts to shake "
                                 "off Fear status track effects."},
                        {'Name': 'Squire',
                         'Desc': "(requires Bonded Mount) You gain a free squire. You must protect your squire; in "
                                 "exchange, one weapon or one suit of armor you possess increases by one quality "
                                 "level (to a maximum of artisan). If your squire dies, he is replaced in one month."}])

career_old_loremaster = Career(
    name='Loremaster',
    career_time='1d6',
    career_time_unit='years',
    prereq='INT 4+',
    logic=2, willpower=1, magic=1,
    available_skills=['[artistic]', '[lore]', '[gaming]', '[magical]'],
    desc="A loremaster is a scholar and academic expert; years spent in libraries studying ancient texts makes "
         "loremasters amongst the most knowledgeable in the world. Loremasters even pick up some minor magical spells "
         "which help them in their studies.",
    available_exploits=[{'Name': 'Secrets', 'Desc': "You learn four secrets."},
                        {'Name': 'Experienced',
                         'Desc': "Your knowledge and expertise borders on the prophetic. Your entire party gains a "
                                 "+1d6 INITIATIVE bonus if they are within 30 feet of you when they make their check."},
                        {'Name': 'Identify',
                         'Desc': "You can automatically identify a magical item, its name, and its properties."},
                        {'Name': 'Language lore',
                         'Desc': "You gain the scholastic ability to speak or read any unknown language with a "
                                 "Difficult [16] INT check."},
                        {'Name': 'Language mastery',
                         'Desc': "(requires Language Lore) You can now speak or read any unknown language "
                                 "automatically."},
                        {'Name': 'Anatomist',
                         'Desc': "You automatically know the resistances and vulnerabilities of any creature you "
                                 "encounter."},
                        {'Name': 'Wise counsel',
                         'Desc': "You can spend two actions to offer advice and counsel, giving one ally within 30' a "
                                 "+2d6 bonus to a single attribute check. Any given target can only benefit from this "
                                 "once per day."},
                        {'Name': 'Ritual',
                         'Desc': "You can cast a specific spell of 3 MP or less as a ritual; this takes one minute "
                                 "per MP, but costs no MP. Devise one spell and note it down. You may take this "
                                 "exploit more than once, creating a new ritual each time."},
                        {'Name': 'Greater ritual',
                         'Desc': "(requires Ritual) You can now cast spells of up to 5 MP or less as a ritual."}])

career_old_mage = Career(
    name='Mage',
    career_time='1d6',
    career_time_unit='years',
    prereq='one [magical] skill',
    magic=1, logic=1, willpower=1, reputation=1,
    available_skills=['[magical]', '[lore]', '[academic]', 'staves', 'prestidigitation'],
    desc="You are practiced in the arcane arts, able to wield spells with ease. A mage is a trained magic-user – "
         "sometimes known as a wizard, or sorcerer. Able to cast a variety of spells, and well-versed in a range of "
         "lore, the mage is a generalist.",
    available_exploits=[{'Name': 'Broad knowledge base',
                         'Desc': "(requires Arcane Knowledge Base) Choose two more [magical] skills and two elemental "
                                 "or creature secrets. You gain these two skills at 1 rank (1d6). This does not "
                                 "increase the rank of an existing skill."},
                        {'Name': 'Arcane knowledge base',
                         'Desc': "Choose four [magical] skills and one element secret. You gain these four skills at "
                                 "1 rank (1d6). This does not increase the rank of an existing skill."},
                        {'Name': 'Arcane secret',
                         'Desc': "You have learned or discovered an arcane secret - either an element, creature type, "
                                 "or virtue. You can take this exploit multiple times, learning a new secret each "
                                 "time, but you may know no more secrets than your LOG attribute."},
                        {'Name': 'Attuned',
                         'Desc': "You are able to detect magic easily. You do not need to make any kind of attribute "
                                 "check to detect magic within 30', and are aware of its existence automatically."},
                        {'Name': 'Familiar',
                         'Desc': "You gain a familiar, which is a tiny-sized creature (cat, bat, owl, mouse, rat, "
                                 "etc.) You can speak to your familiar, which is able to report back things it has "
                                 "seen or heard."},
                        {'Name': 'Learned',
                         'Desc': "When using any [lore] skill as part of a dice pool, you may reroll any 1s."},
                        {'Name': 'Specialization',
                         'Desc': "(requires Arcane Knowledge Base) Choose one secret that you already know. You are "
                                 "specialized in that secret. You may exceed your MAG attribute by 2 points when "
                                 "using that secret. You may only ever specialize in one secret."}])

career_old_man_at_arms = Career(
    name='Man-at-Arms',
    career_time='1d6',
    career_time_unit='years',
    prereq='none',
    strength=1, endurance=1, willpower=1, luck=1,
    available_skills=['spears', 'swords', '[unarmed fighting]', 'carrying', 'running', 'leadership', 'tactics',
                      'carousing', 'survival', 'healing'],
    desc="An infantryman, you fought in battle on the front lines.",
    available_exploits=[
        {'Name': 'Equipped', 'Desc': "You start play with a high quality sword, spear, or suit of chainmail."},
        {'Name': 'Hold the line', 'Desc': "When standing adjacent to an ally, you both gain a 1d6 cover bonus."},
        {'Name': 'Advance!',
         'Desc': "Proficient at charging across poor terrain or mud, you ignore terrain when charging."},
        {'Name': 'Shield-bearer', 'Desc': "Any shield you wear increases its DEFENSE bonus by +4."},
        {'Name': 'Shield wall',
         'Desc': "When standing between two allies, all three gain a +2d6 cover bonus. This does not stack with "
                 "itself or with Hold the Line."}])

career_old_minstrel = Career(
    name='Minstrel',
    career_time='1d6',
    career_time_unit='years',
    prereq='CHA 4+',
    intuition=1, willpower=1, charisma=1, reputation=1,
    available_skills=['carousing', '[performance skills]', '[lore]', '[social]'],
    desc="You used the power of your music to earn a living.",
    available_exploits=[{'Name': 'Instrument',
                         'Desc': "You start play with a high quality musical instrument. You can make money by "
                                 "playing at taverns and doing local performances. You can automatically make 1d6 x "
                                 "10 gc per day by doing this. This ability cannot be used during downtime."},
                        {'Name': 'Song',
                         'Desc': "(requires Instrument) You can take this exploit multiple times, learning a new song "
                                 "each time. Your songs affect sentient beings who can hear and understand them. Each "
                                 "time you learn a song, choose one Status track (e.g. Song of Cheer, "
                                 "Song of Courage, or Song of Tiredness); that song allows you to move those within "
                                 "30' who can hear you one stage up or down that status track. Unwilling targets "
                                 "require a CHA vs. MENTAL DEFENSE attack."},
                        {'Name': 'Beastsong',
                         'Desc': "(requires Song) Select a song that you know. That song will now affect beasts."},
                        {'Name': 'Projection',
                         'Desc': "(requires Song) You use the power of your voice to increase the radius of your "
                                 "songs to 60'."}])

career_old_musketeer = Career(
    name='Musketeer',
    career_time='1d6',
    career_time_unit='years',
    prereq='AGI or INT 5+',
    agility=1, intuition=1, charisma=1, luck=1,
    available_skills=['swords', 'muskets', 'heraldry', 'perception', 'intimidate', 'carousing'],
    desc="Wielding musket and sword, you became a swashbuckling musketeer.",
    available_exploits=[{'Name': 'Cloak flourish',
                         'Desc': "You can use a cape or cloak with a flourish to distract your foes; the garment "
                                 "counts as a small shield, but does not require a free hand to use it."},
                        {'Name': 'Musket charge',
                         'Desc': "When charging with a melee weapon, you may begin your charge with a single musket "
                                 "shot, switch weapons, charge, and end it with a single melee strike."},
                        {'Name': 'Pistol-whip',
                         'Desc': "You can use a firearm as a club by striking with the butt once per turn as a free "
                                 "action as long as you are currently wielding only that weapon."},
                        {'Name': 'Swashbuckler',
                         'Desc': "Your swashbuckling swordplay gives you any two of the following universal exploits: "
                                 "Disarm, Sidestep, Taunt."},
                        {'Name': 'Whites of their eyes',
                         'Desc': "You are accustomed to standing your ground as oncoming hordes charge, firing only "
                                 "when you see the whites of their eyes. When charged by an opponent, you may fire a "
                                 "free musket or pistol shot when they come within 10' of you."},
                        {'Name': 'Quick reload',
                         'Desc': "You can fire your musket every action, rather than just once per turn."}])

career_old_necromancer = Career(
    name='Necromancer',
    career_time='1d6',
    career_time_unit='years',
    prereq='secret of undead.',
    logic=1, willpower=1, charisma=1, magic=1,
    available_skills=['[magical]', 'religion', 'alchemy', 'healing', '[social]', 'knives'],
    desc="A master of the dark arts, a necromancer is able to summon, bind, and control the undead. Eventually, "
         "a necromancer turns into a terrifying lich, the most powerful of undead. A necromancer knows the ways of "
         "disease, poison, and the power of fear.",
    available_exploits=[{'Name': 'Corpse visage',
                         'Desc': "(requires Eyes of the Dead) Your skin and visage alter slightly, becoming more like "
                                 "the undead you surround yourself with. You gain 5 natural SOAK, but become "
                                 "Vulnerable 1d6 (Light) and your CHA attribute is reduced by 2 points (to a minimum "
                                 "of 2)."},
                        {'Name': 'Eyes of the dead',
                         'Desc': "You share the senses of the undead, gaining darksight 60'."},
                        {'Name': 'Necromantic Lore',
                         'Desc': "You gain the skills of summoning, affliction, and creation at a rank of 1 (1d6) if "
                                 "you do not already have them. You also gain the secrets of death and shadow."},
                        {'Name': 'One of us',
                         'Desc': "(requires Corpse Visage) Undead of a lower grade than yourself are unable to attack "
                                 "or harm you in any way."},
                        {'Name': 'Touch of the grave',
                         'Desc': "Your touch gains the foulness of death, doing an additional 1d6 death damage. You "
                                 "also kill any small (non creature) plants you come into contact with."},
                        {'Name': 'Undead servant',
                         'Desc': "You gain an undead slave – a skeleton or zombie – which obeys your every command "
                                 "until destroyed. If destroyed, you may summon a new one with a 24 hour ceremony and "
                                 "access to an appropriate corpse. You may take this exploit multiple times, "
                                 "gaining a new servant each time."},
                        {'Name': 'Undeath',
                         'Desc': "(requires One of Us) You perform a grotesque and elaborate ceremony and become "
                                 "undead yourself. You are now effectively immortal, and will never die of old age, "
                                 "although you will still visibly age forever unless you disguise yourself with "
                                 "illusions. You no longer need to breathe, eat, or sleep, and you are immune to "
                                 "poisons."},
                        {'Name': 'Vampiric touch',
                         'Desc': "(requires Touch of the Grave) You are able to steal the life essence of a victim "
                                 "for yourself. When you use your Touch of the Grave to do damage to another "
                                 "creature, you gain that amount of HEALTH."}])

career_old_pirate = Career(
    name='Pirate',
    career_time='1d6',
    career_time_unit='years',
    prereq='sailing',
    agility=1, intuition=1, luck=1, reputation=1,
    available_skills=['sailing', 'navigation', 'climbing', 'swimming', 'carousing', 'swords', 'knives', 'crossbows',
                      'leadership', 'appraisal', 'thievery', 'law'],
    desc="A scourge of the high seas, you plunder for loot and fame.",
    available_exploits=[{'Name': 'Crows nest',
                         'Desc': "You have spent many hours on the lookout. You can always access the ambush turn."},
                        {'Name': 'Hook',
                         'Desc': "One of your hands is now a hook. You are always considered to be carrying a knife. "
                                 "You also gain a bonus +1 REP."},
                        {'Name': 'Keelhauled',
                         'Desc': "You've been keelhauled or felt the lash of the cat at least once. You gain SOAK 2."},
                        {'Name': 'Rigging', 'Desc': "You do not suffer penalties for fighting while climbing."},
                        {'Name': 'Fearsome reputation',
                         'Desc': "Your reputation precedes you. With a REP vs. MENTAL DEFENSE attack you can "
                                 "intimidate a single target within 30'. If successful, the target moves one stage "
                                 "down the Feat status track."},
                        {'Name': 'Polly',
                         'Desc': "You gain a small bird (crow, parrot, owl, etc.) as an animal companion. See the "
                                 "druid career for information on animal companions."},
                        {'Name': 'Fierce reputation',
                         'Desc': "(requires Fearsome Reputation) Your reputation is now so fierce that you can either "
                                 "push one target two stages down the Fear status track, or all targets within 30' "
                                 "one stage down the track with a REP vs. MENTAL DEFENSE attack."}])

career_old_prisoner = Career(
    name='Prisoner',
    career_time='2d6',
    career_time_unit='years',
    prereq='none',
    strength=1, endurance=1, intuition=1, reputation=1,
    available_skills=['intimidation', 'survival', '[subterfuge]', '[unarmed fighting]', 'knives'],
    desc="Your life of crime ended you up in prison where you served time; or perhaps you were a political prisoner "
         "or a prisoner-of-war. It was a tough environment and you spent most of your time just trying to survive, "
         "although you did make one or two lifelong contacts.",
    available_exploits=[{'Name': 'Prison tough',
                         'Desc': "You are mentally and physically toughened. Each time you take this exploit you gain "
                                 "a permanent +1 bonus to your DEFENSE and MENTAL DEFENSE. You may repeat this "
                                 "exploit."},
                        {'Name': 'Shiv',
                         'Desc': "You are easily able to improvise weapons using your surroundings – glasses, rocks, "
                                 "and so on. You always count as carrying a knife or club."}])

career_old_ranger = Career(
    name='Ranger',
    career_time='1d6',
    career_time_unit='years',
    prereq='WIL 3+',
    agility=1, intuition=1, endurance=1, willpower=1,
    available_skills=['[outdoor]', 'herbalism', 'local knowledge', 'swords', 'bows', 'climbing', 'swimming', 'running',
                      'stealth', 'navigation', 'tracking'],
    desc="Woodsman and hunter, you are a master of the outdoors. The ranger is the quintessential outdoorsman.",
    available_exploits=[{'Name': 'Companion',
                         'Desc': "You gain an animal companion, much like the druid's. This companion will accompany "
                                 "and defend you. If your companion dies, you attract a new companion in one month. "
                                 "However, if you abuse your companion (for example by sending it ahead to set off "
                                 "traps), it will leave you and you will never be able to replace the companion."},
                        {'Name': 'Beastmaster',
                         'Desc': "(requires Companion) You gain a second animal companion. You can repeat this "
                                 "exploit, gaining a new companion each time you take it."},
                        {'Name': '''Nature's secrets''',
                         'Desc': "You learn the secret of plants and the secret of beasts."},
                        {'Name': 'Traveller',
                         'Desc': "You are skilled at wilderness travel, at home under the open sky. You increase the "
                                 "travel increment of a group you lead by one day. You may take this exploit multiple "
                                 "times, increasing the travel increment by one day each time."},
                        {'Name': 'Wilderness stride',
                         'Desc': "You are not affected by difficult terrain caused by plants or undergrowth."},
                        {'Name': '''Nature's camouflage''',
                         'Desc': "You can camouflage yourself to become effectively invisible at a distance of 30' or "
                                 "greater. You may only move at half SPEED while camouflaged, and any attack ends the "
                                 "effect for anybody within sight."},
                        {'Name': 'Beast whisperer',
                         'Desc': "You can speak to animals. This does not grant them special knowledge or "
                                 "intelligence, so the information you can gain is limited by their own capabilities. "
                                 "Neither does it guarantee friendship or cooperation."}])

career_old_ruffian = Career(
    name='Ruffian',
    career_time='1d6',
    career_time_unit='years',
    prereq='none',
    strength=1, endurance=1, charisma=1, luck=1,
    available_skills=['intimidation', 'running', 'brawling', 'clubs', 'knives'],
    desc="You fell into the fringes of society and ended up as a thug on the street, committing petty crimes for "
         "small amounts of money.",
    available_exploits=[{'Name': 'The filth!',
                         'Desc': "You have developed an uncanny ability to detect the Watch. When attempting to sniff "
                                 "out a watchman or similar authority figure, you gain a +1d6 bonus."},
                        {'Name': 'Street tough', 'Desc': "Life on the streets is tough. You gain a natural +2 SOAK."}])

career_old_sailor = Career(
    name='Sailor',
    career_time='1d6',
    career_time_unit='years',
    prereq='none',
    agility=1, intuition=1, luck=1, endurance=1,
    available_skills=['sailing', 'navigation', 'fishing', 'climbing', 'swimming', 'carousing', 'clubs', 'knives',
                      'crossbows', 'leadership'],
    desc="At home on the sea, you spent time aboard a ship mastering the art of sailing.",
    available_exploits=[{'Name': 'Climb the rigging', 'Desc': "You can climb your SPEED instead of half your SPEED."},
                        {'Name': 'Sea legs',
                         'Desc': "You adapt to the motion of a ship; this makes you very hard to knock down. When you "
                                 "are knocked prone, you may make a Challenging [13] AGI check; if you succeed, "
                                 "you remain standing."},
                        {'Name': 'Grog',
                         'Desc': "While you may well enjoy a drink, you never suffer any penalties from intoxication "
                                 "via alcohol."},
                        {'Name': 'Swimmer', 'Desc': "You gain a SWIM speed equal to your regular SPEED."},
                        {'Name': 'Hold breath',
                         'Desc': "(requires Swimmer) You gain two additional countdown dice when holding your breath."},
                        {'Name': 'Sea weather',
                         'Desc': "You are able to ignore the effects of rain, wind, mist, and fog."},
                        {'Name': 'Sea shanty',
                         'Desc': "By singing a sea shanty, a sailor can combat sickness and tiredness. Anyone who "
                                 "hears the shanty is reduced by one stage in the Nausea or Tiredness status tracks ("
                                 "the sailor must choose which of the two songs he is singing)."},
                        {'Name': 'Any port',
                         'Desc': "You may take this exploit multiple times. Each time you take it, you may designate "
                                 "an additional port town. At that location, you will have one contact upon whom you "
                                 "can (generally) rely, and one tavern at which you can drink for free."},
                        {'Name': 'Lookout',
                         'Desc': "Crow's nest duty is a mandatory part of a sailor's life. You gain +1d6 to "
                                 "perception checks."},
                        {'Name': 'Peg leg',
                         'Desc': "One of your legs is a wooden peg. You are used to it, so it does not negatively "
                                 "affect you; you gain a kick attack which increases your unarmed damage by 1d6."}])

career_old_smith = Career(
    name='Smith',
    career_time='1d6',
    career_time_unit='years',
    prereq='STR 4+',
    strength=1, endurance=1, logic=1, reputation=1,
    available_skills=['[crafting]', '[artistic]', 'appraise'],
    desc="A smith is a master metalwork. Blacksmith, weaponsmith, armorer, a smith is able to create, maintain, "
         "and even enchant a warrior's tools. Many smiths combine traditions of smithing and alchemy to learn how to "
         "make magical weapons and armor.",
    available_exploits=[{'Name': 'Maintenance',
                         'Desc': "You know how to maintain equipment. Designate one standard quality suit of armor or "
                                 "a weapon; this item becomes high quality, as long as you spend an hour maintaining "
                                 "it every day."},
                        {'Name': 'Lore of the Masters',
                         'Desc': "You are able to identify rare or magical weapons and armor without making an "
                                 "attribute check."},
                        {'Name': 'Chink in the armor',
                         'Desc': "You know armor, and its styles well, including the weaknesses of each type. Once "
                                 "per suit of armor, you may ignore its SOAK value when attacking."},
                        {'Name': 'Forge',
                         'Desc': "(requires weaponsmithing or armorer) You forge yourself a single standard quality "
                                 "weapon (weaponsmithing) or suit of armor (blackmithing), which you gain for free."},
                        {'Name': 'Quality forge',
                         'Desc': "(requires Forge; weaponsmithing 4 or armorer 4) You forge yourself a single high "
                                 "quality weapon (weaponsmithing) or suit of armor (blackmithing); you must pay for "
                                 "the standard quality version, but it becomes high quality automatically."},
                        {'Name': 'Exceptional forge',
                         'Desc': "(requires Quality Forge; weaponsmithing 7 or armorer 7) You forge yourself a single "
                                 "exceptional quality weapon (weaponsmithing) or suit of armor (blackmithing); you "
                                 "must pay for the standard quality version, but it becomes exceptional quality "
                                 "automatically. You may repeat this exploit."},
                        {'Name': 'Master forge',
                         'Desc': "(requires Exceptional Forge; weaponsmithing 10 or armorer 10) You forge yourself a "
                                 "single mastercraft quality weapon (weaponsmithing) or suit of armor (blackmithing); "
                                 "you must pay for the standard quality version, but it becomes mastercraft quality "
                                 "automatically. You may repeat this exploit."},
                        {'Name': 'Artisanal forge',
                         'Desc': "(requires Master Forge; weaponsmithing 12 or armorer 12) You forge yourself a "
                                 "single artisanal quality weapon (weaponsmithing) or suit of armor (blackmithing); "
                                 "you must pay for the standard quality version, but it becomes artisanal quality "
                                 "automatically. You may repeat this exploit."},
                        {'Name': 'Legendary forge',
                         'Desc': "(requires Artisinal Forge; MAG 3+;; weaponsmithing 15 or armorer 15) You forge "
                                 "yourself a single legendary quality weapon (weaponsmithing) or suit of armor ("
                                 "blackmithing); you must pay for the standard quality version, but it becomes "
                                 "legendary quality automatically. You may repeat this exploit."},
                        {'Name': 'Alchemical weapon',
                         'Desc': "(requires Master Forge, Sticky Concoction, MAG 4+) You combine the Sticky "
                                 "Concoction ability from the Alchemist career and Master Forge or greater from the "
                                 "Smith career, the weapon you created permanently gains the effect granted by the "
                                 "Sticky Concoction. You may repeat this exploit."},
                        {'Name': 'Alchemical armor',
                         'Desc': "(requires Exceptional Forge, Protective Oil, MAG 2+) You combine the Protective Oil "
                                 "ability from the Alchemist career and Exceptional Forge or greater from the Smith "
                                 "career, the armor you created permanently gains the extra protection granted by the "
                                 "Protective Oil. You may repeat this exploit."}])

career_old_squire = Career(
    name='Squire',
    career_time='1',
    career_time_unit='years',
    prereq='none',
    agility=1, charisma=1, luck=1, reputation=1,
    available_skills=['lances', 'swords', 'heraldry', 'carrying', 'healing', 'animal handling', 'riding', 'bravery'],
    desc="You spent time as a squire to a noble knight. While some move straight into knighthood, paying your dues as "
         "a squire is the only way to truly rise to the top of the knightly tradition. You can always tell a knight "
         "who wasn't a squire first, as he lacks some of the basics.",
    available_exploits=[{'Name': 'Sword-sharpener',
                         'Desc': "You know how to maintain your (or your liege's) equipment. One standard quality "
                                 "suit of armor and one standard quality melee weapon becomes high quality, "
                                 "as long as you spend an hour maintaining it every day."},
                        {'Name': 'Etiquette',
                         'Desc': "You learn the ways of court and castle; you gain a +1d6 bonus in situations which "
                                 "involve courtly etiquette, music, dance, and chivalry."},
                        {'Name': 'Loyal guardian',
                         'Desc': "You are able to protect a fallen ally. An unconscious character in an adjacent "
                                 "square cannot be further harmed while you remain adjacent to him; instead you take "
                                 "half damage (round down) from any attacks. In addition, you gain a +1d6 bonus to "
                                 "LOG checks made to stabilize a fallen character or to perform emergency healing on "
                                 "the battlefield."},
                        {'Name': 'Standard-bearer',
                         'Desc': "You can carry a flag or banner which grants allies who can see it +1d6 to "
                                 "INITIATIVE checks."},
                        {'Name': 'Dress wounds',
                         'Desc': "You can heal 1d6 HEALTH using a basic healer's kit; this costs two actions. No "
                                 "recipient can benefit from this more than once per day."}])

career_old_undead_hunter = Career(
    name='Undead Hunter',
    career_time='1d6',
    career_time_unit='years',
    prereq='religion',
    logic=1, willpower=1, charisma=1, luck=1,
    available_skills=['religion', 'abjuration', 'tracking', 'history', 'herbalism', 'linguistics', 'medicine'],
    desc="An expert on the undead, you have vowed to hunt and destroy them. Your academic research and knowledge are "
         "powerful weapons against your immortal foes. Many undead hunters choose to learn a little magic, also.",
    available_exploits=[{'Name': 'Death Bane',
                         'Desc': ". Using an herbalism kit, you can create a death bane—an ointment or natural amulet "
                                 "(such as the stereotypical garlic vs. vampires). This grants<br />you +4 DEFENSE "
                                 "vs. the undead. Death Ward. You learn the secret of undead."},
                        {
                            'Name': 'Divine Strike</strong>. Your attacks do Good damage to the '
                                    'undead.</li><li><strong>Holy Symbol',
                            'Desc': "(requires Turn Undead) Brandishing your holy symbol aloft, your Turn Undead "
                                    "ability now pushes the undead two steps along the Fear status track."},
                        {'Name': 'Lore of the Dead',
                         'Desc': "You can identify undead creatures by sight and know their weaknesses."},
                        {'Name': 'Special Enemy',
                         'Desc': "(requires Lore of the Dead) Choose one type of undead. You become known as a hunter "
                                 "of that type of undead (e.g. a Vampire Hunter), and gain +2 REP. You automatically "
                                 "ignore any natural SOAK that that creature possesses (although not armor SOAK)."},
                        {'Name': 'Stalwart', 'Desc': "You become immune to fear effects caused by the undead."},
                        {'Name': 'Stench of Death', 'Desc': "You can sense the presence of the undead within 30'."},
                        {'Name': 'Turn Undead',
                         'Desc': "(requires Stalwart) You can make a CHA vs. Mental Defense attack which affects all "
                                 "undead within 30' of you. Undead affected by this attack are moved one step along "
                                 "the Fear status track."}])

career_old_warrior_monk = Career(
    name='Warrior-monk',
    career_time='1d6',
    career_time_unit='years',
    prereq='religion or martial arts',
    agility=1, endurance=1, intuition=1, willpower=1,
    available_skills=['martial arts', 'acrobatics', 'religion', 'philosophy', 'dancing', '[artistic]', 'staves'],
    desc="You became a member of a militant monastic order, and were trained in philosophy and martial arts.",
    available_exploits=[{'Name': 'Martial technique base',
                         'Desc': "You gain two of the following universal exploits: Trip, Throw, Sidestep, "
                                 "Flying Kick. You may take this exploit again to gain the remaining two exploits."},
                        {'Name': 'Iron fist', 'Desc': "Your unarmed damage increases by 1d6."},
                        {'Name': 'Martial leap',
                         'Desc': "Increase both your vertical and horizontal JUMP distances by 5'."},
                        {'Name': 'Defensive stance',
                         'Desc': "You gain +4 to your MELEE DEFENSE. This does not stack with Drunken Fist."},
                        {'Name': 'Weapon synthesis',
                         'Desc': "When using any Oriental weapon, you gain one free unarmed melee atatck whenever you "
                                 "make two weapon attacks."},
                        {'Name': 'Drunken fist',
                         'Desc': "When intoxicated through alcohol, you gain +4 to your MELEE DEFENSE. This does not "
                                 "stack with Defensive Stance."},
                        {'Name': 'Iron skin', 'Desc': "Your training grants you +2 natural SOAK."},
                        {'Name': 'Elemental fist',
                         'Desc': "(requires Iron Fist, MAG 2+) Your fist is surrounded by the glow of elemental "
                                 "energy. The damage type becomes heat, and does an additional +1d6 damage."},
                        {'Name': 'Mountain stance',
                         'Desc': "(requires Defensive Stance) You become as immobile as a mountain. No knockdown or "
                                 "knockback attempt by a creature of your size or smaller will work against you."},
                        {'Name': 'Zen mind', 'Desc': "You gain +4 to your MENTAL DEFENSE."}])

career_old_watchman = Career(
    name='Watchman',
    career_time='1d6',
    career_time_unit='years',
    prereq='none',
    endurance=1, intuition=1, luck=1, reputation=1,
    available_skills=['swords', 'clubs', 'perception', 'thievery', 'interrogation', 'tracking', 'intimidate', 'law',
                      'local knowledge'],
    desc="A town guard or local police force, you enforce the law.",
    available_exploits=[{'Name': 'Vigilant',
                         'Desc': "Constantly vigilant, you are hard to surprise. You gain a +1d6 die bonus to access "
                                 "the ambush turn."},
                        {'Name': 'Chaser', 'Desc': "When chasing someone, your SPEED increases by +2."},
                        {'Name': 'Clues',
                         'Desc': "If there are clues to be discovered at the scene of a crime, you automatically find "
                                 "them within 5 minutes."},
                        {'Name': 'Sap',
                         'Desc': "You gain a special sap attack, used to knock out and apprehend criminals. You use "
                                 "any weapon; you do no damage, but a successful attack pushes the target along the "
                                 "Alertness status track by one stage for each 5 points of damage you would have "
                                 "done."},
                        {'Name': 'Troublesense',
                         'Desc': "You are able to spot trouble before it happens. You gain a +1d6 bonus to INITIATIVE "
                                 "checks."}])

career_old_list = [career_old_alchemist, career_old_archer, career_old_assassin, career_old_barbarian,
                   career_old_berserker, career_old_burglar, career_old_cleric, career_old_diabolist, career_old_druid,
                   career_old_firemage, career_old_gladiator, career_old_herbalist, career_old_inquisitor,
                   career_old_knight, career_old_loremaster, career_old_mage, career_old_man_at_arms,
                   career_old_minstrel, career_old_musketeer, career_old_necromancer, career_old_pirate,
                   career_old_prisoner, career_old_ranger, career_old_ruffian, career_old_sailor, career_old_smith,
                   career_old_squire, career_old_undead_hunter, career_old_warrior_monk, career_old_watchman]

for career in career_old_list:
    career.available_skills.sort()
