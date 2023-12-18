from datetime import datetime
import time
from netmiko import ConnectHandler


host_list = "IPAddressList.txt"
username = "admin"
password = "xyz"
commands = [
    "show run",
    "show ip int br"
]

with open(host_list, "r") as fo:
    hosts = [host.strip() for host in fo.readlines()]

while True:
    for host in hosts:
        dev = {
            "device_type": "cisco_ios",
            "host": host,
            "username": username,
            "password": password,
        }
        with open(f"output_{datetime.now().strftime('%Y-%m-%d_%H:%M')}_{host}.txt", "w") as fo:
            try:
                with ConnectHandler(**dev) as net_connect:
                    for cmd in commands:
                        print(f"=== Get {cmd} on {host} ===")
                        output = net_connect.send_command(cmd)
                        print(output)
                        fo.write(f"=== Get {cmd} on {host} ===\n")
                        fo.write(output)
            except Exception as e:
                fo.write(f"=== ERROR connecting to {host}\n{e}\n")

    time.sleep(3600)