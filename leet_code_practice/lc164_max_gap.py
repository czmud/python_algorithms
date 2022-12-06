import math

# experimenting with bucket sort
class Solution:
    def maximumGap(self, nums):
        l = len(nums)
        if l < 2:
            return 0
        
        next_k = min(l, max(6, math.ceil(math.log2(l))))

        nums = self.bucketSort(nums, next_k)

        max_gap = 0
        for i in range(1, l):
            next_gap = nums[i] - nums[i-1]
            max_gap = max(max_gap, next_gap)
        
        return max_gap

    def bucketSort(self, nums, k):
        buckets = [[] for _ in range(k)]
        max_num = max(nums) + 1
        min_num = min(nums)

        for num in nums:
            bucket_index = (k * (num - min_num)) // (max_num - min_num)
            buckets[bucket_index].append(num)
        
        nums = []
        for bucket in buckets:
            l = len(bucket)
            match l:
                case 0:
                    pass
                case 1:
                    nums += bucket
                case 2:
                    nums += [min(bucket), max(bucket)]
                case _:
                    if min(bucket) == max(bucket):
                        nums += bucket
                    else:
                        next_k = min(l, max(6, math.ceil(math.log2(l))))
                        nums += self.bucketSort(bucket, next_k)

        return nums

