result = 0

with open('input.txt', 'r') as file:
    line = file.readline()
    for pair in line.strip().split(','):
        left, right = (int(x) for x in pair.split('-'))
        for n in range(left, right + 1):
            id_number = str(n)
            mid = len(id_number) // 2
            l = id_number[:mid]
            r = id_number[mid:]
            
            if l == r:
                result += n

print(result)
