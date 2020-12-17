import sys
import copy

input_grid = []
for line in sys.stdin:
    input_grid.append(list(line[: -1]))

grid = [[copy.deepcopy(input_grid)]]

def to_old_grid(w, layer, row, col):
    return (w - 1, layer - 1, row - 1, col - 1)

def is_in_grid(w, layer, row, col):
    return w >= 0 and w < len(grid) and layer >= 0 and layer < len(grid[0]) and row >= 0 and row < len(grid[0][0]) and col >= 0 and col < len(grid[0][0][0])

def get_state(w, layer, row, col):
    if is_in_grid(w, layer, row, col):
        return grid[w][layer][row][col]
    else:
        return '.'

neighbors = set()
for w in range(-1, 2):
    for layer in range(-1, 2):
        for row in range(-1, 2):
            for col in range(-1, 2):
                neighbors.add((w, layer, row, col))
neighbors.remove((0, 0, 0, 0))

def get_neighbors_active_n(w, layer, row, col):
    n = 0
    for neighbor in neighbors:
        n += 1 if get_state(w + neighbor[0], layer + neighbor[1], row + neighbor[2], col + neighbor[3]) == '#' else 0
    return n

for _ in range(6):
    new_grid = []
    for w_i in range(len(grid) + 2):
        w = []
        for layer_i in range(len(grid[0]) + 2):
            layer = []
            for row_i in range(len(grid[0][0]) + 2):
                row = []
                for col_i in range(len(grid[0][0][0]) + 2):
                    old_grid = to_old_grid(w_i, layer_i, row_i, col_i)
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
            w.append(layer)
        new_grid.append(w)
    grid = new_grid

active_n = 0
for w_i in range(len(grid)):
    for layer_i in range(len(grid[0])):
        for row_i in range(len(grid[0][0])):
            active_n += len([c for c in grid[w_i][layer_i][row_i] if c == '#'])
print(active_n)
