import sys

entries = []
for line in sys.stdin:
    entries.append(int(line))


def solve(entries):
    for i in range(len(entries) - 2):
        for j in range(i + 1, len(entries) - 1):
            for k in range(j + 1, len(entries)):
                if entries[i] + entries[j] + entries[k] == 2020:
                    return entries[i] * entries[j] * entries[k]

print(solve(entries))
