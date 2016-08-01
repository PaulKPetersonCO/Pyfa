# titanCaldariMissileKineticDmg2
#
# Used by:
# Ship: Leviathan
type = "passive"
def handler(fit, ship, context):
    groups = ("XL Torpedo", "XL Cruise Missile")
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.group.name in groups,
                                    "kineticDamage", ship.getModifiedItemAttr("shipBonusCT1"), skill="Caldari Titan")
