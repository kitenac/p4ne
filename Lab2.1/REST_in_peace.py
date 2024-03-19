import requests

headers = {
    "accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

auth = ('restapi', 'j0sg1280-7@')
r = requests.get('https://10.31.70.209' + '/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces', auth=auth, headers=headers, verify=False)
# TODO - с ответом уже работать - по слайдам

conf_json = r.json()
# print(*conf_json)
ints = r.json()['Cisco-IOS-XE-interfaces-oper:interfaces']['interface']

for int in ints:
    print(f'''
            {int['name']}  
            IN:
                bytes:  {int['statistics']['in-octets']} 
                packets: {int['statistics']['in-unicast-pkts']}
            OUT:
                bytes:  {int['statistics']['out-octets']} 
                packets: {int['statistics']['out-unicast-pkts']}
    ''')
