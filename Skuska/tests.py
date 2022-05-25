import unittest
import RomanToNumberConverter as roman
import MaxNumberFromRoman as maxRoman
import skuska as sk


class Testy_uloha1(unittest.TestCase):

    #def test_Abeceda_I(self)::
        #self.assertEqual(roman.romanToNumber("IVXLCDM", "I"(self)::, 1(self)::

    def test_Abeceda_I(self):
        roman = sk.RomanNumber("I")
        self.assertEqual(roman.romanLetters(), "I")

    def test_Abeceda_IVXLCDMQF(self): 
        roman = sk.RomanNumber("IVXLCDMQF")
        self.assertEqual(roman.romanLetters(), "IVXLCDMQF")

    def test_ZlaAbecedaPismena(self): 
        roman = sk.RomanNumber("IVXLCDMSAC")
        self.assertEqual(roman.romanLetters(), "IVXLCDM")

    def test_maxZlychPismeniek(self): 
        roman = sk.RomanNumber("IVXLCI")
        self.assertEqual(roman.maxNumber(), 3999)

    def test_prazdnyMax(self): 
        roman = sk.RomanNumber(" ")
        self.assertEqual(roman.maxNumber(), 3999)

    def test_max_V(self): 
        roman = sk.RomanNumber("V")
        self.assertEqual(roman.maxNumber(), 3)

    def test_max_IV(self): 
        roman = sk.RomanNumber("IV")
        self.assertEqual(roman.maxNumber(), 8)

    def test_max_IVXL(self): 
        roman = sk.RomanNumber("IVXL")
        self.assertEqual(roman.maxNumber(), 89)

    def test_max_IVXLC(self): 
        roman = sk.RomanNumber("IVXLC")
        self.assertEqual(roman.maxNumber(), 399)

    def test_max_IVXLCDMQF(self): 
        roman = sk.RomanNumber("IVXLCDMQF")
        self.assertEqual(roman.maxNumber(), 39999)

    def test_IVXLCDM_3896(self): 
        roman = sk.RomanNumber
        roman.setValue(3896)
        self.assertEqual(roman.getValue(), 3896)

    def test_I_3(self):
        roman = sk.RomanNumber("I")
        roman.setValue(3)
        self.assertEqual(roman.getValue(), 3)

    def test_IVXLCDM_0(self): 
        roman = sk.RomanNumber
        self.assertFalse(roman.setValue(0))

    def test_IVXLCDM_NO_NUMBER(self): 
        roman = sk.RomanNumber
        self.assertEqual(roman.getValue(), 0)

    def test_IVXLCDM_NO_NUMBER_MAX(self): 
        roman = sk.RomanNumber
        self.assertFalse(roman.setValue(4000))
        self.assertEqual(roman.getValue(), 0)

    def test_IVXLCDMPQRSTUWYZ_53864324(self): 
        roman = sk.RomanNumber("IVXLCDMPQRSTUWYZ")
        roman.setValue(53864324)
        self.assertEqual(roman.getValue(), 53864324)

    def test_IVX_10(self): 
        roman = sk.RomanNumber("IVX")
        roman.setValue(10)
        self.assertEqual(roman.getValue(), 10)

    def test_IVX_39(self): 
        roman = sk.RomanNumber("IVX")
        roman.setValue(39)
        self.assertEqual(roman.getValue(), 39)

    def test_IVX_40(self):
        roman = sk.RomanNumber("IVX")
        roman.setValue(40)
        self.assertEqual(roman.getValue(), 0)

    def test_IVXLCDMPQRSTUWY_16353046(self): 
        roman = sk.RomanNumber("IVXLCDMPQRSTUWY")
        roman.setValue(16353046)
        self.assertEqual(roman.getValue(), 16353046)

    def test_ABCD_80(self): 
        roman = sk.RomanNumber("ABCD")
        roman.setValue(80)
        self.assertEqual(roman.getValue(), 80)


# Run tests
if __name__ == '__main__':
    unittest.main()
