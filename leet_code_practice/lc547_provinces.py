def findCircleNum(isConnected):
    adjacency = {i:[] for i in range(len(isConnected))}
    
    for i in range(0,len(isConnected)):
        for j in range(i+1, len(isConnected[i])):
            if isConnected[i][j] == 1:
                adjacency[i].append(j)
                adjacency[j].append(i)
    
    components = 0
    visited = [False for i in range(len(isConnected))]
    for i in range(len(isConnected)):
        if not visited[i]:
            components += 1

            reachable = [i]
            while reachable:
                next_node = reachable.pop()
                if not visited[next_node]:
                    visited[next_node] = True
                    reachable += adjacency[next_node]
    return components



print(findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))