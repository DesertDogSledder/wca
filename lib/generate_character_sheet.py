from lib.character import calc_dice_pool_size
from lib.character import calc_max_dice_pool_size


def generate_character_sheet(user_character):
    css = \
        '''    * {
                box-sizing: border-box;
            }
            
            .left {
                float: left;
                width: 25em;
                padding: 0px 10px 0px 10px;
            }
            
            .right {
                float: left;
                padding: 0px 10px 0px 10px;
            }
            
            .three-col-1 {
                float: left;
                width: 20em;
                padding: 0px 10px 0px 10px;            
            }
            
            .three-col-2 {
                float: left;
                width: 20em;
                padding: 0px 10px 0px 10px;               
            }
            
            .three-col-3 {
                float: left;
                padding: 0px 10px 0px 10px;               
            }
            
            /* Clear floats after the columns */
            .row:after {
                content: "";
                display: table;
                clear: both;
            }'''

    name_html = '''<b>{}</b>'''.format(user_character.name)
    if len(user_character.career_track) > 0:
        last_career = user_character.career_track[-1]['Career'].name.lower()
    else:
        last_career = '<no careers set!>'
    descriptor_html = '''a[n] {} {} {} {} who {} ({}d6)'''.format(
        user_character.age_descriptor,
        user_character.trait['Name'].lower(),
        user_character.race['Race'].name,
        last_career,
        user_character.hook,
        calc_max_dice_pool_size(len(user_character.career_track)))

    total_stats = user_character.calc_stat_total()
    stats_html = \
        '''<table border="1px">
            <tr>
                <th>STR</th>
                <th>AGI</th>
                <th>END</th>
                <th>INT</th>
                <th>LOG</th>
                <th>WIL</th>
                <th>CHA</th>
                <th>LUC</th>
                <th>REP</th>
                <th>MAG</th>
                <th>CHI</th>
                <th>PSI</th>
            </tr>
            <tr>
                <td>{str} ({str_dp}d6)</td>
                <td>{agi} ({agi_dp}d6)</td>
                <td>{end} ({end_dp}d6)</td>
                <td>{int} ({int_dp}d6)</td>
                <td>{log} ({log_dp}d6)</td>
                <td>{wil} ({wil_dp}d6)</td>
                <td>{cha} ({cha_dp}d6)</td>
                <td>{luc} ({luc_dp}d6)</td>
                <td>{rep} ({rep_dp}d6)</td>
                <td>{mag} ({mag_dp}d6)</td>
                <td>{chi} ({chi_dp}d6)</td>
                <td>{psi} ({psi_dp}d6)</td>
            </tr>
        </table>'''.format(str=total_stats['STR'], str_dp=calc_dice_pool_size(total_stats['STR']),
                           agi=total_stats['AGI'], agi_dp=calc_dice_pool_size(total_stats['AGI']),
                           end=total_stats['END'], end_dp=calc_dice_pool_size(total_stats['END']),
                           int=total_stats['INT'], int_dp=calc_dice_pool_size(total_stats['INT']),
                           log=total_stats['LOG'], log_dp=calc_dice_pool_size(total_stats['LOG']),
                           wil=total_stats['WIL'], wil_dp=calc_dice_pool_size(total_stats['WIL']),
                           cha=total_stats['CHA'], cha_dp=calc_dice_pool_size(total_stats['CHA']),
                           luc=total_stats['LUC'], luc_dp=calc_dice_pool_size(total_stats['LUC']),
                           rep=total_stats['REP'], rep_dp=calc_dice_pool_size(total_stats['REP']),
                           mag=total_stats['MAG'], mag_dp=calc_dice_pool_size(total_stats['MAG']),
                           chi=total_stats['CHI'], chi_dp=calc_dice_pool_size(total_stats['CHI']),
                           psi=total_stats['PSI'], psi_dp=calc_dice_pool_size(total_stats['PSI']))

    derived_stats = user_character.calc_derived_stats()

    health_html = \
        '''<b><i>Health</i></b><br />
                {}'''.format(derived_stats['Health'])

    defenses_html = \
        '''<b><i>Defenses</i></b>
                <table border="1px">
                    <tr>
                        <th>Melee</th>
                        <th>Ranged</th>
                        <th>Mental</th>
                        <th>Vital</th>
                    </tr>
                    <tr>
                        <td>{melee}</td>
                        <td>{ranged}</td>
                        <td>{mental}</td>
                        <td>{vital}</td>
                    </tr>
                </table>'''.format(melee=derived_stats['Melee Defense'],
                                   ranged=derived_stats['Ranged Defense'],
                                   mental=derived_stats['Mental Defense'],
                                   vital=derived_stats['Vital Defense'])

    movement_html = \
        '''<b><i>Movement</i></b>
                <table border="1px" width="100%">
                    <tr>
                        <th>Initiative</th>
                    </tr>
                    <tr>
                        <td align="center">{initiative}</td>
                    </tr>
                </table>
                <table border="1px" width="100%">
                    <tr>
                        <th>Speed</th>
                        <th>Climb</th>
                        <th>Swim</th>
                    </tr>
                    <tr>
                        <td align="center">{speed}</td>
                        <td align="center">{climb}</td>
                        <td align="center">{swim}</td>
                    </tr>
                </table>
                <table border="1px" width="100%">
                    <tr>
                        <th>Zero-G</th>
                        <th>Low-G</th>
                        <th>High-G</th>
                    </tr>
                    <tr>
                        <td align="center">{zero_g}</td>
                        <td align="center">{low_g}</td>
                        <td align="center">{high_g}</td>
                    </tr>
                </table>
                <table border="1px" width="100%">
                    <tr>
                        <th>Vertical Jump</th>
                        <th>Horizontal Jump</th>
                    </tr>
                    <tr>
                        <td align="center">{vjump}'/{vrunjump}'</td>
                        <td align="center">{hjump}'/{hrunjump}'</td>
                    </tr>
                </table>
                <table border="1px" width="100%">
                    <tr>
                        <th>Carry</th>
                    </tr>
                    <tr>
                        <td align="center">{carry}</td>
                    </tr>
                </table>'''.format(initiative=derived_stats['Initiative'],
                                   speed=derived_stats['Speed'],
                                   climb=derived_stats['Climb'],
                                   swim=derived_stats['Swim'],
                                   zero_g=derived_stats['Zero-G'],
                                   low_g=derived_stats['Low-G'],
                                   high_g=derived_stats['High-G'],
                                   vjump=derived_stats['Vertical Jump Standing'],
                                   vrunjump=derived_stats['Vertical Jump Running'],
                                   hjump=derived_stats['Horizontal Jump Standing'],
                                   hrunjump=derived_stats['Horizontal Jump Running'],
                                   carry=derived_stats['Carry'])

    skills_html = \
        '''<b><i>Skills</i></b>
                <table border="1px">
'''

    skill_total = user_character.calc_skill_total()
    for skill, rank in skill_total.items():
        skills_html += \
            '''                <tr>
                    <td>{}</td>
                    <td>{} ({}d6)</td>
                </tr>
'''.format(skill, rank, calc_dice_pool_size(rank))
    skills_html += '''            </table>'''

    exploits_html = '''<b><i>Exploits & Traits</i></b>
                <table border="1px">
'''

    all_exploits = user_character.get_all_exploits()
    for exploit in all_exploits:
        exploits_html += \
            '''                <tr>
                    <td>{}</td>
                    <td>{}</td>
                </tr>'''.format(exploit['Name'], exploit['Desc'])

    exploits_html += '''</table>'''

    careers_html = '''<b><i>Life Path</i></b>
                <table border="1px">
'''

    for career in user_character.career_track:
        careers_html += \
                '''                <tr>
                        <td>{}</td>
                        <td>{}</td>
                    </tr>'''.format(career['Career'].name, career['Length'])

    careers_html += '''</table>'''

    general_gear_html = '''<b>General Gear</b>
                <table border="1px">
                    <tr>
                        <th>Item</th>
                        <th>Weight</th>
                        <th>Quantity</th>
                        <th>Cost</th>
                    </tr>
'''

    for item in user_character.equipment['General']:
        general_gear_html += \
                '''                <tr>
                        <td>{}</td>
                        <td>{}</td>
                        <td>{}</td>
                        <td>{}</td>
                    </tr>'''.format(item['Name'], item['Weight'], item['Quantity'], item['Cost'])

    general_gear_html += '''</table>'''

    weapons_html = '''<b>Weapons</b>
                <table border="1px">
                    <tr>
                        <th>Item</th>
                        <th>Quality</th>
                        <th>Damage</th>
                        <th>Type</th>
                        <th>Range</th>
                        <th>Weight</th>
                        <th>Cost</th>
                        <th>Quantity</th>
                        <th>Special</th>
                    </tr>
'''

    for weapon in user_character.equipment['Weapons']:
        weapons_html += \
            '''                <tr>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
            </tr>'''.format(weapon['Name'], weapon['Quality'], weapon['Damage'], weapon['Type'], weapon['Range'],
                            weapon['Weight'], weapon['Cost'], weapon['Quantity'], weapon['Special'])
        for ammo in weapon['Ammunition']:
            weapons_html += \
            '''<tr>
            <td colspan=7>Ammunition - {}</td>
            <td>{}</td>
            </tr>
            '''.format(ammo['Name'], ammo['Quantity'])

    weapons_html += '''</table>'''

    armor_html = '''<b>Armor</b>
                <table border="1px">
                    <tr>
                        <th>Item</th>
                        <th>Type</th>
                        <th>Quality</th>
                        <th>Soak</th>
                        <th>Defense</th>
                        <th>Speed</th>
                        <th>Weight</th>
                        <th>Cost</th>
                        <th>Quantity</th>
                        <th>Special</th>
                    </tr>
'''

    for armor in user_character.equipment['Armor']:
        armor_html += \
            '''                <tr>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
            </tr>'''.format(armor['Name'], armor['Type'], armor['Quality'], armor['Soak'], armor['Defense'],
                            armor['Speed'], armor['Weight'], armor['Cost'], armor['Quantity'], armor['Special'])

    armor_html += '''</table>'''

    html_str = \
            '''<html>
    <head>
        <style>
        {css}
        </style>
    </head>
    <body>
        <div style="padding: 0px 10px 0px 10px;">
            {name}<br />
            {descriptor}<br />
            <br />
            <b><i>Attributes</i></b>
            {stats}
            <br />
        </div>
        <div class="row">
            <div class="left">
                    {health}
            </div>
            <div class="right">
                    {defenses}
            </div>
        </div><br /><br />
        <div class="row">
            <div class="left">
                    {movement}
            </div>
            <div class="right">
                    {skills}
            </div>
        </div><br /><br />
        <div class="row">
            <div class="left">
                {exploits}
            </div>
            <div class="right">
                {careers}
            </div>
        </div><br /><br />
        <div style="padding: 0px 10px 0px 10px;">
            {general_gear}<br />
            {weapons}<br />
            {armor}<br />
        </div>
        <br /><br />
    </body>
</html>'''.format(css=css, name=name_html, descriptor=descriptor_html, stats=stats_html,
                  health=health_html, defenses=defenses_html, movement=movement_html,
                  skills=skills_html, exploits=exploits_html, careers=careers_html,
                  general_gear=general_gear_html, weapons=weapons_html, armor=armor_html)
    # Character name
    # a[n] ____ who ____
    # Stats

    # Health    # Defenses     #SOAK?
    # Movement    # Skills

    # Attacks

    # Exploits and Traits
    # Life path (age)

    # Wealth
    # XP

    return html_str


# if __name__ == '__main__':
#     path_name = '''C:\\QtUI\\Savany_Tesler.wca'''
#     output_path = '''C:\\QtUI\\Savany_Tesler.html'''
#     try:
#         with open(path_name, 'rb') as file:
#             my_char = pickle.load(file)
#     except IOError:
#         print("Cannot open file '{}'.".format(file))
#
#     html_str = generate_character_sheet(my_char)
#
#     try:
#         with open(output_path, 'w') as file:
#             file.write(str(html_str))
#             print('File written to {}'.format(output_path))
#     except IOError:
#         print("Cannot open file '{}'.".format(file))
