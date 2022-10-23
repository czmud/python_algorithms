def missingNumber(nums):
    
    i = 0
    j = len(nums) - 1
    while i < len(nums):
        if nums[i] == i:
            i += 1
            continue
        if nums[i] == len(nums):
            while nums[j] == j:
                j -= 1
            if i == j:
                return i
            nums[i], nums[j] = nums[j], nums[i]
            continue
        temp = nums[i]
        nums[i] = nums[temp]
        nums[temp] = temp

    return len(nums)