from handlers import handle_plane_group
import dcs
import sys

from dcs import countries
from dcs.unitgroup import PlaneGroup

from comms_plan import UHF_PLAN, VIGGEN_PLAN, INTRA_PLAN

m = dcs.Mission()

print(sys.argv)

if len(sys.argv) < 2:
    print("#                                           #")
    print("# Usage: provide .miz filename to modify    #")
    print("#                                           #")
    sys.exit(1)

filename = sys.argv[1]
print("Attempting to load mission file", filename)
m.load_file(filename)


def processUnit(plane_or_helicopter: PlaneGroup):
    return


# for coalition in m.coalition:
#     print(coalition)

num_updated = 0
for country_id in m._COUNTRY_IDS:
    country = m.country_by_id(country_id)

    if country:
        for group in country.plane_group:
            # print("Group", group)
            num_updated += handle_plane_group(group)
            # for unit in group.units:
            #     print("Unit type", unit.type)

print("{} units were updated/enforced".format(num_updated))

if len(sys.argv) >= 3:
    out_filename = sys.argv[2]
    print("Attempting to save to {}...".format(out_filename))
    m.save(out_filename)
    print("Saved to {}".format(out_filename))
else:
    print("Dry run was completed")