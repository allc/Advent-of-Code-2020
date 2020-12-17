from day16common import *
import sys

notes, your_ticket, nearby_tickets = get_input()
valid_ranges = []
for ranges in notes.values():
    valid_ranges += ranges

valid_ranges = merge_range(valid_ranges)

out_of_range = find_out_of_range(your_ticket, valid_ranges)
ticket_scanning_error_rate = sum(out_of_range)
for t in nearby_tickets:
    ticket_scanning_error_rate += sum(find_out_of_range(t, valid_ranges))

print(ticket_scanning_error_rate)
