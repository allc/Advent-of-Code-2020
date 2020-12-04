import sys

required_fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
required_fields_current = required_fields.copy()
num_valid = 0
for line in sys.stdin:
    if line == '\n':
        if len(required_fields_current) == 0:
            num_valid += 1
        required_fields_current = required_fields.copy()
    else:
        fields = line.split()
        for field in fields:
            field_name, field_value = field.split(':')
            if field_name in required_fields_current:
                required_fields_current.remove(field_name)
# No blank line at the end
if len(required_fields_current) == 0:
    num_valid += 1
    required_fields_current = required_fields.copy()
print(num_valid)
