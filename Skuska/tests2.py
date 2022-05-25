import unittest
import RomanToNumberConverter as roman
import MaxNumberFromRoman as maxRoman
import skuska as sk


class Testy_uloha2(unittest.TestCase):

    #def test_Abeceda_I(self):
        #self.assertEqual(roman.romanToNumber("IVXLCDM", "I"(self)::, 1(self)::

    def test_IVXLCDM_1_Zero(self):
        roman = sk.RomanNumber()
        self.assertEqual(roman.maximum(), 3999)
        self.assertEqual(roman.minimum(), -3999)

    def test_OI(self): 
        roman = sk.RomanNumber("OI")
        self.assertEqual(roman.maximum(), 3)
        self.assertEqual(roman.minimum(), -3)

    def test_O(self): 
        roman = sk.RomanNumber("O")
        self.assertEqual(roman.maximum(), 3999)
        self.assertEqual(roman.minimum(), -3999)

    def test_ABCDEFGHIJKLMN(self): 
        roman = sk.RomanNumber("ABCDEFGHIJKLMN")
        self.assertEqual(roman.maximum(), 3999999)
        self.assertEqual(roman.minimum(), -3999999)

    def test_IVXLCDMPQRSTUWYZ_53864324_Zero(self): 
        roman = sk.RomanNumber("OIVXLCDMPQRSTUWYZ")
        self.assertEqual(roman.maximum(), 89999999)
        self.assertEqual(roman.minimum(), -89999999)


    def test_IVXLCDM_3896(self): 
        roman = sk.RomanNumber()
        roman.setValue(-3896)
        self.assertEqual(roman.getValue(), -3896)

    def test_Zero(self): 
        roman = sk.RomanNumber()
        self.assertTrue(roman.setValue(0))
        self.assertEqual(roman.getValue(), 0)

    def test_IVXLCDM_NO_NUMBER_MAX_Zero(self): 
        roman = sk.RomanNumber()
        self.assertFalse(roman.setValue(4000))
        self.assertEqual(roman.getValue(), 0)

    def test_I_I_5(self): 
        roman = sk.RomanNumber("I")
        roman.setValue(5)
        self.assertEqual(roman.getValue(), 5)

    def test_IVXLCDMPQRSTUWYZ_53864324(self): 
        roman = sk.RomanNumber("OIVXLCDMPQRSTUWYZ")
        roman.setValue(53864324)
        self.assertEqual(roman.getValue(), 53864324)


    def test_TestEfektivnosti_Zero(self):
        for i in range(1000):
            roman = sk.RomanNumber("OIVXLCDMPQRSTUWY")
            roman.setValue(16353048)
            if (roman.getValue() != 16353048): 
                self.assertTrue(False)
            
        self.assertTrue(True)


# Run tests
if __name__ == '__main__':
    unittest.main()
