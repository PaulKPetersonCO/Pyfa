# shipBonusEnergyNeutOptimalAB
#
# Used by:
# Ship: Armageddon
type = "passive"


def handler(fit, src, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Energy Neutralizer", "maxRange",
                                  src.getModifiedItemAttr("shipBonusAB"), skill="Amarr Battleship")
