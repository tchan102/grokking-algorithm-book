def dcSum(arr):
	if len(arr) == 1:
		return arr[0]
	return arr[0] + dcSum(arr[1:])
arr = [4,3,2,1]
print(dcSum(arr))
