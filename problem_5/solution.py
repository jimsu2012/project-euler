import math

def solution():
	def sqrt_floor(num):
		return math.floor(math.sqrt(num))

	def factorize(num, factor_list=[]):
		for factor_to_check in range(2, sqrt_floor(num) + 1):
			if num % factor_to_check == 0:
				return factorize(num / factor_to_check, factor_list + [factor_to_check])
		return factor_list + [num]

	def is_prime(num):
		return len(factorize(num)) == 1

	def lcm_1_to_n(n):
		primes_list = [num for num in range(2, n + 1) if is_prime(num)]
		lcm = 1 #temporary
		for prime in primes_list:
			prime_highest_power = prime #temporary
			while prime_highest_power * prime < n + 1:
				prime_highest_power *= prime
			lcm *= prime_highest_power
		return lcm

	return lcm_1_to_n(20)

if __name__ == "__main__":
	print(solution())
