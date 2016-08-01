# moduleBonusMiningForemanLinkMiningLaserFieldEnhancement
#
# Used by:
# Variations of module: Mining Foreman Link - Mining Laser Field Enhancement I (2 of 2)
type = "gang", "active"
gangBoost = "miningMaxRange"
def handler(fit, module, context):
    if "gang" not in context: return
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Gas Cloud Harvesting") or mod.item.requiresSkill("Ice Harvesting") or mod.item.requiresSkill("Mining"),
                                  "maxRange", module.getModifiedItemAttr("commandBonus"),
                                  stackingPenalties = True)
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("CPU Management"),
                                  "surveyScanRange", module.getModifiedItemAttr("commandBonus"))
