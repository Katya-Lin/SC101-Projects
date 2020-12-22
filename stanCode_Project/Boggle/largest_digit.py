"""
File: largest_digit.py
Name: Katya Lin
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""

def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n:
	:return:
	"""

	if int(n/10) == 0:
		return n

	if int(n/10):
		max = 0

		if n < 0:
			n = -n
		last_num = n % 10
		if last_num > max:
			max = last_num

		if max < find_largest_digit(int(n / 10)):
			max = find_largest_digit(int(n/10))

		return max




if __name__ == '__main__':
	main()
