#!/usr/bin/env python3

import subprocess
import argparse
import re


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface", help="Interface name to change Mac Address")
    parser.add_argument("-m", "--mac", dest="new_mac", help="new mac address")
    args = parser.parse_args()

    if not args.interface: 
        parser.error("[-] Please specify an interface, use --help for more info")
    elif not args.new_mac:
        parser.error("[-] Please .interfacespecify a new mac, use --help for more info ")
    
    return args

def mac_address_changer(interface, new_mac): 
    print(f"[+] Changing Mac address for {interface} to {new_mac} \n")
    subprocess.run(["ifconfig", interface, "down"])
    subprocess.run(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.run(["ifconfig", interface, "up"])


def get_current_mac_address(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    ifconfig_result = ifconfig_result.decode("utf-8")
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] could not read MAC Address")


args = get_arguments()
current_mac = get_current_mac_address(args.interface)
print("current mac: ", current_mac)

mac_address_changer(args.interface, args.new_mac)
current_mac = get_current_mac_address(args.interface)

if current_mac == args.new_mac:
    print(f"[+] Mac address was changed successfully to {current_mac}")
else:
    print(f"[-] Mac address didnot get changed")








