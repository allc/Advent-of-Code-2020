import sys
from day19common import is_valid

rules = {}

input_state = 'rule'
for line in sys.stdin:
    if line == '\n':
        break
    else:
        rule_i, patterns = line.split(': ')
        rule_i = int(rule_i)
        patterns = [[c[1] if c[0] == '"' else int(c) for c in pattern.split()] for pattern in patterns.split(' | ')]
        rules[rule_i] = patterns

result = 0
for line in sys.stdin:
    if is_valid(rules, line[: -1], rules[0]):
        result += 1
print(result)
