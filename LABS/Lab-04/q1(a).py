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
queue = ['1']
visited = []
while queue:
    node = queue.pop(0)
    print('visited', node)
    for child in tree[node]:
        if child not in visited:
            visited.append(child)
            queue.append(child)