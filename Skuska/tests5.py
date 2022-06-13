import unittest
import RomanToNumberConverter as roman
import MaxNumberFromRoman as maxRoman
import SkuskaMain as sk


class Testy_uloha5(unittest.TestCase):

    def test_cislice_I_1(self): 
        number = sk.RomanNumber("I", 1)
        self.assertEqual(number.maxNumber(), 3)

    def test_cislice_I_0(self):
        number = sk.RomanNumber("IV", 0)
        self.assertEqual(number.maxNumber(), 3999)

    def test_maxPrivelky(self):
        number = sk.RomanNumber("IVXLC", 4000)
        self.assertEqual(number.maxNumber(), 3999)

    def test_inaNula_II(self): 
        number = sk.RomanNumber("XYZ", 5)
        self.assertEqual(number.romanLetters(), "XY")
        self.assertEqual(number.maxNumber(), 8)

    def test_OIVXLCDMPQWE_II(self):
        number = sk.RomanNumber("IVXLCDMPQWE", 8900)
        self.assertEqual(number.maxNumber(), 8999)

    def test_maximumOIVXLC_II(self): 
        number = sk.RomanNumber("IVXLCD", 399)
        self.assertEqual(number.maxNumber(), 399)

    def test_O_II(self):
        number = sk.RomanNumber("IV", -1)
        self.assertEqual(number.maxNumber(), 3999)

    def test_minimumOIVXL_II(self): 
        number = sk.RomanNumber("IVXLC", 111)
        self.assertEqual(number.maxNumber(), 399)

    def test_prazdne_II(self):
        number = sk.RomanNumber("", 3)
        self.assertEqual(number.maxNumber(), 3)

    def test_male(self):
        number = sk.RomanNumber("IUHTw", 100)
        self.assertEqual(number.maxNumber(), 399)

    def test_rimskeCisla_max3(self):
        number = sk.RomanNumber("IVXLC", 1)
        self.assertEqual(number.romanLetters(), "I")

    def test_rimskeCisla_max499(self):
        number = sk.RomanNumber("IVXLCDM", 499)
        self.assertEqual(number.romanLetters(), "IVXLCD")


# Run tests
if __name__ == '__main__':
    unittest.main()
