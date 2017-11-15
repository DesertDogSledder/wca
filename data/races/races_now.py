from lib.character import Race

# NOW races
race_now_augmented = Race(
    name='Augmented',
    desc="Maybe there were complications in your infancy, or tragedy struck during your childhood; either way "
         "you've received parts (organic or inorganic) that are an improvement over what you had before. No matter "
         "how it is exactly that you came to be this way, you're stronger for it and have an advantage over those "
         "regular humans, period. Whether or not you’re enlightened by this gift or malignant about it, however, "
         "depends much more on how exactly you're different, and how that colored your upbringing.",
    size='medium',
    endurance=2,
    available_skills=['hardy', 'perception', 'reactions', '[crafting]', '[trivia]', '[gaming]', '[scientific]',
                      '[technical]'],
    exploits=[{'Name': 'Alteration',
               'Desc': '''Augmented begin play with two minor or one major cybernetic alteration.'''},
              {'Name': 'Adaptive',
               'Desc': '''When incorporating new cybernetic alterations, augmented never need to make a check to '''
               '''see if the upgrade takes hold. Additionally, they can incorporate an unlimited number of '''
               '''alterations beyond the normal limit of their END attribute.'''},
              {'Name': 'Inert',
               'Desc': '''Augmented embrace technology over matters of spirit. They may never have a Chi score '''
               '''above zero.'''}])

race_now_chosen = Race(
    name='Chosen',
    desc='''Something about you is better. Maybe you are the result of a sublime genetic match, perhaps your genome '''
         '''was manipulated from before conception. How it is you came to be different is hardly important—how you '''
         '''are different is everything. Some designed are much more likeable or beautiful than the average human, '''
         '''others possess an evolved mental acuity, and some are sterling models of what biomechanics can '''
         '''achieve.\n\n'''
         '''You might be characterized by prophecy and legend, and are often surrounded by stories or myths. '''
         '''Whether you are part of a hereditary line, the touch of destiny graced upon you in the womb, you simply '''
         '''meet the criteria listed in an old prophecy, or whether actual mysticism or magic is involved, you are '''
         '''special.''',
    size='medium',
    chi=3, reputation=2, strength=1, charisma=1,
    available_skills=['negotiating', 'tactics', '[crafting]', '[trivia]', '[gaming]', '[scientific]'],
    exploits=[{'Name': 'Fast-Healing',
               'Desc': '''Chosen heal faster than most people. You may roll an extra 2d6 when determining how much '''
               '''you naturally heal each day.'''},
              {'Name': 'Skill Focus',
               'Desc': '''You start play with two bonus skills of your choice at 3 ranks (2d6).'''},
              {'Name': 'Destiny',
               'Desc': '''Once, when you ordinarily die, you do not die. Instead, you remain at 0 Health until '''
               '''healed. When you have used your extra “life” you cannot use it again.'''}])

race_now_human = Race(
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
               '''they go to a country new to them.'''},
              {'Name': 'Enduring',
               'Desc': '''Humans may not be the fastest or the strongest, but they are known for their resilience. '''
               '''Humans get +1 to their 1d6 die roll to shake off a temporary condition.'''}])

race_now_mutant = Race(
    name='Mutant',
    desc='''You are different, your genetics a variation from the norm. This might be blatantly obvious with '''
         '''physical deformities like albino skin, unnatural growths, discolored eyes, or asymmetrical features, or '''
         '''it may not be immediately noticeable—regardless of the exact nature of your deviant genetics doesn’t '''
         '''matter, but you must always take some action to hide it from society at large. Maybe you wear '''
         '''sunglasses to hide your entirely black eyes, cover yourself in makeup and wear flesh-colored tights to '''
         '''conceal your horrific skin, or wear extraneous clothing that hides your true nature.\n\n'''

         '''Mutants can be excellent users of CHI, exploring their power to great effect (whether for combat, '''
         '''exploration, or otherwise). They don’t often do well as social characters, faced with the adversity of '''
         '''prejudice for being visibly different.\n\n'''

         '''Examples in popular culture include Killer Croc, Johnny Alpha, and many X-Men.''',
    size='small, medium, or large',
    endurance=2, willpower=1, reputation=1, chi=1,
    available_skills=['hardy', 'intimidate', 'resistance', 'survival', '[crafting]', '[trivia]', '[gaming]',
                      'disguise'],
    exploits=[{'Name': 'Mutation',
               'Desc': '''Mutants have one or more mutations. Select one major or two minor mutations. You may '''
               '''select any number of cosmetic mutations, but you must choose at least one.'''}])

race_now_list = [race_now_augmented, race_now_chosen, race_now_human, race_now_mutant]

for race in race_now_list:
    race.available_skills.sort()
    race.exploits.sort(key=lambda x: x['Name'])
