def findMin(nums):
    if nums[0] <= nums[-1]:
        return nums[0]
    
    i = 0
    j = len(nums) -1

    while i < j:
        k = ( i + j ) // 2

        if nums[k] > nums[k+1]:
            return nums[k+1]
        
        if nums[k] > nums[i]:
            i = k + 1
        else:
            j = k
