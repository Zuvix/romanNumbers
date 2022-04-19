import unittest
import RomanConverters as roman
import Calculator as calculator

# Testing section for functions "convert_to_int" and "roman_calculator"
class TestRomanConverterAndCalculator(unittest.TestCase):

    #Tests for function "convert_to_int"
    def test1_conversion(self): 
        self.assertEqual(roman.convert_to_int("I"), 1)

    def test2_conversion(self): 
        self.assertEqual(roman.convert_to_int("V"), 5)

    def test3_conversion(self): 
        self.assertEqual(roman.convert_to_int("-I"), -9999)

    def test4_conversion(self): 
        self.assertEqual(roman.convert_to_int("X"), 10)

    def test5_conversion(self): 
        self.assertEqual(roman.convert_to_int("III"), 3)

    def test6_conversion(self): 
        self.assertEqual(roman.convert_to_int("MMMM"), -9999)

    def test7_conversion(self): 
        self.assertEqual(roman.convert_to_int("IIII"), -9999)

    def test8_conversion(self): 
        self.assertEqual(roman.convert_to_int("DD"), -9999)

    def test9_conversion(self): 
        self.assertEqual(roman.convert_to_int("IV"), 4)

    def test10_conversion(self): 
        self.assertEqual(roman.convert_to_int("VX"), -9999)

    def test11_conversion(self): 
        self.assertEqual(roman.convert_to_int("LC"), -9999)

    def test12_conversion(self): 
        self.assertEqual(roman.convert_to_int("DM"), -9999)

    def test13_conversion(self): 
        self.assertEqual(roman.convert_to_int("IL"), -9999)

    def test14_conversion(self): 
        self.assertEqual(roman.convert_to_int("IIV"), -9999)

    def test15_conversion(self): 
        self.assertEqual(roman.convert_to_int("MXXXIV"), 1034)

    def test16_conversion(self): 
        self.assertEqual(roman.convert_to_int("MCMLXXXVIII"), 1988)

    def test17_conversion(self): 
        self.assertEqual(roman.convert_to_int(""), -9999)

    def test18_conversion(self): 
        self.assertEqual(roman.convert_to_int("  CXIX "), 119)

    def test19_conversion(self): 
        self.assertEqual(roman.convert_to_int("CMCM"), -9999)

    def test20_conversion(self): 
        self.assertEqual(roman.convert_to_int("CMM"), -9999)

    def test21_conversion(self): 
        self.assertEqual(roman.convert_to_int("DCM"), -9999)

    def test22_conversion(self): 
        self.assertEqual(roman.convert_to_int("XCIX"), 99)

    def test23_conversion(self): 
        self.assertEqual(roman.convert_to_int("MMMCM"), 3900)

    def test24_conversion(self): 
        self.assertEqual(roman.convert_to_int("CDC"), -9999)

    def test25_conversion(self): 
        self.assertEqual(roman.convert_to_int("IXIV"), -9999)

    def test26_conversion(self): 
        self.assertEqual(roman.convert_to_int("XXXVIX"), -9999)

    def test27_conversion(self): 
        self.assertEqual(roman.convert_to_int("DCD"), -9999)

    def test28_conversion(self): 
        self.assertEqual(roman.convert_to_int(None), -9999)

    def test29_conversion(self): 
        self.assertEqual(roman.convert_to_int("MMMCMXCIX"), 3999)

    def test30_conversion(self): 
        self.assertEqual(roman.convert_to_int("MCDLXXXVIII"), 1488)

    #Tests for function "roman_calculator"
    def test1_calculator(self): 
        self.assertEqual(calculator.roman_calculator("M I"), "Wrong input")

    def test2_calculator(self): 
        self.assertEqual(calculator.roman_calculator("I +- M"), "Wrong input")

    def test3_calculator(self): 
        self.assertEqual(calculator.roman_calculator(None), "Wrong input")
    
    def test4_calculator(self): 
        self.assertEqual(calculator.roman_calculator("****"), "Wrong input")

    def test5_calculator(self): 
        self.assertEqual(calculator.roman_calculator(""), "Wrong input")
    
    def test6_calculator(self): 
        self.assertEqual(calculator.roman_calculator(" I + M "), "MI")
    
    def test7_calculator(self): 
        self.assertEqual(calculator.roman_calculator("I - M - X"), "Wrong input")

    def test8_calculator(self): 
        self.assertEqual(calculator.roman_calculator("X + X +X +X"), "Wrong input")

    def test9_calculator(self): 
        self.assertEqual(calculator.roman_calculator("MMMM + I"), "Wrong input")

    def test10_calculator(self): 
        self.assertEqual(calculator.roman_calculator("V _ I"), "Wrong input")

    def test11_calculator(self): 
        self.assertEqual(calculator.roman_calculator("I + I +    "), "Wrong input")

    def test12_calculator(self): 
        self.assertEqual(calculator.roman_calculator("+ I + I +"), "Wrong input")

    def test13_calculator(self): 
        self.assertEqual(calculator.roman_calculator("XI + I X"), "XX")

    def test14_calculator(self): 
        self.assertEqual(calculator.roman_calculator("XXV/V"), "V")
    
    def test15_calculator(self): 
        self.assertEqual(calculator.roman_calculator("MMCDXLIV-MCCXXII"), "MCCXXII")

    def test16_calculator(self): 
        self.assertEqual(calculator.roman_calculator("I - C"), "Wrong number")

    def test17_calculator(self): 
        self.assertEqual(calculator.roman_calculator("MCDXLIV / MCDXLV"), "Wrong number")

    def test18_calculator(self): 
        self.assertEqual(calculator.roman_calculator("MMM + M"), "Wrong number")
    

# Run tests
if __name__ == '__main__':
    unittest.main()