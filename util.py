import random

def move(array, index, index2):
	copy = array[index2]
	while index2 != index:
		array[index2] = array[index2-1]
		index2 -= 1
	array[index] = copy
	return array

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
