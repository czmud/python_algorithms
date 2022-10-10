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

def firstMissingPositive2( nums ):
    if len(nums) == 1:
        return 2 if nums[0] == 1 else 1

    count = 0
    l = len(nums)
    i = 0
    while i < l:
        count += 1
        if nums[i] <= 0 or nums[i] > l:
            nums[i] = nums[l-1]
            l -= 1
        elif nums[i] == i + 1:
            i += 1
        else:
            j = nums[i] - 1
            if nums[j] == j + 1:
                nums[i] = nums[l-1]
                l -= 1
            else:
                nums[j], nums[i] = nums[i], nums[j]

    print(f'count: {count}')
    return i + 1

# general explanation of time complexity
# this solution is O(n)
# we are bounded by 1n<= operation_count < 2n
# nums_arr = [
#     [*, *, *, *], # count: 4 (8 - 4)
#     [*, *, 4, 3], # count: 5 (8 - 2* - 1swap)
#     [*, 3, 2, *], # count: 5 (8 - 2* - 1swap)
#     [*, 3, 4, 2], # count: 6 (8 - 1* - 1swap)
#     [2, 1, *, *], # count: 5 (8 - 2* - 1swap)
#     [2, 1, 4, 3], # count: 6 (8 - 0* - 2swap)
#     [2, 3, 1, *], # count: 6 (8 - 1* - 1swap)
#     [2, 3, 4, 1], # count: 7 (8 - )
#     [3, 1, 2, *], # count: 6 (8 - )
#     [3, 1, 4, 2], # count: 7 (8 - )
#     [3, *, 1, *], # count: 5 (8 - )
#     [3, *, 4, 1], # count: 6 (8 - )
#     [4, 1, 2, 3], # count: 7 (8 - )
#     [4, 1, *, 2], # count: 6 (8 - )
#     [4, *, 1, 3], # count: 6 (8 - )
#     [4, *, *, 1]  # count: 5 (8 - )
# ]

nums_arr = [
    [1, 2, 3, 4],
    [1, 2, 4, 3],
    [1, 3, 2, 4],
    [1, 3, 4, 2],
    [2, 1, 3, 4],
    [2, 1, 4, 3],
    [2, 3, 1, 4],
    [2, 3, 4, 1],
    [3, 1, 2, 4],
    [3, 1, 4, 2],
    [3, 2, 1, 4],
    [3, 2, 4, 1],
    [4, 1, 2, 3],
    [4, 1, 3, 2],
    [4, 2, 1, 3],
    [4, 2, 3, 1]
]

for nums in nums_arr:
    firstMissingPositive2(nums)



# nums1 = [8, 1, 6, 5, 7, 2, 3, 4]
# print(firstMissingPositive2(nums1))

# print(nums1)