import csv
from jinja2 import Environment, FileSystemLoader

non_custom_keys = [
    "hostname",
    "ip",
    "username",
    "password",
    "protocol",
    "os",
    "enable_password",
    "platform"
    ]

devices = []
with open("tb.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        custom = [{k: v} for k,v in row.items() if k not in non_custom_keys]
        row["custom"] = custom
        devices.append(row)

with open("testbed.yml", "w") as tb:
    env = Environment(loader=FileSystemLoader("."), trim_blocks=True, lstrip_blocks=True)
    tmplt = env.get_template("testbed.j2")
    tb.write(tmplt.render(devices=devices))