def solution():
	def sum_of_consecutive_integers_1_to_n(n):
		return sum(range(1, n+1))

	def sum_of_consecutive_squares_1_to_n(n):
		return sum([i*i for i in range(1, n+1)])

	n = 100
	return sum_of_consecutive_integers_1_to_n(n) ** 2 - sum_of_consecutive_squares_1_to_n(n)

if __name__ == "__main__":
	print(solution())
