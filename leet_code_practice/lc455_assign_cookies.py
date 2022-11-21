class Solution:
    def findContentChildren(self, g, s):
        if len(s) == 0:
            return 0
        g.sort()
        s.sort()

        res = 0

        i = len(g) - 1
        j = len(s) - 1
        while i >= 0 and j >= 0:
            if g[i] <= s[j]:
                j -= 1
                res += 1
            i -= 1
        
        return res


def findContentChildrenErik(g, s):
    g.sort(reverse=True)
    s.sort(reverse=True)
    i = 0
    j = 0
    while i < len(s) and j < len(g):
        if g[j] <= s[i]:
            i += 1
        j += 1
    return i