# 16.06 Smallest Difference: Given two arrays of integers, compute the pair of
# values (one value in each array) with the smallest (non-negative) difference.
# Return the difference.
def smallestDifference(first, second):
	if (first == None 
		or len(first) == 0 
		or second == None 
		or len(second) == 0):
		return None
	
	first = sorted(first)
	second = sorted(second)
	
	firstIndex = 0
	secondIndex = 0
	
	currentMin = abs(first[firstIndex] - second[secondIndex])
	
	if currentMin == 0:
		return currentMin
		
	while (True):
		if first[firstIndex] < second[secondIndex]:
			if firstIndex != len(first) - 1:
				firstIndex += 1
			else:
				return currentMin
		else:
			if secondIndex != len(second) - 1:
				secondIndex += 1
			else:
				return currentMin
		
		currentMin = min(currentMin, abs(first[firstIndex] - second[secondIndex]))
		
		if currentMin == 0:
			return currentMin