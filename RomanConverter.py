import math
import unittest
# MADE by Filip Novak and Samuel Kubala
# WINNER -> Filip Novak

roman_dict = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


# Function to check if there is a forbidden repetition of characters or bad count of characters
def check_more_than_three_consecutive_chars(romanNumber):
    key_list = list(roman_dict.keys())

    for x in range(len(key_list)):
        sum = 0
        maxSum = 1

        if x % 2 == 0:
            maxSum = 3

        for element in romanNumber:
            if element == key_list[x]:
                sum += 1

                if sum > maxSum:
                    return False
            else:
                sum = 0
    return True


def check_max_count_per_char(romanNumber):
    roman_count_dict = {
        "I": 3,
        "V": 1,
        "X": 4,
        "L": 1,
        "C": 4,
        "D": 1,
        "M": 4
    }

    for element in romanNumber:
        roman_count_dict[element] -= 1

        if roman_count_dict[element] < 0:
            return False

    return True


# Check for invalid characters
def validate_roman_elements(romanNumber):
    for element in romanNumber:
        if not (element in roman_dict):
            return False
    return True


# Check if number is in correct order
def correct_num_order(element, max, usedNumbers_list):
    for item in usedNumbers_list:
        if roman_dict[element] >= roman_dict[item]:
            return False

    if max == "I" and (element in ["L", "C", "D", "M"]):
        return False
    if max == "V" and (element in ["X", "L", "C", "D", "M"]):
        return False
    if max == "X" and (element in ["D", "M"]):
        return False
    if max == "L" and (element in ["C", "D", "M"]):
        return False
    if max == "D" and element == "M":
        return False

    return True


def check_actual_max_number(romanNumber):
    max_value = 1000
    for i in range(0, len(romanNumber)):
        current_element = romanNumber[i]
        next_element = ""
        if(i+1 < len(romanNumber)):
            next_element = romanNumber[i+1]
        if roman_dict[current_element] > max_value:
            return False
        if roman_dict[current_element] < max_value:
            # check if the next value is substractible canSubstract funkciu sprav
            if not can_subtract(current_element, next_element):
                max_value = roman_dict[current_element]
    return True


def can_subtract(current, next):
    if next == "":
        return False
    if roman_dict[current] < roman_dict[next]:
        if current in ["V", "L", "D"]:
            return False
        if current == "I" and (next in ["V", "X"]):
            return True
        if current == "X" and (next in ["L", "C"]):
            return True
        if current == "C" and (next in ["D", "M"]):
            return True

    return False


# Main function to convert roman to INT
def convert_to_int(romanNumber):
    if str != type(romanNumber):
        return -9999

    romanNumber = romanNumber.strip()  # remove leading and trailing whitespaces

    if len(romanNumber) == 0:
        return -9999

    if validate_roman_elements(romanNumber) == False:
        return -9999

    if check_max_count_per_char(romanNumber) == False:
        return -9999

    if check_more_than_three_consecutive_chars(romanNumber) == False:
        return -9999

    if check_actual_max_number(romanNumber) == False:
        return -9999

    i = 0
    sum = 0
    max = None
    repetition = False
    usedNumbers_list = []
    subtractableNumbers_list = []
    prevElem = romanNumber[0]

    for element in romanNumber:
        if i == 0:
            sum += roman_dict[element]
            max = element
            i += 1
            continue

        if correct_num_order(element, max, usedNumbers_list) == False:
            return -9999

        if roman_dict[prevElem] < roman_dict[element]:
            if prevElem in ["V", "L", "D"]:
                return -9999
            if prevElem == "I" and not (element in ["V", "X"]):
                return -9999
            if prevElem == "X" and not (element in ["L", "C"]):
                return -9999
            if prevElem == "C" and not (element in ["D", "M"]):
                return -9999
            if repetition:
                return -9999

            if roman_dict[max] < roman_dict[element]:
                max = element

            usedNumbers_list.append(element)
            subtractableNumbers_list.append(prevElem)
            sum -= 2 * roman_dict[prevElem]

        elif prevElem == element:
            repetition = True
        elif (roman_dict[prevElem] > roman_dict[element]) and repetition:
            repetition = False
        elif element in subtractableNumbers_list:
            return -9999

        sum += roman_dict[element]
        prevElem = element

    if sum > 3999:
        return -9999
    return sum


def convert_to_roman(num):

    m = ["", "M", "MM", "MMM"]
    c = ["", "C", "CC", "CCC", "CD", "D",
         "DC", "DCC", "DCCC", "CM "]
    x = ["", "X", "XX", "XXX", "XL", "L",
         "LX", "LXX", "LXXX", "XC"]
    i = ["", "I", "II", "III", "IV", "V",
         "VI", "VII", "VIII", "IX"]

    # Converting to roman
    thousands = m[num // 1000]
    hundreds = c[(num % 1000) // 100]
    tens = x[(num % 100) // 10]
    ones = i[num % 10]

    result = (thousands + hundreds +
              tens + ones)

    return result
