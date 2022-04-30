def selection_sort(unsorted_list):
	sorted_list = list()
	for i in range(len(unsorted_list)):
		minimum = min(unsorted_list)
		sorted_list.append(minimum)
		unsorted_list.remove(minimum)
	return sorted_list

print(selection_sort([5,4,3,2,1]))
