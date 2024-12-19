def divide_or_square(number: float)->int:

	POWER = 0.5

	if type(number) not in [int, float]:
		return "Invalid input"

	if number <= 0:
		raise ValueError("Invalid number")

	if(number % 5 == 0):
		return round(number ** POWER, 2)

