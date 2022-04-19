from cmath import exp
import RomanConverter as roman

WRONG_INPUT = "Wrong input"
WRONG_NUMBER = "Wrong number"

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

    operands = expression.split(operator)
    roman_val1 = operands[0]
    roman_val2 = operands[1]
    val1 = roman.convert_to_int(roman_val1)
    val2 = roman.convert_to_int(roman_val2)
    result = compute_expression(val1, val2, operator)
    roman_result = roman.convert_to_roman(result)
    return roman_result


print(roman_calculator("MCX + MCIV"))
