# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Project : acs-project-programming_data_science      
@File    : test.py
@Author  : Billy Sheng 
@Contact : shengdl999links@gmail.com  
@Date    : 2020/12/8 10:02 上午
@Version  : 1.0.0
@License : Apache License 2.0
@Desc    : None
"""

# Q3
def ooo(s):
    return s[1:] + s[0]


# print(ooo('nPytho'))
# Python

# Q4
# work_list = list("WORK")
# del work_list[0]
# del work_list[2]
# result_string = "".join(work_list)
# print( result_string )

# Q6  Fish 'n' Chips
# def tttt(s):
#     if '-' in s or "'" in s:
#         return False
#     if not s.islower():
#         return False
#     s = s.replace('//', '-').title()
#     s = s.replace('-And-', " 'n' ")
#     return s
#
# print(tttt('fish//and//chips'))

# Q7
# for n in range(3, 1000):
#     flag = False
#     for k in range( 2, n ):
#         if (n % k == 0):
#             flag = True
#     if not flag:
#         print( n, end= " " )

# Q8
# def analyse(s):
#     L = list(s)
#     if not L == sorted(L):
#         return False
#     return set([(L.count(x),x) for x in L ])
#
# print(analyse('1aabccccddd'))

# Q9
# import random
#
# # Set temp to random value in range 1-100.
# temp = random.randint(1, 100)
#
# # Check whether temp is in tolerable range.
# if (temp > 16 or temp < 27):
#   print( "Temperature tolerable. :)1111111")
# else:
#   print( "Temperature intolerable. :(22222222")

# Q10 [3, 7, 15, 31]
# def fuple(L):
#     for i, x in enumerate(L):
#         L[i] = sum(L[:i+1])
#     return L
#
#
# print(fuple([3,4,5,6]))

# Q11 10.5
# import random
# total = 0
# ss = 1000000
# for i in range(ss):
#     x = sum([random.randint(1, 6) for _ in range(3)])
#     total += x
#
# print(total/ss)


# Q12
[['the', 'answer', 'is'], ['this', 'and', 'that'], ['and', 'the', 'other']]

def listify(s):
    s1 = s.split('::')
    s2 = [x.split(':') for x in s1]
    return s2

print(listify('the:answer:is::this:and:that::and:the:other'))

# Q13
# import random
#
#
# def f1(x):
#     return 2 * x
#
#
# def f2(x):
#     return x ** 2 + 1
#
#
# def f3(x):
#     return 2 ** x + 1
#
#
# def f4(x):
#     return x ** 3 + 3
#
#
# def ranf(n):
#     if not type(n) == int:
#         return False
#     r = random.randint(0, 3)
#     random_function = [f1, f2, f3, f4][r]
#     return random_function(n)
#
#
# RANDOM = random.randint(1, 1000)
#
# def print_x(n):
#     f1s = [f1(i) for i in range(1, n)]
#     f2s = [f2(i) for i in range(1, n)]
#     f3s = [f3(i) for i in range(1, n)]
#     f4s = [f4(i) for i in range(1, n)]
#     print(f1s)
#     print(f2s)
#     print(f3s)
#     print(f4s)
# print(print_x(10))
# print(f3(9))

# Q14
# def xyx( s ):
#     return len(s) < 2 or ( s[0] == s[-1] and xyx( s[1: -1] ) )
#
# def xyx_key(n):
#     s = str(n)
#     l = len(s)
#     if xyx(s) and l%2==0:
#         return s[:int(l/2)]
#     return False
#
# print(xyx_key(12357911975321))


#Q15
# def encode(n):
#     L1 = [ ord('9')-ord(c) for c in str(n)]
#     L2 = [str(x) for x in L1]
#     return int(''.join(L2) )
#
# print(encode('88324576987143'))
# print(ord('9'))

#Q16
# def geekify(n):
#     i=1
#     S=set()
#     while True:
#         i += 1
#         S.add(i)
#         for j in range(2, i//2):
#             if i%j == 0:
#                 S = S - {i}
#         if len(S) >= n:
#             break
#     return sum(S)
#
# print(geekify(1000))

# Q17
# import pandas
#
# WC_DF = pandas.read_csv("worldcities.csv")
#
# population_dict = {}
# for i, row in WC_DF.iterrows():
#     population_dict[ row['city'] ] = row['population']
#
#
# print(population_dict)

# Q18
# def foo(L):
#     d = {}
#     for e in L:
#         if e in d:
#             d[e] += 1
#         else:
#             d[e] = 1
#     return {x for x in d if d[x]> 1}
#
#
# print(foo([1,3, 4, 3,5,6,4,1,'a', 'a']))


# import random
#
# def fxxx(s):
#     out = ""
#     r = 5#random.randint(1, len(s))
#     for n in range( r ):
#         out += s[random.randint(0,r-1)]
#     return out
#
#
# print(fxxx('Hello'))


# mc = [77, 101, 114, 114, 121, 32, 67, 104,
#       114, 105, 115, 116, 109, 97, 115, 33]
#
# print("".join([chr(c) for c in mc]) )