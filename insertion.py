import util

def insertion_sort(array):
	for i in range(1, len(array)):
		curr_unsorted = array[i]
		notfound = True
		index_sorted = i-1
		while notfound:
			if curr_unsorted > array[index_sorted] or index_sorted == -1:
				array = util.move(array, index_sorted + 1, i)
				notfound = False
			else:
				index_sorted -= 1
	return array