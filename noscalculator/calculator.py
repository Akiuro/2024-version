from datastructs import elemental_bonus
from datastructs import up_bonus


class Calculator:
    def __init__(self, attacker, defender):
        self.attacker = attacker
        self.defender = defender

    def atk_tot(self, atk_eq, soft=False):
        up = min(max(self.attacker.up - self.defender.up, 0), 10)

        atk_char = ((atk_eq * (1 + up_bonus[up])
                     + self.attacker.atk_base
                     + self.attacker.atk_effects
                     + self.attacker.atk_sp()
                     + self.attacker.dmg_enhanced)
                    * (1 + self.attacker.dmg_increase_pvp))

        return ((atk_char + self.attacker.atk_skill + 15)
                * (1 + self.attacker.dmg_increase_s)
                * (1 + self.attacker.dmg_increase_eq * int(soft)))

    def def_tot(self):
        up = min(max(self.defender.up - self.attacker.up, 0), 10)

        def_char = ((self.defender.def_equip * (1 + up_bonus[up])
                     + self.defender.def_base
                     + self.defender.def_effects
                     + self.defender.def_sp()
                     + self.defender.def_enhanced)
                    * (1 + self.defender.def_increase_s
                       + self.defender.def_increase_pvp
                       - self.attacker.def_reduction_pvp))

        return ((def_char + self.defender.def_skill)
                * (1 + self.defender.def_pet_pvp)
                * (1 + int(self.defender.def_pot) * 0.2
                   + int(self.defender.def_oil) * 0.05
                   + self.defender.def_costume
                   + self.defender.def_pet))

    def atk_ele_tot(self, atk_eq, soft=False):
        atk_ele = ((self.atk_tot(atk_eq, soft=soft) + 100)
                   * (self.attacker.fairy + self.attacker.ele_sp()))

        return (atk_ele
                + self.attacker.ele_skill
                + self.attacker.ele_effects
                + self.attacker.ele_prop_increase)

    def physical_damage(self, atk_eq, crit=False, soft=False):
        dmg = ((self.atk_tot(atk_eq, soft=soft) - self.def_tot())
               * (1 + int(self.attacker.atk_oil) * 0.05))

        if crit:
            dmg *= (1 + self.attacker.crit_dmg
                    - self.defender.crit_dmg_reduction)

        return dmg

    def elemental_damage(self, atk_eq):
        matchup = f"{self.attacker.type}>{self.defender.type}"
        res = (self.defender.res
               - self.attacker.res_reduction
               - self.attacker.res_reduction_pvp)

        return (self.atk_ele_tot(atk_eq)
                * (1 + elemental_bonus(matchup))
                * (1 - res))

    def final_damage(self, atk_eq, crit=False, soft=False):
        morale = self.attacker.morale() - self.defender.morale()
        print("morale:", morale)

        dmg = ((self.physical_damage(atk_eq, crit=crit, soft=soft) + morale)
               + self.elemental_damage(atk_eq)
               + self.attacker.mob_damage())

        dmg *= ((1 + self.attacker.atk_pvp_book)
                * (1 + self.attacker.atk_pvp_hono)
                * (1 - self.defender.def_pvp_book)
                * (1 - self.defender.def_pvp_hono)
                * (1 - self.defender.magic_dmg_reduction)
                * (1 + self.attacker.atk_hat
                   + self.attacker.atk_pet
                   + int(self.attacker.atk_pot) * 0.2))

        return dmg

    def damage(self, crit=False, soft=False, average=False):
        dmg_min = self.final_damage(
            self.attacker.atk_equip_min,
            crit=crit,
            soft=soft
        )
        dmg_max = self.final_damage(
            self.attacker.atk_equip_max,
            crit=crit,
            soft=soft
        )

        dmg_min = max(dmg_min, 1)
        dmg_max = max(dmg_max, 5)

        # TODO: increase crits min damage

        if average:
            return (dmg_min + dmg_max) / 2

        return dmg_min, dmg_max
