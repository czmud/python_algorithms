# learning bitwise operations
class Solution:
    def singleNumber(self, nums):
        n = 0
        for i in range(len(nums)):
            n ^= nums[i]
        return n