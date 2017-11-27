import collections
import copy
import textwrap
import shutil
import math


def calc_dice_pool_size(raw_score):
    if raw_score <= 0:
        dice_pool_size = 0
    elif raw_score <= 2:
        dice_pool_size = 1
    elif raw_score <= 5:
        dice_pool_size = 2
    elif raw_score <= 9:
        dice_pool_size = 3
    elif raw_score <= 14:
        dice_pool_size = 4
    elif raw_score <= 20:
        dice_pool_size = 5
    else:
        dice_pool_size = 6

    return dice_pool_size


def calc_max_dice_pool_size(career_grade):
    if career_grade <= 5:
        max_dice_pool_size = career_grade
    elif career_grade <= 7:
        max_dice_pool_size = 6
    elif career_grade <= 10:
        max_dice_pool_size = 7
    elif career_grade <= 14:
        max_dice_pool_size = 8
    elif career_grade <= 19:
        max_dice_pool_size = 9
    elif career_grade <= 25:
        max_dice_pool_size = 10
    elif career_grade <= 32:
        max_dice_pool_size = 11
    else:
        max_dice_pool_size = 12

    return max_dice_pool_size


class Character(object):
    def __init__(self, name='unnamed', strength=3, agility=3, endurance=3, willpower=3, intuition=3, logic=3,
                 charisma=3, luck=3, reputation=0, magic=0, chi=0, psionics=0, race=None,
                 homeworld=None, hook='unset', career_track=None, notes='', race_skill_choices=None,
                 homeworld_skill_choices=None, trait=None, misc_exploits=None, age_descriptor='unset'):
        self.name = name
        self.stats = collections.OrderedDict(STR=strength,
                                             AGI=agility,
                                             END=endurance,
                                             INT=intuition,
                                             LOG=logic,
                                             WIL=willpower,
                                             CHA=charisma,
                                             LUC=luck,
                                             REP=reputation,
                                             MAG=magic,
                                             CHI=chi,
                                             PSI=psionics)
        self.race = copy.deepcopy(race)

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

        self.hook = hook

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

        self.age_descriptor = age_descriptor
        self.notes = notes

    def calc_stat_total(self):
        stat_total = copy.deepcopy(self.stats)

        for stat, value in self.race['Stats'].items():
            stat_total[stat] += value

        for stat, value in self.homeworld['Homeworld'].stats.items():
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

    def calc_derived_stats(self):
        derived_stats = collections.OrderedDict()
        stat_total = self.calc_stat_total()
        skill_total = self.calc_skill_total()

        ##########
        # HEALTH #
        ##########
        end_dice_pool = calc_dice_pool_size(stat_total['END'])
        wil_dice_pool = calc_dice_pool_size(stat_total['WIL'])
        average_health = end_dice_pool + wil_dice_pool
        health_info = 'Roll END ({}d6) + WIL ({}d6)'.format(end_dice_pool, wil_dice_pool)

        if 'hardy' in skill_total:
            hardy_dice_pool = calc_dice_pool_size(skill_total['hardy'])
            health_info += ' + hardy ({}d6)'.format(hardy_dice_pool)
            average_health += hardy_dice_pool

        average_health *= 3.5
        if average_health >= 10:
            health_info += ' (average = {})'.format(average_health)
        else:
            health_info += ' (average bumped up to minimum = 10)'

        derived_stats['Health'] = health_info

        #########
        # SPEED #
        #########
        base_speed = calc_dice_pool_size(stat_total['STR']) + calc_dice_pool_size(stat_total['AGI'])
        speed = base_speed
        if 'running' in skill_total:
            speed += calc_dice_pool_size(skill_total['running'])

        climbing = base_speed
        swimming = base_speed
        zero_g = base_speed
        high_g = base_speed
        low_g = base_speed

        if 'climbing' in skill_total:
            climbing += calc_dice_pool_size(skill_total['climbing'])
        if 'swimming' in skill_total:
            swimming += calc_dice_pool_size(skill_total['swimming'])
        if 'zero-g' in skill_total:
            zero_g += calc_dice_pool_size(skill_total['zero-g'])
        if 'high-g' in skill_total:
            high_g += calc_dice_pool_size(skill_total['high-g'])
        if 'low-g' in skill_total:
            low_g += calc_dice_pool_size(skill_total['low-g'])

        climbing = math.ceil(climbing / 2)
        swimming = math.ceil(swimming / 2)
        zero_g = math.ceil(zero_g / 2)
        high_g = math.ceil(high_g / 2)
        low_g = math.ceil(low_g / 2)

        derived_stats['Speed'] = speed
        derived_stats['Climbing'] = climbing
        derived_stats['Swimming'] = swimming
        derived_stats['Zero-G'] = zero_g
        derived_stats['High-G'] = high_g
        derived_stats['Low-G'] = low_g

        ########
        # JUMP #
        ########
        derived_stats['Horizontal Jump'] = '{}\' (standing: {}\')'.format(stat_total['AGI']*2, stat_total['AGI'])
        # Vertical jump values cannot exceed horizontal jump values
        if stat_total['STR'] <= stat_total['AGI']:
            vertical_jump_standing = stat_total['STR']
            vertical_jump_running = stat_total['STR'] * 2
        else:
            vertical_jump_standing = stat_total['AGI']
            vertical_jump_running = stat_total['AGI'] * 2
        derived_stats['Vertical Jump'] = '{}\' (standing: {}\')'.format(vertical_jump_running, vertical_jump_standing)

        #########
        # CARRY #
        #########
        if 'carry' in skill_total:
            base_carry = (stat_total['STR'] + stat_total['END'] + skill_total['carry']) * 10
        else:
            base_carry = (stat_total['STR'] + stat_total['END']) * 10

        derived_stats['Carry'] = '{} (before exploits and size modifiers)'.format(base_carry)

        return derived_stats

    def get_all_exploits(self):
        all_exploits = []
        all_exploits += self.race['Race'].exploits
        all_exploits.append(self.trait)
        for career in self.career_track:
            all_exploits.append(career['Exploit'])
        all_exploits += self.misc_exploits

        all_exploits.sort(key=lambda x: x['Name'])
        return all_exploits

    def __str__(self):
        terminal_size = shutil.get_terminal_size()
        width = terminal_size[0]

        if len(self.career_track) > 0:
            output = '{}\n'.format(self.name)
            if self.age_descriptor[0] in 'aeiou':
                output += 'an '
            else:
                output += 'a '
            output += '{} {} {} {} who {} ({}d6)\n\n'.format(self.age_descriptor, self.trait['Name'].lower(),
                                                             self.race['Race'].name,
                                                             self.career_track[len(self.career_track)-1]
                                                             ['Career'].name.lower(),
                                                             self.hook,
                                                             calc_max_dice_pool_size(len(self.career_track)))
        else:
            output = ''
        output += 'Name: {}\n'.format(self.name)
        output += 'Race: {}\n'.format(self.race['Race'].name)
        output += 'Homeworld: {}\n'.format(self.homeworld['Homeworld'].name)
        output += 'Hook: {}\n'.format(self.hook)
        output += 'Career track:\n'
        count = 1
        for career in self.career_track:
            output += '    [{}] {} ({})\n'.format(count, career['Career'].name, career['Length'])
            count += 1
        output += '\nStat totals:\n'
        for key, value in self.calc_stat_total().items():
            output += '    {}: {} ({}d6)\n'.format(key, value, calc_dice_pool_size(value))
        output += '\nSkill totals:\n'
        for key, value in self.calc_skill_total().items():
            output += '    {}: {} ({}d6)\n'.format(key, value, calc_dice_pool_size(value))
        output += '\nExploits:\n'
        for exploit in self.get_all_exploits():
            output += '    {} - '.format(exploit['Name'])
            for line in textwrap.wrap((exploit['Desc']), width-len(exploit['Name'])):
                output += '{}\n    '.format(line)
            output += '\n'
        output += 'Derived Statistics:\n'
        for key, value in self.calc_derived_stats().items():
            output += '        {}: {}\n'.format(key, value)

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
                                             INT=intuition,
                                             LOG=logic,
                                             WIL=willpower,
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
        terminal_size = shutil.get_terminal_size()
        width = terminal_size[0]
        output = '{}\n'.format(self.name)
        for line in textwrap.wrap(self.desc, width):
            output += '{}\n'.format(line)
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
            output += '    {} - '.format(exploit['Name'])
            for line in textwrap.wrap((exploit['Desc']), width - len(exploit['Name'])):
                output += '{}\n    '.format(line)
            output += '\n'

        return output


class Homeworld(object):
    def __init__(self, name='Homeworld', strength=0, agility=0, endurance=0, willpower=0, intuition=0, logic=0,
                 charisma=0, luck=0, reputation=0, magic=0, chi=0, psionics=0, available_skills=None):
        self.name = name
        self.stats = collections.OrderedDict(STR=strength,
                                             AGI=agility,
                                             END=endurance,
                                             INT=intuition,
                                             LOG=logic,
                                             WIL=willpower,
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
                                             INT=intuition,
                                             LOG=logic,
                                             WIL=willpower,
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
        terminal_size = shutil.get_terminal_size()
        width = terminal_size[0]
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
            output += '    {} - '.format(exploit['Name'])
            for line in textwrap.wrap((exploit['Desc']), width-len(exploit['Name'])):
                output += '{}\n    '.format(line)
            output += '\n'

        return output
