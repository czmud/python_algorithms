class Solution:
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        while n > 1:
            m = n >> 1
            if m << 1 != n:
                return False
            n = m
        return True
    def isPowerOfTwo2(self, n):
        if n <= 0:
            return False
        return not (n & n - 1)

solution = Solution()

print(solution.isPowerOfTwo(16))


print("{0:b}".format(9))
print(str(bin(-50)))