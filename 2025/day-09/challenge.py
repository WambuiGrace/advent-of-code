# part one

reds = []
with open('input.txt', 'r') as file:
    for line in file:
        x, y = map(int, line.strip().split(','))
        reds.append((x, y))

max_area = 0

for i in range(len(reds)):
    x1, y1 = reds[i]
    for j in range(i + 1, len(reds)):
        x2, y2 = reds[j]

        width = abs(x1 - x2) + 1
        height = abs(y1 - y2) + 1
        area = width * height

        if area > max_area:
            max_area = area

print("Part one:", max_area)

# part two

from collections import deque

max_x = max(x for x, y in reds) + 2
max_y = max(y for x, y in reds) + 2

grid = [['.' for _ in range(max_x)] for _ in range(max_y)]

for x, y in reds:
    grid[y][x] = '#'

for i in range(len(reds)):
    x1, y1 = reds[i]
    x2, y2 = reds[(i + 1) % len(reds)]  
    
    if x1 == x2:  
        for y in range(min(y1, y2), max(y1, y2) + 1):
            if grid[y][x1] == '.':
                grid[y][x1] = 'X'
    elif y1 == y2: 
        for x in range(min(x1, x2), max(x1, x2) + 1):
            if grid[y1][x] == '.':
                grid[y1][x] = 'X'

avg_x = sum(x for x, y in reds) // len(reds)
avg_y = sum(y for x, y in reds) // len(reds)

queue = deque([(avg_x, avg_y)])
while queue:
    x, y = queue.popleft()
    if 0 <= x < max_x and 0 <= y < max_y and grid[y][x] == '.':
        grid[y][x] = 'X'
        queue.append((x + 1, y))
        queue.append((x - 1, y))
        queue.append((x, y + 1))
        queue.append((x, y - 1))

def is_valid_rectangle(x1, y1, x2, y2):
    min_x = min(x1, x2)
    max_x = max(x1, x2)
    min_y = min(y1, y2)
    max_y = max(y1, y2)
    
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if grid[y][x] not in ('#', 'X'):
                return False
    return True

max_area_part2 = 0

for i in range(len(reds)):
    x1, y1 = reds[i]
    for j in range(i + 1, len(reds)):
        x2, y2 = reds[j]
        
        if is_valid_rectangle(x1, y1, x2, y2):
            width = abs(x1 - x2) + 1
            height = abs(y1 - y2) + 1
            area = width * height
            
            if area > max_area_part2:
                max_area_part2 = area

print("Part two:", max_area_part2)