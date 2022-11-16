import heapq
import math
import random

#read documentation for heapq and realized how .nlargest() works
# heapify(nums) is no longer necessary, given .nlargest() is already doing a similar max heapify in the background
# https://github.com/python/cpython/blob/3.11/Lib/heapq.py
class Solution:
    def findKthLargest1(self, nums, k):
        return heapq.nlargest(k, nums )[-1]
    def findKthLargest2(self, nums, k):
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]
    def findKthLargest(self, nums, k):
        p = random.choice(nums)
        
        g = []
        e = []
        l = []
        for num in nums:
            if num > p:
                g.append(num)
            elif num == p:
                e.append(num)
            else:
                l.append(num)
        
        if len[g] >= k:
            return self.findKthLargest( g, k )
        elif len[l] > len[nums] - k:
            return self.findKthLargest( l, k - len(e) - len(g) )
        return e[0]



nums1 = [11, 12, 13, 14, 15, 16, 17, 18]

solution = Solution()
print(solution.findKthLargestQuickSelect(nums1, 3))
