# PROBLEM:
# You have secret keys (strings of letters and numbers) that you need to provide to your users.  However, long access codes can be difficult to read.  Create an algorithm that will take in a secret key and insert hyphens in order to make the code easier to read.

# SPECIFICATIONS:
# - Codes that are 5 digits or fewer do not need hyphens
# - For all other codes, insert hyphens to separate the digits into groups, as follows:
#     - Wherever possible, group digits into threes
#     - If not evenly divisible into threes, then the last group (or the last two groups) should have four digits
# - Return a hyphenated string

# TEST CASES:
# IN                OUT
# ""                ""
# "1"               "1"
# "12345"           "12345"
# "123456"          "123-456"
# "1234567"         "123-4567"
# "12345678"        "1234-5678"
# "123456789"       "123-456-789"
# "1234567890"      "123-456-7890"
# "1234567890abcd"  "123-456-7890-abcd"


def insertHyphens( code ):
    if len(code) < 6:
        return code

    fours = int(len(code) % 3)
    threes = int(( len(code) / 3 ) - fours)

    if threes > 0:
        hyphenated = code[0: 3]
        threes -= 1
        codex = 3
    else:
        hyphenated = code[0:4]
        fours -= 1
        codex = 4

    for _ in range(threes):
        hyphenated += "-"
        hyphenated += code[codex: codex+3]
        codex += 3

    for _ in range(fours):
        hyphenated +="-"
        hyphenated += code[codex: codex+4]
        codex += 4

    return hyphenated



print(insertHyphens(""))
print(insertHyphens("1"))
print(insertHyphens("12345"))
print(insertHyphens("123456"))
print(insertHyphens("1234567"))
print(insertHyphens("12345678"))
print(insertHyphens("123456789"))
print(insertHyphens("1234567890"))
print(insertHyphens("1234567890abcd"))