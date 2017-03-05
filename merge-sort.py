# Merge sort algorithm
# using recursion
# running time : 6nlog2(n) + 6n

from copy import deepcopy

unsorted = [0, 9, 3, 2, 4, 6, 1, 5, 7, 8]


def merge(l, r, arr):
	# print arr, "l :", l, "r :", r
	i = 0
	j = 0

	nl = len(l)
	nr = len(r)
	k = 0
	while i < nl and j < nr:
		if l[i] < r[j]:
			arr[k] = l[i]
			i += 1
			k += 1
		else:
			arr[k] = r[j]
			j += 1
			k += 1
	# merge remaining list items from each list
	while i < nl:
		arr[k] = l[i]	
		i += 1
		k += 1

	while j < nr:
		arr[k] = r[j]		
		j += 1
		k += 1
	# print arr
	return arr


def merge_sort(unsorted):
	if len(unsorted) < 2:
		return

	n = len(unsorted)
	mid = n/2
	left_list = deepcopy(unsorted[:mid])
	right_list = deepcopy(unsorted[mid:n])
	merge_sort(left_list)
	merge_sort(right_list)
	
	merge(left_list, right_list, unsorted)

	return unsorted

print merge_sort(unsorted)
