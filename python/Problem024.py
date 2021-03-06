#!/usr/bin/python
import time

# https://www.nayuki.io/page/next-lexicographical-permutation-algorithm

def next_permutation(arr):
	# Find non-increasing suffix
	i = len(arr) - 1
	while i > 0 and arr[i - 1] >= arr[i]:
		i -= 1
	if i <= 0:
		return False
	
	# Find successor to pivot
	j = len(arr) - 1
	while arr[j] <= arr[i - 1]:
		j -= 1
	arr[i - 1], arr[j] = arr[j], arr[i - 1]
	
	# Reverse suffix
	arr[i : ] = arr[len(arr) - 1 : i - 1 : -1]
	return True

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

start = time.clock()
for i in range(1000000):
	next_permutation(arr)
print "".join(map(str, arr))
print(time.clock() - start)
