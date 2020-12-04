import sys

result = 0

for line in sys.stdin:
    line_split = line.split()
    positions = line_split[0].split('-')
    p1 = int(positions[0])
    p2 = int(positions[1])
    character = line_split[1][0]
    password = line_split[2]
    count = 0
    if password[p1 - 1] == character:
        count += 1
    if password[p2 - 1] == character:
        count += 1
    if count == 1:
        result += 1

print(result)
