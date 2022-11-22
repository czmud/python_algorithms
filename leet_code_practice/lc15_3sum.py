class Solution:
    def threeSumNaive(self, nums):
        res = []
        triplets = {}
        nums.sort()
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if (nums[i], nums[j], nums[k]) not in triplets:
                        if nums[i] + nums[j] + nums[k] == 0:
                            triplets[(nums[i], nums[j], nums[k])] = True
                            res.append([nums[i], nums[j], nums[k]])
                        else:
                            triplets[(nums[i], nums[j], nums[k])] = False
        return res
    def threeSum(self, nums):
        triplets = set()
        num_hash = set()

        nums.sort()
        
        res = []
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                comp = -(nums[i] + nums[j])
                if comp in num_hash:
                    triplets.add((nums[i], nums[j], comp))
            num_hash.add(nums[i])

        return [[x, y, z] for (x, y, z) in triplets]