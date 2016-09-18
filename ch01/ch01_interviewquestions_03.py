# 1.3
def urlify(input):
	return [x if x != ' ' else ['%', '2', '0'] for x in input]