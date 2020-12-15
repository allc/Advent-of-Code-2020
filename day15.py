start = list(map(int, input().split(',')))
last_seen = {}
for i, n in enumerate(start[:-1]):
    last_seen[n] = i
last = start[-1]
for i in range(len(start), 100):
    if last in last_seen:
        new_last = i - last_seen[last] - 1
    else:
        new_last = 0
    last_seen[last] = i - 1
    last = new_last
    print(last)
print(last) 