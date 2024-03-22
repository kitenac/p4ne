import glob
import sys


# Collect everything looking like IP - preparations
configs = glob.glob(r"C:\Users\ay.alabin\PycharmProjects\p4ne\Lab1.6\*.log")
buff = []

# get array of strings - exsisting configs. configs - list of config names to get
def get_cfgs(configs):
    cfgs = []
    for fl in configs:
     with open(fl) as fl:
        cfgs.append([])
        for ln in fl:
            cfgs[-1].append(ln)
    return cfgs


Configs_txt = [] # list of lists: each sublist is config file - list of strings

for fl in configs:
    Configs_txt.append([])
    with open(fl) as fl:
        for ln in fl:
            if ln.count('.') >= 3:
                #print(ln)
                buff.append(ln)
                Configs_txt[-1].append(ln)

'System name'

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

# Apply parsing function - for each suspended line in given list of strings
def apply_parsing(buff, parse_smth_f):
    smth_lst = [] # list for parsed data
    for l in buff:
        smth = parse_smth_f(l)
        if len(smth) != 0:
            smth_lst.extend(smth)

    return set(smth_lst) # only uniq


def get_IPs(buff_Str):
    return apply_parsing(buff_Str, parse_smth_f=parse_ip)

if __name__ == "__main__":
    IPs = get_IPs(Configs_txt[0])
    print(f'Parsed {len(IPs)} uniqe IPs:')
    for ip in IPs:
        print(ip)


