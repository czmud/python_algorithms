
# simple recursive solution. Breaks/times-out as n increases.
def climbStairs( n ):
    if n < 2:
        return 1
    if n < 3:
        return 2

    sum_one = climbStairs( n - 1 )
    sum_two = climbStairs( n - 2 )

    return sum_one + sum_two


#copied memoized solution from @OldCodingFarmer
class Solution:
    def __init__(self):
        self.dic = {1:1, 2:2}

    def climbStairs(self, n):
        if n not in self.dic:
            self.dic[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dic[n]


solution1 = Solution()

print(climbStairs(20))
print(solution1.climbStairs(38))