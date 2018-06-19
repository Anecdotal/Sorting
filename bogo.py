import util 

def bogo_sort(array):
	while True:
		if util.is_sorted(array):
			return array
		else:
			array = util.shuffle(array)
