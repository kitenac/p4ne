import sys
import glob
import re
import requests

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


# API related staff:
host_web_serv = 'https://10.31.70.209'
login = 'restapi'
pwd = 'j0sg1280-7@'
api_url = r'/restconf/data/Cisco-IOS-XE-process-memory-oper:memory-usage-processes'

# Use of API:
def API_get_info():
    headers = {
        "accept": "application/yang-data+json",
        "Content-Type": "application/yang-data+json"
    }
    r = requests.get(
        host_web_serv + api_url,
        headers=headers,
        auth=(login, pwd),
        verify=False)

    data = r.json()
    process = data['Cisco-IOS-XE-process-memory-oper:memory-usage-processes']['memory-usage-process']

    # take only interesting poles from dictionary
    lst = [ [ f'({x['pid']}) ' +x['name'],  x['holding-memory']] for x in process ]
    def sort_prc(lst_i):
        return lst_i[-1]

    lst = sorted(lst, key=sort_prc)

    return lst[0:10]

#print(API_get_info())