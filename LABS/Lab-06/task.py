import heapq
def astar(graph, start, goal, heuristic_values):
    open_list = [(heuristic_values[start], start)]
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic_values[start]
    while open_list:
        _, current = heapq.heappop(open_list)
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        for neighbor in graph[current]:
            tentative_g_score = g_score[current] + 1

            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic_values[neighbor]
                heapq.heappush(open_list, (f_score[neighbor], neighbor))
    return None
graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['E'], 'D': ['F'], 'E': ['G'], 'F': ['G'], 'G': []}
heuristic_values = {'A': 4, 'B': 3, 'C': 2, 'D': 3, 'E': 1, 'F': 2, 'G': 0}
start_node = 'A'
goal_node = 'G'
path = astar(graph, start_node, goal_node, heuristic_values)
if path:
    print("Path found:", path)
else:
    print("No path found.")