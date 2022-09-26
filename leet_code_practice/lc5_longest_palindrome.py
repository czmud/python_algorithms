


def longestPalindrome( s: str) -> str:
    returnString = s[0]
    maxLength = 1
    j = 0
    k = 0
    d = 0

    print(len(s))
    for i in range(len(s)-1):
        print(f'i: {i}')
        if s[i] == s[i+1]:
            k = i + 1
            if i + 2 < len(s):
                continue
        while j - d - 1 >= 0 and k + d + 1 < len(s):
            if s[j-d-1] == s[k+d+1]:
                d += 1
                print(f'd: {d}')
            else:
                break
        if k - j + 2*d + 1 > maxLength:
            maxLength = k - j + 2*d + 1
            print(f'maxLength: {maxLength}')
            returnString = s[j-d:k+d+1]
        
        j = i+1
        print(f'j: {j}')
        k = i+1
        print(f'k: {k}')
        d = 0
    
    return returnString


print(longestPalindrome("aba"))