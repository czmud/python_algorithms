def reverse(x: int) -> int:
    x_str = str(x)
    if len(x_str) <= 1:
        return x

    result_str = ""
    end = -1
    if x < 0:
        end = 0

    for i in range(len(x_str)-1, end, -1):
        result_str += x_str[i]
    
    
    if len(result_str) < 10:
        if end < 0:
            return int(result_str)
        else:
            return int("-"+result_str)
    
    test = [ 2, 1, 4, 7, 4, 8, 3, 6, 4, 8]

    for j in range(10):
        if( int(result_str[j]) > test[j]):
            return 0
        if( int(result_str[j]) < test[j]):
            break
    
    if end < 0:
        if( int(result_str[9]) > 7 ):
            return 0
        else:
            return int(result_str)

    return int("-"+result_str)

print(reverse(8463847412))



