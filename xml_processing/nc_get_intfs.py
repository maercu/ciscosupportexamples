from ncclient import manager
import xml.dom.minidom
import xmltodict

if __name__ == '__main__':
    host = "devnetsandboxiosxe.cisco.com"
    username = "admin"
    password = "C1sco12345"

    ns = {"interfaces-ios-xe-oper": "http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper"}
    #xpath_ = "/interfaces-ios-xe-oper:interfaces/interfaces-ios-xe-oper:interface[name='GigabitEthernet1']/interfaces-ios-xe-oper:oper-status"
    xpath_ = "/interfaces-ios-xe-oper:interfaces/interfaces-ios-xe-oper:interface/interfaces-ios-xe-oper:oper-status"

    with manager.connect(host=host, port=830, username=username, password=password, hostkey_verify=False,
                                  look_for_keys=False) as m:
        c = m.get(filter=('xpath', (ns, xpath_)))

        print("\n\nXML")
        print(xml.dom.minidom.parseString(c.data_xml).toprettyxml())

        print("\nXML/xml.etree.ElementTree.Element")
        for intf in c.data.findall(".//interfaces-ios-xe-oper:interface", ns):
            print(intf.find("interfaces-ios-xe-oper:name", ns).text, intf.find("interfaces-ios-xe-oper:oper-status", ns).text)

        print("\nJSON/xmltodict")
        for intf in xmltodict.parse(c.data_xml).get("data").get("interfaces").get("interface"):
            print(intf.get("name"), intf.get("oper-status"))

  