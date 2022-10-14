def canJump(nums):
    if len(nums) == 1:
        return True
    for i in range(len(nums)-2,-1,-1):
        if nums[i] == 0:
            gap = 1
            while( gap <= i and nums[i-gap] < gap+1):
                gap += 1
            if gap == i + 1:
                return False
            i = i - gap
    return True

def canJump2(nums):
    reach = 0
    for i in range(len(nums)-1):
        if nums[i] == 0:
            if i >= reach:
                return False
        else:
            reach = max(reach, i + nums[i])
            if reach >= len(nums)-1:
                return True
    return True

def canJumpErik(nums):
    good_position = len(nums) - 1
    for i in range(len(nums)-2,-1,-1):
        if i + nums[i] >= good_position:
            good_position = i
    return not bool(good_position)





print(canJump2([4,2,1,0,0]))


