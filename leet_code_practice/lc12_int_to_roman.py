def intToRoman(num: int) -> str:
    result_str = ""
    while( num > 0 ):
        if num >= 1000:
            result_str += "M"
            num -= 1000
        elif num >= 900:
            result_str += "CM"
            num -= 900
        elif num >= 500:
            result_str += "D"
            num -= 500
        elif num >= 400:
            result_str += "CD"
            num -= 400
        elif num >= 100:
            result_str += "C"
            num -= 100
        elif num >= 90:
            result_str += "XC"
            num -= 90
        elif num >= 50:
            result_str += "L"
            num -= 50
        elif num >= 40:
            result_str += "XL"
            num -= 40
        elif num >= 10:
            result_str += "X"
            num -= 10
        elif num >= 9:
            result_str += "IX"
            num -= 9
        elif num >= 5:
            result_str += "V"
            num -= 5
        elif num >= 4:
            result_str += "IV"
            num -= 4
        elif num >= 1:
            result_str += "I"
            num -= 1
    return result_str

#... maybe it would be better to repeat ourselves less...
def intToRoman(num: int) -> str:
    result_str = ""
    map = { 1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 
            50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I" }
    for val, rom in map.items():
        while( num >= val ):
            result_str += rom
            num -= val
    return result_str



print(intToRoman(509))

