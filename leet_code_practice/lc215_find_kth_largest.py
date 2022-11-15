import heapq

#read documentation for heapq and realized how .nlargest() works
# heapify(nums) is no longer necessary, given .nlargest() is already doing a similar max heapify in the background
# https://github.com/python/cpython/blob/3.11/Lib/heapq.py
class Solution:
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums )[-1]

nums1 = [1, 2, 3, 4, 5, 6, 7, 8]

solution = Solution()
print(solution.findKthLargest(nums1, 3))
