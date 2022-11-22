class Solution:
    def search(nums, target):
        if nums[0] == target:
            return 0
        if nums[-1] == target:
            return len(nums)-1 

        i = 0
        j = len(nums) -1
        while i < j:

            k = ( i + j ) // 2

            if target == nums[k]:
                return k
            
            if target > nums[k]:
                i = k + 1
            else:
                j = k - 1
        return -1
    # simplified and changed variables names to l, r, c
    def search2(nums, target):
        l = 0
        r = len(nums) -1
        while l <= r:
            c = ( l + r ) // 2
            if target == nums[c]:
                return c
            if target > nums[c]:
                l = c + 1
            else:
                r = c - 1
        return -1
