# the best solution for this problem computationally uses probability to calculate
# thought it would be fun to devise a recursive solution instead
# memoization added to decrease time complexity
class Solution:
    def __init__(self):
        self.memo = {}
    def numberOfWays(self, startPos, endPos, k):
        
        delta = abs(endPos - startPos)
        dof = k - delta
        if delta > k or ( endPos + startPos + k ) % 2 == 1:
            return 0
        
        memo_str = f'{k}-{startPos}'
        if memo_str not in self.memo:
            if dof == 0:
                self.memo[memo_str] = 1
            else:
                left = 0
                right = 0
                if startPos > endPos or dof > 0:
                    left = self.numberOfWays(startPos - 1, endPos, k - 1 )
                if startPos < endPos or dof > 0:
                    right = self.numberOfWays(startPos + 1, endPos, k - 1 )
                self.memo[memo_str] = left + right
        return self.memo[memo_str] % (10**9+7)

solution1 = Solution()

print(solution1.numberOfWays(0, 3, 53))