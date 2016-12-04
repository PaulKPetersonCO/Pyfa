# covertOpsCloakCpuPercentBonus1
#
# Used by:
# Ships from group: Covert Ops (5 of 6)
type = "passive"
runTime = "early"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Cloaking"),
                                  "cpu", ship.getModifiedItemAttr("eliteBonusCoverOps1"), skill="Covert Ops")
