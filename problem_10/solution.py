import math

def solution():
	def find_sum_of_primes_below(upper_bound):
		nums = [0, 0] + list(range(2, upper_bound))
		for i in range(2, math.floor(math.sqrt(upper_bound))+2):
			for j in range(2, math.ceil(upper_bound/i)):
				nums[j*i] = 0
		return sum(nums)

	return find_sum_of_primes_below(2000000)

if __name__ == "__main__":
	print(solution())
