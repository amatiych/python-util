graph = {
            'A':['B'],
            'B':['C'],
            'C':['E','F'],
            'D':['F'],
            'E':['D']
            
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


if __name__ == '__main__':
    routes = calc_routes(graph,"A","F")
    print(routes)
