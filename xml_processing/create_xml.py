import xml.etree.ElementTree as ET
from ncclient import manager

ns = {
    "nc": "urn:ietf:params:xml:ns:netconf:base:1.0",
    "xe_native": "http://cisco.com/ns/yang/Cisco-IOS-XE-native"
}

intfs = {
    "Loopback": [
        {
            "name": "84",
            "description": "MZ-TEST1"
        },
        {
            "name": "90",
            "description": "MZ-TEST2"
        }
    ]
}

builder = ET.TreeBuilder()
builder.start("config", {"xmlns": ns.get("nc")})
builder.start("native", {"xmlns": ns.get("xe_native")})
builder.start("interface", {})
for intf_type, intf_cfgs in intfs.items():
    for intf_cfg in intf_cfgs:
        builder.start(intf_type, {})
        for k, v in intf_cfg.items():
            builder.start(k, {})
            builder.data(v)
            builder.end(k)
        builder.end(intf_type)

builder.end("interface")
builder.end("native")
builder.end("config")


root = ET.ElementTree(builder.close()).getroot()
ET.indent(root, space="\t", level=0)
xml_str = ET.tostring(root, encoding="unicode")
print(xml_str)
print(type(root))

host = "devnetsandboxiosxe.cisco.com"
username = "admin"
password = "C1sco12345"

with manager.connect(host=host, port=830, username=username, password=password, hostkey_verify=False, look_for_keys=False) as m:
    res = m.edit_config(xml_str, target="running")
    print(res.ok)



