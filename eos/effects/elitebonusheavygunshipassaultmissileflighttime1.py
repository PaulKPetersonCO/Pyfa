# eliteBonusHeavyGunshipAssaultMissileFlightTime1
#
# Used by:
# Ship: Cerberus
type = "passive"


def handler(fit, ship, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Heavy Assault Missiles"),
                                    "explosionDelay", ship.getModifiedItemAttr("eliteBonusHeavyGunship1"),
                                    skill="Heavy Assault Cruisers")
