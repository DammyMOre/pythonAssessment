import unittest
import discount

class Discount(unittest.TestCase):
	def test_that_discount_function_exist(self):
		discount.my_discount(150, 15)

	def test_that_discount_function_returns_discount_result(self):
		self.assertEqual(discount.my_discount(150,15),127.5)

	def test_that_discount_function_returns_discount_result_with_floating_value(self):
		self.assertEqual(discount.my_discount(150.5,15),127.925)

	def test_that_discount_function_returns_discount_result_with_floating_percentage(self):
		self.assertEqual(discount.my_discount(150.5,15.75),126.79625)

	def test_that_discount_function_raises_error_with_negative_value(self):
		self.assertRaises(ValueError,discount.my_discount,-150,-12)









	
