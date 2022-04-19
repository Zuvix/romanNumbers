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


# TEST FUNCTIONS
def test1():
    assert convert_to_int("I") == 1, "Test1, should be 1"


def test2():
    assert convert_to_int("V") == 5, "Test2, should be 5"


def test3():
    assert convert_to_int("-I") == -9999, "Test3, should be -9999"


def test4():
    assert convert_to_int("X") == 10, "Test4, should be 10"


def test5():
    assert convert_to_int("III") == 3, "Test5, should be 3"


def test6():
    assert convert_to_int("MMMM") == -9999, "Test6, should be -9999"


def test7():
    assert convert_to_int("IIII") == -9999, "Test7, should be -9999"


def test8():
    assert convert_to_int("DD") == -9999, "Test8, should be -9999"


def test9():
    assert convert_to_int("IV") == 4, "Test9, should be 4"


def test10():
    assert convert_to_int("VX") == -9999, "Test10, should be -9999"


def test11():
    assert convert_to_int("LC") == -9999, "Test11, should be -9999"


def test12():
    assert convert_to_int("DM") == -9999, "Test12, should be -9999"


def test13():
    assert convert_to_int("IL") == -9999, "Test13, should be -9999"


def test14():
    assert convert_to_int("IIV") == -9999, "Test14, should be -9999"


def test15():
    assert convert_to_int("MXXXIV") == 1034, "Test15, should be 1034"


def test16():
    assert convert_to_int("MCMLXXXVIII") == 1988, "Test16, should be 1988"


def test17():
    assert convert_to_int("") == -9999, "Test17, should be -9999"


def test18():
    assert convert_to_int("  CXIX ") == 119, "Test18, should be 119"


def test19():
    assert convert_to_int("CMCM") == -9999, "Test19, should be -9999"


def test20():
    assert convert_to_int("CMM") == -9999, "Test20, should be -9999"


def test21():
    assert convert_to_int("DCM") == -9999, "Test21, should be -9999"


def test22():
    assert convert_to_int("XCIX") == 99, "Test22, should be 99"


def test23():
    assert convert_to_int("MMMCM") == 3900, "Test23 should be 3900"


def test24():
    assert convert_to_int("CDC") == -9999, "Test24 should be -9999"


def test25():
    assert convert_to_int("IXIV") == -9999, "Test25 should be -9999"


def test26():
    assert convert_to_int("XXXVIX") == -9999, "Test26 should be -9999"


def test27():
    assert convert_to_int("DCD") == -9999, "Test27 should be -9999"


def test28():
    assert convert_to_int(None) == -9999, "Test28 should be -9999"


# RUN TESTS
test1()
test2()
test3()
test4()
test5()
test6()
test7()
test8()
test9()
test10()
test11()
test12()
test13()
test14()
test15()
test16()
test17()
test18()
test19()
test20()
test21()
test22()
test23()
test24()
test25()
test26()
test27()
test28()
