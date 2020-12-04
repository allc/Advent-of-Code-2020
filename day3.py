import sys

grid = []

for line in sys.stdin:
    grid.append(line)

def trees_encounter(right, down):
    count = 0
    current_col = 0
    len_row = len(grid[0]) - 1 # length of line minus new line '\n'
    for i in range(0, len(grid), down):
        if grid[i][current_col % len_row] == '#':
            count += 1
        current_col = current_col % len_row + right
    return count

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

multiple = 1

for slope in slopes:
    trees = trees_encounter(*slope)
    print(slope, trees)
    multiple *= trees

print(multiple)
