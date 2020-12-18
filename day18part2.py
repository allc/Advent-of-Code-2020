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
    
    oprands2 = []
    oprands.reverse()
    operators.reverse()
    while operators:
        operator = operators.pop()
        if operator == '+':
            oprands.append(oprands.pop() + oprands.pop())
        else:
            oprands2.append(oprands.pop())
    oprands2.append(oprands[0])
    product = 1
    for n in oprands2:
        product *= n
    return product
        

for line in sys.stdin:
    if line == '\n':
        break
    line = line[: -1].replace('(', '( ').replace(')', ' )')
    result += calc(line.split())
print(result)
