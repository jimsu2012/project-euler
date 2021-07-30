import math

def solution():
	def is_palindrome(num):
		num_str = str(num)
		num_str_len = len(num_str)
		return all([num_str[i] == num_str[-i-1] for i in range(math.floor(num_str_len / 2))])

	def compute_largest_palindromic_product(digit_count):
		range_n_digit = range(pow(10, digit_count) - 1, pow(10, digit_count - 1) - 1, -1)
		palindrome_products = []
		for i in range_n_digit:
			for j in range_n_digit:
				product = i * j
				if is_palindrome(product):
					palindrome_products.append(product)
					break
		return max(palindrome_products)

	return compute_largest_palindromic_product(3)

if __name__ == "__main__":
	print(solution())
