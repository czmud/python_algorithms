# fun, but runtime is way too slow...
def divide(dividend: int, divisor: int) -> int:
    count = 0
    negative = False

    if dividend < 0:
        dividend -= (dividend + dividend)
        negative = not negative
    if divisor < 0:
        divisor -= (divisor + divisor)
        negative = not negative

    while dividend > 0:
        dividend -= divisor
        count += 1
    if dividend + divisor < abs(dividend):
        count -= 1

    if negative:
        shrimp = count + count
        count -= shrimp
    return count

# still not great - I think this will overflow the 32-bit constraint placed on this problem
def divide2(dividend: int, divisor: int) -> int:
    negative = False

    dividend_str = str(dividend)

    dividend_arr = []
    for i in range(len(dividend_str)-1,-1,-1):
        dividend_arr.append(dividend_str[i])

    divisor_str = str(divisor)
    if divisor_str[0] == '-':
        divisor = int(divisor_str[1:])
        negative = not negative
    
    if dividend_arr[-1] == '-':
        dividend_arr.pop()
        negative = not negative
    
    quotient_str = '-' if negative else '' 

    next_dividend_str = ''
    while dividend_arr:
        next_quotient = 0
        next_dividend_str += dividend_arr.pop()
        next_dividend = int(next_dividend_str)

        while next_dividend >= divisor:
            next_dividend -= divisor
            next_quotient += 1

        next_dividend_str = str(next_dividend)
        quotient_str += str(next_quotient)

    #edge cases because we want to add rules for digit sizing
    quotient = int(quotient_str)
    if quotient > 2147483647:
        return 2147483647
    if quotient < -2147483648:
        return -2147483648
    return int(quotient_str)



print(divide2(-2147483648,-1))