# Original Problem Statement (page 70):
# Given a smaller string s and a bigger string b, design an algorithm to
# find all permutations of the shorter string within the longer one.
# Print the location of each permutation.
#
# My Problem Statement:
# Given a string 'find' and a string 'search', design an algorithm to
# find all permutations of the 'find' string within 'search'.
# Return a list containing the location of each permutation or an empty
# list if no permutations exist.
#
# The real trick to this problem is not understanding what you are asked
# to find but understanding what you were not asked to find.  The obvious
# solution is calculate every permutation of 'find' and then window over
# search and compare every permutation to that window.  This has an abysmal
# runtime of O(find! * search).  But the problem does not ask that you
# identify the _specific_ permutation that was found but, rather, only that
# you identify that _a_ permutation was found.  That is a major difference
# and it has a huge impact on the solution.
from collections import defaultdict

# O(search) + O(find)
def vii_example_03(search, find):
	
	result = []
	
	# If the length 'find' is longer than the length 'search' then 
	# return an empty array.
	if len(find) > len(search):
		return result
	
	# Hash all the letters 'find' and the number of times they occur.
	# runtime: O(find)
	findDict = defaultdict(int)
	for l in find:
		findDict[l] += 1
	
	# The plan is to window over 'search' and count letters as they 
	# enter and leave the window.  I will use a dictionary to count
	# each letter.
	searchDict = defaultdict(int)
	
	# 'count' is the number of letters in 'findDict' that are not in 
	# agreement with 'searchDict'.  Initialize this to the length of
	# 'find' because 'searchDict' is initially empty so obviously
	# every letter in 'findDict' is not in agreement with 'searchDict'.
	count = len(find)
	
	# This is where I actually move the window across 'search'.
	# runtime: O(search)
	for i in range(len(search)):
		# When the window moves the letter at index 'i' has entered
		# the window.
		newLetter = search[i]
		searchDict[newLetter] += 1
		diff = searchDict[newLetter] - findDict[newLetter]
		# If 'findDict' and 'searchDict' are in agreement for the new
		# letter then decrement 'count'.
		if diff == 0:
			count -= 1
		# If there is a difference of 1 then the two dictionaries were
		# in agreement but they no longer are so increment 'count'.
		if diff == 1:
			count += 1
		
		# When the window moves the letter at index 'i - len(find)' (if it
		# is nonnegative) has left the window.
		if i - len(find) >= 0:
			lostLetter = search[i - len(find)]
			searchDict[lostLetter] -= 1
			diff = searchDict[lostLetter] - findDict[lostLetter]
			# If 'findDict' and 'searchDict' are in agreement for the lost
			# letter then decrement 'count'.
			if diff == 0:
				count -= 1
			# If there is a difference of -1 then the two dictionaries were
			# in agreement but they no longer are so increment 'count'.
			if diff == -1:
				count += 1
		
		# If 'count == 0' then the current window is a permutation of 'find'
		# so add the index of the beginning of the window to 'result'.
		if count == 0:
			result.append(i+1-len(find))
	
	return result
