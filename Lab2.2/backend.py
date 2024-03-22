import sys
import glob
import re

sys.path.append('C:\\Users\\ay.alabin\\PycharmProjects\\p4ne\\Lab1.6')
from IP_parser_regex import get_IPs, get_cfgs


def get_host_names(fl_lst):
    for ln in fl_lst:
        res = re.finditer(r'hostname ([A-Za-z0-9\-\.\:\_]{1,100})', ln)
        res = list(res)
        if res and len(res) != 0:
            return res[0].group(1)

        res = re.finditer(r'sysname ([A-Za-z0-9\-\.\:\_]{1,100})', ln)
        res = list(res)

        if res and len(res) != 0:
            return res[0].group(1)

    return 'NO_NAME_FOUND'

# Get dictionary with IPs of each host
def get_Info():
    configs = glob.glob(r"C:\Users\ay.alabin\PycharmProjects\p4ne\Lab1.6\*.log")
    Configs_txt = get_cfgs(configs)

    IPs, hosts = [], []

    for config in Configs_txt:
        IPs.append(get_IPs(config))
        hosts.append(get_host_names(config))

    return { f'{hosts[i]}':IPs[i] for i in range(0, len(hosts)) }

#print(get_Info())