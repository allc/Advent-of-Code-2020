import sys

mask = None
mem = {}
for line in sys.stdin:
    item, value = line[: -1].split(' = ')
    if item == 'mask':
        mask = list(value)
    else:
        addr = int(item[: -1].split('[')[1])
        value = list(bin(int(value))[2:])
        value = ['0'] * (len(mask) - len(value)) + value
        for i in range(len(value)):
            if mask[i] == '1':
                value[i] = '1'
            elif mask[i] == '0':
                value[i] = '0'
        mem[addr] = int(''.join(value), 2)
print(sum(mem.values()))
