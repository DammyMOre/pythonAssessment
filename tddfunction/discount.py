def my_discount(price, discount):
	PERCENTAGE = 100
	percentage_discount = discount/PERCENTAGE
	discounted = percentage_discount * price
	discounted_price = price - discounted 
	return discounted_price

	if price< 0 or discount < 0:
		raise ValueError("invalid number")

	result = my_discount(-150.5, -15.75)
