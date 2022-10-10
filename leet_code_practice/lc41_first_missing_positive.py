def firstMissingPositive( nums ):
    # edge case
    if len(nums) == 1:
        if nums[0] == 1:
            return 2
        else:
            return 1
    
    # input: [1, 2, 3, 4]
    # transforms to [1, 2, 3, 4]
    # output: 5

    # input: [2, 3, -1, 1]
    # transforms to [ 1, 2, 3, 0]
    # output: 4

    # input: [3, 4, -1, 1]
    # transforms to [ 1, 0, 0, 0]
    # output: 2

    l = len(nums)
    i = 0
    while i < l:
        # if number is negative, discard we dont care about it
        # if number is greater than length of array, discard we dont care about it
        if nums[i] <= 0 or nums[i] > l:
            nums[i] = nums[l-1]
            nums[l-1] = 0
            l -= 1
        # number is still needed and in correct position, increment i
        elif nums[i] == i + 1:
            i += 1
        # number is still needed, move to correct position
        else:
            j = nums[i] - 1
            # position j already has it's correct value, we can safely discard num[i] to end of array
            if nums[j] == j + 1:
                nums[i] = nums[l-1]
                nums[l-1] = 0
                l -= 1
            # else swap with num[j]
            else:
                nums[j], nums[i] = nums[i], nums[j]
    
    #increment through transformed array and find first missing number
    for i in range(len(nums)):
        if nums[i] != i + 1:
            return i + 1
    
    return i + 2

nums1 = [1, 1]
print(firstMissingPositive(nums1))

print(nums1)