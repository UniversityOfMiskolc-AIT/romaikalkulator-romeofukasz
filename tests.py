import unittest
from romai_kalkulator import arabic_to_roman, roman_to_arabic, evaulate_roman_number_expression


class EvaluateRomanNumberExpressionTestCase(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(evaulate_roman_number_expression("IX+III"), "XII")

    def test_subtraction(self):
        self.assertEqual(evaulate_roman_number_expression("XIII-V"), "VIII")

    def test_multiplication(self):
        self.assertEqual(evaulate_roman_number_expression("IV*V"), "XX")

    def test_division(self):
        self.assertEqual(evaulate_roman_number_expression("XXXIII/IX"), "III")

    def test_modulus(self):
        self.assertEqual(evaulate_roman_number_expression("XXXX%IX"), "IV")

    def test_exponentiation(self):
        self.assertEqual(evaulate_roman_number_expression("II**VI"), "LXIV")

    def test_complex_expression(self):
        # (II**III/VIII)*III+(VII-III*II) -> (2**3/8)*3+(7-3*2) = 4
        self.assertEqual(evaulate_roman_number_expression("(II**III/VIII)*III+(VII-III*II)"), "IV")

    def test_if_expression_result_out_of_bounds_raises_value_error(self):
        with self.assertRaises(ValueError):
            evaulate_roman_number_expression("X**X")  # 10**10 = 10,000,000,000

    def test_if_non_string_input_raises_type_error(self):
        with self.assertRaises(TypeError):
            evaulate_roman_number_expression(False)

    def test_if_invalid_expression_raises_value_error(self):
        with self.assertRaises(ValueError):
            evaulate_roman_number_expression("X meg X szer III")


class ArabicToRomanTestCase(unittest.TestCase):

    def test_convert_five(self):
        self.assertEqual(arabic_to_roman(5), "V")

    def test_convert_nine(self):
        self.assertEqual(arabic_to_roman(9), "IX")

    def test_convert_ninetynine(self):
        self.assertEqual(arabic_to_roman(99), "XCIX")

    def test_if_non_integer_input_raises_type_error(self):
        with self.assertRaises(TypeError):
            arabic_to_roman("kilenc")

    def test_if_too_high_input_raises_value_error(self):
        with self.assertRaises(ValueError):
            arabic_to_roman(10000)

    def test_if_too_low_input_raises_value_error(self):
        with self.assertRaises(ValueError):
            arabic_to_roman(0)


class RomanToArabicTestCase(unittest.TestCase):

    def test_convert_five(self):
        self.assertEqual(roman_to_arabic("V"), 5)

    def test_convert_nine(self):
        self.assertEqual(roman_to_arabic("IX"), 9)

    def test_convert_ninetynine(self):
        self.assertEqual(roman_to_arabic("XCIX"), 99)

    def test_if_non_string_input_raises_type_error(self):
        with self.assertRaises(TypeError):
            roman_to_arabic(True)

    def test_if_invalid_input_raises_value_error(self):
        with self.assertRaises(ValueError):
            roman_to_arabic("ezer")


if __name__ == "__main__":
    unittest.main()
