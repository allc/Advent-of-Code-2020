import sys

result = 0

for line in sys.stdin:
    line_split = line.split()
    count_range = line_split[0].split('-')
    lower = int(count_range[0])
    upper = int(count_range[1])
    character = line_split[1][0]
    count = 0
    for c in line_split[2]:
        if c == character:
            count += 1
    if count >= lower and count <= upper:
        result += 1

print(result)
