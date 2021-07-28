def solution():
	def fib(n):
		if n == 1 or n == 2:
			return n
		return fib(n - 2) + fib(n - 1)

	max_ = 4000000
	n = 1
	current_fib = fib(n)
	sum_ = 0
	while current_fib < max_:
		if current_fib % 2 == 0:
			sum_ += current_fib
		n += 1
		current_fib = fib(n)
	return sum_

if __name__ == "__main__":
	print(solution())
