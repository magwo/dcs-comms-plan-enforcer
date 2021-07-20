import dcs
from dcs.flyingunit import FlyingUnit
from dcs.unitgroup import PlaneGroup
from comms_plan import UHF_PLAN, VIGGEN_PLAN, INTRA_PLAN


def handle_plane_group(group: PlaneGroup) -> int:
    """ Returns number of units updated """
    intra = INTRA_PLAN.get(group.name) or None

    num_updated = 0
    # if intra:
    #     print("Group {} has intra {}".format(group.name, intra))

    for unit in group.units:
        if unit.type == "AJS37":
            handle_ajs37(unit, intra)
            num_updated += 1
        elif unit.type == "F-16C_50":
            handle_f_16c_50(unit, intra)
            num_updated += 1
        elif unit.type == "FA-18C_hornet":
            handle_fa_18c(unit, intra)
            num_updated += 1
        elif unit.type == "F-14B":
            handle_f_14b(unit, intra)
            num_updated += 1
        elif unit.type == "A-10C_2":
            handle_a10c2(unit, intra)
            num_updated += 1
        
        # TODO: Handle else: generic uhf capable like harrier etc
    
    return num_updated


def handle_ajs37(unit: FlyingUnit, intra: tuple[float, float]):
    for i in range(0, len(VIGGEN_PLAN)):
        chanNum = i + 1
        unit.set_radio_channel_preset(1, chanNum, VIGGEN_PLAN[i])

def handle_f_16c_50(unit: FlyingUnit, intra: tuple[float, float]):
    handle_generic_uhf_preset_capable(unit, 1, 1)
    if intra:
        unit.set_radio_channel_preset(2, 1, intra[1])

def handle_fa_18c(unit: FlyingUnit, intra: tuple[float, float]):
    handle_generic_uhf_preset_capable(unit, 1, 1)
    if intra:
        unit.set_radio_channel_preset(2, 1, intra[0])

def handle_f_14b(unit: FlyingUnit, intra: tuple[float, float]):
    handle_generic_uhf_preset_capable(unit, 1, 1)
    if intra:
        unit.set_radio_channel_preset(2, 1, intra[0])

def handle_a10c2(unit: FlyingUnit, intra: tuple[float, float]):
    handle_generic_uhf_preset_capable(unit, 1, 1)
    if intra:
        unit.set_radio_channel_preset(2, 1, intra[0])


def handle_generic_uhf_preset_capable(unit: FlyingUnit, radioNum: int, chanNumOffset: int):
    for i in range(0, len(UHF_PLAN)):
        chanNum = i + chanNumOffset
        # print("Setting freq", chanNum, UHF_PLAN[i])
        unit.set_radio_channel_preset(radioNum, chanNum, UHF_PLAN[i])