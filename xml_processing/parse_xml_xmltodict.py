import xmltodict
import json

# Read XML content from file
with open("xml_output_2.xml", "r") as fo:
    xml = fo.read()

# parse it using xmltodict
parsed_xml = xmltodict.parse(xml)

# print the type of the 
print(type(parsed_xml))

# pretty print the data using json.dumps
print(json.dumps(parsed_xml, indent=1))

# print interface name and oper state for all interfaces
for intf in parsed_xml.get("data").get("interfaces").get("interface"):
    print(intf.get("name"), intf.get("oper-status"))