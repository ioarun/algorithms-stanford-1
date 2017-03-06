# Counting inversions using recursion
# Time complexity : O(nlogn)
# D(n) = B(n/2) + C(n/2)
# The split inversions involving an element y
# of 2nd array C are precisely the numbers left in
# the array B when y gets copied to the output D
#
# Reason : Inversion means P[i] > Q[j] where i < j.
# If we have two sorted arrays B and C which are components
# of D, if any element y in C is less than an element in B,
# then y should be less than all the elements in B after that element.
# Hence has split inversion with all those remaining elements in B

from copy import deepcopy

array = [5 , 1, 7, 2, 4, 6, 3, 8]
# array = [1, 2, 3, 4, 5, 6]
count = 0

def merge_countinv(left, right, arr):
	global count
	nl = len(left)
	nr = len(right)
	i = 0
	j = 0
	k = 0

	while i < nl and j < nr:
		if left[i] < right[j]:
			arr[k] = left[i]
			i += 1
			k += 1
		else:
			arr[k] = right[j]
			j += 1
			k += 1
			count += len(left[i:len(left)])

	while i < nl:
		arr[k] = left[i]
		i += 1
		k += 1

	while j < nr:
		arr[k] = right[j]
		j += 1
		k += 1

def merge_sort_countinv(arr):
	n = len(arr)
	if n == 1:
		return

	mid = n/2

	left_list = deepcopy(arr[:mid])
	right_list = deepcopy(arr[mid:n])

	merge_sort_countinv(left_list)
	merge_sort_countinv(right_list)
	merge_countinv(left_list, right_list, arr)

merge_sort_countinv(array)

print count