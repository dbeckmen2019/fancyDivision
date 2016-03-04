remainderOrDemicals = raw_input("Would you like to divide calculating remainders or have the answer include decimals? Type remainders for the first and decimals for the second option: ")
remainderOrDemicals.lower() #any capital letters typed by user will be converted to lowercase

x = 4 #for the conditions on our loops
y = 4

dividend = raw_input("Enter a dividend: ")
while x != 1: #will tell user when the number they entered is not a real number rather than ending program with error
	try:
		dividend = int(dividend)
		x=1 #will break out of loop
	except ValueError: 
		dividend = raw_input("The dividend you entered is not a real number. Try again: ")

divisor = raw_input("Enter a divisor: ")
while y != 1: #same block as above, but for the divisor rather than the dividend. 
	try:
		divisor = int(divisor)
		y = 1
	except ValueError: 
		divisor = raw_input("The divisor you entered is not a real number. Try again: ")

#Dividing while calculating remainders. 
if remainderOrDemicals == "remainders":
	#Since dividend and divisor are int, the variable wholeNumberAnswer will be the rounded down number
	wholeNumberAnswer = dividend / divisor
	#Mod operator to calculate the remainder
	remainder = dividend % divisor
	if remainder == 0: #there is no need to print that the remainder is 0. 
		print("{} divided by {} is {}." .format(dividend, divisor, wholeNumberAnswer))
	else:
		print("{} divided by {} is {} with a remainder of {}." .format(dividend, divisor, wholeNumberAnswer, remainder))

#Divide using decimals. 
if remainderOrDemicals == "decimals": 
	dividend = float(dividend) #have to convert to floats in order to get decimals
	divisor = float(divisor)
	decimalAnswer = dividend / divisor
	decimalAnswer = round(decimalAnswer,2) #rounding function
	print("{} divided by {} is {}." .format(dividend, divisor, decimalAnswer))
