from scapy.all import sniff, ARP
from detector import check_arp
from scanner import arp_scan

arp_scan()

print("ARP MONITOR AKTİF")

def process(pkt):
    if pkt.haslayer(ARP):
        check_arp(pkt.psrc, pkt.hwsrc)

sniff(filter="arp", prn=process, store=0)

def process(pkt):
    if pkt.haslayer(ARP):
        print("PACKET:", pkt.psrc, pkt.hwsrc)
        check_arp(pkt.psrc, pkt.hwsrc)
