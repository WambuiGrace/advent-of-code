grid = []
with open('input.txt', 'r') as file:
    for line in file:
        grid.append(list(line.strip()))

rows = len(grid)
cols = len(grid[0])

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Get all neighboring positions around a given position
def get_neighbours(pos):
    neighbours = []
    for dx in (-1, 0, 1):          
        for dy in (-1, 0, 1):      
            if dx == 0 and dy == 0:
                continue           
            nx, ny = pos.x + dx, pos.y + dy
            if 0 <= nx < cols and 0 <= ny < rows:
                neighbours.append(Position(nx, ny))
    return neighbours

# Find all positions that should be removed
def position_to_remove():
    to_remove = []
    for y in range(rows):
        for x in range(cols):
            pos = Position(x, y)
            if grid[y][x] != '@':
                continue
            count_neighbours = sum(grid[n.y][n.x] == '@' for n in get_neighbours(pos))
            if count_neighbours < 4:
                to_remove.append(pos)
    return to_remove
# part 01
print(len(position_to_remove()))

# part 02
total_removed = 0
while True:
    remove_list = position_to_remove()
    if not remove_list:   
        break
    total_removed += len(remove_list)
    for pos in remove_list:
        grid[pos.y][pos.x] = '.'

print(total_removed)
