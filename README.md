
# Mac Address Changer

MAC spoofing or MAC Address Changer is a technique for changing a factory-assigned Media Access Control (MAC) of a Network Interface on a networked device. The MAC address that is hard-coded on a Network Interface controller (NIC) cannot be changed. However, many drivers allow the MAC address to be changed. Additionally, there are tools which can make an operating system believe that the NIC has the MAC address of a user's choosing. The process of masking a MAC address is known as MAC spoofing. Essentially, MAC spoofing entails changing a computer's identity, for any reason.

# What is MAC (Media Access Control) Address?
A MAC (Media Access Control) address is a unique 48-bit identifier assigned to a network interface controller (NIC). It is crucial for network communication, facilitating the delivery of data packets within Ethernet networks. Typically represented as six pairs of hexadecimal digits, the MAC address is hardcoded by the manufacturer, identifying the device on the network. Unlike IP addresses, which are logical, MAC addresses are tied to the device's hardware.

# Why do we need to change MAC Address?
* Conceal Device Identity: Masking the device's identity assists in keeping it hidden.
* Evasion of Tracking: Changing the MAC address helps users avoid tracking or tracing of device activities
* Network Access Bypass: Enables entry into networks restricted to specific MAC addresses by altering the device's MAC address.

# Clone

    git clone https://github.com/RoyTonmoy/mac-address-changer.git

# Usage
python3 mac_changer.py --help


usage: mac_changer.py [-h] [-i INTERFACE] [-m NEW_MAC]

options:
  -h, --help            show this help message and exit
  
  -i INTERFACE, --interface INTERFACE
                        Interface name to change Mac Address
  
  -m NEW_MAC, --mac NEW_MAC
                        new mac address

N.B. Mac address should be stated with 00 and run with sudo access

# Tested Distro

Debian (kali , Ubuntu)

## 🔗 Links

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/tonmoy-roy11/)


