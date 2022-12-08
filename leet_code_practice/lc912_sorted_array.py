import random
class Solution:
    # LSD
    def sortArray(self, nums):
        radix = [[],[]]
        neg_nums = []
        pos_nums = []

        # split into negatives and positives
        # because im feeling so angsty and python is annoying
        for num in nums:
            if num < 0:
                neg_nums.append(num*-1)
            else:
                pos_nums.append(num)

        # loop 16 times to encounter all bits up to 5E4
        # log_2(50000) = 15.61 -> 16
        for p in range(16):
            # positives
            for num in pos_nums:
                sig_val = ( num >> p ) & 1
                radix[sig_val].append(num)
            pos_nums = radix[0] + radix[1]
            radix = [[],[]]

            # negatives
            for num in neg_nums:
                sig_val = ( num >> p ) & 1
                radix[sig_val].append(num)
            neg_nums = radix[0] + radix[1]
            radix = [[],[]]

        neg_nums.reverse()
        for i in range(len(neg_nums)):
            neg_nums[i] *= -1
        
        return neg_nums + pos_nums

    def sortArray2(self, nums):
        for num in nums:
            print(f'{num} {bin(num)}')
            num = num ^ -9223372036854775808
            print(f'{num} {bin(num)}')
            num = num ^ -9223372036854775808
            print(f'{num} {bin(num)}')
            print('-----')
        return



    def sortArrayErik(self, nums):
        for i in range(16):
            nums = self.CountingSort(nums, i)

        j = 0
        while j < len(nums) and nums[j] >= 0: 
            j += 1

        return nums[j:] + nums[:j]

    # stable sort of nums with sort key = bit 2^m
    def CountingSort(self, nums, m):
        length = len(nums)
        count = [0, 0]
        # output = [None] * length

        bitmap = 1 << m
        for i in range(length):
            b = 1 if nums[i] & bitmap else 0
            count[b] += 1

        count[1] = count[0] + count[1]
        mid_point = count[0]

        next_num = nums[-1]
        while count[0] > 0 or count[1] > mid_point:
            b = 1 if next_num & bitmap else 0
            match b:
                case 0:
                    count[b] -= 1
                    temp = nums[count[b]]
                    nums[count[b]] = next_num
                    next_num = temp
                case 1:
                    count[b] -= 1
                    nums[count[b]] = next_num
                    next_num = nums[count[b] - 1]

        return nums

    def sortArrayErik2(self, nums):
        for i in range(16):
            nums = self.CountingSortErik2(nums, i)

        j = 0
        while j < len(nums) and nums[j] >= 0: 
            j += 1

        return nums[j:] + nums[:j]

    # stable sort of nums with sort key = bit 2^m
    def CountingSortErik2(self, nums, m):
        length = len(nums)
        count = [0, 0]
        output = [None] * length

        bitmap = 1 << m
        for i in range(length):
            j = 1 if nums[i] & bitmap else 0
            count[j] = count[j] + 1

        count[1] = count[0] + count[1]

        for i in range(length - 1, -1, -1):
            j = 1 if nums[i] & bitmap else 0
            count[j] = count[j] - 1
            output[count[j]] = nums[i]

        return output

    def sortArrayQuick(self, nums):
        l = len(nums)

        match l:
            case 0:
                return []
            case 1:
                return nums
            case 2:
                return [min(nums), max(nums)]
            case _:
                if min(nums) == max(nums):
                    return nums
        
        pivot = random.choice(nums)

        left_nums = []
        right_nums = []
        for num in nums:
            if num < pivot:
                left_nums.append(num)
            else:
                right_nums.append(num)

        return self.sortArray(left_nums) + self.sortArray(right_nums)
    
    def sortArrayQuickInPlace(self, nums):
        right = len(nums)

        self.QuickSortInPlace(nums, 0, right )

        return nums

    def QuickSortInPlace(self, nums, left, right):
        length = right - left

        match length:
            case 0:
                return
            case 1:
                return
            case 2:
                if nums[left] > nums[right-1]:
                    nums[left], nums[right-1] = nums[right-1], nums[left]
                return

        pivot = random.choice(nums[left:right])

        p = left
        i = left
        j = right - 1
        while i <= j:
            # if larger than pivot: move to far right side of current array slice. p doesn't change.
            if nums[i] > pivot:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
                continue
            # if less than pivot: move to pivot placeholder (p). increment p.
            elif nums[i] < pivot:
                if i != p:
                    nums[i], nums[p] = nums[p], nums[i]
                p += 1
            # if equal to pivot: move nothing. p doesn't change.
            i += 1

        # if 5 was chosen as the pivot for the following array:
        # [ 2, 7, 5, 5, 9, 5, 1 ]
        #
        # then after the end of while loop, we will have a partitioned array in the form of:
        #         p     j  i
        # [ 2, 1, 5, 5, 5, 9, 7 ]
        # so we can recursively partition (left:p) and (j+1:right) 
        # to effectively exclue whatever our pivot value had been

        self.QuickSortInPlace(nums, left, p)
        self.QuickSortInPlace(nums, j+1, right)




nums1 = [-4, -3, -2, -1, 0, 1, 2, 3, 4,]

solution = Solution()

print(bin(-9223372036854775808))
solution.sortArray2(nums1)