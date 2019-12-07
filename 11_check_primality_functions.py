#!/usr/bin/env python3

def check_prime_number(x: int) -> bool:
	if x == 2:
		return True
	elif (x < 3) or (x % 2 == 0):
		return False

	d = 3
	while d * d <= x:
		if x % d == 0:
			return False
		d += 1
	return True


def main():
	number = int(input('Enter a number, bro >>> '))
	if check_prime_number(number):
		print('It seems that {} is prime.'.format(number))
	else:
		print('Nope, it\'s not prime')


if __name__ == '__main__':
	main()
