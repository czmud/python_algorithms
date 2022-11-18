import heapq
class Solution:
    # using heaps
    def findClosestElements(self, arr, k, x):
        if len(arr) == k:
            return arr
        
        # make heap for the first k+1 items in the form of:
        # (-distance, -val, index)
        # this will keep our furthest numbers at the top of min heap
        # ties for distance will be broken by largest value
        dist_heap = [(-abs(arr[i] - x),-arr[i], i) for i in range(k+1)]
        heapq.heapify(dist_heap)

        # pushpop all remaining numbers in arr
        for i in range(k+1, len(arr)):
            heapq.heappushpop(dist_heap, (-abs(arr[i]-x),-arr[i], i))
        # finally pop the k+1 extra value we had in our array.
        heapq.heappop(dist_heap)

        # now instead of sorting, let's find the smallest index
        # this will allow us to slice our answer directly out of original arr
        
        # generate heap of indicies
        indx_heap = [a[2] for a in dist_heap]
        heapq.heapify(indx_heap)
        # set h equal to smallest index
        h = indx_heap[0]
        
        if h == 0:
            return arr[:k]
        return arr[h:h+k]

    # sliding window approach
    def findClosestElements1(self, arr, k, x):
        if len(arr) <= k:
            return arr
        if x <= arr[0]:
            return arr[:k]
        if x >= arr[-1]:
            return arr[-k:]
        

        i = len(arr) - k
        while i > 0 and abs( arr[i-1] - x ) <= abs( arr[i-1+k] - x ):
            i -= 1
        return arr[i:i+k]
    
    # non ideal solution
    def findClosestElements2(self, arr, k, x):
        if len(arr) <= k:
            return arr
        if x <= arr[0]:
            return arr[:k]
        if x >= arr[-1]:
            return arr[-k:]

        # generate new array with absolute difference
        arr_diff = [abs( n - x ) for n in arr]
        d_sum = sum(arr_diff[:k])

        # generate array of summation of k next abs differences
        arr_sums = [d_sum]
        for i in range(len(arr_diff)-k):
            d_sum = d_sum - arr_diff[i] + arr_diff[i+k]
            arr_sums.append(d_sum)

        # move back to front until we hit a larger sum
        j = len(arr_sums) - 1
        while j > 0 and arr_sums[j-1] <= arr_sums[j]:
            j -= 1
        
        # slice original sum using index j
        return arr[j:j+k]