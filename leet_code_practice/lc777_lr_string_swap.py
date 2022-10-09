def canTransform(start, end):

    i = j = 0
    while i < len(start) or j < len(end):

        while i < len(start) and start[i] == 'X':
            i += 1
        while j < len(start) and end[j] == 'X':
            j += 1

        if i >= len(start):
            if not (j >= len(end)):
                return False
        elif j >= len(end):
            return False
        elif start[i] != end[j]:
            return False
            
        elif start[i] == 'R' and j < i:
            return False
        elif start[i] == 'L' and i < j:
            return False
        i += 1
        j += 1

    return True

def canTransform2(start, end):

    j = 0
    for i in range(len(start)):
        
        match start[i]:
            case 'X':
                continue
            case 'R':
                if j > len(end):
                    return False
                while end[j] != 'R':
                    j += 1
                    if j >= len(end) or end[j] == 'L':
                        return False
                if j < i:
                    return False
            case 'L':
                if j > len(end):
                    return False
                while end[j] != 'L':
                    j += 1
                    if j > i or end[j] == 'R':
                        return False
        
        j += 1

    for k in range(j, len(end)):
        if end[k] != 'X':
            return False

    return True


print(canTransform2("XRRXL", "XRRLX"))
