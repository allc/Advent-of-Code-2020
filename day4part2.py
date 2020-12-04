import sys
import string

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
            if field_name == 'byr':
                if len(field_value) != 4 or not field_value.isdigit() or field_value < '1920' or field_value > '2002':
                    continue
            if field_name == 'iyr':
                if len(field_value) != 4 or not field_value.isdigit() or field_value < '2010' or field_value > '2020':
                    continue
            if field_name == 'eyr':
                if len(field_value) != 4 or not field_value.isdigit() or field_value < '2020' or field_value > '2030':
                    continue
            if field_name == 'hgt':
                if field_value[-2:] == 'cm':
                    if not field_value[:-2].isdigit() or int(field_value[:-2]) < 150 or int(field_value[:-2]) > 193:
                        continue
                elif field_value[-2:] == 'in':
                    if not field_value[:-2].isdigit() or int(field_value[:-2]) < 59 or int(field_value[:-2]) > 76:
                        continue
                else:
                    continue
            if field_name == 'hcl':
                if field_value[0] != '#':
                    continue
                if not all(c in string.hexdigits for c in field_value[1:]):
                    continue
            if field_name == 'ecl':
                if field_value not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                    continue
            if field_name == 'pid':
                if not len(field_value) == 9 or not field_value.isdigit():
                    continue
            if field_name in required_fields_current:
                required_fields_current.remove(field_name)
# No blank line at the end
if len(required_fields_current) == 0:
    num_valid += 1
    required_fields_current = required_fields.copy()
print(num_valid)
