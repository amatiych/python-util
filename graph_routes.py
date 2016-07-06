graph = {
            'A':['B'],
            'B':['C'],
            'C':['E','F'],
            'D':['F'],
            'E':['D']
            
        }


tree = {
            'A':['B'],
            'B':['C','D'],
            'C':['E']

       }

def calc_routes(graph,start, end,path=[]):
    """
    walk the graph such as desribed above and calculate all routes
    """
    path = path + [start]
    if start == end:
        return [path]

    if start not in graph:
        return []

    newpaths = []
    for node in graph[start]:
        if node not in path:
            next_routes = calc_routes(graph,node,end,path)
            for route in next_routes:
                newpaths.append(route)

    return newpaths

def walk_tree(tree,start,path=[]):
    """
        walk the tree as described above. the difference to the graph is that there is no end node"
    """
    path = path + [start]
    if start not in tree:
        return [path]

    newbranches = []
    for node in tree[start]:
        if node not in path:
            subbranches = walk_tree(tree,node,path)
            for branch in subbranches:
                newbranches.append(branch)

    return newbranches
 


if __name__ == '__main__':
    routes = calc_routes(graph,"A","F")
    branches = walk_tree(tree,'A')
    print(routes)
    print(branches)
