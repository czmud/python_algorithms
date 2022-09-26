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

def lengthOfLongestSubstring3( s: str ) -> int:
    lastPosition = {}
    maxLength = 0
    start = 0
    for i, char in enumerate(s):
        if char in lastPosition:
            if start < lastPosition[char] + 1:
                start = lastPosition[char] + 1
        if i - start + 1 > maxLength:
            maxLength = i - start + 1
        lastPosition[char] = i
    return maxLength

print(lengthOfLongestSubstring3('asldglahlvlis'))

