# 4.1
# Write out the code for the earlier sum function

def override_sum(arr):
	if len(arr) == 1:
		return arr[0]
	return arr[0] + sum(arr[1:])

# 4.2
# Write a recursive function to count the number of items in a list

def override_count(arr):
	if len(arr) == 0:
		return 0
	return 1 + count(arr[:-1])
# 4.3
def override_max(arr):
	if len(arr) == 1:
		return arr[0]
	n = max(arr[1:])
	return arr[0] if arr[0] > n else n
# 4.4
def binary_search(arr, k):
	l, r = 0, len(arr) - 1
	while l <= r:
		mid = l + (r - l) // 2
		if arr[mid] == k:
			return mid
		if arr[mid] > k:
			r = mid-1
		else:
			l = mid+1
	return None
def dc_binary_search(arr, l, r, k):
	if r >= l:
		mid = l + (r - l) // 2
		if arr[mid] == k:
			return mid
		elif arr[mid] > k:
			return dc_binary_search(arr,l,mid - 1,k)
		else:
			return dc_binary_search(arr,mid + 1,r, k)
	return -1
def quicksort(arr):
	if len(arr) < 2:
		return arr
	pivot = arr[0]
	less = [i for i in arr[1:] if i <= pivot]
	
	greater = [i for i in arr[1:] if i >= pivot]
	
	return quicksort(less) + [pivot] + quicksort(greater)
print(quicksort([10,5,2,3]))
