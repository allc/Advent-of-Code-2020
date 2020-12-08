import sys

instructions = []
for line in sys.stdin:
    operation, argument = line.split()
    instructions.append((operation, int(argument)))

repeat = [False] * len(instructions)
pointer = 0
acc = 0
while True:
    if repeat[pointer]:
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
print(acc)
