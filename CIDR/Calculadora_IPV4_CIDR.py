import ipaddress

NETWORKS = [
    '127.2.56.0/30',
    '',
]

for n in NETWORKS:
    net = ipaddress.ip_network(n)
    print('{!r}'.format(net))
    print('     is private:', net.is_private)
    print('      broadcast:', net.broadcast_address)
    print('     compressed:', net.compressed)
    print('   with netmask:', net.with_netmask)
    print('  with hostmask:', net.with_hostmask)
    print('  num addresses:', net.num_addresses)
    print()