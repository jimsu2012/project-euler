def solution():
	def mults_below(base, max_):
		mults = set()
		mult = base
		while mult < max_:
			mults.add(mult)
			mult += base
		return mults
	
	max_ = 1000
	return sum(mults_below(3, max_) | mults_below(5, max_))

if __name__ == "__main__":
	print(solution())
