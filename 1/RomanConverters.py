# MADE by Filip Novak and Samuel Kubala
# WINNER -> Filip Novak

INCORRECT_NUMBER = -9999
MAX_NUMBER = 3999

roman_dict = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

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
        if element not in roman_dict:
            return False
    return True


def check_numbers_list(element, numbers_list):
    for item in numbers_list:
        if roman_dict[element] >= roman_dict[item]:
            return False

    return True


def check_number_order(romanNumber):
    max_value = 1000
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
        return INCORRECT_NUMBER

    romanNumber = romanNumber.strip()  # remove leading and trailing whitespaces

    if len(romanNumber) == 0:
        return INCORRECT_NUMBER

    if validate_roman_elements(romanNumber) == False:
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

    if sum > MAX_NUMBER:
        return INCORRECT_NUMBER
    return sum


# Main function to convert INT to roman
def convert_to_roman(num):
    m_list = ["", "M", "MM", "MMM"]
    c_list = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    x_list = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    i_list = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

    # Converting to roman
    thousands = m_list[int(num // 1000)]
    hundreds = c_list[int((num % 1000) // 100)]
    tens = x_list[int((num % 100) // 10)]
    ones = i_list[int(num % 10)]

    result = thousands + hundreds + tens + ones
    return result
