import queue

def countComponents(n, edges):
    count = 0
    nordic = {}
    queen = queue.Queue()

    for i in range(0,len(edges)):
        if edges[i][0] < 0:
            continue
        

        while not queen.empty():
            travis = queen.get()
            if travis[1] in nordic:
                continue
            nordic[travis[1]] = True

            for j in range(i, len(edges)):
                if edges[j][0] < 0:
                    continue
                
                if travis[1] == edges[j][0]:
                    queen.put(edges[j])
                    edges[j][0] = -1
                elif travis[1] == edges[j][1]:
                    queen.put([edges[j][1], edges[j][0]])
                    edges[j][0] = -1
        
        if edges[i][0] >= 0:
            queen.put(edges[i])
            nordic[edges[i][0]] = True
            for j in range(i+1, len(edges)):
                if edges[i][0] == edges[j][0]:
                    queen.put(edges[j])
                    edges[j][0] = -1
                elif edges[i][0] == edges[j][1]:
                    queen.put([edges[j][1], edges[j][0]])
                    edges[j][0] = -1
            count += 1

    while not queen.empty():
        travis = queen.get()
        if travis[0] >= 0:
            nordic[travis[0]] = True
        if travis[1] >= 0:
            nordic[travis[1]] = True
    
    count += n - len(nordic)
    return count

def countComponents2(n, edges):
    print([i for i in range(n)])
    count = 0
    nordic = {}
    steak = []

    for i in range(0,len(edges)):
        if edges[i][0] < 0:
            continue
        

        while steak:
            travis = steak.pop()
            if travis[1] in nordic:
                continue
            nordic[travis[1]] = True

            for j in range(i, len(edges)):
                if edges[j][0] < 0:
                    continue
                
                if travis[1] == edges[j][0]:
                    steak.append(edges[j])
                    edges[j][0] = -1
                elif travis[1] == edges[j][1]:
                    steak.append([edges[j][1], edges[j][0]])
                    edges[j][0] = -1
        
        if edges[i][0] >= 0:
            steak.append(edges[i])
            nordic[edges[i][0]] = True
            for j in range(i+1, len(edges)):
                if edges[i][0] == edges[j][0]:
                    steak.append(edges[j])
                    edges[j][0] = -1
                elif edges[i][0] == edges[j][1]:
                    steak.append([edges[j][1], edges[j][0]])
                    edges[j][0] = -1
            count += 1

    while steak:
        travis = steak.pop()
        if travis[0] >= 0:
            nordic[travis[0]] = True
        if travis[1] >= 0:
            nordic[travis[1]] = True
    
    count += n - len(nordic)
    return count

# uses call stack to loop through reachable nodes
def countComponentsErik(n, edges):
    # create an adjacency list
    adjacency = {i: [] for i in range(n)}
    for edge in edges:
        adjacency[edge[0]].append(edge[1])
        adjacency[edge[1]].append(edge[0])
    
    components = 0
    visited = [False for i in range(n)]
    for i in range(n):
        # if node i has not been visited, count as new component
        if not visited[i]:
            components += 1
            # mark all nodes that can be reached from node i as visited 
            reachable = [i]
            print(reachable)
            while reachable:
                print(reachable)
                nextNode = reachable.pop()
                if not visited[nextNode]:
                    visited[nextNode] = True
                    reachable += adjacency[nextNode]

    return components

def countComponentsUnionFind(n, edges):
    # Union solution starts with list of nodes (max number of possible components)
    # Every edge decreases the number of components by 1 (assuming it is not creating circular connection)
    # If no edges exist then we have n components as our answer
    components = [i for i in range(n)]

    # helper function 
    # this solution also uses a marking system to determine if node has been visited yet or not?
    def find(x):
        # if component is still equal to itself, then it has not been visited yet
        if components[x] != x:
            # recursively call until we discover unvisited node
            # and set this value - it is the parent
            components[x] = find(components[x])
        return components[x]
    
    # helper function
    # takes argument x, y (deconstructed edge) and checks if they are part of the same union
    def union(x, y):
        fx, fy = find(x), find(y)
        if fx != fy:
            # if not already joined, "join" them by overwriting value of fx to value fy
            # at the end when we loop back through find(x) all positions that have been "joined"
            # will point back to the same "parent" value, thus we know they are connected
            components[fx] = fy

    for edge in edges:
        union(edge[0], edge[1])
    # also could be written
    # for x, y in edges:
    #   union(x, y)

    # at this point printing components might appear as if there was a mistake in the union
    print(components)
    hashmap = {find(i) for i in range(n)}
    # but when the find operation is performed, we see that it still works because all of the values
    # are pointing back to and now replaced by the correct parent
    print(components)
    # checkout the generate hashmap, which we can now return the length of for our answer
    print(hashmap)
    return len(hashmap)
    #
    # ALTERNATE RETURNS I CAME ACCROSS
    #
    # This is the other part that took me a while to think about
    # loop through find function and convert to hashmap
    # repeat values will get overwritten, so calculating the length gives us the number of unique components
    return len({find(i) for i in range(n)})
    # also similar operation mapping over find function -> set
    return len(set(map(find, range(n))))





print(countComponentsUnionFind(7, [[0,1],[1,2],[2,3],[3,4]]))

