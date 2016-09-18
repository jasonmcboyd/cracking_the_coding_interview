# 2.5 Sum Lists: You have two numbers represented by a linked list,
# where each node contains a single digit.  The digits are stored 
# in reverse order, such that the 1's digit is at the head of the 
# list.  Write a function thhat adds the two numbers and returns the
# sum as a linked list.
def addLinkedLists(list1, list2):
	result = SinglyLinkedList()
	node1 = list1.first()
	node2 = list2.first()
	carry = 0
	while node1 != None or node2 != None:
		num1 = 0
		num2 = 0
		if node1 != None:
			num1 = node1.value
			node1 = node1._next
		if node2 != None:
			num2 = node2.value
			node2 = node2._next
		num1 += num2 + carry
		if num1 >= 10:
			carry = 1
			num1 -= 10
		else:
			carry = 0
		result.addLast(num1)
	if carry == 1:
		result.addLast(1)
	return result