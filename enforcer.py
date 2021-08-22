from os import name
from typing import List

from dcs.helicopters import Mi_24P, Mi_8MT, UH_1H
from dcs.unit import Skill
from util import fuzzy_find_by_name, print_bold, print_error, print_success, print_warning
from dataclasses import dataclass
from dcs.flyingunit import FlyingUnit
from dcs.unitgroup import HelicopterGroup, PlaneGroup
from dcs.planes import AJS37, A_10C, A_10C_2, F_16C_50, FA_18C_hornet, F_14B, AV8BNA, F_5E_3, JF_17, L_39C, L_39ZA, M_2000C, MiG_21Bis

supported_type_ids = [
    AJS37.id,
    F_16C_50.id,
    FA_18C_hornet.id,
    F_14B.id,
    # A_10C.id,
    # A_10C_2.id,
    AV8BNA.id,
    F_5E_3.id,
    L_39C.id,
    L_39ZA.id,
    UH_1H.id,
    Mi_24P.id,
    Mi_8MT.id,
    MiG_21Bis.id,
    JF_17.id,
    M_2000C.id
]

zero_indexed_type_ids = [
    MiG_21Bis.id,
    L_39C.id,
    L_39ZA.id,
    Mi_24P.id,
]

double_uhf_type_ids = [
    FA_18C_hornet.id,
    F_14B.id,
    AV8BNA.id,
]

vhf_secondary_type_ids = [
    F_16C_50.id,
    A_10C.id,
    A_10C_2.id,
    M_2000C.id
]

def get_radio_ch_index_for_plan_index(type_id: str, plan_index: int) -> int:
    if type_id in zero_indexed_type_ids:
        if plan_index < 19:
            return plan_index + 2
        else:
            return 1
    else:
        return plan_index + 1

@dataclass
class IntraFrequencies:
    uhf: float
    vhf: float
    # TODO: Use this class

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
    
    # TODO: Put check and enforce in same functions
    def handle_group(self, group: PlaneGroup or HelicopterGroup) -> int:
        """ Returns number of units updated """
        intra = fuzzy_find_by_name(self.intra_plan, group.name)
        # if intra:
        #     print(f"Group {group.name} has intra freq {intra}")

        handled_as_ai = self.handle_ai_group_if_applicable(group)
        if not handled_as_ai:
            self.check_and_set_group_frequency(group)

        num_updated = 0
        previously_skipped_type = None
        for unit in group.units:
            if unit.type in supported_type_ids:
                # print(f"Unit {unit.type} has {len(unit.radio)} radios", unit.radio)
                uhf_primary_ok = self.check_uhf_primary(unit)
                intra_ok = self.check_intra_if_applicable(unit, intra)
                if not uhf_primary_ok or not intra_ok:
                    print_bold(f"Enforcing channels of {unit.type} {unit.name}")
                    num_updated += 1
                    if unit.type == AJS37.id:
                        self.handle_ajs37(unit, intra)
                    elif unit.type in vhf_secondary_type_ids:
                        self.handle_uhf_vhf_capable(unit, intra)
                    elif unit.type in double_uhf_type_ids:
                        self.handle_double_uhf_capable(unit, intra)
                    else:
                        self.handle_single_uhf_only_capable(unit)

            elif previously_skipped_type != unit.type:
                print("Unit type {} not supported, skipping".format(unit.type))
                previously_skipped_type = unit.type
        
        return num_updated

    def check_and_set_group_frequency(self, group: PlaneGroup or HelicopterGroup):
        if len(group.units) > 0:
            if group.units[0].type == AJS37.id:
                frequency = self.viggen_plan[0]
            elif group.units[0].type in zero_indexed_type_ids:
                frequency = self.uhf_plan[-1]
            else:
                frequency = self.uhf_plan[0]

            if group.frequency != frequency:
                print_warning(f"Incorrect group frequency ({group.frequency}) for {group.name}")
                print_bold(f"Setting {group.name} group frequency to {frequency}")
                group.frequency = frequency
                self.accumulated_errors += 1
            else:
                print_success(f"{group.name} has correct group frequency {group.frequency}")

    def check_uhf_primary(self, unit: FlyingUnit) -> bool:
        """Returns True if unit has correct presets already"""
        numIncorrect = 0
        try:
            uhf_primary_radio = unit.radio[1]
            channels = uhf_primary_radio.get("channels")
            
            if unit.type == "AJS37":
                expectedChannels = self.viggen_plan
            else:
                expectedChannels = self.uhf_plan

            for i in range(0, len(expectedChannels)):
                chanNum = get_radio_ch_index_for_plan_index(unit.type, i)
                if channels.get(chanNum):
                    if channels.get(chanNum) != expectedChannels[i]:
                        numIncorrect += 1
                        self.accumulated_errors += 1
                        print_warning(f"{unit.type} {unit.name} incorrect channel {chanNum}: {channels[chanNum]} should be {expectedChannels[i]}")
                    else:
                        pass
                        #print(f"{unit.name} correct channel {chanNum}: {channels[chanNum]} should be {expectedChannels[i]}")
                else:
                    if unit.type not in zero_indexed_type_ids:
                        print_error(f"{unit.name} unexpectedly missing channel {chanNum}")
            if numIncorrect > 0:
                print_warning(f"{numIncorrect} incorrect channels for unit {unit.name}")
            else:
                print_success(f"{unit.type} {unit.name} has correct primary channels!")
        except (AttributeError, TypeError) as e:
            if unit.skill in [Skill.Player, Skill.Client]:
                print_warning(f"Unit {unit.name} of type {unit.type} with radio {unit.radio} not checkable, probably because A-10")
            return True

        return numIncorrect == 0

    def check_intra_if_applicable(self, unit: FlyingUnit, intra):
        if not intra:
            return True
        try:
            if unit.type in vhf_secondary_type_ids or unit.type in double_uhf_type_ids:
                intra_used = intra[0] if unit.type in double_uhf_type_ids else intra[1]
                secondary_radio = unit.radio.get(2)
                channels = secondary_radio.get("channels")
                if channels.get(1) == intra_used:
                    print_success(f"{unit.type} {unit.name} has correct intra {intra_used}!")
                else:
                    print_warning(f"{unit.type} {unit.name} has incorrect intra {channels[1]}, expected {intra_used}")
                    self.accumulated_errors += 1
                    return False
        except (AttributeError, TypeError) as e:
            print_warning(f"Could not check intra of {unit.name} of type {unit.type} with radio {unit.radio} probably because A-10 or AI controlled {e}")
        return True


    def handle_ai_group_if_applicable(self, group: PlaneGroup) -> bool:
        expected_frequency = fuzzy_find_by_name(self.ai_frequencies, group.name)
        if expected_frequency != None:
            if group.frequency != expected_frequency:
                print_warning(f"AI group {group.name} has wrong frequency {group.frequency}. Expected {expected_frequency}")
                print_bold(f"Setting frequency {expected_frequency} of AI group {group.name}")
                group.frequency(expected_frequency)
                self.accumulated_errors += 1
            else:
                print_success(f"AI group {group.name} has correct frequency {group.frequency}")
            return True
        return False


    def handle_ajs37(self, unit: FlyingUnit, intra: tuple[float, float]):
        for i in range(0, len(self.viggen_plan)):
            chanNum = i + 1
            unit.set_radio_channel_preset(1, chanNum, self.viggen_plan[i])

    def handle_uhf_vhf_capable(self, unit: FlyingUnit, intra: tuple[float, float]):
        self.handle_primary_uhf_radio(unit, 1)
        if intra:
            unit.set_radio_channel_preset(2, 1, intra[1])

    def handle_double_uhf_capable(self, unit: FlyingUnit, intra: tuple[float, float]):
        self.handle_primary_uhf_radio(unit, 1)
        if intra:
            unit.set_radio_channel_preset(2, 1, intra[0])

    def handle_single_uhf_only_capable(self, unit: FlyingUnit):
        self.handle_primary_uhf_radio(unit, 1)

    def handle_primary_uhf_radio(self, unit: FlyingUnit, radioNum: int):
        if not unit.radio or not unit.radio[radioNum]:
            print_warning(f"Unit {unit.name} has no radio {radioNum}, literally can't even :S")
            return
        uhf_plan = self.uhf_plan
        for i in range(0, len(uhf_plan)):
            chanNum = get_radio_ch_index_for_plan_index(unit.type, i)
            if chanNum <= unit.num_radio_channels(radioNum):
                print(f"Setting chan {chanNum} of radio {radioNum} ({uhf_plan[i]})")
                unit.set_radio_channel_preset(radioNum, chanNum, uhf_plan[i])