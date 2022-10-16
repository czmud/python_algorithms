# represents an API call that returns if a version is good or bad
def isBadVersion( n ) -> bool:
    print(f'n: {n}')
    newest_n = 0
    if n > newest_n:
        return True
    return False

import math
def firstBadVersion( n ):
    if isBadVersion( 1 ):
        return 1
    g = 1
    b = n
    t = (b + g) // 2
    while g + 1 < b:
        if isBadVersion( t ):
            b = t
        else:
            g = t
        t = b+g // 2
    return b

print(firstBadVersion(2))