#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    roman_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for j in range(len(roman_string)):
        if j > 0 and roman_n[roman_string[j]] > roman_n[roman_string[j - 1]]:
            result += roman_n[roman_string[j]] - 2 * \
                        roman_n[roman_string[j - 1]]
        else:
            result += roman_n[roman_string[j]]
    return result
