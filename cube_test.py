
	pass
PERCENTAGE = 100
	percentage_discount = discount/PERCENTAGE
	discounted = percentage_discount * price
	discounted_price = price - discounted 
	return discounted_price

print(result)





def test_that_discount_function_returns_discount_result(self):
	self.assertEqual(discount.get_discount(150,15),127.5)

	def test_that_cube_function_raise_error_with_negative_amount(self):
		self.assertRaises(ValueError, cube.get_cube, -3)
	
	def test_that_cube_function_returns_error_with_string_value(self):
		self.assertRaises(TypeError, cube.get_cube,"byte")


if number < 0:
		raise ValueError("Invalid number")
	return number **3
