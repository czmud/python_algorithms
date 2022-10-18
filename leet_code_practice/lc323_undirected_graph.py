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




print(countComponents2(5, [[0,1],[1,2],[2,3],[3,4]]))

