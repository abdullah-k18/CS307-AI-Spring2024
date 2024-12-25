tree = {'1' : ['2', '3', '4'],
        '2' : ['5', '6'],
        '3' : [],
        '4' : ['7', '8'],
        '5' : ['9', '10'],
        '6' : [],
        '7' : ['11', '12'],
        '8' : [],
        '9' : [],
        '10' : [],
        '11' : [],
        '12' : []}
visited = set()
stack = ['1']
while stack:
    node = stack.pop()
    if node not in visited:
        print("Visited", node)
        visited.add(node)
        for neighbour in reversed(tree[node]):
            if neighbour not in visited:
                stack.append(neighbour)