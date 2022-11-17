import heapq
class Solution:
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