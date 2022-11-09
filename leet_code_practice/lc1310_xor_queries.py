class Solution:
    def xorQueries(self, arr, queries):
        for i in range(1,len(arr)):
            arr[i] ^= arr[i-1]
        arr.append(0)

        res = []
        for q in queries:
            l, r = q
            res.append(arr[l - 1]^arr[r])

        return res