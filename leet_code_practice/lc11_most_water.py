def maxArea(height) -> int:
    left_bounds = {height[0]: 1}
    max_height = height[0]
    max_area = 0
    for i in range(1, len(height)):
        for h, w in left_bounds.items():
            if w * min(height[i], h) > max_area:
                max_area = w * min(height[i], h)
            left_bounds[h] += 1
        if height[i] > max_height:
            max_height = height[i]
            left_bounds[height[i]] = 1
    return max_area

def maxArea2(height) -> int:
    left_bounds = {height[0]: 1}
    max_height = height[0]
    max_area = 0
    for i in range(1, len(height)):
        height_keys = list(left_bounds.keys())
        for h in height_keys:
            print(f'h: {h} w: {left_bounds[h]}')
            if left_bounds[h] * min(height[i], h) > max_area:
                max_area = left_bounds[h] * min(height[i], h)
            if height[i] >= h * (left_bounds[h] +1):
                left_bounds.pop(h)
            else:
                left_bounds[h] += 1
        if height[i] > max_height:
            max_height = height[i]
            left_bounds[height[i]] = 1
    return max_area

# Used explanation given by @StefanPochmann as basis for solution
def maxArea3(height) -> int:
    l = 0
    r = len(height) - 1
    max_area = 0
    while l < r:
        max_area = max(max_area, (r-l) * min(height[l], height[r]) )

        if height[l] > height[r]:
            r -= 1
        elif height[l] < height[r]:
            l += 1
        else:
            r -= 1
            l += 1
    return max_area



print(maxArea3([1,8,6,2,5,4,8,3,7]))