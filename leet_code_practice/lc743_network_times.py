import heapq
class Solution:
    def networkDelayTime(self, times, n, k):
        earliest_times = {i:float('+inf') for i in range(1,n+1)}
        earliest_times[k] = 0

        visited = set()

        adjacency = {i:[] for i in range(1,n+1)}
        for start_node, dest_node, travel_time in times:
            adjacency[start_node].append((dest_node, travel_time))

        node_heap = [(0,k)]
        while node_heap:
            curr_time, curr_node = heapq.heappop(node_heap)
            
            visited.add(curr_node)
            
            if len(visited) == n:
                return curr_time

            adj_nodes = adjacency[curr_node]
            while adj_nodes:
                next_node, travel_time = adj_nodes.pop()
                if curr_time + travel_time < earliest_times[next_node]:
                    heapq.heappush(node_heap, (curr_time + travel_time, next_node))
                    earliest_times[next_node] = curr_time + travel_time

        return -1