import unittest
import RomanToNumberConverter as roman
import MaxNumberFromRoman as maxRoman
import skuska as sk


class Testy_uloha3(unittest.TestCase):

    #def test_Abeceda_I(self):
        #self.assertEqual(roman.romanToNumber("IVXLCDM", "I"(self)::, 1(self)::

    def test_PrazdnaAbeceda(self): 
        roman = sk.RomanNumber("")
        roman.setRomanNumber("MMDCIX")
        self.assertEqual(roman.getValue(), 2609)

    def test_ASDFG(self): 
        roman = sk.RomanNumber("ASDFG")
        roman.setRomanNumber("GGGSA")
        self.assertEqual(roman.getValue(), 306)

    def test_LLA(self): 
        roman = sk.RomanNumber("ALP")
        roman.setRomanNumber("LA")
        roman.setRomanNumber("LLA")
        self.assertEqual(roman.getValue(), 6)

    def test_KLO(self): 
        roman = sk.RomanNumber("POILK")
        roman.setRomanNumber("PI")
        roman.setRomanNumber("KLO")
        self.assertEqual(roman.getValue(), 155)

    def test_IAVXLCQDM(self): 
        roman = sk.RomanNumber("IAVXLCQDM")
        roman.setRomanNumber("QVA")
        self.assertEqual(roman.getValue(), 1015)

    def test_I(self): 
        roman = sk.RomanNumber("I")
        roman.setRomanNumber("I")
        self.assertEqual(roman.getValue(), 1)

    def test_IVXLCDMPQRSTUWY(self): 
        roman = sk.RomanNumber("IVXLCDMPQRSTUWY")
        roman.setRomanNumber("YWUSSSRMMMXLVI")
        self.assertEqual(roman.getValue(), 16353046)


    def test_PrazdneCislo(self): 
        roman = sk.RomanNumber("IVX")
        roman.setRomanNumber("")
        self.assertEqual(roman.getValue(), 0)

    def test_ZleZnakyCisla(self): 
        roman = sk.RomanNumber("IVXLCDM")
        roman.setRomanNumber("MMDXXL")
        self.assertEqual(roman.getValue(), 0)

    def test_IV_IVI(self): 
        roman = sk.RomanNumber("IV")
        roman.setRomanNumber("IVI")
        self.assertEqual(roman.getValue(), 0)

    def test_IV_VIV(self): 
        roman = sk.RomanNumber("IV")
        roman.setRomanNumber("VIV")
        self.assertEqual(roman.getValue(), 0)

    def test_IVX_VX(self): 
        roman = sk.RomanNumber("IVX")
        roman.setRomanNumber("VX")
        self.assertEqual(roman.getValue(), 0)

    def test_IIX(self): 
        roman = sk.RomanNumber("IVX")
        roman.setRomanNumber("IIX")
        self.assertEqual(roman.getValue(), 0)

    def test_IVXL_LC(self): 
        roman = sk.RomanNumber("IVXL")
        roman.setRomanNumber("LC")
        self.assertEqual(roman.getValue(), 0)

    def test_ZlaAbeceda(self): 
        roman = sk.RomanNumber("IVXLCDMSAC")
        roman.setRomanNumber("SMMDCCCLXXXVIII")
        self.assertEqual(roman.getValue(), 0)


    #Class RomanNumberFull
    #Set roman number
    def test_IVXLCDM_MMMDCCCXCIV_Zero(self): 
        roman = sk.RomanNumberFull
        roman.setRomanNumber("MMMDCCCXCIV")
        self.assertEqual(roman.getValue(), 3894)

    def test_IVX_X_Zero(self): 
        roman = sk.RomanNumberFull("OIVX")
        roman.setRomanNumber("XIV")
        self.assertEqual(roman.getValue(), 14)

    def test_IVXLCDMPQRSTUWY_YWUSSSRMMMXLVI_Zero(self): 
        roman = sk.RomanNumberFull("OIVXLCDMPQRSTUWY")
        roman.setRomanNumber("YWUSSSRMMMXLVI")
        self.assertEqual(roman.getValue(), 16353046)

    def test_ABCD_DCCC_Zero(self): 
        roman = sk.RomanNumberFull("OABCD")
        roman.setRomanNumber("DCCCAC")
        self.assertEqual(roman.getValue(), 89)

    def test_TestEfektivnostiPatiek_Zero(self): 
        roman = sk.RomanNumberFull("OIVXLCDMPQRSTUW")
        for i in range(1000):
            roman.setRomanNumber("WUSSSRMMMXLVIII")
            if (roman.getValue() != 6353048):
                self.assertTrue(False)
            
        
        self.assertTrue(True)


    #Wrong roman number
    def test_IV_OIV_Zero(self): 
        roman = sk.RomanNumberFull("OIV")
        self.assertFalse(roman.setRomanNumber("OI"))
        self.assertEqual(roman.getValue(), 0)


    #Get roman number
    def test_IVXLCDMPQRSTUWYZ_53864324_Zero(self): 
        roman = sk.RomanNumberFull("OIVXLCDMPQRSTUWYZ")
        roman.setValue(53864324)
        self.assertEqual(roman.getRomanNumber(), "ZUUUTSSSRQMPCCCXXIV")

    def test_IVXLCDM_3896_Zero(self): 
        roman = sk.RomanNumberFull
        roman.setValue(-3896)
        self.assertEqual(roman.getRomanNumber(), "-MMMDCCCXCVI")

    def test_OMPQRSTUWYZABCD(self): 
        roman = sk.RomanNumberFull("OMPQRSTUWYZABCD")
        roman.setValue(7777777)
        self.assertEqual(roman.getRomanNumber(), "DCCBAAZYYWUUTSSRQQPMM")

    def test_O(self): 
        roman = sk.RomanNumberFull("OMPQRSTUWYZABCD")
        roman.setValue(0)
        self.assertEqual(roman.getRomanNumber(), "O")


# Run tests
if __name__ == '__main__':
    unittest.main()
