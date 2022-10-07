def longestValidParentheses(s):
    open_stack = []
    completed = []

    for char in s:
        if char == '(':
            open_stack.append('(')
            completed.append(-1)
        else:
            if open_stack:
                open_stack.pop()
                for i in range(len(completed)-1, -1, -1 ):
                    if completed[i] == -1:
                        completed[i] = 2
                        break
            else:
                completed.append(0)

    temp_max = 0
    result_max = 0
    for val in completed:
        if val > 0:
            temp_max += val
            result_max = max(result_max, temp_max)
        else:
            temp_max = 0

    return result_max

# Added visualization to Erik's solution
def longestValidParenthesesErik(s):
    longest = 0
    unmatched_parentheses = 0
    first_occurrence = {0: -1}
    carat_zero = 30
    for i in range(len(s)):
        if s[i] == "(":
            unmatched_parentheses += 1
            if unmatched_parentheses not in first_occurrence:
                first_occurrence[unmatched_parentheses] = i
            print(f'"(" i: {i} unmatched: {unmatched_parentheses} occur: {first_occurrence}')
            carat_str = ''.join(' '*(carat_zero + 7*unmatched_parentheses)) + '^'
            print(carat_str)
        else:
            first_occurrence.pop(unmatched_parentheses)
            unmatched_parentheses -= 1
            if unmatched_parentheses not in first_occurrence:
                first_occurrence[unmatched_parentheses] = i
                carat_zero += 7
            else:
                longest = max(longest, i - first_occurrence[unmatched_parentheses])
            print(f'")" i: {i} unmatched: {unmatched_parentheses} occur: {first_occurrence}')
            carat_str = ''.join(' '*(carat_zero + 7*unmatched_parentheses)) + '^'
            print(carat_str)
    return longest

print(longestValidParenthesesErik('())(()'))
