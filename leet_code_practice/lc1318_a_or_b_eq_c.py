class Solution:
    def minFlips(self, a, b, c):
        # since we can only change bits in a or b
        # we are forced to double count incorrect 1s
        # but single count incorrect 0s

        # n is all the 1s in a that need to change to 0 (to match c)
        n = a ^ ( a & c )
        # m is all the 1s in b that need to change to 0 (to match c)
        m = b ^ ( b & c )
        # o is all the 0s common to a | b that need to change to 1 (to match c)
        o = c ^ ( c & ( a | b))

        return self.count_ones(n) + self.count_ones(m) + self.count_ones(o)

    # This is based on Brian Kernighan's algorithm for counting the ones in a binary string
    # if we have 6 = (0110)
    # 1: 6 & 5 = 0110 & 0101 = 0100
    # 2: 4 & 3 = 0100 & 0011 = 0000
    # num now equals to 0. Break while loop and return count = 2
    def count_ones(self, num):
        count = 0
        while num != 0:
            num = num & ( num - 1 )
            count += 1
        return count