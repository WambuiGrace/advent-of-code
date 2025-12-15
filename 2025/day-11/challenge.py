def parse_input(filename):
    """
    Parse the input file and build a graph.
    Returns a dictionary where keys are device names and values are lists of connected devices.
    """
    graph = {}
    
    with open(filename) as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split(':')
            device = parts[0].strip()
            outputs = parts[1].strip().split()
            graph[device] = outputs
    
    return graph


def count_paths(graph, start, end, visited=None):
    """
    Count all possible paths from start to end using DFS (Depth-First Search).
    
    Args:
        graph: Dictionary of device connections
        start: Starting device name
        end: Target device name
        visited: Set of devices already visited in current path (to avoid cycles)
    
    Returns:
        Number of paths from start to end
    """
    if visited is None:
        visited = set()
    if start == end:
        return 1
    if start not in graph:
        return 0
    
    visited.add(start)
    total_paths = 0
    for next_device in graph[start]:
        if next_device not in visited:
            total_paths += count_paths(graph, next_device, end, visited)
    visited.remove(start)
    
    return total_paths


def count_paths_with_required(graph, start, end, required_nodes, visited=None, seen_required=None):
    """
    Count all possible paths from start to end that visit ALL required nodes.
    
    Args:
        graph: Dictionary of device connections
        start: Starting device name
        end: Target device name
        required_nodes: Set of nodes that must be visited in the path
        visited: Set of devices already visited in current path (to avoid cycles)
        seen_required: Set tracking which required nodes we've seen so far
    
    Returns:
        Number of paths from start to end that visit all required nodes
    """
    if visited is None:
        visited = set()
    if seen_required is None:
        seen_required = set()
    
    visited.add(start)   
    if start in required_nodes:
        seen_required.add(start)
    if start == end:
        count = 1 if seen_required == required_nodes else 0
        visited.remove(start)
        if start in required_nodes:
            seen_required.discard(start)
        return count
    if start not in graph:
        visited.remove(start)
        if start in required_nodes:
            seen_required.discard(start)
        return 0
    
    total_paths = 0
    for next_device in graph[start]:
        if next_device not in visited:
            total_paths += count_paths_with_required(
                graph, next_device, end, required_nodes, visited, seen_required
            )
    
    visited.remove(start)
    if start in required_nodes:
        seen_required.discard(start)
    
    return total_paths


def solve_part1(filename):
    """Solve Part 1: Count paths from 'you' to 'out'."""
    graph = parse_input(filename)
    num_paths = count_paths(graph, "you", "out") 
    return num_paths


def solve_part2(filename):
    """Solve Part 2: Count paths from 'svr' to 'out' that visit both 'dac' and 'fft'."""
    graph = parse_input(filename)
    required_nodes = {"dac", "fft"}
    num_paths = count_paths_with_required(graph, "svr", "out", required_nodes)
    return num_paths


if __name__ == "__main__":
    answer_one = solve_part1("input.txt")
    print(f"Part one - Number of paths from 'you' to 'out': {answer_one}")
    answer_two = solve_part2("input.txt")
    print(f"Part two - Paths from 'svr' to 'out' visiting both 'dac' and 'fft': {answer_two}")
