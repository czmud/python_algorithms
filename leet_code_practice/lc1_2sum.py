class Solution:
    def twoSum(self, nums, target):
        num_pos = {}
        for i in range(len(nums)):
            if nums[i] in num_pos:
                num_pos[nums[i]].append(i)
            else:
                num_pos[nums[i]] = [i]

        nums.sort() # O(n logn) to sort
        for i in range(len(nums)-1): # O( n logn ) to complete n binary searches
            if self.binarySearch(nums[i+1:], target-nums[i]):
                x = num_pos[nums[i]].pop()
                y = num_pos[target - nums[i]].pop()
                return [x, y]
        return []

    def binarySearch(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            c = (l+r) // 2
            if nums[c] == target:
                return True

            if nums[c] < target:
                l = c + 1
            else:
                r = c - 1
        return False
    # can reduce to O(n) with hash table
    def twoSumHashTable(self, nums, target):
        num_hash = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in num_hash:
                return([i, num_hash[comp]])
            num_hash[nums[i]] = i
        return []
