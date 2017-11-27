"""
	by: Andre Christian
	last modified: 20/11/2017
"""

class Node:
	def __init__(self, item, n=None):
		self.value = item
		self.next = n

class Queue:
	def __init__(self):
		self.front = None
		self.back = None
		self.count = 0
	
	def __len__(self):
		return self.count
	
	def is_empty(self):
		return self.count == 0
		
	def is_full(self):
		return False
		
	def append(self, item):
		new_node = Node(item)
		if self.is_empty():
			self.front = new_node
		else:
			self.back.next = new_node
		self.back = new_node
		self.count += 1
	
	def serve(self):
		if self.is_empty():
			return None
		ret = self.front.value
		self.front = self.front.next
		self.count -= 1
		if self.is_empty():
			self.back = None
		return ret
		
	