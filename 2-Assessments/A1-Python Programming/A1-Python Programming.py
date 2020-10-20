# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Project : acs-project-programming_data_science      
@File    : A1-Python Programming.py
@Author  : Billy Sheng 
@Contact : shengdl999links@gmail.com  
@Date    : 2020/10/19 9:32 下午
@Version  : 1.0.0
@License : Apache License 2.0
@Desc    : None
"""


def anagrams(s1, s2):
    # replace the 'pass' command (which does nothing) with code that
    # computes and returns the requried result for any strings s1 and s2
    s1 = s1.strip()
    s2 = s2.strip()
    if s1 == '' or s1 == None or s2 == '' or s2 == None:
        print('------ 0')
        return False

    elif s1.lower() == s2.lower():
        print('------ 1')
        return False

    elif len(s1) != len(s2):
        print('------ 2')
        return False

    else:
        print('------ 3')
        list1 = sorted(list(s1.lower()))
        list2 = sorted(list(s2.lower()))
        print(list1)
        print(list2)

        return True


# print(anagrams('sidebar', "seabird"))


## Q2(c) answer code cell
## Modify this function definition to fulfill the given requirements
## Expected code length: less than 10 lines.

def is_palindrome(s):
    i = 0
    j = len(s) - 1

    while i <= j:
        if s[i].isalpha() and s[j].isalpha():
            if s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1
        elif not s[i].isalpha():
            i += 1

        elif not s[j].isalpha():
            j -= 1

    return True


print(is_palindrome('Was it a cat I aw'))