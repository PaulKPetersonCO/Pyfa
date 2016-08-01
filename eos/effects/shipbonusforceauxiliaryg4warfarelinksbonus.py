# shipBonusForceAuxiliaryG4WarfareLinksBonus
#
# Used by:
# Ship: Ninazu
type = "passive"
def handler(fit, src, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Skirmish Warfare Specialist"), "commandBonus", src.getModifiedItemAttr("shipBonusForceAuxiliaryG4"), skill="Gallente Carrier")
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Armored Warfare Specialist"), "commandBonus", src.getModifiedItemAttr("shipBonusForceAuxiliaryG4"), skill="Gallente Carrier")
