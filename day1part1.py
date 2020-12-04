entries = set()
while True:
    line = input()
    if line:
        n = int(line)
        target = 2020 - n
        if target in entries:
            print(n * target)
            break
        entries.add(n)
