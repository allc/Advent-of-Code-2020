import sys
import copy

input_grid = []
for line in sys.stdin:
    input_grid.append(list(line[: -1]))

grid = [copy.deepcopy(input_grid)]

def to_old_grid(layer, row, col):
    return (layer - 1, row - 1, col - 1)

def is_in_grid(layer, row, col):
    return layer >= 0 and layer < len(grid) and row >= 0 and row < len(grid[0]) and col >= 0 and col < len(grid[0][0])

def get_state(layer, row, col):
    if is_in_grid(layer, row, col):
        return grid[layer][row][col]
    else:
        return '.'

neighbors = set()
for layer in range(-1, 2):
    for row in range(-1, 2):
        for col in range(-1, 2):
            neighbors.add((layer, row, col))
neighbors.remove((0, 0, 0))

def get_neighbors_active_n(layer, row, col):
    n = 0
    for neighbor in neighbors:
        n += 1 if get_state(layer + neighbor[0], row + neighbor[1], col + neighbor[2]) == '#' else 0
    return n

for _ in range(6):
    new_grid = []
    for layer_i in range(len(grid) + 2):
        layer = []
        for row_i in range(len(grid[0]) + 2):
            row = []
            for col_i in range(len(grid[0][0]) + 2):
                old_grid = to_old_grid(layer_i, row_i, col_i)
                state = get_state(*old_grid)
                neighbors_active_n = get_neighbors_active_n(*old_grid)
                if state == '#':
                    if neighbors_active_n == 2 or neighbors_active_n == 3:
                        row.append('#')
                    else:
                        row.append('.')
                else:
                    if neighbors_active_n == 3:
                        row.append('#')
                    else:
                        row.append('.')
            layer.append(row)
        new_grid.append(layer)
    grid = new_grid

active_n = 0
for i, layer in enumerate(grid):
    print('Layer', i)
    for row in grid[i]:
        active_n += len([c for c in row if c == '#'])
        print(row)
print(active_n)
