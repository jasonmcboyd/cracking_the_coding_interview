# 1.1 Implement an algorithm to determine if a string has all unique characters
def hasUniqueCharacters(input):
	chars = set()
	# Possible optimization would be to check the length after each add
	# operation and return early.
	for i in input:
		chars.add(i)
	return len(chars) == len(input)
