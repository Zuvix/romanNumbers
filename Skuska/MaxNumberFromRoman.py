import RomanToNumberConverter as roman

INCORRECT_NUMBER = -9999


def maxNumberFromRomanLetters(romanLetters):
    if str != type(romanLetters):
        return INCORRECT_NUMBER

    romanLetters = romanLetters.strip()

    if len(romanLetters) == 0:
        return INCORRECT_NUMBER

    if roman.validate_roman_letters(romanLetters) == False:
        return INCORRECT_NUMBER

    if roman.check_roman_letters_for_unique_letters(romanLetters) == False:
        return INCORRECT_NUMBER

    roman.set_roman_letters(romanLetters)

    index = len(romanLetters)-1
    final_sequence = ""

    while(index >= 0):
        if index % 2 == 0:
            if romanLetters[index] not in final_sequence:
                final_sequence += romanLetters[index]*3
            if index > 0:
                if index-2 >= 0:
                    final_sequence += romanLetters[index-2]
                    final_sequence += romanLetters[index]
                    index = index-2
                elif index-1 >= 0:
                    final_sequence += romanLetters[index-1]
                    return roman.convert_to_int(final_sequence)
            else:
                return roman.convert_to_int(final_sequence)

        if index % 2 == 1:
            final_sequence += romanLetters[index]
            index -= 1
