def gravity_sort(array):
	#Construct bead structure
	beads_not_built = 1
	cols = []
	while beads_not_built != 0:
		list_sum = 0
		col = []
		for i in range(len(array)):
			if array[i] != 0:
				col.append(1) 
				array[i] -= 1
			else:
				col.append(0)
			list_sum += array[i]
		cols.append(col)
		beads_not_built = list_sum
	#Go Through Each Column
	for col in cols:
		#Let 'Gravity' Take Its Course
		num_ones = 0
		num_correct = 0
		for bead in col:
			num_ones += bead
		i = len(col) - 1
		while num_ones != 0:
			if num_correct == num_ones:
				if col[i] == 1:
					col[i] = 0
					num_ones -= 1
					num_correct -= 1
			else:
				if col[i] == 0:
					col[i] = 1
					num_correct += 1
				else:
					num_ones -= 1
			i -= 1
	for element in array:
		element = 0
	for col in cols:
		for i in range(len(col)):
			array[i] += col[i]
	return array
