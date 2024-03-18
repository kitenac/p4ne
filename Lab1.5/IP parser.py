import glob
import re
import ipaddress

def Find_IPs(s: str):
    match = re.match(r' ?ip address ([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}) ([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})', s)
    if match == None:
        return None

    return ipaddress.IPv4Network(match.group(1)+'/'+match.group(2), strict=False)


# Collect every line
configs = glob.glob("*.log")

IPs = []
for fl in configs:
    with open(fl) as fl:
        for ln in fl:
            res = Find_IPs(ln)
            if res != None:
                IPs.append(res)


for ip in IPs:
    print(ip)