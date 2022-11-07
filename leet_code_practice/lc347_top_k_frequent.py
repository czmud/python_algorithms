import heapq

class Solution:
    def topKFrequent(self, nums, k):
        if k == 0:
            return []

        frequency = {}
        for i in range(len(nums)):
            if nums[i] not in frequency:
                frequency[nums[i]] = 1
            else:
                frequency[nums[i]] += 1
        
        if k == 1:
            return [max(frequency, key=frequency.get)]
        
        min_heap = []
        for n in frequency.keys():
            heapq.heappush(min_heap, (frequency[n], n))
        
        max_k = heapq.nlargest(k, min_heap)

        return [a[1] for a in max_k]