import ipaddress
from ipaddress import *
for x in range(33):
    n = ipaddress.ip_network(f'93.138.161.94/{x}',False)
    print(n)
