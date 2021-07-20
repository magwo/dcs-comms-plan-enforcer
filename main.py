import dcs
import sys

from dcs import countries
from dcs.unitgroup import PlaneGroup

from comms_plan import UHF_PLAN, VIGGEN_PLAN, INTRA_PLAN

m = dcs.Mission()

if len(sys.argv) < 2:
    print("#                                           #")
    print("# Usage: provide .miz filename to modify    #")
    print("#                                           #")
    sys.exit(1)

filename = sys.argv[1]
print("Attempting to load mission file", filename)
load_result = m.load_file(filename)
# print("Load result", load_result)


def processUnit(plane_or_helicopter: PlaneGroup):
    return


for coalition in m.coalition:
    print(coalition)

for country_id in m._COUNTRY_IDS:
    country = m.country_by_id(country_id)
    
    if country:
        for group in country.plane_group:
            print("Group", group)
            for unit in group.units:
                # print("Unit type", unit.type)
                if unit.type == "AJS37":
                    print("Unit type", unit.type)
                    print("Radio", unit.radio)
                    unit.set_radio_channel_preset(1, 1, 265.25)
            
        # for plane in country.planes:
        #     print("Plane", plane)

# m.save("output.miz")