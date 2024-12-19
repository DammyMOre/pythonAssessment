import unittest
import discount

class Discount(unittest.TestCase):
	def test_that_discount_function_exist(self):
		discount.get_discount(150, 15)

def test_that_discount_function_returns_discount_result(self):
	self.assertEqual(discount.get_discount(150,15),127.5)