import xml.etree.ElementTree as ET

# Load XML data into ET
tree = ET.parse("xml_output.xml")
root = tree.getroot()

# Iterate over the tree
for itr in root.iter():
    print(itr.tag)

# Search for all interface tags, search for name + oper-status tag and print the text of these elements
for intf in root.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}interface"):
    print(intf.find("{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}name").text)
    print(intf.find("{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}oper-status").text)
    print()

# Same as above, but use a namespace dict
ns = {"ios_intf_oper":"http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper"}

for intf in root.findall(".//ios_intf_oper:interface", ns):
    print(intf.find("ios_intf_oper:name", ns).text)
    print(intf.find("ios_intf_oper:oper-status", ns).text)
    print()