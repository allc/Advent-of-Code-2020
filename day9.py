import sys

PREAMBLE = 25

l = []
for line in sys.stdin:
    if line == '\n':
        break
    l.append(int(line))

'''
Part 1
'''
def is_valid(l, preamble, current):
    for i in range(current - preamble, current - 1):
        for j in range(i + 1, current):
            if l[i] + l[j] == l[current]:
                return True
    return False

current = PREAMBLE
while current < len(l):
    if is_valid(l, PREAMBLE, current):
        current += 1
    else:
        invalid = l[current]
        print(invalid)
        break

'''
Part 2
'''
def find_contiguous():
    s = l[0]
    left = 0
    right = 0
    while True:
        if s == invalid and right > left:
            return (left, right)
        if s < invalid:
            right += 1
            s += l[right]
        else:
            s -= l[left]
            left += 1
            if right < left:
                right = left
                s = l[right]

left, right = find_contiguous()
print(min(l[left: right + 1]) + max(l[left: right + 1]))
