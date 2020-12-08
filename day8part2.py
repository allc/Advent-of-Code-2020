import sys

instructions = []
for line in sys.stdin:
    operation, argument = line.split()
    instructions.append((operation, int(argument)))

for i in range(len(instructions)):
    # Swap operation
    operation, argument = instructions[i]
    if operation == 'nop':
        instructions[i] = ('jmp', argument)
    elif operation == 'jmp':
        instructions[i] = ('nop', argument)
    else:
        continue

    repeat = [False] * len(instructions)
    pointer = 0
    acc = 0
    while True:
        if pointer == len(instructions) or repeat[pointer]:
            break
        repeat[pointer] = True
        operation, argument = instructions[pointer]
        if operation == 'acc':
            acc += argument
            pointer += 1
        elif operation == 'jmp':
            pointer += argument
        elif operation == 'nop':
            pointer += 1
    if pointer == len(instructions):
        print(acc)
        break
    # Swap operation back
    operation, argument = instructions[i]
    if operation == 'nop':
        instructions[i] = ('jmp', argument)
    elif operation == 'jmp':
        instructions[i] = ('nop', argument)
