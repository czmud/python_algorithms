# this was the original solution that I came up with on my own
def nextPermutation( nums ):
    # 1. edge case. we can return immediately if 1 or less numbers in array
    if len(nums) <= 1:
        return
    big_brother = nums[-1]

    # 2. work backwards to find first smaller position (baby_brother)
    # this will be the position from which we start swapping
    for i in range(len(nums)-2, -1, -1):
        if nums[i] >= big_brother:
            big_brother = nums[i]
        else:
            break
    
    # 3. now look for next biggest number to swap with baby_brother
    # step 3 gets skipped if entire array already in lex order
    if nums[i] != big_brother:
        b = i + 1
        for j in range(i+1,len(nums)):
            if nums[i] < nums[j] and nums[j] < big_brother:
                big_brother = nums[j]
                b = j
        nums[i], nums[b] = nums[b], nums[i]
        # increment i, we do not want to include baby_brother in our final sort
        i += 1
    
    # now sort remainder of array in ascending order
    nums[i::] = sorted(nums[i::])

    return


# but then after looking at other submissions, I realized another trick
# Which somehow magically, we don't need to sort the remaining array
# we only need to reverse it, because we know it is already in lex order
# if not step #2 would have stopped at an earlier position
def nextPermutation( nums ):
    # 1.
    if len(nums) <= 1:
        return
    big_brother = nums[-1]

    # 2.
    for i in range(len(nums)-2, -1, -1):
        if nums[i] >= big_brother:
            big_brother = nums[i]
        else:
            break
    
    # 3.
    if nums[i] != big_brother:
        b = i + 1
        for j in range(i+1,len(nums)):
            # had to adjust to use '<=' to swap with last position found for repeat numbers
            if nums[i] < nums[j] and nums[j] <= big_brother:
                big_brother = nums[j]
                b = j
        nums[i], nums[b] = nums[b], nums[i]
        i += 1
    
    # 4. now REVERSE remainder of array -> ascending order
    nums[i::] = reversed(nums[i::])

    return

numbers = [2,3,1,3,3]
nextPermutation(numbers)
print(numbers)