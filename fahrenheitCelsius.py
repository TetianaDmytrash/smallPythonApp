import random

THERMOMETR_SCALE_NUMBER_SYSTEM = ['Fahrenheit', 'Celsius']

def calculateCelsius(degrees):
	return (degrees - 32) * (5/9)

def calculateFahrenheit(degrees):
	return ((degrees * (9/5)) + 32)

def choiceConvertor():
	while True:
		'''choice what conver do'''
		print(f'Convertor: Fahrenheit || Celsius')
		print(f'press 1: fahrenheit -> celsius')
		print(f'press 2: celsius -> fahrenheit')
		userChoice = int(input(f'select conversion method: '))
		if userChoice == 1 || userChoice == 2:
			return userChoice

def enterUserDegrees():
	while True:
		'''enter the number'''
		try:
			userTemperature = float(input(f'Enter temperature in {THERMOMETR_SCALE_NUMBER_SYSTEM[calculateChoice-1]}: '))
			return userTemperature
		except ValueError:
			print(f'Oops!  That was no valid temperature.  Try again...')


if __name__ == '__main__':
	userChoice = choiceConvertor()
	userDegrees = enterUserDegrees()
	print(f'the result: {userDegrees} in ', end='')
	print(f'{THERMOMETR_SCALE_NUMBER_SYSTEM[userChoice-1]} -> ', end='')
	if userChoice == 1:
		celsiusResult = calculateCelsius(degrees=userDegrees)
		print(f'{celsiusResult} in {THERMOMETR_SCALE_NUMBER_SYSTEM[userChoice]}')
	elif userChoice == 2:
		fahrenheitResult = calculateFahrenheit(degrees=userDegrees)
		print(f'{fahrenheitResult} in {THERMOMETR_SCALE_NUMBER_SYSTEM[userChoice%2]}')
	else:
		print(f'it situation unknown for me')

