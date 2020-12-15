import sys

mask = None
mem = {}

for line in sys.stdin:
    item, value = line[: -1].split(' = ')
    if item == 'mask':
        mask = list(value)
    else:
        addr = list(bin(int(item[: -1].split('[')[1]))[2:])
        addr = ['0'] * (len(mask) - len(addr)) + addr
        value = int(value)
        addresses = [[]]
        for i in range(len(addr)):
            print(i)
            tmp_addresses = []
            if mask[i] == '0':
                for address in addresses:
                    address_copy = address.copy()
                    address_copy.append(addr[i])
                    tmp_addresses.append(address_copy)
            elif mask[i] == '1':
                for address in addresses:
                    address_copy = address.copy()
                    address_copy.append('1')
                    tmp_addresses.append(address_copy)
            else:
                for address in addresses:
                    address_copy = address.copy()
                    address_copy.append('0')
                    tmp_addresses.append(address_copy)
                    address_copy = address.copy()
                    address_copy.append('1')
                    tmp_addresses.append(address_copy)
            addresses = tmp_addresses
        for address in addresses:
            address = int(''.join(address))
            mem[address] = value
        
print(sum(mem.values()))
