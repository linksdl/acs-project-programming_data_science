## Author: Daolin Sheng
## Date: 22/09/2020

"""
What is the sum of the numbers on the diagonals in a 2001 by 2001 spiral formed in the
same way?
"""

"""
inferred formula: 
f(0) = 1
f(n) = 16*n**3/3 + 10*n**2 + 26*n/3 + 1 (n >=1 and n%2 != 0).
"""

def solution_1(n):
    if n < 1: return None
    if n % 2 == 0: return None  # the parameter must be an odd number
    if n == 1: return 1
    ra = (n - 1) / 2
    res = 16 * ra ** 3 / 3 + 10 * ra ** 2 + 26 * ra / 3 + 1
    return int(res)


dimension = 2001
print("the sum of the numbers on the diagonals in a ", dimension, " by ", dimension, " spiral is :",
      solution_1(dimension))

"""
What is the dimension of the spiral for which the percentage of primes on the diagonals first
falls below 30%?
"""


## determine whether it is a prime number
def is_prime(i):
    if i <= 1: return False
    if i == 2: return True
    flag = True
    for j in range(2, i):
        if i % j == 0:
            flag = False

    return flag


# print(is_prime(21))

def is_diagonal_prime(i, j):
    if i == j ** 2 or i == j ** 2 - j + 1 or i == j ** 2 - 2 * j + 2 or i == j ** 2 - 3 * j + 3:
        return True
    else:
        return False


def solution_2(n):
    is_over = True
    side_len = 3  # the length of side begin from 3
    prime_diagonal_num = 0
    while is_over:
        prime_num = side_len * 2 - 1
        start = (side_len - 2) ** 2 + 1
        stop = side_len ** 2 + 1
        for i in range(start, stop):
            if is_prime(i):
                # print(i)
                if is_diagonal_prime(i, side_len):
                    # print("===")
                    prime_diagonal_num += 1

        if (prime_diagonal_num / prime_num) * 100 < n:
            # print(prime_diagonal_num/prime_num)
            is_over = False
            return side_len

        side_len += 2


v_percent = 30
print("the length of the side for which the percentage first drops below", v_percent, "%:", solution_2(v_percent))
