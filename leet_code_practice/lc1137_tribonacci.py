# Recursive solution with memoization
class Solution:
    def __init__(self):
        self.memo = {
            0: 0,
            1: 1,
            2: 1
        }
    
    def tribonacci(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
    
        self.memo[n] = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        
        return self.memo[n]

# dynamic bottom up solution
def tribonacci2(n):
    if n == 0:
        return 0
    if n == 1 or n ==2:
        return 1
    
    t0 = 0
    t1 = 1
    t2 = 1
    
    for i in range(1, n):
        t = t2 + t1 + t0
        t0 = t1
        t1 = t2
        t2 = t
    return t