def trash_compactor(filename='input.txt'):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    if not lines:
        return 0
    
    operator_line = lines[-1].strip('\n')
    number_lines = [line.strip('\n') for line in lines[:-1]]
    max_length = len(operator_line)
    padded_number_lines = []

    for line in number_lines:
        padded_number_lines.append(line.ljust(max_length))
    problem_starts = []

    for i in range(len(operator_line)):
        char = operator_line[i]
        if char == '+' or char == '*':
            problem_starts.append(i)
    problem_boundaries = problem_starts + [max_length]
    grand_total = 0

    for i in range(len(problem_starts)):
        start = problem_starts[i]
        end = problem_boundaries[i + 1]
        operator = operator_line[start]
        current_problem_numbers = []

        # Extract numbers for the column range
        for line in padded_number_lines:
            number_str = line[start:end].strip()
            if number_str:
                current_problem_numbers.append(int(number_str))
        
        # Skip if there are no numbers in the column
        if not current_problem_numbers:
            continue

        if operator == '+':
            result = 0
            for number in current_problem_numbers:
                result += number

        elif operator == '*':
            result = current_problem_numbers[0]
            for j in range(1, len(current_problem_numbers)):
                result *= current_problem_numbers[j]
        
        grand_total += result
    return grand_total

print(trash_compactor())


