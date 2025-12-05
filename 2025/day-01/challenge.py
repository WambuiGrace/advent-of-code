dial = 50
password = 0
password_to_open_door = 0

with open('input.txt', 'r') as file:
    for line in file.readlines():
        num = int(line[1:])
        if line[0] == 'L':
            num *= -1
        full_rotations = abs(num) // 100
        password_to_open_door += full_rotations
        if num < 0:
            remainder = num + 100 * full_rotations
        else:
            remainder = num - 100 * full_rotations

        if remainder < 0 and dial > 0 and remainder + dial <= 0:
            password_to_open_door += 1
        elif remainder > 0 and remainder + dial > 99:
            password_to_open_door += 1

        dial = (dial + num) % 100
        if dial == 0:
            password += 1

        # print(line, password, password_to_open_door)

print(password)
print(password_to_open_door)