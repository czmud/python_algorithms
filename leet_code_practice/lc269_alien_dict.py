from collections import deque
from copy import deepcopy

class Solution:
    def alienOrder(self, words):
        res = ""

        adjacency = {}
        for word in words:
            for char in word:
                if char not in adjacency:
                    adjacency[char] = []

        head = words[0][0]
        for i in range(len(words)-1):
            word_1, word_2 = words[i], words[i+1]
            
            if word_1 == word_2:
                continue

            j = 0
            while j < len(word_1) and j < len(word_2) and word_1[j] == word_2[j]:
                j += 1

            if j >= len(word_2):
                return ""

            if j >= len(word_1):
                continue
            
            adjacency[word_1[j]].append(word_2[j])
            if head == word_2[j]:
                head = word_1[j]

        path = {c:set() for c in adjacency.keys() }

        char_queue = deque([(0, head)])
        while char_queue:
            curr_path_len, curr_char = char_queue.popleft()

            adj_chars = adjacency[curr_char]
            while adj_chars:
                next_char = adj_chars.pop()
                if len(path[next_char]) < curr_path_len + 1:
                    if next_char in path[curr_char]:
                        return ""
                    path[next_char] = deepcopy(path[curr_char])
                    path[next_char].add(curr_char)
                    char_queue.append((curr_path_len + 1, next_char ))

        for key in sorted(path, key=lambda p: len(path[p])):
            res += key

        return res

    def alienOrder2(self, words):
        res = ""

        adjacency = {}
        for word in words:
            for char in word:
                if char not in adjacency:
                    adjacency[char] = []

        coming_before = {c:0 for c in adjacency.keys()}

        for i in range(len(words)-1):
            word_1, word_2 = words[i], words[i+1]
            
            if word_1 == word_2:
                continue

            j = 0
            while j < len(word_1) and j < len(word_2) and word_1[j] == word_2[j]:
                j += 1

            if j >= len(word_2):
                return ""

            if j >= len(word_1):
                continue
            if word_2 not in adjacency[word_1[j]]:
                adjacency[word_1[j]].append(word_2[j])
                coming_before[word_2[j]] += 1

        char_queue = deque([])
        for char in coming_before.keys():
            if coming_before[char] == 0:
                char_queue.append(char)

        while char_queue:
            curr_char = char_queue.popleft()

            res += curr_char

            adj_chars = adjacency[curr_char]
            while adj_chars:
                next_char = adj_chars.pop()
                coming_before[next_char] -= 1
                if coming_before[next_char] == 0:
                    char_queue.append(next_char)
        
        return res if len(res) == len(adjacency) else ""


solution = Solution()

words1 = ["zy","zx"]


print(solution.alienOrder2(words1))