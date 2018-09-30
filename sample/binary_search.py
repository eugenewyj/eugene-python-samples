# -*- coding: utf-8 -*-


def binary_search(list1, item):
	"""
	二分查找
	:param list1: 查找的数组
	:param item: 待查找项
	:return: 查找项在数组中的索引
	"""
	low = 0
	high = len(list1) - 1

	while low <= high:
		mid = (low + high) // 2
		guess = list1[mid]
		if guess == item:
			return mid
		if guess < item:
			low = mid + 1
		else:
			high = mid - 1

	return None


my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))
print(binary_search(my_list, 11))
