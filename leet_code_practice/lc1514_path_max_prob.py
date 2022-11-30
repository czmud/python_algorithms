import heapq
class Solution:
    def maxProbability(self, n, edges, succProb, start, end):
        
        adjacency = {i:[] for i in range(n)}
        for i in range(len(edges)):
            a, b = edges[i][0], edges[i][1]
            prob = succProb[i]
            # must add both directions for undirected graph
            adjacency[b].append((a, prob))
            adjacency[a].append((b, prob))

        if len(adjacency[start]) == 0 or len(adjacency[end]) == 0:
            return 0
        
        max_probability = {i:0 for i in range(n)}

        node_heap = [(-1, start)]

        while node_heap:
            curr_neg_prob, curr_node = heapq.heappop(node_heap)
            if curr_node == end or -curr_neg_prob <= max_probability[end]:
                break

            adj_nodes = adjacency[curr_node]
            while adj_nodes:
                next_node, next_prob = adj_nodes.pop()
                next_comb_prob = -curr_neg_prob * next_prob
                if next_comb_prob > max_probability[next_node] and next_comb_prob > max_probability[end]:
                    heapq.heappush(node_heap, (-next_comb_prob, next_node))
                    max_probability[next_node] = next_comb_prob
        return max_probability[end]