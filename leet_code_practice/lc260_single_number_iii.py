class Solution:
    def singleNumber(self, nums):
        # initial bitmask
        n = 0
        for num in nums:
            n = n^num

        # if our two single values are x and y
        # then we now have found n == x^y
        
        # let's uncover the larger number and call it y
        y = 0
        for num in nums:
            # we use the following test to selectively only let the larger of x and y through
            # some of the pairs will pass through this filter, others will not
            # we don't really care. If we have nums [a, a, b, b, x, y ]
            # if one a get's through, then both a will. If b doesn't get through, then neither b will
            if num > n^num:
                y = y^num

        # now we use y to extract x from n
        x = n^y
        return [x, y]

solution = Solution()

print(solution.singleNumber([7, 4, 3, 1, 4, 3, 5, 1, 7, 6]))