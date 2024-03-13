'''
1) SNMP messages retrivie: via two methods: GET and GET_NEXT
2) message parsing
'''

from pysnmp.hlapi import * # Импортировать только High-level
engine = SnmpEngine()
comm_data = CommunityData("public", mpModel=0) # пароль для доступа по SNMP вроде

# параметры кортеж: (ip, порт snmp).  161 - SNMP
transport = UdpTransportTarget(( "10.31.70.209", 161))
context_data = ContextData()

snmp_version = ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)
snmp_interfaces = ObjectIdentity('1.3.6.1.2.1.2.2.1.2')

# SNMP methods: GET - переменную получить, GET_NEXT - генератор

# GET
result = getCmd(engine, comm_data, transport, context_data, ObjectType(snmp_version))
# GET_NEXT
# lexicographicMode=False - чтоб не избыточно было
result2 = nextCmd(engine, comm_data, transport, context_data, ObjectType(snmp_interfaces), lexicographicMode=False)

# к списку генератор привели
result = list(result)
result2 = list(result2)

print('\nSoftware info:')
for r in result:
    for r2 in r[3]:
        print(r2)

# Here we play around to find the way to parse interface from SNMP response
'''print(dir(result2[1][-1]))
print(str(result2[1][-1][-1]).split(' ')[-1])'''

print('\nInterfaces:')
for r in result2:
    print(str(r[-1][-1]).split(' ')[-1])