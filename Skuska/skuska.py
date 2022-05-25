import RomanToNumberConverter as roman
import MaxNumberFromRoman as maxRoman
DEFINED_ALPHABET = "IVXLCDM"


class RomanNumber:
    # Public methodes and Constructor
    def __init__(self, romanLetters):
        self.romanLetters = self.check_alphabet(romanLetters)
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
        # Prviate methodes

    def getValue(self):
        return self.value

    def check_alphabet(self, romanLetters):
        if (str != type(romanLetters)):
            return DEFINED_ALPHABET

        romanLetters = romanLetters.strip()

        if (len(romanLetters) == 0):
            return DEFINED_ALPHABET

        if roman.validate_roman_letters(romanLetters) == False:
            return DEFINED_ALPHABET

        if roman.check_roman_letters_for_unique_letters(romanLetters) == False:
            return DEFINED_ALPHABET
