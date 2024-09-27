def get_cube(number):
	if number < 0:
		raise ValueError("Invalid number")
	return number **3






"""
pseudo code
collect price, save as price
collect discount, save as discount
initialize PERCENTAGE to 100
divide discount by PERCENTAGE
save as percentage_discount
multiply percentage_discount by price
save as discounted
subtract discounted from price
save as discounted_price
display result
"""
def my_discount(price, discount):

	PERCENTAGE = 100
	percentage_discount = discount/PERCENTAGE
	discounted = percentage_discount * price
	discounted_price = price - discounted 
	return discounted_price

result = my_discount(150, 15)
print(result)
	





class DollarToNaira(unittest.TestCase):
	def test_that_dollartonaira_function_exist(self):
		dollartonaira.get_dollartonaira(1550)

def test_that_dollartonaira_function_returns_dollartonaira_result(self):
	self.assertEqual(dollartonaira.get_dollartonaira(2),3100)