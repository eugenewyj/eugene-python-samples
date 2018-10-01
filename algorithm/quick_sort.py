# -*- coding: utf-8 -*-


def quick_sort(arr):
	"""
	快速排序算法
	:param arr:待排序数组
	:return: 排序后数组
	"""
	if len(arr) < 2:
		return arr
	else:
		pivot = arr[0]
		less = [i for i in arr[1:] if i <= pivot]
		greater = [i for i in arr[1:] if i > pivot]

		return quick_sort(less) + [pivot] + quick_sort(greater)


print(quick_sort([10, 5, 2, 3]))

