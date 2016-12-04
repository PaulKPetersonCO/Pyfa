# shipBonusThermMissileDmgMD1
#
# Used by:
# Ship: Bifrost
type = "passive"


def handler(fit, src, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Missile Launcher Operation"), "thermalDamage",
                                    src.getModifiedItemAttr("shipBonusMD1"), skill="Minmatar Destroyer")
