result_one = 0
result_two = 0

def part_one(n):
    id_number = str(n)
    mid = len(id_number) // 2
    l = id_number[:mid]
    r = id_number[mid:]
    return l == r

def part_two(n):
    id_number = str(n)
    m = len(id_number)
    for k in range(2, m+1):
        first_token = id_number[:m // k]
        if id_number == first_token * k:
            return True
    return False

with open('input.txt', 'r') as file:
    line = file.readline()
    for pair in line.strip().split(','):
        left, right = (int(x) for x in pair.split('-'))
        for n in range(left, right + 1):
            if part_one(n):
                result_one += n
            if part_two(n):
                result_two += n

print(result_one)
print(result_two)
