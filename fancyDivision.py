#Author: Drew Beckmen
#Date: 2/4/16

dividend = int(raw_input("Enter a dividend: "))
divisor = int(raw_input("Enter a divisor: "))

#Since dividend and divisor are int, the variable wholeNumberAnswer will be the rounded down number
wholeNumberAnswer = dividend/divisor

#Using the mod operator to calculate the remainder. No other calculations are needed. 
remainder = dividend%divisor

#Using format strings avoids the need to change all variables back into strings
if remainder == 0:
	print("{} divided by {} is {}." .format(dividend, divisor, wholeNumberAnswer))
else:
	print("{} divided by {} is {} with a remainder of {}." .format(dividend, divisor, wholeNumberAnswer, remainder))