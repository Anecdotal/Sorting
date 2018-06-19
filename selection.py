import util

def selection_sort(array):
	for i in range(len(array)):
		smallest = i
		for j in range(i+1, len(array)):
			if array[smallest] > array[j]:
				smallest = j
		array = util.swap(array, i, smallest)
	return array