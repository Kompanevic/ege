import ipaddress
from ipaddress import *
for x in range(33):
    net = ipaddress.ip_network(f'147.222.199.75/{x}',False)
    print(net)