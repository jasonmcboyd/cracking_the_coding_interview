# 2.6 Palindrome: Implement a function to check if a linked list is 
# a palindrome.
def isLinkedListAPalindrome(linkedList):
	chase = linkedList._head
	if chase == None:
		return True
	lead = chase._next
	if lead == None:
		return True
	stack = deque()
	while lead != None:
		stack.append(chase.value)
		chase = chase._next
		lead = lead._next
		if lead == None:
			break
		lead = lead._next
		if lead == None:
			chase = chase._next
	while len(stack) > 0:
		if stack.pop() != chase.value:
			return False
		chase = chase._next
	return True