class Solution:
    def permute(self, nums: List[int] ) -> List[List[int]]:
        results = []
        if len(nums) == 1:
            results.append(nums)
            return results
        
        for i in range(len(nums)):
            next_seed = [nums[i]]
            results += self.helper( nums[0:i]+nums[i+1:len(nums)], next_seed)
        return results
    
    def helper(self, nums, seed):
        if len(nums) == 1:
            return [seed + [nums[0]]]
        results = []
        for i in range(len(nums)):
            next_seed = seed + [nums[i]]
            results += self.helper( nums[0:i]+nums[i+1:len(nums)], next_seed)
        return results