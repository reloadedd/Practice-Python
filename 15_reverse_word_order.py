#!/usr/bin/env python3


def reverse_string() -> None:
	"""This function asks the user for a string and then returns the reversed
	version of the string."""
	input_string = input('Enter a string >>> ')
	reversed_string = input_string.split()
	reversed_string.reverse()	# reverse the list withing itself

	reversed_string = ' '.join(reversed_string)
	print(reversed_string)


def main():
	reverse_string()


if __name__ == '__main__':
	main()
