import random

listOfElements = [random.randint(1, 100) for _ in range(100)]

for element in listOfElements:
	print(element, end=' ')

print(f"\n{'-'*100}")
for i in range(len(listOfElements)):
	print(listOfElements[i], end=' ')