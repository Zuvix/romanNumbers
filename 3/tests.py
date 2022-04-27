import unittest
import RomanToNumberConverter as roman

# Testing section for functions "romanToNumber"
class TestRomanConverterAndMaxNumberFromRoman(unittest.TestCase):

    #Tests for function "romanToNumber"
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

    #Tests for function "roman_calculator"
    
    

# Run tests
if __name__ == '__main__':
    unittest.main()