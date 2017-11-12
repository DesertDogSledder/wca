import collections
import copy


class Character(object):
    def __init__(self, name='Devon Default', strength=3, agility=3, endurance=3, willpower=3, intuition=3, logic=3,
                 charisma=3, luck=3, reputation=0, magic=0, chi=0, psionics=0, race=None, race_stats=None,
                 homeworld=None, hook=None, career_track=None, notes='', race_skill_choices=None,
                 homeworld_skill_choices=None, trait=None, misc_exploits=None):
        self.name = name
        self.stats = collections.OrderedDict(STR=strength,
                                             AGI=agility,
                                             END=endurance,
                                             WIL=willpower,
                                             INT=intuition,
                                             LOG=logic,
                                             CHA=charisma,
                                             LUC=luck,
                                             REP=reputation,
                                             MAG=magic,
                                             CHI=chi,
                                             PSI=psionics)
        self.race = copy.deepcopy(race)
        if self.race is not None:
            self.race_stats = copy.deepcopy(self.race.stats)
        else:
            self.race_stats = collections.OrderedDict(STR=0,
                                                      AGI=0,
                                                      END=0,
                                                      WIL=0,
                                                      INT=0,
                                                      LOG=0,
                                                      CHA=0,
                                                      LUC=0,
                                                      REP=0,
                                                      MAG=0,
                                                      CHI=0,
                                                      PSI=0)
        if race_skill_choices is not None:
            self.race_skill_choices = copy.deepcopy(race_skill_choices)
            self.race_skill_choices.sort()
        else:
            self.race_skill_choices = []

        self.homeworld = copy.deepcopy(homeworld)

        if homeworld_skill_choices is not None:
            self.homeworld_skill_choices = copy.deepcopy(homeworld_skill_choices)
            self.homeworld_skill_choices.sort()
        else:
            self.homeworld_skill_choices = []

        if hook is not None:
            self.hook = copy.deepcopy(hook)
        else:
            self.hook = {'Hook': 'unset', 'Attribute': 'strength'}

        if career_track is not None:
            self.career_track = copy.deepcopy(career_track)
        else:
            self.career_track = []

        if trait is not None:
            self.trait = copy.deepcopy(trait)
        else:
            self.trait = {'Name': '''unset''', 'Desc': '''unset'''}

        if misc_exploits is not None:
            self.misc_exploits = copy.deepcopy(misc_exploits)
            self.misc_exploits.sort(key=lambda x: x['Name'])
        else:
            self.misc_exploits = []

        self.notes = notes

    def calc_stat_total(self):
        stat_total = copy.deepcopy(self.stats)

        for stat, value in self.race_stats.items():
            stat_total[stat] += value

        for stat, value in self.homeworld.stats.items():
            stat_total[stat] += value

        for career in self.career_track:
            for stat, value in career['Stats'].items():
                stat_total[stat] += value

        return stat_total

    def calc_skill_total(self):
        skill_list = []
        skill_total = collections.OrderedDict()

        for skill in self.race_skill_choices:
            skill_list.append(skill)

        for skill in self.homeworld_skill_choices:
            skill_list.append(skill)

        for career in self.career_track:
            for skill in career['Skills']:
                skill_list.append(skill)

        for skill in skill_list:
            if skill in skill_total:
                skill_total[skill] += 1
            else:
                skill_total[skill] = 1
        skill_total = collections.OrderedDict(sorted(skill_total.items(), key=lambda item: item))
        return skill_total

    def get_all_exploits(self):
        all_exploits = []
        all_exploits += self.race.exploits
        for career in self.career_track:
            all_exploits.append(career['Exploit'])
        all_exploits += self.misc_exploits

        all_exploits.sort(key=lambda x: x['Name'])
        return all_exploits

    def __str__(self):
        output = 'Name: {}\n'.format(self.name)
        output += 'Race: {}\n'.format(self.race.name)
        output += 'Homeworld: {}\n'.format(self.homeworld.name)
        output += 'Hook ({}): {}\n'.format(self.hook['Attribute'], self.hook['Hook'])
        output += 'Career track:\n'
        count = 1
        for career in self.career_track:
            output += '\t[{}] {} ({})\n'.format(count, career['Career'].name, career['Length'])
            count += 1
        output += 'Stat totals:\n'
        for key, value in self.calc_stat_total().items():
            output += '\t{}: {}\n'.format(key, value)
        output += 'Skill totals:\n'
        for key, value in self.calc_skill_total().items():
            output += '\t{}: {}\n'.format(key, value)
        output += 'Exploits:\n'
        for exploit in self.get_all_exploits():
            output += '\t{}\n'.format(exploit['Name'])
        return output


class Race(object):
    def __init__(self, name='Race', desc='Description', strength=0, agility=0, endurance=0, willpower=0, intuition=0,
                 logic=0, charisma=0, luck=0, reputation=0, magic=0, chi=0, psionics=0, size='medium',
                 available_skills=None, exploits=None):
        self.name = name
        self.desc = desc
        self.stats = collections.OrderedDict(STR=strength,
                                             AGI=agility,
                                             END=endurance,
                                             WIL=willpower,
                                             INT=intuition,
                                             LOG=logic,
                                             CHA=charisma,
                                             LUC=luck,
                                             REP=reputation,
                                             MAG=magic,
                                             CHI=chi,
                                             PSI=psionics)
        self.size = size
        if available_skills is not None:
            self.available_skills = copy.deepcopy(available_skills)
        else:
            self.available_skills = []

        if available_skills is not None:
            self.exploits = copy.deepcopy(exploits)
        else:
            self.available_skills = []

    def __str__(self):
        output = '{}\n'.format(self.name)
        output += 'Size: {}\n'.format(self.size)
        for key, value in self.stats.items():
            if value < 0 or value > 0:
                output += '{}: {}\n'.format(key, value)

        output += 'Skill choices: '
        skill_str = ''
        for skill in self.available_skills:
            skill_str += '{}, '.format(skill)
        output += '{}\n'.format(skill_str[:-2])

        output += 'Exploits:\n'
        for exploit in self.exploits:
            output += '\t{} - {}\n'.format(exploit['Name'], exploit['Desc'])

        return output


class Homeworld(object):
    def __init__(self, name='Homeworld', strength=0, agility=0, endurance=0, willpower=0, intuition=0, logic=0,
                 charisma=0, luck=0, reputation=0, magic=0, chi=0, psionics=0, available_skills=None):
        self.name = name
        self.stats = collections.OrderedDict(STR=strength,
                                             AGI=agility,
                                             END=endurance,
                                             WIL=willpower,
                                             INT=intuition,
                                             LOG=logic,
                                             CHA=charisma,
                                             LUC=luck,
                                             REP=reputation,
                                             MAG=magic,
                                             CHI=chi,
                                             PSI=psionics)
        if available_skills is not None:
            self.available_skills = copy.deepcopy(available_skills)
        else:
            self.available_skills = []

    def __str__(self):
        output = '{}\n'.format(self.name)
        for key, value in self.stats.items():
            if value < 0 or value > 0:
                output += '{}: {}\n'.format(key, value)
        output += 'Available skills: '
        skill_str = ''
        for skill in self.available_skills:
            skill_str += '{}, '.format(skill)
        output += '{}\n'.format(skill_str[:-2])

        return output


class Career(object):
    def __init__(self, name='Career', strength=0, agility=0, endurance=0, willpower=0, intuition=0, logic=0,
                 charisma=0, luck=0, reputation=0, magic=0, chi=0, psionics=0,
                 available_skills=None, available_exploits=None,
                 career_time='1d6', career_time_unit='years', desc='Description', prereq='none'):
        self.name = name
        self.stats = collections.OrderedDict(STR=strength,
                                             AGI=agility,
                                             END=endurance,
                                             WIL=willpower,
                                             INT=intuition,
                                             LOG=logic,
                                             CHA=charisma,
                                             LUC=luck,
                                             REP=reputation,
                                             MAG=magic,
                                             CHI=chi,
                                             PSI=psionics)
        if available_skills is not None:
            self.available_skills = copy.deepcopy(available_skills)
        else:
            self.available_skills = []
        if available_exploits is not None:
            self.available_exploits = copy.deepcopy(available_exploits)
        else:
            self.available_exploits = []
        self.career_time = career_time
        self.career_time_unit = career_time_unit
        self.desc = desc
        self.prereq = prereq

    def __str__(self):
        output = '{}\n'.format(self.name)
        output += 'Prerequisities: {}\n'.format(self.prereq)
        output += 'Description: {}\n'.format(self.desc)
        for key, value in self.stats.items():
            if value < 0 or value > 0:
                output += '{}: {}\n'.format(key, value)
        output += 'Available skills: '
        skill_str = ''
        for skill in self.available_skills:
            skill_str += '{}, '.format(skill)
        output += '{}\n'.format(skill_str[:-2])

        output += 'Available exploits:\n'
        for exploit in self.available_exploits:
            output += '\t{} - {}\n'.format(exploit['Name'], exploit['Desc'])

        return output
