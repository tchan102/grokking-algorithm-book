def binary_search(sorted_arr, target):
	l = 0
	r = len(sorted_arr) - 1
	while l <= r:
		m = l + ((r - l) // 2)
		if sorted_arr[m] == target:
			return m
		if sorted_arr[m] > target:
			r = m - 1
		else:
			l = m + 1
	return None

print(binary_search([1,2,3,4,5], 5))
