class Solution:
    def __init__(self):
        self.paths = []

    def canIWin(self, maxChoosableInteger, desiredTotal):
        nums = [i for i in range(1, maxChoosableInteger+1)]
        moves = []
        return self.iChoose(nums, desiredTotal, moves)

    def iChoose(self, nums, desiredTotal, moves):
        if len(nums) == 0:
            self.paths.append(moves)
            return False
        
        if nums[-1] >= desiredTotal:
            self.paths.append(moves + [nums[-1]])
            return True

        if len(nums) == 1:
            self.paths.append(moves + [nums[0]])
            return False

        # can we make it another round?
        if nums[-1] >= desiredTotal + nums[0]:
            self.paths.append(moves + [nums[0]] + [-nums[-1]])
            return False

        i = 0
        # else try all the solutions where we don't automatically loose
        while i < len(nums) and nums[i] < desiredTotal - nums[-1]:
            if not self.friendChoose(nums[:i]+nums[i+1:], desiredTotal - nums[i], moves + [nums[i]]):
                return True
            i += 1
        return False

    def friendChoose(self, nums, desiredTotal, moves):
        print(moves)
        if nums[-1] >= desiredTotal + nums[0]:
            self.paths.append(moves + [-nums[0]] + [nums[-1]])
            return False
        
        i = 0
        while i < len(nums) and nums[i] < desiredTotal - nums[-1]:
            if not self.iChoose(nums[:i]+nums[i+1:], desiredTotal - nums[i], moves + [-nums[i]]):
                return True
            i += 1
        return False

class Solution2:
    def __init__(self):
        self.bit_hash = {}
    def canIWin(self, maxChoosableInteger, desiredTotal):
        nums = [i for i in range(1, maxChoosableInteger+1)]
        bit_mask = 0
        for num in nums:
            bit_mask ^= num
        self.bit_hash[bit_mask] = nums

        return self.iChoose(nums, desiredTotal)

    def friendChoose(self, nums, desiredTotal):
        if nums[-1] >= desiredTotal + nums[0]:
            return False
        
        i = 0
        while i < len(nums) and nums[i] < desiredTotal - nums[-1]:
            if not self.iChoose(nums[:i]+nums[i+1:], desiredTotal - nums[i]):
                return True
            i += 1
        return False

    def iChoose(self, nums, desiredTotal):
        if len(nums) == 0:
            return False
        
        if nums[-1] >= desiredTotal:
            return True

        if len(nums) == 1:
            return False

        # can we make it another round?
        if nums[-1] >= desiredTotal + nums[0]:
            return False

        i = 0
        # else try all the solutions where we don't automatically loose
        while i < len(nums) and nums[i] < desiredTotal - nums[-1]:
            if not self.friendChoose(nums[:i]+nums[i+1:], desiredTotal - nums[i]):
                return True
            i += 1
        return False

class Solution3:
    def __init__(self):
        self.decode = {}
        self.solutions = {}

    def canIWin(self, maxChoosableInteger, desiredTotal):
        M = maxChoosableInteger
        N = desiredTotal

        # summation formula check from Erik
        if M * (M+1) < 2 * N:
            return False

        for i in range(M):
            bit = 1 << i
            self.decode[bit] = i+1
        bitmap = (1 << M) - 1

        return self.canWinFromHere(bitmap, desiredTotal)

    def canWinFromHere(self, bitmap, desiredTotal):
        if bitmap in self.solutions:
            return self.solutions[bitmap]

        safeNextTarget = desiredTotal - self.decode[self.leftMostBit(bitmap)]
        if safeNextTarget <= 0:
            self.solutions[bitmap] = True
            return True

        b = bitmap
        while b:
            i = b & -b
            if safeNextTarget - self.decode[i] <= 0:
                break
            if not self.canWinFromHere(bitmap & ~i, desiredTotal - self.decode[i]):
                self.solutions[bitmap] = True
                return True
            b = b & ~i
        self.solutions[bitmap] = False
        return False
        
    def leftMostBit(self, n):
        l = 0
        while n > 1:
            l += 1
            n = n >> 1
        return 1 << l


solution = Solution3() 
print(solution.canIWin(5, 12))
for sol, val in solution.solutions.items():
    print(f'{bin(sol)}: {val}')

res = {
    146: True,
    147: True,
    148: True,
    149: True,
    150: True,
    151: True,
    152: False,
    157: True,
    158: False,
    159: True
}
