def area_of_polygon(points):
    """Calculate the area of a polygon using the shoelace formula."""
    n = len(points)
    area = 0
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        area += x1 * y2 - x2 * y1
    return abs(area) // 2

def find_polygons(segments):
    """Find all unique polygons formed by the given line segments."""
    from collections import defaultdict
    
    # Create a graph to represent connections
    graph = defaultdict(list)
    
    for (x1, y1, x2, y2) in segments:
        graph[(x1, y1)].append((x2, y2))
        graph[(x2, y2)].append((x1, y1))
    
    visited = set()
    polygons = []
    
    def dfs(start, current, path):
        if current in visited:
            if current == start and len(path) >= 3:
                polygons.append(path[:])
            return
        visited.add(current)
        for neighbor in graph[current]:
            path.append(neighbor)
            dfs(start, neighbor, path)
            path.pop()
        visited.remove(current)
    
    for point in graph.keys():
        if point not in visited:
            dfs(point, point, [point])
    
    return polygons

def maximum_area(segments):
    polygons = find_polygons(segments)
    max_area = 0
    for polygon in polygons:
        max_area = max(max_area, area_of_polygon(polygon))
    return max_area

# Input reading
N = int(input())
segments = []
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    segments.append((x1, y1, x2, y2))

# Calculate the maximum area
result = maximum_area(segments)
print(result)