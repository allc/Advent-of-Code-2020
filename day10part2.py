import sys

adapters = []
for line in sys.stdin:
    adapters.append(int(line))
adapters.sort()

ways = [0] * (adapters[-1] + 3)
ways[2] = 1
for adapter in adapters:
    i = adapter + 2
    ways[i] = ways[i - 1] + ways[i - 2] + ways[i - 3]

print(ways[-1])
