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

nums1 = [-4, -3, -2, -1, 0, 1, 2, 3, 4,]

solution = Solution()

print(bin(-9223372036854775808))
solution.sortArray2(nums1)

