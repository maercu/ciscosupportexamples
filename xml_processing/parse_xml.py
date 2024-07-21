import xml.etree.ElementTree as ET

tree = ET.parse("xml_output_1.xml")
root = tree.getroot()

# for itr in root.iter():
#     print(itr.tag)

ns = {"intfs_iosxe": "http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper"}

for intf in root.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}interface"):
    print(intf.tag)

ns = {"ios_intf_oper":"http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper"}

# for intf in root.findall(".//ios_intf_oper:interface", ns):
#     print(intf.find("ios_intf_oper:name", ns).text, intf.find("ios_intf_oper:oper-status", ns).text)