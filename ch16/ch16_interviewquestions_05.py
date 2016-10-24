# 16.05 Factorial Zeros: Write an algorithm which computes the number of
# trailing zeros in n factorial.
def factorialZeros(num):
	divisor = 5
	result = 0
	quotient = num // divisor
	while quotient > 0:
		result += quotient
		quotient //= 5
	return result