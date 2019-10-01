
from scapy.all import *

interface = "wlan1mon"

ap_list = []

def PacketHandler(packet) :
    if packet.haslayer(Dot11) :
        if packet.type == 0 and packet.subtype == 8:
            if packet.addr2 not in ap_list:
                ap_list.append(packet.addr2)
                print("Access Point MAC: %s with SSID: %s " %(packet.addr2, packet.info))
                print(type(packet.info))
                if packet.info.decode("utf-8") == "airEAFIT":
                    print("JAJAXD")

print("[*] Start sniffing…")
sniff(iface=interface, prn=PacketHandler,  store=0)
print("[*] Stop sniffing…")
