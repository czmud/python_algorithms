class Solution:
    def uniquePaths(self, m, n):
        if m == 1 or n == 1:
            return 1
        # the "dynamic" aspect of this problem is seeing that
        # uniquePaths(n, m) = uniquePaths(n-1, m) + uniquePaths(n, m-1)
        # thus we can start at the smallest solution and add up from there
        squares = {
            (0,0): 0,
            (0,1): 1,
            (1,0): 1
        }
        squeue = [(0,0)] #square queue for looping through squares

        i = 0
        while i < len(squeue):
            y, x = squeue[i]
            
            # add current case to dict
            if (y, x) not in squares:
                if y == 0 or x == 0:
                    squares[(y, x)] = 1
                else:
                    squares[(y, x)] = squares[(y-1, x)] + squares[(y, x-1)]
            
            # generate next squeue
            if y < m-1:
                squeue.append((y+1, x))
                if y == 0 and x < n-1:
                    squeue.append((y, x+1))
            
            i += 1

        return squares[(m-1,n-1)]

    def uniquePaths2(self, m, n):
        if m == 1 or n == 1:
            return 1
        
        rows = {0: 1}
        squeue = [(i,0) for i in range(m)]

        i = 0
        while i < len(squeue):
            y, x = squeue[i]
            
            if y not in rows:
                rows[y] = 1
            elif y != 0:
                rows[y] += rows[y-1]
                # this is essentially saying squares(y, x) = squares(y, x-1) + squares(y-1, x)
                #                               row[y]    ->   row[y]      +    row[y-1]   
                # and then we are 'discarding' squares(y, x-1) because we no longer need this value
            
            if x < n - 1:
                squeue.append((y, x+1))
            
            i += 1

        return rows[m-1]



solution1 = Solution()

print(solution1.uniquePaths(3, 7))