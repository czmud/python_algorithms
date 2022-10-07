def longestValidParentheses(s: str):
    open_stack = []
    completed = []

    for char in s:
        if char == '(':
            open_stack.append('(')
            completed.append(-1)
        elif char == ')':
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

