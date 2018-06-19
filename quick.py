import util

def quick_sort(array):
	if len(array) <= 1:
		return array
	else:
		pivot = array[len(array) - 1]
		wall = 0
		for i in range(len(array) - 1):
			if array[i] < pivot:
				array = util.swap(array, i, wall)
				wall += 1
		array = util.swap(array, len(array)-1, wall)
		subarray = quick_sort(array[:wall])
		subarray2 = quick_sort(array[wall+1:])
		array = subarray + [array[wall]] + subarray2
		return array