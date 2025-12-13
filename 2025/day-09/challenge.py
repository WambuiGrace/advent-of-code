from collections import deque

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
# Create set of all points for fast lookup
points_set = set(reds)

# Only check rectangles formed by actual coordinate pairs
max_area_part2 = 0

for i in range(len(reds)):
    x1, y1 = reds[i]
    for j in range(i + 1, len(reds)):
        x2, y2 = reds[j]
        
        # Calculate area
        width = abs(x1 - x2) + 1
        height = abs(y1 - y2) + 1
        area = width * height
        
        # Only check if this could be larger than current max
        if area > max_area_part2:
            # Check if all 4 corners exist in the point set
            min_x, max_x = min(x1, x2), max(x1, x2)
            min_y, max_y = min(y1, y2), max(y1, y2)
            
            corners = [
                (min_x, min_y),
                (min_x, max_y),
                (max_x, min_y),
                (max_x, max_y)
            ]
            
            if all(corner in points_set for corner in corners):
                max_area_part2 = area

print("Part two:", max_area_part2)