def atk_base_build(attack=0, build=None):
    if build:
        attack = build[0]

    if attack == 0:
        return 0
    if 1 <= attack <= 10:
        return 5 + atk_base_build(attack - 1)
    if 11 <= attack <= 20:
        return 6 + atk_base_build(attack - 1)
    if 21 <= attack <= 30:
        return 8 + atk_base_build(attack - 1)
    if 31 <= attack <= 40:
        return 7 + atk_base_build(attack - 1)
    if 41 <= attack <= 50:
        return 9 + atk_base_build(attack - 1)
    if 51 <= attack <= 60:
        return 10 + atk_base_build(attack - 1)
    if 61 <= attack <= 70:
        return 11 + atk_base_build(attack - 1)
    if 71 <= attack <= 80:
        return 13 + atk_base_build(attack - 1)
    if 81 <= attack <= 90:
        return 14 + atk_base_build(attack - 1)
    if 91 <= attack <= 94:
        return 15 + atk_base_build(attack - 1)
    if attack == 95:
        return 16 + atk_base_build(attack - 1)
    if 96 <= attack <= 97:
        return 17 + atk_base_build(attack - 1)
    if 98 <= attack <= 100:
        return 20 + atk_base_build(attack - 1)
    if 101 <= attack <= 110:
        return 15 + atk_base_build(attack - 1)
    if 111 <= attack <= 120:
        return 20 + atk_base_build(attack - 1)    
    raise ValueError("SP build attack points must be an integer"
                     "between 0 and 120")


def _atk_bonus_atk(attack=0):
    if attack == 0:
        return 0
    if 1 <= attack <= 29:
        return 5
    if 30 <= attack <= 69:
        return 10
    if 70 <= attack <= 99:
        return 15
    if 100 <= attack <= 109:
        return 20
    if 110 <= attack <= 119:
        return 30    
    if attack == 120:
        return 40
    raise ValueError("SP build attack points must be an integer"
                     "between 0 and 120")


def _atk_bonus_hp(hp=0):
    if 0 <= hp <= 4:
        return 0
    if 5 <= hp <= 9:
        return 5
    if 10 <= hp <= 14:
        return 10
    if 15 <= hp <= 19:
        return 15
    if 20 <= hp <= 24:
        return 20
    if 25 <= hp <= 29:
        return 25
    if 30 <= hp <= 34:
        return 30
    if 35 <= hp <= 39:
        return 35
    if 40 <= hp <= 44:
        return 40
    if 45 <= hp <= 49:
        return 50
    if 50 <= hp <= 54:
        return 60
    if 55 <= hp <= 59:
        return 70
    if 60 <= hp <= 64:
        return 80
    if 65 <= hp <= 69:
        return 90
    if 70 <= hp <= 74:
        return 100
    if 75 <= hp <= 79:
        return 115
    if 80 <= hp <= 84:
        return 130
    if 85 <= hp <= 89:
        return 145
    if 90 <= hp <= 94:
        return 160
    if 95 <= hp <= 99:
        return 180
    if 100 <= hp <= 109:
        return 200
    if 110 <= hp <= 120:
        return 230
    raise ValueError("SP build hp points must be an integer"
                     "between 0 and 120") 


def atk_bonus_build(attack=0, hp=0, build=None):
    if build:
        attack = build[0]
        hp = build[3]

    return _atk_bonus_atk(attack) + _atk_bonus_hp(hp)


def ele_base_build(element=0, build=None):
    if build:
        element = build[2]

    if element == 0:
        return 0
    if 1 <= element <= 50:
        return 1 + ele_base_build(element - 1)
    if 51 <= element <= 120:
        return 2 + ele_base_build(element - 1)
    raise ValueError("SP build element points must be an integer "
                     "between 0 and 120")


def ele_bonus_build(element=0, build=None):
    if build:
        element = build[2]

    if element == 0:
        return 0
    if 1 <= element <= 29:
        return 2
    if 30 <= element <= 59:
        return 4
    if 60 <= element <= 89:
        return 6
    if 90 <= element <= 99:
        return 8
    if 100 <= element <= 109:
        return 10
    if 110 <= element <= 119:
        return 12    
    if element == 120:
        return 14
    raise ValueError("SP build element points must be an integer"
                     "between 0 and 120")


def def_base_build(defense=0, build=None):
    if build:
        defense = build[1]

    if defense == 0:
        return 0
    if 1 <= defense <= 10:
        return 1 + def_base_build(defense - 1)
    if 11 <= defense <= 20:
        return 2 + def_base_build(defense - 1)
    if 21 <= defense <= 30:
        return 3 + def_base_build(defense - 1)
    if 31 <= defense <= 40:
        return 4 + def_base_build(defense - 1)
    if 41 <= defense <= 50:
        return 5 + def_base_build(defense - 1)
    if 51 <= defense <= 60:
        return 6 + def_base_build(defense - 1)
    if 61 <= defense <= 70:
        return 7 + def_base_build(defense - 1)
    if 71 <= defense <= 80:
        return 8 + def_base_build(defense - 1)
    if 81 <= defense <= 90:
        return 9 + def_base_build(defense - 1)
    if 91 <= defense <= 105:
        return 10 + def_base_build(defense - 1)
    if 106 <= defense <= 110:
        return 12 + def_base_build(defense - 1)
    if 111 <= defense <= 115:
        return 14 + def_base_build(defense - 1)
    if 116 <= defense <= 119:
        return 15 + def_base_build(defense - 1)
    if defense == 100:
        return 20 + def_base_build(defense - 1)
    raise ValueError("SP build defense points must be an integer"
                     "between 0 and 120")


def def_bonus_build(hp=0, build=None):
    if build:
        hp = build[2]

    if 0 <= hp <= 19:
        return 0
    if 20 <= hp <= 39:
        return 10
    if 40 <= hp <= 69:
        return 25
    if 70 <= hp <= 89:
        return 45
    if 90 <= hp <= 99:
        return 70
    if 100 <= hp <= 114:
        return 100
    if 115 <= hp <= 120:
        return 135
    raise ValueError("SP build hp points must be an integer"
                     "between 0 and 120")


def sp_points(job, up):
    if not 0 <= job <= 99:
        raise ValueError("SP job must be an integer between 0 and 99")
    if not 0 <= up <= 20:
        raise ValueError("SP up must be an integer between 0 and 20")

    job_points = max(0, job - 20) * 3
    from datastructs import constants as cs

    return job_points + cs.sp_up_bonus[up]


def atk_points(attack=0, build=None):
    if build:
        attack = build[0]

    if attack == 0:
        return 0
    if 1 <= attack <= 10:
        return 1 + atk_points(attack - 1)
    if 11 <= attack <= 19:
        return 2 + atk_points(attack - 1)
    if 20 <= attack <= 39:
        return 3 + atk_points(attack - 1)
    if 40 <= attack <= 59:
        return 4 + atk_points(attack - 1)
    if 60 <= attack <= 79:
        return 5 + atk_points(attack - 1)
    if 80 <= attack <= 90:
        return 6 + atk_points(attack - 1)
    if 91 <= attack <= 97:
        return 7 + atk_points(attack - 1)
    if attack == 98:
        return 8 + atk_points(attack - 1)
    if attack == 99:
        return 9 + atk_points(attack - 1)
    if attack == 100:
        return 10 + atk_points(attack - 1)
    if 101 <= attack <= 104:
        return 3 + atk_points(attack - 1)
    if 105 <= attack <= 119:
        return 4 + atk_points(attack - 1)
    if attack == 120:
        return 5 + atk_points(attack - 1)       
    raise ValueError("SP build attack points must be an integer"
                     "between 0 and 120")


def def_points(defense=0, build=None):
    if build:
        defense = build[0]

    if defense == 0:
        return 0
    if 1 <= defense <= 10:
        return 1 + def_points(defense - 1)
    if 11 <= defense <= 29:
        return 2 + def_points(defense - 1)
    if 30 <= defense <= 40:
        return 3 + def_points(defense - 1)
    if 41 <= defense <= 60:
        return 4 + def_points(defense - 1)
    if 61 <= defense <= 75:
        return 5 + def_points(defense - 1)
    if 76 <= defense <= 84:
        return 6 + def_points(defense - 1)
    if 85 <= defense <= 94:
        return 7 + def_points(defense - 1)
    if 95 <= defense <= 99:
        return 8 + def_points(defense - 1)
    if defense == 100:
        return 10 + def_points(defense - 1)
    if 101 <= defense <= 104:
        return 3 + def_points(defense - 1)
    if 105 <= defense <= 119:
        return 4 + def_points(defense - 1)
    if defense == 120:
        return 5 + def_points(defense - 1)
    raise ValueError("SP build defense points must be an integer"
                     "between 0 and 120")


def ele_points(element=0, build=None):
    if build:
        element = build[0]

    if element == 0:
        return 0
    if 1 <= element <= 20:
        return 1 + ele_points(element - 1)
    if 21 <= element <= 30:
        return 2 + ele_points(element - 1)
    if 31 <= element <= 40:
        return 3 + ele_points(element - 1)
    if 41 <= element <= 50:
        return 4 + ele_points(element - 1)
    if 51 <= element <= 70:
        return 5 + ele_points(element - 1)
    if 71 <= element <= 80:
        return 6 + ele_points(element - 1)
    if 81 <= element <= 100:
        return 7 + ele_points(element - 1)
    if 101 <= element <= 104:
        return 3 + ele_points(element - 1)
    if 105 <= element <= 119:
        return 4 + ele_points(element - 1)
    if element == 120:
        return 5 + ele_points(element - 1)    
    raise ValueError("SP build element points must be an integer"
                     "between 0 and 120")


def hp_points(hp=0, build=None):
    if build:
        hp = build[0]

    if hp == 0:
        return 0
    if 1 <= hp <= 10:
        return 1 + hp_points(hp - 1)
    if 11 <= hp <= 30:
        return 2 + hp_points(hp - 1)
    if 31 <= hp <= 50:
        return 3 + hp_points(hp - 1)
    if 51 <= hp <= 60:
        return 4 + hp_points(hp - 1)
    if 61 <= hp <= 70:
        return 5 + hp_points(hp - 1)
    if 71 <= hp <= 80:
        return 6 + hp_points(hp - 1)
    if 81 <= hp <= 90:
        return 7 + hp_points(hp - 1)
    if 91 <= hp <= 100:
        return 8 + hp_points(hp - 1)
    if 101 <= hp <= 104:
        return 3 + hp_points(hp - 1)
    if 105 <= hp <= 119:
        return 4 + hp_points(hp - 1)
    if hp == 120:
        return 5 + hp_points(hp - 1)    
    raise ValueError("SP build hp points must be an integer"
                     "between 0 and 120")


def crit_dmg_increase(attack=0, build=None):
    if build:
        attack = build[0]

    if 0 <= attack <= 39:
        return 0
    if 40 <= attack <= 89:
        return 10
    if 90 <= attack <= 99:
        return 30
    if 100 <= attack <= 109:
        return 50
    if 110 <= attack <= 119:
        return 80
    if attack == 120:
        return 90
    raise ValueError("SP build attack points must be an integer"
                     "between 0 and 120")


def crit_prob_increase(attack=0, build=None):
    if build:
        attack = build[0]

    if 0 <= attack <= 19:
        return 0
    if 20 <= attack <= 79:
        return 2
    if 80 <= attack <= 99:
        return 5
    if 100 <= attack <= 119:
        return 8
    if attack == 120:
        return 10
    raise ValueError("SP build attack points must be an integer"
                     "between 0 and 120")


def build_points(build):
    return (atk_points(build[0])
            + def_points(build[1])
            + ele_points(build[2])
            + hp_points(build[3]))


def validate_build(job, up, build):
    return sp_points(job, up) >= build_points(build)
