import sys

result = 0

def calc(s):
    oprands = []
    operators = []
    sub = []
    for c in s:
        if operators and operators[-1] == '(':
            if c == ')':
                operators.pop()
                if operators and operators[-1] == '(':
                    sub.append(')')
                else:
                    oprands.append(calc(sub))
                    sub = []
            else:
                if c == '(':
                    operators.append('(')
                sub.append(c)
        else:
            if c.isdigit():
                oprands.append(int(c))
            else:
                operators.append(c)
    
    oprands.reverse()
    operators.reverse()
    while operators:
        operator = operators.pop()
        oprand2 = oprands.pop()
        oprand1 = oprands.pop()
        if operator == '+':
            oprands.append(oprand1 + oprand2)
        else:
            oprands.append(oprand1 * oprand2)
    return oprands[0]
        

for line in sys.stdin:
    if line == '\n':
        break
    line = line[: -1].replace('(', '( ').replace(')', ' )')
    result += calc(line.split())
print(result)
