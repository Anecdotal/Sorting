import math
def build_max_heap(array):
	# Starts at halfway through the list (skipping leaf nodes)
	i = math.floor(len(array)/2)
	while i > 0:
		# Max_heapifies all the subheaps
		max_heapify(array, int(i))
		i -= 1
	return array

def max_heapify(array, index):
	# Defines indexes of left and right children
	leftChild = 2 * index
	rightChild = 2 * index + 1
	# Finds the index of the largest node of a parent and its children
	if leftChild <= len(array) and array[leftChild - 1] > array[index - 1]:
		largest = leftChild 
	else:
		largest = index
	if rightChild <= len(array) and array[rightChild - 1] > array[largest - 1]:
		largest = rightChild
	if largest != index:
		# Swap the largest with the root node
		swap = array[index - 1]
		array[index - 1] = array[largest - 1]
		array[largest - 1] = swap
		# Max_Heapify the swapped node, in case of errors caused by the swaps
		max_heapify(array, largest) 

def heap_sort(array):
	# Builds a max heap of the array
	array = build_max_heap(array)
	# Iteratively puts the highest element (the first) at the front of another array, sorting the list
	array_sorted = []
	for i in range(len(array)):
		array_sorted.insert(0, array[0])
		# Swaps the last element into first
		array[0] = array[-1]
		del array[-1]
		# Max_heapifies the array to correct for the swap
		max_heapify(array, 1)
	return array_sorted

for i in range(100000):
	heap_sort([12, 420, 1, 69, 0])


