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