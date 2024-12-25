graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['E'], 'D': ['F'], 'E': ['G'], 'F': ['G'], 'G': []}
heuristic_values = {'A': 4, 'B': 3, 'C': 2, 'D': 3, 'E': 1, 'F': 2, 'G': 0}
def best_first_search(graph, start, goal, heuristic_values):
    open_list = [start]
    closed_list = []
    while open_list:
        open_list.sort(key=lambda x: heuristic_values[x])
        current_node = open_list.pop(0)
        closed_list.append(current_node)
        if current_node == goal:
            return "Success"
        successors = graph[current_node]
        for successor in successors:
            if successor not in open_list and successor not in closed_list:
                open_list.append(successor)
    return "Failure"
result = best_first_search(graph, 'A', 'G', heuristic_values)
print("Result:", result)