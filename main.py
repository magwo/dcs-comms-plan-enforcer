from util import print_bold, print_warning
from enforcer import Enforcer
import dcs
import sys
import json
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

filename = filedialog.askopenfilename(title="Select mission file", filetypes=[('Mission files', '.miz')])

if not filename:
    sys.exit()

m = dcs.Mission()
print("Attempting to load mission file", filename)
m.load_file(filename)
print("Loaded mission file", filename)


num_updated = 0
comms_plan_filename = filedialog.askopenfilename(title="Select comms plan JSON file", filetypes=[('JSON files', '.json')])
with open(comms_plan_filename, "r") as f:
    json_content = f.read()
    all_comms_plans = json.loads(json_content)

    for coalition_name in m.coalition:
        comms_plan = all_comms_plans.get(coalition_name)

        if comms_plan:
            print_bold("Found comms plan for {}".format(coalition_name))
            enforcer = Enforcer(comms_plan=comms_plan)

            for country_name in m.coalition[coalition_name].countries:
                country = m.coalition[coalition_name].countries[country_name]

                for planeGroup in country.plane_group:
                    num_updated += enforcer.handle_group(planeGroup)
                for heliGroup in country.helicopter_group:
                    num_updated += enforcer.handle_group(heliGroup)
        else:
            print_bold("No comms plan found for {}".format(coalition_name))

print_bold("{} units were updated/enforced".format(num_updated))
if enforcer.accumulated_errors > 0:
    print_warning(f"There were {enforcer.accumulated_errors} incorrects")
else:
    print_bold("MISSION CHECKS OUT")

out_filename = filedialog.asksaveasfilename(title="Save enforced mission as", filetypes=[('Mission files', '.miz')])

if out_filename:
    print("Attempting to save to {}...".format(out_filename))
    m.save(out_filename)
    print("Saved to {}".format(out_filename))
else:
    print("Dry run was completed")

input("Press Enter to continue...")
