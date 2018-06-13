import time
import radix
import bogo
import merge
import heap
import random

def speed_test(algo, generate_input, input_length, x):
	start = time.clock()
	for i in range(x):
		if input_length == 0:
			randInput = generate_input(random.randint(1, 100)) # Generalize upper bound for random length?
		else:
			randInput = generate_input(input_length)
		algo(randInput)
		total = time.clock()
	total -= start
	if input_length == 0:
		total /= x
	return total

def generate_array(length):
	array = []
	for i in range(length):
		array.append(random.randint(0, 999)) # Generalize upper bound for list members?
	return array

def asymptotic_test(algo, generate_input, x):
	array = []
	for i in range(20):
		array.append(speed_test(algo, generate_input, i, x))
	return array

print "Radix is"
print asymptotic_test(radix.radix_sort2, generate_array, 10000)
print "Merge is"
print asymptotic_test(merge.merge_sort, generate_array, 10000)
print "Heap is"
print asymptotic_test(heap.heap_sort, generate_array, 10000)



	

