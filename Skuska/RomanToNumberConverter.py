# MADE by Filip Novak and Samuel Kubala
from collections import OrderedDict
import math


INCORRECT_NUMBER = -9999

roman_dict = OrderedDict()


def set_roman_letters(romanLetters):
    current_value = 1
    index = 0
    global roman_dict
    roman_dict = OrderedDict()  # reset roman_dict

    for letter in romanLetters:
        roman_dict[letter] = current_value

        if index % 2 == 0:
            current_value *= 5
        else:
            current_value *= 2
        index += 1


def validate_roman_letters(romanLetters):
    if romanLetters.isalpha():
        if romanLetters.isupper():
            return True
    return False


def check_roman_letters_for_unique_letters(romanLetters):
    duplicates = []

    for letter in romanLetters:
        if letter not in duplicates:
            duplicates.append(letter)
        else:
            return False
    return True

# Function to check if there is a forbidden repetition of characters


def check_more_than_three_consecutive_chars(romanNumber):
    key_list = list(roman_dict.keys())

    for x in range(len(key_list)):
        sum = 0
        max_sum = 1

        if x % 2 == 0:
            max_sum = 3

        for element in romanNumber:
            if element == key_list[x]:
                sum += 1

                if sum > max_sum:
                    return False
            else:
                sum = 0
    return True


def check_max_count_per_char(romanNumber):
    roman_count_dict = roman_dict.copy()
    key_list = list(roman_count_dict.keys())
    index = 0

    for key in key_list:
        if index == 0:
            roman_count_dict[key] = 3
        elif index % 2 == 0:
            roman_count_dict[key] = 4
        else:
            roman_count_dict[key] = 1
        index += 1

    for element in romanNumber:
        roman_count_dict[element] -= 1

        if roman_count_dict[element] < 0:
            return False

    return True

# Check for invalid characters


def validate_roman_number_elements(romanNumber):
    for element in romanNumber:
        if element not in roman_dict:
            return False
    return True


def check_numbers_list(element, numbers_list):
    for item in numbers_list:
        if roman_dict[element] >= roman_dict[item]:
            return False
    return True


def check_number_order(romanNumber):
    last_key = list(roman_dict)[-1]
    max_value = roman_dict[last_key]
    romanNumber_length = len(romanNumber)

    for i in range(0, romanNumber_length):
        current_element = romanNumber[i]
        next_element = ""

        if(i+1 < romanNumber_length):
            next_element = romanNumber[i+1]
        if roman_dict[current_element] > max_value:
            return False
        if roman_dict[current_element] < max_value:
            if not can_subtract(current_element, next_element):
                max_value = roman_dict[current_element]

    return True


def can_subtract(current, next):
    if next == "":
        return False

    if roman_dict[current] < roman_dict[next]:
        key_list = list(roman_dict.keys())
        current_index = key_list.index(current)

        if current_index % 2 != 0:
            return False

        next_index = key_list.index(next)

        if (next_index == current_index + 1) or (next_index == current_index + 2):
            return True

    return False

# Main function to convert roman to number


def convert_to_int(romanNumber):
    if str != type(romanNumber):
        return INCORRECT_NUMBER

    romanNumber = romanNumber.strip()

    if len(romanNumber) == 0:
        return INCORRECT_NUMBER

    if validate_roman_number_elements(romanNumber) == False:
        return INCORRECT_NUMBER

    if check_max_count_per_char(romanNumber) == False:
        return INCORRECT_NUMBER

    if check_more_than_three_consecutive_chars(romanNumber) == False:
        return INCORRECT_NUMBER

    if check_number_order(romanNumber) == False:
        return INCORRECT_NUMBER

    i = 0
    sum = 0
    repetition = False
    usedNumbers_list = []
    subtractedNumbers_list = []
    prevElement = romanNumber[0]

    for element in romanNumber:
        if i == 0:
            sum += roman_dict[element]
            i += 1
            continue

        if check_numbers_list(element, usedNumbers_list) == False:
            return INCORRECT_NUMBER

        if roman_dict[prevElement] < roman_dict[element]:
            if not can_subtract(prevElement, element):
                return INCORRECT_NUMBER
            if repetition:
                return INCORRECT_NUMBER

            usedNumbers_list.append(element)
            subtractedNumbers_list.append(prevElement)
            sum -= 2 * roman_dict[prevElement]

        elif prevElement == element:
            repetition = True
        elif (roman_dict[prevElement] > roman_dict[element]) and repetition:
            repetition = False
        elif check_numbers_list(element, subtractedNumbers_list) == False:
            return INCORRECT_NUMBER

        sum += roman_dict[element]
        prevElement = element

    return sum


def romanToNumber(romanLetters, romanNumber):
    if str != type(romanLetters):
        return INCORRECT_NUMBER

    romanLetters = romanLetters.strip()

    if len(romanLetters) == 0:
        return INCORRECT_NUMBER

    if validate_roman_letters(romanLetters) == False:
        return INCORRECT_NUMBER

    if check_roman_letters_for_unique_letters(romanLetters) == False:
        return INCORRECT_NUMBER

    set_roman_letters(romanLetters)

    return convert_to_int(romanNumber)


def integerToRoman(alphabet, value):
    set_roman_letters(alphabet)
    reverseDict = OrderedDict()
    for key in roman_dict:
        reverseDict[roman_dict[key]] = key
    div = 1
    while value >= div:
        div *= 10

    div /= 10

    res = ""

    while value:

        lastNum = int(value / div)

        if lastNum <= 3:
            res += (reverseDict[div] * lastNum)
        elif lastNum == 4:
            res += (reverseDict[div] +
                    reverseDict[div * 5])
        elif 5 <= lastNum <= 8:
            res += (reverseDict[div * 5] +
                    (reverseDict[div] * (lastNum - 5)))
        elif lastNum == 9:
            res += (reverseDict[div] +
                    reverseDict[div * 10])

        value = math.floor(value % div)
        div /= 10

    return res


# Driver code
