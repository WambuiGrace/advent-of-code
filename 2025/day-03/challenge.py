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
        num = 0
        current_index = 0

        for step in range(12):
            # print("Step: ", step, "Current index", current_index)
            search_end = len(bank) - 12 + step + 1
            current_largest = max(bank[current_index:search_end])
            num += current_largest * (10 ** (12 - step - 1))
            current_index = bank.index(current_largest, current_index) + 1
        result_two += num

print(result_one)
print(result_two)