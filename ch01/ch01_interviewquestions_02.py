# 1.2 Given two strings, write a method to determine if one is a permutation
# of the other.
from collections import defaultdict

def arePermutations(first, second):
	# If the two strings are not the same length then 
	# they are not permutations of each other.
	if len(first) != len(second):
		return False
	
	# Create a default dictionary to track the number
	# of occurrences of each character
	counter = defaultdict(int)
	
	# Count all of the characters in the first string.
	for i in first:
		counter[i] += 1
	
	# For every character in the second string decrement
	# the count of that character in the dictionary.
	# If the resulting count is less than zero then we
	# have found a character in the second string that
	# was not in the first string.
	#
	# But what happens if there are fewer occurrences of 
	# a character in the second string than the first, 
	# you say.
	# The early termination test only checks for the case
	# when there are more of a particular character in the
	# second string than the first, you say.
	# Good point, but we know the two strings are the same
	# length (see first test at the top of the method). 
	# So if the second string has fewer of one character
	# but the two strings are the same length then it must
	# be the case that the second string has more of a
	# different character.  We will eventually come across
	# that character and terminate early.
	for i in second:
		counter[i] -= 1
		if counter[i] < 0:
			return False
			
	# If we have not returned yet then the two strings
	# are permutations.
	return True
