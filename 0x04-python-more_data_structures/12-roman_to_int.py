#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return (0)

    roman_letter = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    converted = 0
    last = 0
    for char in roman_string:
        value = roman_letter.get(char, 0)
        if value > last:
            converted += value - 2 * last
        else:
            converted += value
        last = value

    return (converted)
