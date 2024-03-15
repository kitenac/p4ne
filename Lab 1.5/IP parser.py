import glob

# Collect everything looking like IP - preparations
configs = glob.glob("*.log")
buff = []
for fl in configs:
    with open(fl) as fl:
        for ln in fl:
            if ln.count('.') >= 3:
                #print(ln)
                buff.append(ln)

def parse_ip(line:str):
    # each ip in line is separated by space
    words = line.split(' ')
    #print(f'words: {words}')
    # search candidats
    quazi_ips = [word.split('.') for word in words]
    #print(f'q_ips: {quazi_ips}\n\n')

    posible = '0123456789/' # containing of smth like IP address/network
    ips = []

    # check every octet to be in 'possible' set
    def is_ip(quasi_ip):
        for ch in quasi_ip:
            if len(ch) > 1:
                for c in ch:
                    if c in posible:
                        continue
                    else:
                        return False
                continue
            else:
                if ch in posible:
                    continue
                else:
                    return False
        return True

    for q_ip in quazi_ips:
        if len(q_ip) == 4 and is_ip(q_ip):
            ips.append('.'.join(q_ip))

    return ips

# Apply parsing for each suspended line
IPs = []
for l in buff:
    ips = parse_ip(l)
    if len(ips) != 0:
        IPs.extend(ips)

IPs = set(IPs)
print(f'Parsed {len(IPs)} uniqe IPs:')
for ip in IPs:
    print(ip)