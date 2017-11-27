"""
	by: Andre Christian
	last modified: 28/11/2017
"""

def swap(array, a, b):
	array[a], array[b] = array[b], array[a]

#-------------------------------
#SELECTION SORT
#-------------------------------

"""
	@:param: an array of numbers
	@:pre: none
	@:post: returns the max number's index of the array
	@:complexity: O(N) where N is the length of the array
"""
def _get_min(array, left, right):
	assert len(array) > 0, 'Array is empty!'
	min = array[left]
	min_index = left
	for i in range(left, right):
		if array[i] < min:
			min = array[i]
			min_index = i
	return min_index

"""
	@:param: an array of numbers
	@:pre: none
	@:post: sorts the array
	@:complexity: O(N^2) where N is the length of the array
"""
def selection_sort(array):
	for i in range(len(array)-1):
		min_index = _get_min(array, i, len(array))
		swap(array, i, min_index)

#-------------------------------
#INSERTION SORT
#-------------------------------

"""
	@:param: an array of numbers
	@:pre: none
	@:post: sorts the array
	@:complexity:
		worst: O(N^2)
		best: O(N) if the list is sorted
			where N is the length of the array
"""
def insertion_sort(array):
	for i in range(1, len(array)):
		curr = array[i]
		j = i - 1
		while j > -1 and curr < array[j]:
			swap(array, j, j+1)
			j -= 1

#-------------------------------
#BUBBLE SORT
#-------------------------------

"""
	@:param: an array of numbers
	@:pre: none
	@:post: sorts the array
	@:complexity: O(N^2) where N is the length of the array
"""
def bubble_sort(array):
	flag = True
	i = 0
	while i < len(array) and flag:
		flag = False
		for j in range(len(array)-i-1):
			if array[j] > array[j+1]:
				flag = True
				swap(array, j, j+1)
		i += 1

#-------------------------------
#MERGE SORT
#-------------------------------
def _merge(array, left, mid, right, tmp):
	i = left
	j = mid + 1
	for k in range(left, right+1):
		if i > mid:
			tmp[k] = array[j]
			j += 1
		elif j > right:
			tmp[k] = array[i]
			i += 1
		elif array[i] <= array[j]:
			tmp[k] = array[i]
			i += 1
		else:
			tmp[k] = array[j]
			j += 1


def _merge_sort_aux(array, left, right, tmp):
	if left < right:
		mid = (left + right) // 2
		_merge_sort_aux(array, left, mid, tmp)
		_merge_sort_aux(array, mid + 1, right, tmp)
		_merge(array, left, mid, right, tmp)
		for i in range(left, right+1):
			array[i] = tmp[i]

"""
	@:param: an array of numbers
	@:pre: none
	@:post: sorts the array
	@:comp: O(NlogN) where N is the length of the array
"""
def merge_sort(array):
	tmp = [None] * len(array)
	left = 0
	right = len(array) - 1
	_merge_sort_aux(array, left, right, tmp)

#-------------------------------
#QUICK SORT
#-------------------------------

def _partition(array, low, high):
	mid = (low + high) // 2
	pivot = array[mid]

	#switch mid to low
	i = low
	j = low
	k = high - 1
	while i <= k:
		if (array[i] < pivot):
			array[i], array[j] = array[j], array[i]
			i += 1
			j += 1
		elif (array[i] > pivot):
			array[i], array[k] = array[k], array[i]
			k -= 1
		else:
			i += 1
	return j

def _quick_sort_aux(array, low, high):
	if low < high:
		index = _partition(array, low, high)
		_quick_sort_aux(array, low, index)
		_quick_sort_aux(array, index + 1, high)

"""
	@:param: an array of numbers
	@:pre: none
	@:post: sorts the array
"""
def quick_sort(array):
	_quick_sort_aux(array, 0, len(array))

