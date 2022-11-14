import heapq
class Solution:
    def findKthLargest(self, nums, k):
        heapq.heapify(nums)
        return heapq.nlargest(k, nums )[-1]
