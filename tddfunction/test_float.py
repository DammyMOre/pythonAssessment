import unittest
import float

class Float(unittest.TestCase):
	def test_that_only_float_function_exist(self):
		float.only_float(150, 15)


	def test_that_only_float_function_return_only_float(self):
		self.assertEqual(float.only_float(15.5, 15.5),2)
	
	def test_that_only_float_function_return_result(self):
		self.assertEqual(float.only_float(15.5, 15),1)
