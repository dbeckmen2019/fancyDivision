remainderOrDemicals = raw_input("Would you like to divide calculating remainders or have the answer include decimals? Type remainders for the first and decimals for the second option: ")
remainderOrDemicals.lower()

dividend = raw_input("Enter a dividend: ")
divisor = raw_input("Enter a divisor: ")
#try:
	#dividend = int(dividend)
#except ValueError: 
	#dividend = raw_input("Ynot a real number. Try again: ")

if remainderOrDemicals == "remainders":
	#Since dividend and divisor are int, the variable wholeNumberAnswer will be the rounded down number
	wholeNumberAnswer = dividend/divisor

	#Using the mod operator to calculate the remainder. No other calculations are needed. 
	remainder = dividend%divisor

	#Using format strings avoids the need to change all variables back into strings
	if remainder == 0:
		print("{} divided by {} is {}." .format(dividend, divisor, wholeNumberAnswer))
	else:
		print("{} divided by {} is {} with a remainder of {}." .format(dividend, divisor, wholeNumberAnswer, remainder))
if remainderOrDemicals == "decimals": 
	dividend = float(dividend)
	divisor = float(divisor)
	decimalAnswer = dividend/divisor
	decimalAnswer = round(decimalAnswer,2)
	print("{} divided by {} is {}." .format(dividend, divisor, decimalAnswer))
