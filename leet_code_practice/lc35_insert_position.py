def searchInsert(nums, target):
    if nums[0] >= target:
        return 0
    for i in range(1, len(nums)):
        if nums[i] >= target:
            return i
    return len(nums)
print(searchInsert([5], 2))
