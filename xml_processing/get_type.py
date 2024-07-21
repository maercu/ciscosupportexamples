import xmltodict
import xml.etree.ElementTree as ET
import json

ns = {"intfs_iosxe": "http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper"}

#xml_file = "data_multichilds.xml"
xml_file = "data_singlechild.xml"

with open(xml_file) as fo:
    xml_content = fo.read()
    print("\nRAW XML data")
    print("="*40)
    print(xml_content)

print("\nxmltodict")
print("="*40)
xml_dict = xmltodict.parse(xml_content)
print(json.dumps(xml_dict, indent=2))
print(type(xml_dict.get("data").get("interfaces").get("interface")))
print(len(xml_dict.get("data").get("interfaces").get("interface")))

print("\nxml.etree.ElementTree")
print("="*40)
tree = ET.parse(xml_file)
root = tree.getroot()
print(type(root.findall(".//intfs_iosxe:interface", ns)))
print(len(root.findall(".//intfs_iosxe:interface", ns)))