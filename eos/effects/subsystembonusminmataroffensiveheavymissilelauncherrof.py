# subsystemBonusMinmatarOffensiveHeavyMissileLauncherROF
#
# Used by:
# Subsystem: Loki Offensive - Hardpoint Efficiency Configuration
type = "passive"


def handler(fit, module, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Missile Launcher Heavy",
                                  "speed", module.getModifiedItemAttr("subsystemBonusMinmatarOffensive"),
                                  skill="Minmatar Offensive Systems")
