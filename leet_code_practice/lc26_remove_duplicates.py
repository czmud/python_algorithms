def removeDuplicates( nums ):
    k = 1
    for i in range(len(nums)):
        if nums[i] != nums[k - 1]:
            nums[k] = nums[i]
            k += 1
    return k
