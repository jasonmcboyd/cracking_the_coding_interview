# 1.2 Given two strings, write a method to determine if one is a permutation
# of the other.
from collections import defaultdict

def arePermutations(first, second):
	counter = defaultdict(int)
	
	for i in first:
		counter[i] += 1
	
	for i in second:
		counter[i] -= 1
		if counter[i] < 0:
			return False
		
	for i in counter.values():
		if i != 0:
			return False
	
	return True