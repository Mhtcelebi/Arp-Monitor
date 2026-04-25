from logger import write

def arp_scan():
    devices = [
        {"ip": "192.168.1.1", "mac": "aa:bb:cc"},
        {"ip": "192.168.1.5", "mac": "dd:ee:ff"}
    ]

    write({
        "type": "DISCOVERY",
        "devices": devices
    })
