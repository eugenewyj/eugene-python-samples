# -*- coding: utf-8 -*-


def find_smallest(arr):
	"""
	查找数组中最小元素的索引
	:param arr: 未排序数组
	:return: 返回数组中最小元素的索引
	"""
	smallest = arr[0]
	smallest_index = 0
	for i in range(1, len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
			smallest_index = i
	return smallest_index


def select_sort(arr):
	"""
	选择排序算法实现按照从小到大排序数组
	:param arr: 待排序数组
	:return: 排序后数组
	"""
	new_arr = []
	for i in range(len(arr)):
		smallest = find_smallest(arr)
		new_arr.append(arr.pop(smallest))
	return new_arr


print(select_sort([5, 3, 6, 2, 10]))


