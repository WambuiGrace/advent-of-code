from collections import deque 

def parse_line(line: str):
    line = line.strip()
    
    # Parse target from curly braces (joltage requirements)
    start = line.find('{')
    end = line.find('}')
    target_str = line[start+1:end]
    target = [int(x) for x in target_str.split(',')]

    # Parse buttons from parentheses
    buttons = []
    i = 0
    while i < len(line):
        if line[i] == '(':
            j = i + 1
            while j < len(line) and line[j] != ')':
                j += 1
            group = line[i + 1:j]
            if group.strip():
                indices = [int(x) for x in group.split(',')]
                buttons.append(indices)
            i = j
        i += 1  
    return target, buttons

def min_press(target, buttons):
    n = len(target)
    
    # Pre-compute button effects
    button_masks = []
    for indices in buttons:
        mask = [0] * n
        for idx in indices:
            mask[idx] += 1
        button_masks.append(mask)

    start = tuple([0] * n)
    target_tuple = tuple(target)
    queue = deque([(start, 0)])
    seen = {start}

    while queue:
        state, presses = queue.popleft()
        if state == target_tuple:
            return presses
        
        for mask in button_masks:
            # Increment counters (not toggle)
            next_state = tuple(state[i] + mask[i] for i in range(n))
            
            # Prune if we exceed target
            if any(next_state[i] > target_tuple[i] for i in range(n)):
                continue
            
            if next_state not in seen:
                seen.add(next_state)
                queue.append((next_state, presses + 1))
    
    return -1

def solve_file(filename):
    total = 0
    with open(filename) as file:
        for line in file:
            if not line.strip():
                continue
            target, buttons = parse_line(line)
            presses = min_press(target, buttons)
            total += presses
    return total

if __name__ == "__main__":
    answer = solve_file("input.txt")
    print(answer)