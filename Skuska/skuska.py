DEFINED_ALPHABET = "IVXLCDM"


class RomanNumber:
    def __init__(self, romanLetters):
        self.romanLetters = self.check_alphabet(romanLetters)
        self.value = 0

    def romanLetters(self):
        return self.romanLetters

    def maxNumber(self):
        return

    def check_alphabet(self, romanLetters):
        if (str != type(romanLetters)):
            return DEFINED_ALPHABET

        romanLetters = romanLetters.strip()

        if (len(romanLetters) == 0):
            return DEFINED_ALPHABET

        if self.validate_roman_letters(romanLetters) == False:
            return DEFINED_ALPHABET

        if self.check_roman_letters_for_unique_letters(romanLetters) == False:
            return DEFINED_ALPHABET

    def validate_roman_letters(self, romanLetters):
        if romanLetters.isalpha():
            if romanLetters.isupper():
                return True
        return False

    def check_roman_letters_for_unique_letters(self, romanLetters):
        duplicates = []

        for letter in romanLetters:
            if letter not in duplicates:
                duplicates.append(letter)
            else:
                return False
        return True
