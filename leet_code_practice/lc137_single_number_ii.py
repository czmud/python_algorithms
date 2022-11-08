class Solution:
    def singleNumber(self, nums ):
        seen_once = 0
        seen_twice = 0
        print(f'x  bin(x) | (~s_t) & (s_o^x) -> s_o | ')
        for x in nums:
            line = f'{x}  {bin3(x)}  |'
            print(bin(~seen_twice))
            seen_once = ~seen_twice & (seen_once^x)
            seen_twice = ~seen_once & (seen_twice^x)
            
            print(bin3(seen_once))
            print(bin3(seen_twice))
            print(line)
        return seen_once

def binShort(l):
    def binL(n):
        if n <= 0:
            n = -n
        b = bin(n)
        result_str = "0"*(l-len(b)+2)
        result_str += b[2:]
        return result_str
    return binL

bin3 = binShort(3)

solution = Solution()


nums1 = [5, 4, 5, 3, 3, 5, 3 ]
print(solution.singleNumber(nums1))
print(bin(5))