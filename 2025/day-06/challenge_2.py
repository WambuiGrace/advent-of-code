def trash_compactor(filename='input.txt'):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    if not lines:
        return 0
    
    matrix = []
    for line in lines:
        matrix.append(list(line.strip('\n')))
    
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    
    for _ in range(num_cols - len(matrix[-1])):
        matrix[-1].append(' ')
    
    grand_total = 0
    current_col = 0
    
    while current_col < num_cols:
        operator = matrix[-1][current_col]
        next_col = current_col + 1
        
        while next_col < num_cols and matrix[-1][next_col] == ' ':
            next_col += 1
        
        if operator == '+':
            problem_result = 0
        else:
            problem_result = 1
        
        for col in range(current_col, next_col):
            column_string = ''.join(matrix[row][col] for row in range(num_rows - 1))
            if not column_string.strip():
                continue
            number = int(column_string)
            
            if operator == '+':
                problem_result += number
            else:
                problem_result *= number
        
        grand_total += problem_result
        current_col = next_col
    
    return grand_total

print(trash_compactor())