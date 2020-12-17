import sys
import copy

def get_input():
    nearby_tickets = []
    notes = {}
    input_stage = 'notes'
    for line in sys.stdin:
        line = line[: -1]
        if line == '':
            if input_stage == 'nearby tickets':
                break
            continue
        if line == 'your ticket:':
            input_stage = 'your ticket'
            continue
        if line == 'nearby tickets:':
            input_stage = 'nearby tickets'
            continue
        if input_stage == 'notes':
            field, ranges = line.split(': ')
            ranges = ranges.split(' or ')
            ranges = [list(map(int, r.split('-'))) for r in ranges]
            notes[field] = ranges
            continue
        if input_stage == 'your ticket':
            your_ticket = list(map(int, line.split(',')))
            continue
        if input_stage == 'nearby tickets':
            nearby_tickets.append(list(map(int, line.split(','))))
    return (notes, your_ticket, nearby_tickets)

def merge_range(ranges):
    ranges = copy.deepcopy(ranges)
    ranges.sort()
    merged_ranges = [ranges[0]]
    for l, r in ranges[1:]:
        if l <= merged_ranges[-1][1]:
            merged_ranges[-1][1] = max(merged_ranges[-1][1], r)
        else:
            merged_ranges.append([l, r])
    return merged_ranges

def find_out_of_range(ticket, ranges):
    out_of_range = []
    for v in ticket:
        is_out_of_range = True
        for l, r in ranges:
            if v >= l and v <= r:
                is_out_of_range = False
                break
        if is_out_of_range:
            out_of_range.append(v)
    return out_of_range
