# Author: Daolin Sheng
# Date: 21/09/2020

"""
Find the sum of all multiples of 3 or 7 below 10000.
"""


def solution_1(n):
    v_sum = 0
    for i in range(1, n):
        if i % 3 == 0 or i % 7 == 0:
            v_sum = v_sum + i

    return v_sum


n = 10000
sum = solution_1(n)
print("the sum of all multiples of 3 or 7 below 10000:", sum)

## answer is 21426429.


"""
What is the smallest positive integer that is evenly dividable by each of the numbers between
1 and 100?
"""


def gcd(a, b):
    if b != 0:
        return gcd(b, a % b)
    else:
        return a


def solution_2(n):
    if n < 1: return None
    if n < 2: return n
    res = n

    for i in range(n - 1, 1, -1):
        if res % i != 0:
            res *= i / gcd(res, i)

    return res


smallest_posi_inter = solution_2(100)
print("the smallest positive integer:", smallest_posi_inter)
# the answer is 7.978644329462954e+115
