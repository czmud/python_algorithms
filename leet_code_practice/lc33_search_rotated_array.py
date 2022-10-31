def search(nums, target):
    if nums[0] == target:
        return 0
    if nums[-1] == target:
        return len(nums) - 1
    if len(nums) == 1:
        return -1

    i = 0
    j = len(nums) - 1
    # binary search for pivot position
    while i < j:

        k = (i + j ) // 2
        if nums[k] > nums[k+1]:
            break

        if nums[k] > nums[i]:
            i = k + 1
        else:
            j = k

    if target > nums[0]:
        i = 0
        j = k
    else:
        i = k+1
        j = len(nums) - 1

    while i < j:
        k = (i + j ) // 2
        if target == nums[k]:
            return k

        if target > nums[k]:
            i = k + 1
        else:
            j = k

    if target == nums[i]:
        return i
    if target == nums[j]:
        return j
    return -1


array1 = [4,5,6,7,8,9,2,3]

print(search(array1, 9))