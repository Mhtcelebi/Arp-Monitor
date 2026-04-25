from logger import log, alert

arp_table = {}

def check_arp(ip, mac):
    if ip not in arp_table:
        arp_table[ip] = mac
        log(f"Yeni cihaz: {ip} -> {mac}")
        return

    if arp_table[ip] != mac:
        alert(f"ARP değişimi: {ip}")
        log(f"MAC değişti: {ip} {arp_table[ip]} -> {mac}")
        arp_table[ip] = mac
    else:
        log(f"Normal trafik: {ip} -> {mac}")

print("DETECTOR ÇALIŞTI")
