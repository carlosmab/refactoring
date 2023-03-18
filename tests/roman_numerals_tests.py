import unittest

def convert(number):
    roman = ""

    arabic_numerals = [50, 40, 10, 9, 5, 4, 1]
    roman_numerals = ["L", "XL", "X", "IX", "V", "IV", "I"]

    for i in range(len(arabic_numerals)):
        while number >= arabic_numerals[i]:
            roman += roman_numerals[i]
            number -= arabic_numerals[i]

    return roman


class RomanNumeralsTest(unittest.TestCase):
    def test_for_1(self):
        self.assertEqual(convert(1), "I")  # add assertion here

    def test_for_2(self):
        self.assertEqual(convert(2), "II")

    def test_for_3(self):
        self.assertEqual(convert(3), "III")

    def test_for_4(self):
        self.assertEqual(convert(4), "IV")

    def test_for_5(self):
        self.assertEqual(convert(5), "V")

    def test_for_8(self):
        self.assertEqual(convert(8), "VIII")

    def test_for_9(self):
        self.assertEqual(convert(9), "IX")

    def test_for_10(self):
        self.assertEqual(convert(10), "X")

    def test_for_20(self):
        self.assertEqual(convert(20), "XX")

    def test_for_27(self):
        self.assertEqual(convert(27), "XXVII")

    def test_for_38(self):
        self.assertEqual(convert(38), "XXXVIII")

    def test_for_40(self):
        self.assertEqual(convert(40), "XL")

    def test_for_50(self):
        self.assertEqual(convert(50), "L")


if __name__ == '__main__':
    unittest.main()
