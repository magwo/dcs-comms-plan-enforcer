from util import print_bold, print_warning
from enforcer import Enforcer
import dcs
import sys
import json


if len(sys.argv) < 2:
    print("#                                           #")
    print("# Usage: provide .miz filename to modify    #")
    print("#                                           #")
    sys.exit(1)

filename = sys.argv[1]
m = dcs.Mission()
print("Attempting to load mission file", filename)
m.load_file(filename)
print("Loaded mission file", filename)


num_updated = 0
with open("comms_plan.json", "r") as f:
    json_content = f.read()
    all_comms_plans = json.loads(json_content)

    for coalition_name in m.coalition:
        comms_plan = all_comms_plans.get(coalition_name)

        if comms_plan:
            print("Found comms plan for {}".format(coalition_name))
            enforcer = Enforcer(comms_plan=comms_plan)

            for country_name in m.coalition[coalition_name].countries:
                country = m.coalition[coalition_name].countries[country_name]

                for planeGroup in country.plane_group:
                    num_updated += enforcer.handle_group(planeGroup)
                for heliGroup in country.helicopter_group:
                    num_updated += enforcer.handle_group(heliGroup)
        else:
            print("No comms plan found for {}".format(coalition_name))

print("{} units were updated/enforced".format(num_updated))
if enforcer.accumulated_errors > 0:
    print_warning(f"There were {enforcer.accumulated_errors} incorrects")
else:
    print_bold("MISSION CHECKS OUT")

if len(sys.argv) >= 3:
    out_filename = sys.argv[2]
    print("Attempting to save to {}...".format(out_filename))
    m.save(out_filename)
    print("Saved to {}".format(out_filename))
else:
    print("Dry run was completed")