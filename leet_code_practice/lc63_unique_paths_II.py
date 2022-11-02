class Solution:
    def uniquePathsWithObstacles(obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if m == 1:
            for x in range(n):
                if obstacleGrid[0][x] == 1:
                    return 0
            return 1
        if n == 1:
            for y in range(m):
                if obstacleGrid[y][0] == 1:
                    return 0
            return 1
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        
        rows = {0: 1}
        squeue = [(i,0) for i in range(m)]

        i = 0
        while i < len(squeue):
            y, x = squeue[i]
            
            if obstacleGrid[y][x] == 1:
                rows[y] = 0
            elif y not in rows:
                rows[y] = rows[y-1]
            elif y != 0:
                rows[y] += rows[y-1]

            # generate next cases and append to squeue
            if x < n - 1:
                squeue.append((y, x+1))
            
            i += 1

        return rows[m-1]
    
    # using in place memory
    def uniquePathsWithObstacles2(obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0
        obstacleGrid[0][0] = 1

        for x in range(1, n):
            if obstacleGrid[0][x] == 1:
                obstacleGrid[0][x] = 0
            else:
                obstacleGrid[0][x] = obstacleGrid[0][x-1]
        for y in range(1, m):
            if obstacleGrid[y][0] == 1:
                obstacleGrid[y][0] = 0
            else:
                obstacleGrid[y][0] = obstacleGrid[y-1][0]
            for x in range(1, n):
                if obstacleGrid[y][x] == 1:
                    obstacleGrid[y][x] = 0
                else:
                    obstacleGrid[y][x] = obstacleGrid[y-1][x] + obstacleGrid[y][x-1]
        return obstacleGrid[-1][-1]

obstacles1 = [[0,0,0],[0,1,0],[0,0,0]]
solution1 = Solution()

print(solution1.uniquePathsWithObstacles(obstacles1))