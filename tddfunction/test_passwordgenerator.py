import unittest
import passwordgenerator
import string

class Testpasswordgenerator(unittest.TestCase):
	
	def test_that_passwordgenerator_function_exist(self):

		passwordgenerator.get_password()


	def test_that_passwordgenerator_length_is_16(self):

		self.assertEqual(len(passwordgenerator.get_password()), 16)


	def test_that_passwordgenerator_has_uppercase_letter(self):

		password_collection = passwordgenerator.get_password()

		self.assertTrue(any(count for count in password_collection if count in string.ascii_uppercase))




	def test_that_passwordgenerator_has_lowercase_letter(self):

		password_collection = passwordgenerator.get_password()

		self.assertTrue(any(count for count in password_collection if count in string.ascii_lowercase))


	def test_that_passwordgenerator_has_digits(self):

		password_collection = passwordgenerator.get_password()

		self.assertTrue(any(count for count in password_collection if count in string.digits))



	def test_that_passwordgenerator_has_punctuation_symbols(self):

		password_collection = passwordgenerator.get_password()

		self.assertTrue(any(count for count in password_collection if count in string.punctuation))
