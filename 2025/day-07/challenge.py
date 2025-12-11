grid = []
with open('input.txt', 'r') as file:
    for row_number, line in enumerate(file):
        line = line.strip()
        grid.append(line)

        if 'S' in line:
            start_row = row_number
            start_col = line.index('S')

total_rows = len(grid)
total_cols = len(grid[0])
total_splits = 0

active_beams = {(start_row, start_col)}

for current_row in range(start_row, total_rows -1):
    next_beams = set()

    for beam_row, beam_col in active_beams:
        next_row = beam_row + 1
        next_col = beam_col

        cell_below = grid[next_row][next_col]
        if cell_below == '^':
            total_splits +=1

            next_beams.add((next_row, next_col - 1))
            next_beams.add((next_row, next_col + 1))
        else:
            next_beams.add((next_row, next_col))
    active_beams = next_beams
print(total_splits)


#part two
def count_path(row, col, memo):
    if (row, col) in memo:
        return memo[(row, col)]
    
    if row >= total_rows:
        return 1
    
    current_cell = grid[row][col] if col < len(grid[row]) else '.'
    
    if current_cell == '^':
        left_col = col - 1
        right_col = col + 1
        
        if left_col < 0:
            left_paths = 0
        else:
            next_row = row + 1
            while next_row < total_rows and left_col < len(grid[next_row]) and grid[next_row][left_col] == '+':
                next_row += 1
            left_paths = count_path(next_row, left_col, memo)
        
        if right_col >= total_cols:
            right_paths = 0
        else:
            next_row = row + 1
            while next_row < total_rows and right_col < len(grid[next_row]) and grid[next_row][right_col] == '+':
                next_row += 1
            right_paths = count_path(next_row, right_col, memo)
        
        memo[(row, col)] = left_paths + right_paths
    else:
        next_row = row + 1
        while next_row < total_rows and col < len(grid[next_row]) and grid[next_row][col] == '+':
            next_row += 1
        memo[(row, col)] = count_path(next_row, col, memo)
    
    return memo[(row, col)]
beam_row, beam_col = start_row, start_col
beam_row +=1

while beam_row < total_rows and grid[beam_row][beam_col] == '+':
    beam_row +=1
memo = {}
print(count_path(beam_row, beam_col, memo))