def correctInput():
	number = 0
	while True:
		try:
			number = float(input("Please enter a number: "))
			break
		except ValueError:
			print("That was no valid number. Try again...")
	return number


firstNumber = correctInput()
secondNumber = correctInput()
thirdNumber = correctInput()

# first variant
if firstNumber > secondNumber and firstNumber > thirdNumber:
	greatestNumber = firstNumber
elif secondNumber > firstNumber and secondNumber > thirdNumber:
	greatestNumber = secondNumber
else: 
	greatestNumber = thirdNumber

print(f'The greatest number is {greatestNumber}')

# second variant
numbers = []
numbers.append(firstNumber)
numbers.append(secondNumber)
numbers.append(thirdNumber)
print(f'The greatest number is {max(numbers)}')

# third variant
from functools import reduce

greatest = reduce(lambda x, y: x if x > y else y, numbers)
print(f'The greatest number is {greatest}')

# fourth variant
numbers.sort()
print(f'The greatest number is {numbers[-1]}')