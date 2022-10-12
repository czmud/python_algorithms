from math import comb
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
                self.memo[memo_str] = ( left + right ) % (10**9+7)
        return self.memo[memo_str]

# copy of same solution, this time testing tuples as memo key instead of strings
class Solution2:
    def __init__(self):
        self.memo = {}
    def numberOfWays(self, startPos, endPos, k):
        
        delta = abs(endPos - startPos)
        dof = k - delta
        if delta > k or ( endPos + startPos + k ) % 2 == 1:
            return 0
        
        memo_tup = (k, startPos)
        if memo_tup not in self.memo:
            if dof == 0:
                self.memo[memo_tup] = 1
            else:
                left = 0
                right = 0
                if startPos > endPos or dof > 0:
                    left = self.numberOfWays(startPos - 1, endPos, k - 1 )
                if startPos < endPos or dof > 0:
                    right = self.numberOfWays(startPos + 1, endPos, k - 1 )
                self.memo[memo_tup] = ( left + right ) % (10**9+7)
        return self.memo[memo_tup]

# 1 liner using math.comb
class Solution3:
    def numberOfWays(self, startPos, endPos, k):
        return 0 if (startPos-endPos+k) % 2 or (startPos-endPos+k) < 0 else comb(k, (startPos-endPos+k)//2) % (10**9+7)



solution2 = Solution2()

print(solution2.numberOfWays(0, 3, 53))