import subprocess
import optparse
def input():
    parse = optparse.OptionParser()
    parse.add_option("-i", "--interface", dest="interface", help="interface changing")
    parse.add_option("-m", "--mac", dest="mac_address", help="new mac address")
    return parse.parse_args()

def mac(inter, mac_addres):
    subprocess.call(["ifconfig", inter, "down"])
    subprocess.call(["ifconfig", inter, "hw", "ether", mac_addres])
    subprocess.call(["ifconfig", inter, "up"])


(userInput, arguments) = input()
mac(userInput.interface, userInput.mac_address)
print("You changed mac adress!")
