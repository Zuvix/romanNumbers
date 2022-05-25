import unittest
import RomanToNumberConverter as roman
import MaxNumberFromRoman as maxRoman

# Testing section for functions "romanToNumber" and "maxNumberFromRomanLetters"

class TestRomanConverterAndMaxNumberFromRoman(unittest.TestCase):

    # Tests for function "romanToNumber"
    # Old tests for converter"
    def test1_conversion(self):
        self.assertEqual(roman.romanToNumber("IVXLCDM", "I"), 1)

    def test2_conversion(self):
        self.assertEqual(roman.romanToNumber("IVXLCDM", "V"), 5)

    def test3_conversion(self):
        self.assertEqual(roman.romanToNumber("IVXLCDM", "-I"), -9999)

    def test4_conversion(self):
        self.assertEqual(roman.romanToNumber("IVXLCDM", "X"), 10)

    def test5_conversion(self):
        self.assertEqual(roman.romanToNumber("IVXLCDM", "III"), 3)

    def test6_conversion(self):
        self.assertEqual(roman.romanToNumber("IVXLCDM", "MMMM"), -9999)

    def test7_conversion(self):
        self.assertEqual(roman.romanToNumber("IVXLCDM", "IIII"), -9999)

    def test8_conversion(self):
        self.assertEqual(roman.romanToNumber("IVXLCDM", "DD"), -9999)

    def test9_conversion(self):
        self.assertEqual(roman.romanToNumber("IVXLCDM", "IV"), 4)

    def test10_conversion(self):
        self.assertEqual(roman.romanToNumber("IVXLCDM", "VX"), -9999)

    def test11_conversion(self):
        self.assertEqual(roman.romanToNumber("IVXLCDM", "LC"), -9999)

    def test12_conversion(self):
        self.assertEqual(roman.romanToNumber("IVXLCDM", "DM"), -9999)

    def test13_conversion(self):
        self.assertEqual(roman.romanToNumber("IVXLCDM", "IL"), -9999)

    def test14_conversion(self):
        self.assertEqual(roman.romanToNumber("IVXLCDM", "IIV"), -9999)

    def test15_conversion(self):
        self.assertEqual(roman.romanToNumber("IVXLCDM", "MXXXIV"), 1034)

    def test16_conversion(self):
        self.assertEqual(roman.romanToNumber("IVXLCDM", "MCMLXXXVIII"), 1988)

    def test17_conversion(self):
        self.assertEqual(roman.romanToNumber("IVXLCDM", ""), -9999)

    def test18_conversion(self):
        self.assertEqual(roman.romanToNumber("IVXLCDM", "  CXIX "), 119)

    def test19_conversion(self):
        self.assertEqual(roman.romanToNumber("IVXLCDM", "CMCM"), -9999)

    def test20_conversion(self):
        self.assertEqual(roman.romanToNumber("IVXLCDM", "CMM"), -9999)

    def test21_conversion(self):
        self.assertEqual(roman.romanToNumber("IVXLCDM", "DCM"), -9999)

    def test22_conversion(self):
        self.assertEqual(roman.romanToNumber("IVXLCDM", "XCIX"), 99)

    def test23_conversion(self):
        self.assertEqual(roman.romanToNumber("IVXLCDM", "MMMCM"), 3900)

    def test24_conversion(self):
        self.assertEqual(roman.romanToNumber("IVXLCDM", "CDC"), -9999)

    def test25_conversion(self):
        self.assertEqual(roman.romanToNumber("IVXLCDM", "IXIV"), -9999)

    def test26_conversion(self):
        self.assertEqual(roman.romanToNumber("IVXLCDM", "XXXVIX"), -9999)

    def test27_conversion(self):
        self.assertEqual(roman.romanToNumber("IVXLCDM", "DCD"), -9999)

    def test28_conversion(self):
        self.assertEqual(roman.romanToNumber("IVXLCDM", None), -9999)

    def test29_conversion(self):
        self.assertEqual(roman.romanToNumber("IVXLCDM", "MMMCMXCIX"), 3999)

    def test30_conversion(self):
        self.assertEqual(roman.romanToNumber("IVXLCDM", "MCDLXXXVIII"), 1488)

    def test31_conversion(self):
        self.assertEqual(roman.romanToNumber("IVXLCDM", "IXV"), -9999)

    # New tests for converter"

    def test32_conversion(self):
        self.assertEqual(roman.romanToNumber("IV", "VIII"), 8)
    
    def test33_conversion(self):
        self.assertEqual(roman.romanToNumber("AKBA", "AK"), -9999)
    
    def test34_conversion(self):
        self.assertEqual(roman.romanToNumber("", "MMM"), -9999)

    def test35_conversion(self):
        self.assertEqual(roman.romanToNumber("TYQW", ""), -9999)

    def test36_conversion(self):
        self.assertEqual(roman.romanToNumber(None, "I"), -9999)

    def test37_conversion(self):
        self.assertEqual(roman.romanToNumber("ABCdE", "BC"), -9999)

    def test38_conversion(self):
        self.assertEqual(roman.romanToNumber(" ABCDE  ", "EEEDAC"), 359)

    def test39_conversion(self):
        self.assertEqual(roman.romanToNumber("@?W", "@@"), -9999)

    def test40_conversion(self):
        self.assertEqual(roman.romanToNumber("I", "IV") , -9999)

    def test41_conversion(self):
        self.assertEqual(roman.romanToNumber("IAVXLCQDM", "QVA") , 1015)

    def test42_conversion(self):
        self.assertEqual(roman.romanToNumber("IVXLCDMPQRS", "SSS") , 300000)
    

    # Tests for function "maxNumberFromRomanLetters"
    def test1_romanMax(self):
        self.assertEqual(maxRoman.maxNumberFromRomanLetters("I"), 3)

    def test2_romanMax(self):
        self.assertEqual(maxRoman.maxNumberFromRomanLetters("A"), 3)

    def test3_romanMax(self):
        self.assertEqual(maxRoman.maxNumberFromRomanLetters("IV+"), -9999)

    def test4_romanMax(self):
        self.assertEqual(maxRoman.maxNumberFromRomanLetters("IV"), 8)

    def test5_romanMax(self):
        self.assertEqual(maxRoman.maxNumberFromRomanLetters("ABC"), 39)

    def test6_romanMax(self):
        self.assertEqual(maxRoman.maxNumberFromRomanLetters("ABKW"), 89)

    def test7_romanMax(self):
        self.assertEqual(maxRoman.maxNumberFromRomanLetters("VI"), 8)

    def test8_romanMax(self):
        self.assertEqual(maxRoman.maxNumberFromRomanLetters("IVXLCDM"), 3999)

    def test9_romanMax(self):
        self.assertEqual(maxRoman.maxNumberFromRomanLetters("IVXLCDMK"), 8999)

    def test10_romanMax(self):
        self.assertEqual(maxRoman.maxNumberFromRomanLetters(""), -9999)

    def test11_romanMax(self):
        self.assertEqual(maxRoman.maxNumberFromRomanLetters("ABABA"), -9999)

    def test12_romanMax(self):
        self.assertEqual(maxRoman.maxNumberFromRomanLetters("QWERT"), 399)


# Run tests
if __name__ == '__main__':
    unittest.main()
