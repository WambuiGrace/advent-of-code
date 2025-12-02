dial = 50
result = 0

with open('input.txt', 'r') as file:
    for line in file.readlines():
        num = int(line[1:])
        if line[0] == 'L':
            num *= -1

        dial = (dial + num) % 100
        if dial == 0:
            result += 1

print(result)