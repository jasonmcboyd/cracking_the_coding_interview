# 10.1 Sorted Merge: You are given two sorted arrays, A and B, where A
# has a large enough buffer at the end to hold B.  Write a method to 
# merge B into A in sorted order.
def merge(A, B):
	a = len(A)-len(B)-1
	b = len(B)-1
	i = len(A)-1
	while a >= 0 and b >= 0:
		if A[a] > B[b]:
			A[i] = A[a]
			a -= 1
		else:
			A[i] = B[b]
			b -= 1
		i -= 1
	
	while a >= 0:
		A[i] = A[a]
		a -= 1
		i -= 1
	
	while b >= 0:
		A[i] = B[b]
		b -= 1
		i -= 1
	
	return A