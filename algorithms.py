from collections import deque
import heapq
def is_valid_cell(grid, row, col):
    return (
        0 <= row < len(grid)
        and 0 <= col < len(grid[0])
        and grid[row][col] == 0
    )
def get_neighbors(grid, row, col):
    neighbors = []
    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]
    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc
        if is_valid_cell(grid, new_row, new_col):
            neighbors.append((new_row, new_col))
    return neighbors
def bfs(grid, start, end):
    queue = deque([start])
    visited = {start}
    parent = {start: None}
    explored = []
    while queue:
        current = queue.popleft()
        explored.append(current)
        if current == end:
            break
        for neighbor in get_neighbors(grid, current[0], current[1]):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)
    if end not in visited:
        return [], explored
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse()
    return path, explored
def dijkstra(grid, start, end):
    priority_queue = [(0, start)]
    distances = {start: 0}
    parent = {start: None}
    explored = []
    while priority_queue:
        current_distance, current = heapq.heappop(priority_queue)
        if current_distance > distances[current]:
            continue
        explored.append(current)
        if current == end:
            break
        for neighbor in get_neighbors(grid, current[0], current[1]):
            new_distance = current_distance + 1
            if neighbor not in distances or new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                parent[neighbor] = current
                heapq.heappush(
                    priority_queue,
                    (new_distance, neighbor)
                )
    if end not in distances:
        return [], explored
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse()
    return path, explored
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
def a_star(grid, start, end):
    priority_queue = [(0, start)]
    g_cost = {start: 0}
    parent = {start: None}
    explored = []
    while priority_queue:
        _, current = heapq.heappop(priority_queue)
        explored.append(current)
        if current == end:
            break
        for neighbor in get_neighbors(grid, current[0], current[1]):
            new_g_cost = g_cost[current] + 1
            if neighbor not in g_cost or new_g_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_g_cost
                f_cost = new_g_cost + heuristic(
                    neighbor,
                    end
                )
                parent[neighbor] = current
                heapq.heappush(
                    priority_queue,
                    (f_cost, neighbor)
                )
    if end not in g_cost:
        return [], explored
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse()
    return path, explored