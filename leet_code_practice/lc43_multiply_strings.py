# From description:
# You must not use any built-in BigInteger library or convert the inputs to
# integer directly.
# Which is slightly ambiguous. Solved assuming you could convert character by
# character to int to complete multiplication and addition operations.
# to do these operations on string/char datatypes seems nonsensical

def multiply( num1: str, num2: str):
    result_int = 0
    for i in range(len(num1)):
        for j in range(len(num2)):
            add_int = int(num1[i]) * int(num2[j]) * 10**(len(num1)+len(num2)-i-j-2)
            result_int += add_int
    return str(result_int)

print(multiply("123","456"))