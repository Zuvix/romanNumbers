import RomanToNumberConverter as roman
import MaxNumberFromRoman as maxRoman
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

    if (len(romanLetters) == 0):
        return default_alphabet

    if roman.validate_roman_letters(romanLetters) == False:
        return default_alphabet

    if roman.check_roman_letters_for_unique_letters(romanLetters) == False:
        return default_alphabet

    return romanLetters


class RomanNumber:
    def __init__(self, romanLetters=DEFINED_ALPHABET):
        self.alphabet = check_alphabet(romanLetters, False)
        self.value = 0

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
        roman.set_roman_letters(self.alphabet)
        testNumber = roman.convert_to_int(romanNumber)
        if(testNumber == roman.INCORRECT_NUMBER):
            return False
        self.value = testNumber
        return True

    def getRomanNumber(self):
        roman.set_roman_letters(self.alphabet)
        return roman.romanToNumber(self.value)


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
        roman.set_roman_letters(self.alphabet)
        if self.value == 0:
            return self.zeroChar
        if self.value < 0:
            non_negative_value = abs(self.value)
            return "-"+roman.romanToNumber(self.value)
        return roman.romanToNumber(self.value)

    def setRomanNumber(self):
        roman.set_roman_letters(self.alphabet)


x = RomanNumber("IS")
print(x.maxNumber())
print(x.romanLetters())
