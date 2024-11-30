def calculate_string_value(edges, input_string):
    from collections import defaultdict, deque

    # Create the graph
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    
    # Build the graph and track in-degrees
    for edge in edges:
        u, v = edge.split()
        graph[u].append(v)
        in_degree[v] += 1
        if u not in in_degree:
            in_degree[u] = 0  # Ensure every node is in in_degree
    
    # Determine levels using BFS
    level = {}
    queue = deque()
    
    # Initialize levels for nodes with no incoming edges
    for word in in_degree:
        if in_degree[word] == 0:
            level[word] = 1
            queue.append(word)
    
    while queue:
        current = queue.popleft()
        current_level = level[current]
        
        for neighbor in graph[current]:
            if neighbor not in level:
                level[neighbor] = current_level + 1
            else:
                level[neighbor] = max(level[neighbor], current_level + 1)
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Calculate the value of the input string
    words = input_string.split()
    total_value = 0
    
    for word in words:
        total_value += level.get(word, 1)  # Default level is 1 if not found
    
    return total_value

# Read input
N = int(input().strip())
edges = [input().strip() for _ in range(N)]
input_string = input().strip()

# Calculate and print the result
result = calculate_string_value(edges, input_string)
print(result)