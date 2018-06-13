import random

def swap(array, index, index2):
	x = array[index2]
	array[index2] = array[index]
	array[index] = x
	return array

def shuffle(array):
	for i in range(len(array)):
		array = swap(array, i, random.randint(0, len(array)-1))
	return array

def is_sorted(array):
	for i in range(len(array)-1):
		if array[i] > array[i+1]:
			return False
	return True

def bogosort(array):
	while True:
		if is_sorted(array):
			return array
		else:
			array = shuffle(array)

print bogosort([2, 420, 1, 3, 5, 0, 4, 90, 69])

