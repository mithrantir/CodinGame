roman_value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, '0': 0}


def roman_to_int(s):
    val, ind = 0, 0
    while ind < len(s)-1:
        if roman_value[s[ind]] >= roman_value[s[ind+1]]:
            val += roman_value[s[ind]]
        else:
            val += roman_value[s[ind+1]] - roman_value[s[ind]]
            ind += 1
        ind += 1
    return val


def int_to_roman(n):
    roman = ""
    while n != 0:
        if n >= 1000:
            roman, n = roman + "".join('M' for k in range(n // 1000)), n % 1000
        elif n >= 500:
            if n < 900:
                roman, n = roman + 'D', n - 500
            else:
                roman, n = roman + 'CM', n - 900
        elif n >= 100:
            if n < 400:
                roman, n = roman + "".join('C' for k in range(n//100)), n % 100
            else:
                roman, n = roman + 'CD', n - 400
        elif n >= 50:
            if n < 90:
                roman, n = roman + 'L', n - 50
            else:
                roman, n = roman + 'XC', n - 90
        elif n >= 10:
            if n < 40:
                roman, n = roman + "".join('X' for k in range(n // 10)), n % 10
            else:
                roman, n = roman + 'XL', n - 40
        elif n >= 5:
            if n < 9:
                roman, n = roman + 'V', n - 5
            else:
                roman, n = roman + 'IX', n - 9
        elif n >= 1:
            if n < 4:
                roman, n = roman + "".join('I' for k in range(n)), 0
            else:
                roman, n = roman + 'IV', n - 4
    return roman


rom_1 = input()+'0'
rom_2 = input()+'0'
print(int_to_roman(roman_to_int(rom_1)+roman_to_int(rom_2)))
