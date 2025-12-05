with open("input.txt", 'r') as file:
    data = [line.strip() for line in file.readlines()]

def part_one(data):
    blank_line_index = data.index("")

    ranges = []
    for line in data[:blank_line_index]:
        start, end = map(int, line.split("-"))
        ranges.append([start, end])

    ids = [int(x) for x in data[blank_line_index + 1:]]

    total = 0
    for id_number in ids:
        for start, end in ranges:
            if start <= id_number <= end + 1:
                total += 1
                break
    return total
print(part_one(data))

def part_two(data):
    blank_line_index = data.index("")
    
    ranges = []
    for line in data[:blank_line_index]:
        start, end = map(int, line.split("-"))
        ranges.append([start, end])
    ranges.sort()

    merged_ranges = [ranges[0]]
    for start_two, end_two in ranges[1:]:
        start_one, end_one = merged_ranges[-1]
        if start_two > end_one:
            merged_ranges.append([start_two, end_two])
        else:
            merged_ranges[-1][1] = max(end_one, end_two)
    
    total = 0
    for start, end in merged_ranges:
        total += (end - start +1)
    return total
print(part_two(data))