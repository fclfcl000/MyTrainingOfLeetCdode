# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def addTwoNumbers(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		re = None
		tl = None
		gv = 0
		while l1 != None or l2 != None or gv != 0:
			n1 = 0
			n2 = 0
			if l1 != None:
				n1 = l1.val
				l1 = l1.next
			if l2 != None:
				n2 = l2.val
				l2 = l2.next
			add = n1 + n2 + gv
			if tl == None:
				tl = ListNode(add % 10)
				re = tl
			else:
				tl.next = ListNode(add % 10)
				tl = tl.next
			gv = int(add / 10)
		return re
#	def createList(self, v):
#		l = None
#		r = None
#		if v == None:
#			return None
#		for i in v:
#			if l == None:
#				l = ListNode(i)	
#				r = l
#			else:
#				l.next = ListNode(i)
#				l = l.next
#		return r