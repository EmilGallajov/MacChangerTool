import subprocess
import optparse
parse = optparse.OptionParser()
parse.add_option("-i", "--interface", dest="interface", help="interface changing")
parse.add_option("-m", "--mac", dest="mac_address", help="new mac address")

(inputs, arguments) = parse.parse_args()

inter = inputs.interface
mac_addres = inputs.mac_address

subprocess.call(["ifconfig", inter, "down"])
subprocess.call(["ifconfig", inter, "hw", "ether", mac_addres])
subprocess.call(["ifconfig", inter, "up"])

print("You changed mac adress!")

