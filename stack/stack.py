"""
	by: Andre Christian
	last modified: 20/11/2017
"""

class Stack:
	def __init__(self):
		self.the_stack = []

	def __len__(self):
		return len(self.the_stack)
	
	def is_empty(self):
		return len(self.the_stack) == 0
	
	def peek(self):
		if self.is_empty() == 0:
			return None
		return self.the_stack[-1]
		
	def pop(self):
		if self.is_empty():
			return None
		return self.the_stack.pop()
	
	def push(self, item):
		self.the_stack.append(item)
	