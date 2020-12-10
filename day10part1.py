import sys

adapters = []
for line in sys.stdin:
    adapters.append(int(line))
adapters.sort()

n = [0] * 4
current = 0
for adapter in adapters:
    n[adapter - current] += 1
    current = adapter
n[3] += 1

print(n[1] * n[3])
