result_one = 0
result_two = 0

with open('input.txt', 'r') as file:
    for line in file:
        bank = [int(char) for char in line.strip()]
        
        # part 1
        largest_first = max(bank[:-1])
        index_of_largest = bank.index(largest_first)
        largest_second = max(bank[index_of_largest + 1:])
        result_one += (10 * largest_first + largest_second)

        # part 2


print(result_one)