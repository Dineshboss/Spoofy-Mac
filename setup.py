#! /usr/bin/python
import subprocess
import optparse
import re
def argument():
    parser =optparse.OptionParser()
    parser.add_option("-i","--interface",dest="interface",help="Interface to change its mac address")
    parser.add_option("-m","--mac",dest="mac_new",help="New_mac")
    (options,arguments)=parser.parse_args()
    if not options.interface:
        parser.error("please specify the interface")
    elif not options.mac_new:
        parser.error("please specify the mac address")
    return(options)

def mac_changer(interface,mac_new):
   subprocess.call(["ifconfig" ,  interface  ,  "down"])
   subprocess.call(["ifconfig" ,  interface  ,  "hw" ,  "ether" ,  mac_new])
   subprocess.call(["ifconfig" ,  interface  ,  "up"])
def out(interface):
    mac_address = subprocess.check_output(["ifconfig", interface])
    mac_address_changer = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", mac_address)
    return(mac_address_changer.group(0))
options=argument()
mac_add=mac_changer(options.interface,options.mac_new)
current_mac=out(options.interface)
print(options.interface)
if options.mac_new==current_mac:
         print("[+] operation is successful")
         print(current_mac)
else:
         print("[+] operation is not successful")




