from typing import Dict
import dcs
from dataclasses import dataclass
from dcs.flyingunit import FlyingUnit
from dcs.unitgroup import PlaneGroup

supported_types = [
    "AJS37",
    "F-16C_50",
    "FA-18C_hornet",
    "F-14B",
    "A-10C_2",
    "AV8BNA",
    # TODO: Add more
]

@dataclass
class Enforcer:
    comms_plan: Dict

    @property
    def uhf_plan(self):
        return self.comms_plan.get("uhf", [])

    @property
    def intra_plan(self):
        return self.comms_plan.get("intra", {})

    @property
    def viggen_plan(self):
        return self.comms_plan.get("viggen", [])

    def handle_plane_group(self, group: PlaneGroup) -> int:
        """ Returns number of units updated """
        intra = self.intra_plan.get(group.name)
            
        if intra:
            print("Assigning intra {} to flight {}".format(intra, group.name))

        num_updated = 0
        previously_skipped_type = None
        for unit in group.units:
            if unit.type in supported_types:
                print("Updating/enforcing {} {}".format(unit.type, unit.name))
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
            elif previously_skipped_type != unit.type:
                print("Unit type {} not supported, skipping".format(unit.type))
                previously_skipped_type = unit.type
        
        return num_updated


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