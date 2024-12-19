import unittest
import practicepasswordgenerator

class Testpracticepasswordgenerator(unittest.TestCase):

	def test_that_practicepasswordgenerator_function_exist(self):

		practicepasswordgenerator.get_password()


	def test_that_practicepasswordgenerator_length_is_12(self):
		
		self.assertEqual(len(practicepasswordgenerator.get_password()), 12)



	def test_that_practicepasswordgenerator_has_uppercase_letters(self):
		password_collector = practicepasswordgenerator.get_password
		
		self.assertTrue(any(for count in password_collector if count in string.ascii_uppercase))