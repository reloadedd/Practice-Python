#!/usr/bin/env python3


def first_and_last_element_list(the_list):
	"""This function takes a list and returns a new list that contains only the first and the last element of list given as parameter.
	"""
	new_list = []
	new_list.append(the_list[0])
	new_list.append(the_list[-1])
	return new_list


def main():
	a = [5, 10, 15, 20, 25]
	list_2 = first_and_last_element_list(a)
	print(list_2)


if __name__ == '__main__':
	main()
