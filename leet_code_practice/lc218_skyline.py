import heapq
class Solution:
    def getSkyline(self, buildings):
        if len(buildings) == 1:
            return [[buildings[0][0], buildings[0][2]], [buildings[0][1], 0]]
        
        # priority queue for determing next highest building:
        # ( -height, x_left, x_right )
        high_heap = []
        
        # now just imagine we have a building of 0 height spanning the entire earth
        # humans naively call this the ground
        # but as moles, we know better than that
        high_heap.append((0, 0, 2E31 - 1))

        # we mark x position as start of first building profile
        x = buildings[0][0]
        
        # add all buildings with left edge equal to first building
        i = 0
        while i < len(buildings) and buildings[i][0] == x:
            heapq.heappush(high_heap, (-buildings[i][2], buildings[i][0], buildings[i][1]))
            i += 1

        skyline = []
        while i < len(buildings):
            # remove all irrelevant buildings
            while high_heap and x >= high_heap[0][2]:
                heapq.heappop(high_heap)

            # conditions

            # 1: does highest building end before next building?
            if high_heap[0][2] < buildings[i][0]:
                next_bldg = heapq.heappop(high_heap)

                # check to ensure we don't add to an equivalent run
                if not skyline or skyline[-1][1] != -next_bldg[0]:
                    skyline.append([x, -next_bldg[0]])
                x = next_bldg[2]
                continue
            
            # 2: is next building taller?
            if -high_heap[0][0] < buildings[i][2]:
                if not skyline or skyline[-1][1] != -high_heap[0][0]:
                    skyline.append([x, -high_heap[0][0]])
                x = buildings[i][0]
            
            heapq.heappush(high_heap, (-buildings[i][2], buildings[i][0], buildings[i][1]))
            i += 1

        # continuation of prior loop
        # except now we no longer need to check for new buildings
        while high_heap:
            # again, remove all irrelevant buildings
            if x >= high_heap[0][2]:
                heapq.heappop(high_heap)
                continue
            
            next_bldg = heapq.heappop(high_heap)
            if not skyline or skyline[-1][1] != -next_bldg[0]:
                skyline.append([x, -next_bldg[0]])
            x = next_bldg[2]

        return skyline