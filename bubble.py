import util

def bubble_sort(array):
	for j in range(len(array)):
		for i in range(len(array) - j - 1):
			if array[i] > array[i+1]:
				array = util.swap(array, i, i+1)
	return array
