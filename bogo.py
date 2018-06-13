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

def bogo_sort(array):
	while True:
		if is_sorted(array):
			return array
		else:
			array = shuffle(array)

for i in range(10000):
	bogo_sort([12, 420, 1, 69, 0])

