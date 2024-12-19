import unittest
import dividesquare

class TestDivideSquare(unittest.TestCase):
	def test_that_divide_or_square_function_exist(self):
		dividesquare.divide_or_square(3)

	def test_that_divide_or_square_function_returns_square_root(self):
		self.assertEqual(dividesquare.divide_or_square(10), 3.16)

	
	def test_that_divide_or_square_function_returns_negative_values(self):
		self.assertRaises(ValueError,dividesquare.divide_or_square, -1) 
	
	def test_that_divide_or_square_function_raise_error_with_string_value(self):
		self.assertRaises(TypeError,dividesquare.divide_or_square("sule"), "Invalid input") 
		self.assertRaises(TypeError,dividesquare.divide_or_square(""), "Invalid input") 




