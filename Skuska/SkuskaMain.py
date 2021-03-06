from tkinter.tix import INTEGER
import RomanToNumberConverter as roman
import MaxNumberFromRoman as maxRoman
import Calculator as calc
import sys

WRONG_INPUT = "Wrong input"
DEFINED_ALPHABET = "IVXLCDM"
DEFINED_ZERO_ALPHABET = "OIVXLCDM"


def check_alphabet(romanLetters, hasZero):

    if hasZero:
        default_alphabet = DEFINED_ZERO_ALPHABET
    else:
        default_alphabet = DEFINED_ALPHABET

    if (str != type(romanLetters)):
        return default_alphabet

    romanLetters = romanLetters.strip()

    if (len(romanLetters) == 0 and not hasZero):
        return default_alphabet

    if (len(romanLetters) < 2 and hasZero):
        return default_alphabet

    if roman.validate_roman_letters(romanLetters) == False:
        return default_alphabet

    if roman.check_roman_letters_for_unique_letters(romanLetters) == False:
        return default_alphabet

    return romanLetters


class RomanNumber:
    def __init__(self, romanLetters=DEFINED_ALPHABET, max=sys.maxsize):
        self.alphabet = check_alphabet(romanLetters, False)
        self.value = 0

        if (max != sys.maxsize):
            ourMax = self.maxNumber()

            if  max < 1 or max > ourMax:
                self.alphabet = DEFINED_ALPHABET
            else:
                temp = self.alphabet

                while ourMax >= max:
                    temp = self.alphabet
                    self.alphabet = self.alphabet[:-1]
                    ourMax = self.maxNumber()
                self.alphabet = temp

    def romanLetters(self):
        return self.alphabet

    def maxNumber(self):
        return maxRoman.maxNumberFromRomanLetters(self.alphabet)

    def setValue(self, value):
        if value > self.maxNumber() or value <= 0:
            return False
        self.value = value
        return True

    def getValue(self):
        return self.value

    def setRomanNumber(self, romanNumber):
        testNumber = roman.romanToNumber(self.alphabet, romanNumber)
        if(testNumber == roman.INCORRECT_NUMBER):
            return False
        self.value = testNumber
        return True

    def getRomanNumber(self):
        return roman.integerToRoman(self.alphabet, self.value)


class RomanNumberFull:
    # Public methodes and Constructor
    def __init__(self, romanLetters=DEFINED_ZERO_ALPHABET):
        self.alphabet = check_alphabet(romanLetters, True)
        self.value = 0
        self.zeroChar = self.alphabet[0]
        self.alphabet = self.alphabet[1:]

    def maximum(self):
        return maxRoman.maxNumberFromRomanLetters(self.alphabet)

    def minimum(self):
        return -1*maxRoman.maxNumberFromRomanLetters(self.alphabet)

    def setValue(self, value):
        if value > self.maximum() or value < self.minimum():
            return False
        self.value = value
        return True

    def getValue(self):
        return self.value

    def getRomanNumber(self):
        if self.value == 0:
            return self.zeroChar
        if self.value < 0:
            non_negative_value = abs(self.value)
            return "-"+roman.integerToRoman(self.alphabet, non_negative_value)
        return roman.integerToRoman(self.alphabet, self.value)

    def setRomanNumber(self, value):
        if value == self.zeroChar:
            self.value = 0
            return True
        if "-" in value:
            value = value[1:]
            test_value = roman.romanToNumber(self.alphabet, value)
            if test_value == roman.INCORRECT_NUMBER:
                return False
            self.value *= -1
            return True

        testNumber = roman.romanToNumber(self.alphabet, value)
        if(testNumber == roman.INCORRECT_NUMBER):
            return False
        self.value = testNumber
        return True

    def calculator(self, expression):
        result = calc.roman_calculator(expression)

        if result == WRONG_INPUT:
            return False
        
        self.setValue(result)
        return True

