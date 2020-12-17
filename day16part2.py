from day16common import *
import sys

notes, your_ticket, nearby_tickets = get_input()
'''
Eliminate invalid tickets
'''
valid_ranges = []
for ranges in notes.values():
    valid_ranges += ranges

valid_ranges = merge_range(valid_ranges)

valid_tickets = [t for t in nearby_tickets if len(find_out_of_range(t, valid_ranges)) == 0]
valid_tickets.append(your_ticket)

'''
Find possible fields for each value
'''
def is_value_valid_for_field(value, ranges):
    for l, r in ranges:
        if value >= l and value <= r:
            return True
    return False

def is_all_values_valid_for_field(values, ranges):
    return all([is_value_valid_for_field(v, ranges) for v in values])

possible_fields = []
for i in range(len(valid_tickets[0])):
    values = []
    for j in range(len(valid_tickets)):
        values.append(valid_tickets[j][i])
    fields = []
    for field, ranges in notes.items():
        if is_all_values_valid_for_field(values, ranges):
            fields.append(field)
    possible_fields.append(fields)

'''
Find field for each value
'''
possible_fields = [(i, possible_fields[i]) for i in range(len(possible_fields))]
possible_fields.sort(key=lambda x: len(x[1]))

def find_fields_index():
    results = [{}]
    for i, fields in enumerate(possible_fields):
        new_results = []
        for result in results:
            possible_next_fields = set(fields[1]) - set(result.keys())
            for f in possible_next_fields:
                tmp_result = result.copy()
                tmp_result[f] = fields[0]
                new_results.append(tmp_result)
        results = new_results
    return results

fields_index = find_fields_index()[0]

'''
Calculate results:
'''
result = 1
for i in [fields_index[k] for k in fields_index.keys() if k.find('departure') >= 0]:
    result *= your_ticket[i]
print(result)
