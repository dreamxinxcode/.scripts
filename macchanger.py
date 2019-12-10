from subprocess import call
import psutil

print("\033[95m")
print("• ▌ ▄ ·.  ▄▄▄·  ▄▄·      ▄▄·  ▄ .▄ ▄▄▄·  ▐ ▄  ▄▄ • ▄▄▄ .▄▄▄")
print("·██ ▐███▪▐█ ▀█ ▐█ ▌▪    ▐█ ▌▪██▪▐█▐█ ▀█ •█▌▐█▐█ ▀ ▪▀▄.▀·▀▄ █·")
print("▐█ ▌▐▌▐█·▄█▀▀█ ██ ▄▄    ██ ▄▄██▀▐█▄█▀▀█ ▐█▐▐▌▄█ ▀█▄▐▀▀▪▄▐▀▀▄")
print("██ ██▌▐█▌▐█ ▪▐▌▐███▌    ▐███▌██▌▐▀▐█ ▪▐▌██▐█▌▐█▄▪▐█▐█▄▄▌▐█•█▌")
print("▀▀  █▪▀▀▀ ▀  ▀ ·▀▀▀     ·▀▀▀ ▀▀▀ · ▀  ▀ ▀▀ █▪·▀▀▀▀  ▀▀▀ .▀  ▀")


addrs = psutil.net_if_addrs()

for interface in addrs.keys():
    call(["sudo", "ip", "link", "set", str(interface), "down"])
    print("Setting \033[1m\033[96m{}\033[0m down..".format(interface))
    wait(2000)


for interface in addrs.keys():
    print(
        "Randomizing \033[1m\033[96m{}\033[0m MAC address..".format(interface))
    call(["sudo", "macchanger", "-r", interface])

for interface in addrs.keys():
    print("Bringing \033[1m\033[96m{}\033[0m back up..".format(interface))
    call(["sudo", "ip", "link", "set", interface, "up"])
