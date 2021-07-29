from os import name

from dcs.helicopters import Mi_24P, Mi_8MT, UH_1H
from util import fuzzy_find_by_name, print_bold, print_success, print_warning
from dataclasses import dataclass
from dcs.flyingunit import FlyingUnit
from dcs.unitgroup import HelicopterGroup, PlaneGroup
from dcs.planes import AJS37, F_16C_50, FA_18C_hornet, F_14B, A_10C, A_10C_2, AV8BNA, JF_17, L_39C, L_39ZA, M_2000C, MiG_21Bis

supported_type_ids = [
    AJS37.id,
    F_16C_50.id,
    FA_18C_hornet.id,
    F_14B.id,
    A_10C.id,
    A_10C_2.id,
    AV8BNA.id,
    L_39C.id,
    L_39ZA.id,
    UH_1H.id,
    Mi_24P.id,
    Mi_8MT.id,
    MiG_21Bis.id,
    JF_17.id,
    M_2000C.id
]

@dataclass
class Enforcer:
    comms_plan: dict
    accumulated_errors = 0

    @property
    def uhf_plan(self):
        return self.comms_plan.get("uhf", [])

    @property
    def intra_plan(self):
        return self.comms_plan.get("intra", {})

    @property
    def viggen_plan(self):
        return self.comms_plan.get("viggen", [])
    
    @property
    def ai_frequencies(self):
        return self.comms_plan.get("ai_frequencies", {})

    def handle_group(self, group: PlaneGroup or HelicopterGroup) -> int:
        """ Returns number of units updated """
        intra = fuzzy_find_by_name(self.intra_plan, group.name)
        # if intra:
        #     print(f"Group {group.name} has intra freq {intra}")

        self.handle_ai_group_if_applicable(group)

        num_updated = 0
        previously_skipped_type = None
        for unit in group.units:
            if unit.type in supported_type_ids:
                print()
                self.check_unit(unit)

                print_bold(f"Enforcing channels of {unit.type} {unit.name}")
                num_updated += 1
                if unit.type == "AJS37":
                    self.handle_ajs37(unit, intra)
                elif unit.type == "F-16C_50":
                    self.handle_uhf_vhf_capable(unit, intra)
                elif unit.type == "FA-18C_hornet":
                    self.handle_double_uhf_capable(unit, intra)
                elif unit.type == "F-14B":
                    self.handle_double_uhf_capable(unit, intra)
                elif unit.type == "AV8BNA":
                    self.handle_double_uhf_capable(unit, intra)
                elif unit.type == "A-10C_2":
                    # TODO: See if it works
                    self.handle_uhf_vhf_capable(unit, intra)
                elif unit.type == "A-10C":
                    # TODO: See if it works
                    self.handle_uhf_vhf_capable(unit, intra)
            elif previously_skipped_type != unit.type:
                print("Unit type {} not supported, skipping".format(unit.type))
                previously_skipped_type = unit.type
        
        return num_updated

    def check_unit(self, unit: FlyingUnit):
        print(f"Checking unit {unit.name} of type {unit.type}")
        try:
            uhf_primary_radio = unit.radio[1]
            # print("Radio 1 is", uhf_primary_radio)
            channels = uhf_primary_radio.get("channels")
            
            if unit.type == "AJS37":
                expectedChannels = self.viggen_plan
            else:
                expectedChannels = self.uhf_plan

            numIncorrect = 0
            for i in range(0, len(expectedChannels)):
                chanNum = i + 1
                if channels[chanNum] != expectedChannels[i]:
                    numIncorrect += 1
                    self.accumulated_errors += 1
                    print_warning(f"Incorrect channel {chanNum}: {channels[chanNum]} should be {expectedChannels[i]}")
            if numIncorrect > 0:
                print_warning(f"{numIncorrect} incorrect channels for unit {unit.name}")
            else:
                print_success(f"Unit {unit.name} has correct primary channels!")

        except (AttributeError, TypeError) as e:
            print_warning(f"Unit {unit.name} of type {unit.type} with radio {unit.radio} not checkable, probably because A-10 or AI controlled")


    def handle_ai_group_if_applicable(self, group: PlaneGroup):
        expected_frequency = fuzzy_find_by_name(self.ai_frequencies, group.name)
        if expected_frequency != None:
            if group.frequency != expected_frequency:
                print_warning(f"AI group {group.name} has wrong frequency. Expected {expected_frequency}")
                print_bold(f"Setting frequency {expected_frequency} of AI group {group.name}")
                self.accumulated_errors += 1
            else:
                print_success(f"AI group {group.name} has correct frequency {group.frequency}")


    def handle_ajs37(self, unit: FlyingUnit, intra: tuple[float, float]):
        for i in range(0, len(self.viggen_plan)):
            chanNum = i + 1
            unit.set_radio_channel_preset(1, chanNum, self.viggen_plan[i])

    def handle_uhf_vhf_capable(self, unit: FlyingUnit, intra: tuple[float, float]):
        self.handle_generic_uhf_preset_capable(unit, 1, 1)
        if intra:
            unit.set_radio_channel_preset(2, 1, intra[1])

    def handle_double_uhf_capable(self, unit: FlyingUnit, intra: tuple[float, float]):
        self.handle_generic_uhf_preset_capable(unit, 1, 1)
        if intra:
            unit.set_radio_channel_preset(2, 1, intra[0])

    def handle_generic_uhf_preset_capable(self, unit: FlyingUnit, radioNum: int, chanNumOffset: int):
        uhf_plan = self.uhf_plan
        for i in range(0, len(uhf_plan)):
            chanNum = i + chanNumOffset
            # print("Setting freq", chanNum, uhf_plan[i])
            unit.set_radio_channel_preset(radioNum, chanNum, uhf_plan[i])