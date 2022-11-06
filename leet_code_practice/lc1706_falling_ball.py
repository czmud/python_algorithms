class Solution:
    def findBall(self, grid):
        width = len(grid[0])
        # results array initialized with ball starting columns
        # Value = index to start
        results = [j for j in range(width)]

        for j in results:
            # b used to track position of ball through each layer
            b = j
            i = 0
            while i < len(grid):
                match grid[i][b]:
                    case 1:
                        # if right edge or we form a v
                        # set b to -1 and break current loop
                        if b + 1 >= width or grid[i][b+1] == -1:
                            b = -1
                            break
                        b += 1
                    case -1:
                        # if left edge or we form a v
                        # set b to -1 and break current loop
                        if b == 0 or grid[i][b-1] == 1:
                            b = -1
                            break
                        b -= 1
                i += 1
            results[j] = b
        return results
    
    # slightly modified approach that marks visited squares = 0 if they stop the ball
    # conclusion is that this modification makes the problem slower
    # We avoid repeated logic at the expense of many extra write operations
    def findBall2(self, grid):
        results = [j for j in range(len(grid[0]))]

        for i in range(len(grid)):
            if grid[i][0] == -1:
                grid[i][0] = 0
            if grid[i][-1] == 1:
                grid[i][-1] = 0

        for j in results:
            # b used to track position of ball through each layer
            b = j
            i = 0
            while i < len(grid):
                match grid[i][b]:
                    case 0:
                        b = -1
                        break
                    case 1:
                        # if right edge or we form a v
                        # set b to -1 and break current loop
                        if grid[i][b+1] == -1:
                            grid[i][b] = 0
                            grid[i][b+1] = 0
                            b = -1
                            break
                        b += 1
                    case -1:
                        # if left edge or we form a v
                        # set b to -1 and break current loop
                        if grid[i][b-1] == 1:
                            grid[i][b] = 0
                            grid[i][b-1] = 0
                            b = -1
                            break
                        b -= 1
                i += 1
            results[j] = b
        return results
