import RomanToNumberConverter as roman

WRONG_INPUT = "Wrong input"
WRONG_NUMBER = "Wrong number"
INCORRECT_NUMBER = -9999
MIN_NUMBER = 1
MAX_NUMBER = 3999

operator_list = ['+', '-', '*', '/']


def compute_expression(val1, val2, operator):
    if operator == '+':
        return val1 + val2
    if operator == '-':
        return val1 - val2
    if operator == '*':
        return val1 * val2
    if operator == '/':
        return val1 / val2


def roman_calculator(expression):
    if str != type(expression):
        return WRONG_INPUT

    expression = expression.strip()
    expression = expression.replace(" ", "")

    if len(expression) == 0:
        return WRONG_INPUT

    operator = ""
    for element in expression:
        if element in operator_list:
            operator = element
            break

    if operator == "":
        return WRONG_INPUT

    operands = expression.split(operator)
    operands_length = len(operands)

    if operands_length < 2 or operands_length > 2:
        return WRONG_INPUT

    roman_val1 = operands[0]
    roman_val2 = operands[1]
    int_val1 = roman.convert_to_int(roman_val1)
    if int_val1 == INCORRECT_NUMBER:
        return WRONG_INPUT

    int_val2 = roman.convert_to_int(roman_val2)
    if int_val2 == INCORRECT_NUMBER:
        return WRONG_INPUT

    result = compute_expression(int_val1, int_val2, operator)
    if result < MIN_NUMBER or result > MAX_NUMBER:
        return WRONG_NUMBER

    roman_result = roman.convert_to_roman(result)
    return roman_result
