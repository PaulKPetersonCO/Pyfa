# drawbackCPUOutput
#
# Used by:
# Modules from group: Rig Drones (58 of 64)
type = "passive"
def handler(fit, module, context):
    fit.ship.boostItemAttr("cpuOutput", module.getModifiedItemAttr("drawback"))