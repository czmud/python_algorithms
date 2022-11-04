# Beats 99%!
class Solution:
    def __init__(self):
        self.components = {}
        self.parts = {}

    # Set problem up in main function
    def findMaxForm(self, strs, m, n ):
        for string in strs:    
            key = self.decompose(string)

            # use key (zeroes, ones) in hash table to count the number of equivalent strings
            # since the desirability of a string is order-agnostic, we can combine many strings into the same key
            # for example "001", "010", and "100" all decompose -> (1, 2)
            # adding any of these three strings affects our count equally
            if key not in self.parts:
                self.parts[key] = 1
            else:
                self.parts[key] += 1
        # generate list of all the keys in our parts dictionary for iterating through
        parts_keys = list(self.parts.keys())
        return self.findMaxRecursive( parts_keys, m, n)

    # Recurse through combinations and return max
    def findMaxRecursive(self, keys, m, n):
        if not keys:
            return 0
        
        count = self.parts[keys[0]]

        # Optimization
        # Since "0" -> (0, 1) and "1" -> (1, 0) never threaten the future addition of better combinations
        # we can safely add as many as possible, up to the constraint of <= m and <= n, respectively
        match keys[0]:
            case (1, 0):
                count = min(count, m)
                return count + self.findMaxRecursive( keys[1:], m - count, n )
            case (0, 1):
                count = min(count, n)
                return count + self.findMaxRecursive( keys[1:], m, n - count )

        # solve reject case first before iterating through the rest
        # we know the reject case is always possible
        # so even if while loop never executes, we sill have something to return
        result_max = self.findMaxRecursive(keys[1:], m, n)

        i = 1
        i_m = keys[0][0]
        i_n = keys[0][1]
        while i <= count and i*i_m <= m and i*i_n <= n:
            result_max = max(result_max, i + self.findMaxRecursive(keys[1:], m - (i*i_m), n - (i*i_n)))

            i += 1
        
        
        return result_max

    # helper function to break values into their component 0s and 1s
    def decompose(self, s):
        if s not in self.components:
            z = 0
            o = 0
            for c in s:
                match c:
                    case "0":
                        z += 1
                    case "1":
                        o += 1
            self.components[s] = (z, o)
        return self.components[s]

strs1 = ["011","1","11","0","010","1","10","1","1","0","0","0","01111","011","11","00","11","10","1","0","0","0","0","101","001110","1","0","1","0","0","10","00100","0","10","1","1","1","011","11","11","10","10","0000","01","1","10","0"]
solution = Solution()
results = solution.findMaxForm(strs1, 18, 15)
print(results)

