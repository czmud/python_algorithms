def maxSubArray(nums):
    return_max = nums[0]
    maximus = 0
    for num in nums:
        maximus += num
        return_max = max(return_max, maximus )
        maximus = max(0, maximus)
    return return_max