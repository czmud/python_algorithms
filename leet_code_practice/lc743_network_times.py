import heapq
from collections import deque
class Solution:
    def networkDelayTime(self, times, n, k):
        # earliest_times keeps track of the earliest we can reach a given node
        earliest_times = {i:float('+inf') for i in range(1,n+1)}
        earliest_times[k] = 0

        # visited hashmap keeps track of all the nodes we visit
        visited = set()

        # build adjacency map containing all the nodes that can be reached for a given node
        adjacency = {i:[] for i in range(1,n+1)}
        for start_node, dest_node, travel_time in times:
            adjacency[start_node].append((dest_node, travel_time))

        # initialize min-heap as priority queue for traversing our graph
        # the priority queue is important, as it assures that when we reach a node for the first time
        # it will be via the fasted path to that node
        node_heap = [(0,k)]
        while node_heap:
            curr_time, curr_node = heapq.heappop(node_heap)
            
            # thus if curr_node is already visited we can safely skip
            if curr_node in visited:
                continue

            visited.add(curr_node)
            
            # if we have visited all nodes, then early-return the curr_time
            # this optimization allows us to avoid traversing all the other paths
            if len(visited) == n:
                return curr_time

            adj_nodes = adjacency[curr_node]
            # iterate through all adjacent nodes
            while adj_nodes:
                next_node, travel_time = adj_nodes.pop()
                # if faster way to reach the node exists
                # then add it to priority queue and update earliest time
                if curr_time + travel_time < earliest_times[next_node]:
                    heapq.heappush(node_heap, (curr_time + travel_time, next_node))
                    earliest_times[next_node] = curr_time + travel_time

        return -1

    def networkDelayTime2(self, times, n, k):
        earliest_times = {i:float('+inf') for i in range(1,n+1)}
        earliest_times[k] = 0

        adjacency = {i:[] for i in range(1,n+1)}
        for start_node, dest_node, travel_time in times:
            adjacency[start_node].append((dest_node, travel_time))

        node_queue = deque([(0,k)])
        i = 0
        while node_queue:
            curr_time, curr_node = node_queue.popleft()

            if curr_time > earliest_times[curr_node]:
                continue

            for next_node, travel_time in adjacency[curr_node]:
                if curr_time + travel_time < earliest_times[next_node]:
                    node_queue.append((curr_time + travel_time, next_node))
                    earliest_times[next_node] = curr_time + travel_time
        
        max_time = max(earliest_times.values())
        return max_time if max_time < float('+inf') else -1