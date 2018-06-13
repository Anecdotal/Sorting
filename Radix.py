#Function radix-sorts a list of nonnegative integers (obviously the radix will be 10, unless the integers are in binary or other bases).
#The exponent parameter defines how many digits are in the integer list given (in other words, 10^x).
def radix_sort(intList, exponent, radix):
	for i in range(exponent):
		qList = []
		for k in range(radix):
			qList.append([])
		for x in intList:
			qList[x % (radix**(i+1)) / (radix**(i))].append(x)
		intList = []
		for j in qList:
			if j != []:
				intList.extend(j)
	return intList

for i in range(100000):
	radix_sort([1, 420, 1, 123, 15, 120, 987, 789, 69, 00], 3, 10)
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
