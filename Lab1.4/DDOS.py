import random
import ipaddress



# Наследуемся от встроенного в питон объекта - ipaddress.IPv4Network
class IPv4RandomNetwork(ipaddress.IPv4Network):
    def __init__(self):
        mask = random.randint(8, 24)
        addr = ipaddress.IPv4Address(random.randint(0x0b000000, 0xdf000000)) # от 11.0.0.0 (0x0B000000) до 223.0.0.0 (0xDF000000)
        Network = ipaddress.IPv4Network(addr.__str__()+'/'+str(mask), strict=False)

        self.netmask = Network.netmask
        self.network_address = Network.network_address

        while self.is_private != False:
            self.network_address = ipaddress.IPv4Address(random.randint(0x0b000000, 0xdf000000))

    def __str__(self):
        return self.network_address.__str__()+'   /' + str(self.netmask)

    def regular(self):
        return not self.is_reserved

gen_ip = [IPv4RandomNetwork() for i in range(0, 50)]


def sort_f(x:ipaddress.IPv4Network):
    return int(x.netmask) * 2**32 + int(x.network_address)


gen_ip = sorted(gen_ip, key=sort_f)

for ip in gen_ip:
    print(f'{ip} regular? - {ip.regular()}')

