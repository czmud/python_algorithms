# brute force approach
def maximalSquare(matrix):
    max_side = min(len(matrix), len(matrix[0]))

    result_max = 0

    i = 0
    while i < len(matrix) - result_max:
        for j in range(len(matrix[i])):
            if matrix[i][j] == "0":
                continue

            # ripple
            r = 1
            rippling = True
            while( i + r < len(matrix) and j + r < len(matrix[i])):
                for ri in range(i, i + r + 1):
                    if matrix[ri][j+r] == "0":
                        rippling = False
                        break
                if rippling:
                    for rj in range(j, j + r ):
                        if matrix[i + r][rj] == "0":
                            rippling = False
                            break
                if rippling:
                    r += 1
                else:
                    break
            result_max = max(result_max, r)
        i += 1
    return result_max * result_max

# dynamic programming approach - break into smaller squares
def maximalSquare(matrix):
    result_max = matrix[0][0] = int(matrix[0][0])
    for j in range(1,len(matrix[0])):
        matrix[0][j] = int(matrix[0][j])
        result_max = max(result_max, matrix[0][j])
    for i in range(1,len(matrix)):
        matrix[i][0] = int(matrix[i][0])
        result_max = max(result_max, matrix[i][0])
        for j in range(1,len(matrix[i])):
            if matrix[i][j] == "0":
                continue
            matrix[i][j] = min(matrix[i-1][j], matrix[i-1][j-1], matrix[i][j-1]) + 1
            result_max = max(result_max, matrix[i][j])
    return result_max * result_max

test_matrix = [["1","1"],["1","1"]]

print(maximalSquare(test_matrix))



