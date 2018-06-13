import math

def merge_sort(array):
	if len(array) <= 1:
		# Base case: if the array length is 1 (and therefore is sorted), the recursion stops
		return array
	else:
		# Split the unsorted array into two subarrays
		subarray = []
		subarray2 = []
		for i in range(len(array)):
			if i < math.floor(len(array)/2):
				subarray.append(array[i])
			else:
				subarray2.append(array[i])
		# Sort the two subarrays recursively
		subarray = merge_sort(subarray)
		subarray2 = merge_sort(subarray2)
		# Sort/Combine the two sorted subarrays back into the first array
		j = 0
		k = 0
		i = 0
		while j <= (len(subarray) - 1) and k <= (len(subarray2) - 1):
			if subarray[j] > subarray2[k]:
				array[i] = subarray2[k]
				k += 1
			else:
				array[i] = subarray[j]
				j += 1
			i += 1
		if j == len(subarray):
			for x in range(len(subarray2) - k):
				array[i] = subarray2[k + x] 
				i += 1
		else:
			for x in range(len(subarray) - j):
				array[i] = subarray[j + x] 
				i += 1
		return array

for i in range(100000):
	merge_sort([1, 420, 1, 123, 15, 120, 987, 789, 69, 00])