import math
 
def solution():
    def sqrt_floor(num):
        return math.floor(math.sqrt(num))
 
    def factorize(num, factor_list=[]):
        for factor_to_check in range(2, sqrt_floor(num)):
            if num % factor_to_check == 0:
                return factorize(num / factor_to_check, factor_list + [factor_to_check])
        return factor_list + [num]
 
    def find_largest_prime_factor(num):
        return max(factorize(num))
 
    num = 600851475143
    return find_largest_prime_factor(num)
 
if __name__ == "__main__":
    print(solution())
