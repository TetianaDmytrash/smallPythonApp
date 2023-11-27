import re

print(f'return the longest word in text')

# open(f"C:\\proj_2023\\PeEx\\smallPythonProgram\\longestWord\\text.txt")
with open(f"text.txt") as textFile:
	fileListText = textFile.read().split()
	#re.sub() - replaces all substrings that do not match with empty substrings 
	cleanStrList = [re.sub(r'[^a-zA-Z]', '', strText) for strText in fileListText]
	longestWord = []
	quantityUniqueWord = 0
	quantitySameWord = 0
	for word in fileListText:
		if len(word) == len(max(fileListText, key=len)):
			if word not in longestWord:
				longestWord.append(word)
				quantityUniqueWord += 1
			quantitySameWord += 1
	print(f'longest word: {longestWord[0]}')
	print(f'quantity unique words: {quantityUniqueWord}')
	print(f'quantity words with same length: {quantitySameWord}')



# max(valueList, keyFunk) -> keyFunk-according to which rule they are looking for