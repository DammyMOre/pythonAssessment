def get_mydiscount(price,discount):
	pass
PERCENTAGE = 100
	percentage_discount = discount/PERCENTAGE
	discounted = percentage_discount * price
	discounted_price = price - discounted 
	return discounted_price

result = my_discount(150, 15)
print(result)