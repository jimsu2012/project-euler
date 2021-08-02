import math

def solution():
	# Order matters; c must be the hypotenuse
	def is_pythagorean_triplet(a, b, c):
		return a*a + b*b == c*c

	def find_pythagorean_triplet_given_sum(sum_):
		c_range_min = math.ceil(sum_ / 3) # c must be larger than a and b
		c_range_max = math.floor(sum_ / 2) # c cannot be larger than the sum of a and b
		for c in range(c_range_min, c_range_max):
			for a in range(1, sum_ - c):
				b = sum_ - a - c
				if is_pythagorean_triplet(a, b, c):
					return (a, b, c)
		return None

	triplet = find_pythagorean_triplet_given_sum(1000)
	(a, b, c) = triplet
	return a * b * c

if __name__ == "__main__":
	print(solution())
