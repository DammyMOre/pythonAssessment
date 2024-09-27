import unittest
import dollartonaira

class DollarToNaira(unittest.TestCase):
	def test_that_dollartonaira_function_exist(self):
		dollartonaira.get_dollartonaira(1550)

def test_that_dollartonaira_function_returns_dollartonaira_result(self):
	self.assertEqual(dollartonaira.get_dollartonaira(2),3100)