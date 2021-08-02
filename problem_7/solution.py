import math

def solution():
	def find_nth_prime(n, sieve_size):
		nums = [0, 0] + list(range(2, sieve_size+2))
		for i in range(2, n+2):
			for j in range(2, math.floor(sieve_size/i)):
				nums[j*i] = 0
		prime_counter = 0
		for i, num in enumerate(nums):
			if num != 0:
				prime_counter += 1
			if prime_counter == n:
				nth_prime_index = i
				break
		return nums[nth_prime_index]
	
	return find_nth_prime(10001, 1000000)

if __name__ == "__main__":
	print(solution())
