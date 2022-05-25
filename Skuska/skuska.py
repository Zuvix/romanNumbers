import RomanToNumberConverter as roman
import MaxNumberFromRoman as maxRoman
DEFINED_ALPHABET = "IVXLCDM"
DEFINED_ZERO_ALPHABET = "OIVXLCDM"


def check_alphabet(romanLetters, hasZero):

    if hasZero:
        alphabet = DEFINED_ZERO_ALPHABET
    else:
        alphabet = DEFINED_ALPHABET
    if (str != type(romanLetters)):
        return alphabet

    romanLetters = romanLetters.strip()

    if (len(romanLetters) == 0):
        return alphabet

    if roman.validate_roman_letters(romanLetters) == False:
        return alphabet

    if roman.check_roman_letters_for_unique_letters(romanLetters) == False:
        return alphabet


class RomanNumber:
    def __init__(self, romanLetters):
        self.romanLetters = check_alphabet(romanLetters, False)
        self.value = 0

    def romanLetters(self):
        return self.romanLetters

    def maxNumber(self):
        return maxRoman.maxNumberFromRomanLetters(self.romanLetters)

    def setValue(self, value):
        if value > self.maxNubmer() or value <= 0:
            return False
        self.value = value
        return True

    def getValue(self):
        return self.value

    def setRomanNumber(self, romanNumber):
        roman.set_roman_letters(self.romanLetters)
        testNumber = roman.convert_to_int(romanNumber)
        if(testNumber == roman.INCORRECT_NUMBER):
            return False
        self.value = testNumber
        return True

    def getRomanNumber(self):
        roman.set_roman_letters(self.romanLetters)
        return roman.convert_to_int(self.value)


class RomanNumberFull:
    # Public methodes and Constructor
    def __init__(self, romanLetters):
        self.romanLetters = self.check_alphabet(romanLetters, True)
        self.value = 0
        self.zeroChar = romanLetters[0]
        self.romanLetters = self.romanLetters[1:]

    def maximum(self):
        return maxRoman.maxNumberFromRomanLetters(self.romanLetters)

    def mimnimum(self):
        return -1*maxRoman.maxNumberFromRomanLetters(self.romanLetters)

    def setvalue(self, value):
        if value > self.maximum() or value < self.mimnimum():
            return False
        self.value = value
        return True


x = RomanNumber("l")
