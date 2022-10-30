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
