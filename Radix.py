#Radix-sorts a list of nonnegative integers
#'array' is a given unsorted array with numbers in some base ('radix'), normally 10
#Each number in the list can have a maximum number of digits 'exponent' (in other words, radix to what exponent is expressed in the highest number)
def radix_sort(array, exponent, radix):
	for i in range(exponent):
		bucketList = []
		for k in range(radix):
			bucketList.append([])
		for x in array:
			bucketList[x % (radix**(i+1)) / (radix**(i))].append(x)
		array = []
		for j in bucketList:
			if j != []:
				array.extend(j)
	return array

#This version of the algorithm is less generalized, with radix of 10 and exponent as 3
#This way, the function only takes in one input, rendering it easier for generalized speed testing
def radix_sort_base10(array):
	for i in range(3):
		qList = []
		for k in range(10):
			qList.append([])
		for x in array:
			qList[x % (10**(i+1)) / (10**(i))].append(x)
		array = []
		for j in qList:
			if j != []:
				array.extend(j)
	return array

'''
print radix_sort([19, 35, 20, 61, 14], 2, 10)
print radix_sort([00, 420, 1, 123, 15], 3, 10)
print radix_sort([35, 20, 69, 0], 2, 10)
print radix_sort([12000, 987, 789, 69, 14, 1], 5, 10)
print radix_sort([1, 2, 5, 9, 0, 0], 1, 10)
print radix_sort([0b10, 0b01, 0b11, 0b100, 0b101], 3, 2) #Interesting because it shifts the binary to base 10 after sorting
print radix_sort([0b10, 0b1100101, 0b11, 0b111, 0b1001], 6, 2)
print radix_sort([0123, 0100, 07, 017, 0777], 3, 8)
'''
