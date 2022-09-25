# 3. Longest Substring Without Repeating Characters. Medium.
from datastructures import queue



def lengthOfLongestSubstring(self, s: str) -> int:
    strQueue = queue.Queue()
    maxLength = 0

    for char in s:
        while strQueue.contains(char):
            strQueue.dequeue()
        strQueue.enqueue(char)
        if strQueue.size > maxLength:
            maxLength = strQueue.size
    return maxLength

def lengthOfLongestSubstring2( s: str) -> int:
    maxLength = 0
    start = 0
    for i, char in enumerate(s):
        for j in range( start, i):
            if s[j] == char:
                start = j + 1
        if i + 1 - start > maxLength:
            maxLength = i + 1 - start
    return maxLength
