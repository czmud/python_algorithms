

def romanToInt(s: str) -> int:
    result_int = 0
    for i in range(len(s)):
        if s[i] == "M":
            result_int += 1000
        elif s[i] == "D":
            result_int += 500
        elif s[i] == "C":
            if i+1 < len(s) and (s[i+1] == "D" or s[i+1] == "M"):
                result_int -= 100
            else:
                result_int += 100
        elif s[i] == "L":
            result_int += 50
        elif s[i] == "X":
            if i+1 < len(s) and (s[i+1] == "L" or s[i+1] == "C"):
                result_int -= 10
            else:
                result_int += 10
        elif s[i] == "V":
            result_int += 5
        elif s[i] == "I":
            if i+1 < len(s) and (s[i+1] == "V" or s[i+1] == "X"):
                result_int -= 1
            else:
                result_int += 1
        else:
            return None
    return result_int


# more concise solution, concept taken from @wenfengqiu
# had the general idea, but was missing the comparison portion of it 
# so code was getting too complex
def romanToInt2(s: str) -> int:
    map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    trouble = {"I": True, "V": False, "X": True, "L": False, "C": True, "D": False, "M": False}

    result_int = 0
    for i in range(len(s)-1):
        result_int += map[s[i]]
        if trouble[s[i]] and map[s[i]] < map[s[i+1]]:
            result_int -= map[s[i]] + map[s[i]]
    result_int += map[s[-1]]
    return result_int


print(romanToInt2("DXIV"))

