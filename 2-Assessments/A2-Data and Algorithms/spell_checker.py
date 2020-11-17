# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Project : acs-project-programming_data_science      
@File    : spell_checker.py
@Author  : Billy Sheng 
@Contact : shengdl999links@gmail.com  
@Date    : 2020/11/17 9:47 上午
@Version  : 1.0.0
@License : Apache License 2.0
@Desc    : None
"""


## Q3 answer code cell
## Modify this function definition to fulfill the given requirements.
## Maximum code length: 50 lines

# Get all English words set.
def get_english_words():
    with open("english_words.txt") as f:
        words = f.readlines()
    words = {word.strip() for
             word in words}
    return words


# all words set
ENGLISH_WORDS = get_english_words()


# Determine if a word is an english word.
def is_english_word(s):
    common_words = ['I']
    if s in common_words:
        return True

    if (s.islower() or s.istitle() or s.isupper()) and s.lower() in ENGLISH_WORDS:
        return True
    else:
        return False

    # print(is_english_word('lve'))


# spell checking function
def spell_check_file(filename):
    # with open(filename) as f:
    #     words = f.read().strip()
    #     words = words.replace('.', '').replace(',', '').replace(';', '').replace('!', '').replace('?', '')
    #     words = words.replace('_', '').replace('--', '').replace('"', '').replace('(', '').replace(')', '').replace('*',
    # print(words)

    with open(filename) as f:
        lines = f.readlines()

    special_char = ',;!?_()"*[]{}&#'
    common_words = ['the', 'be', 'of', 'and', 'a', 'to', 'in', 'he', 'have', 'it', 'that', 'for', 'they', 'I', 'with',
                    'as', 'not', 'on', 'she', 'at', 'by', 'this', 'we', 'you', 'do', 'but', 'from', 'or', 'which',
                    'one', 'would', 'all', 'will', 'there', 'say', 'who', 'make', 'when', 'can', 'more', 'if', 'no',
                    'man', 'out', 'other', 'so', 'what', 'time', 'up', 'go', 'about', 'than', 'into', 'could', 'only',
                    'new', 'year', 'some', 'take', 'come', 'these', 'know', 'see', 'use', 'get', 'like', 'then', 'is']

    # step1, remove the special char in the text
    list_of_lines = []

    for line in lines:
        line = line.strip()
        for char in special_char:
            line = line.replace(char, ' ').replace('--', ' ').replace("=>", ' ').replace('...', ' ')
        line = ' '.join(line.split())
        list_of_lines.append(line.split(' '))

    # step2, remove the common words base on the common words list
    list_of_clear_lines = []
    # for i in range(len(list_of_lines) - 15960):
    line = ['re-use', 'it', 'under', 'the', 'terms', 'of', 'the', 'Project', 'Gutenberg', 'License', 'included']
    print("---", line)

    for j in range(len(common_words)):
        w = common_words[j]
        new_line = [l for l in line if w != l and w.upper() != l and w.title() != l]
        # if w in line:
        #     print('---1', w, w.upper(), w.title())
        #     line.remove(w)
        #     print(line)
        # if w.upper() in line:
        #     print('---2', w, w.upper(), w.title())
        #     line.remove(w.upper())
        # if w.title() in line:
        #     print('---3', w, w.upper(), w.title())
        #     line.remove(w.title())
        line = new_line

    print('===', line)

    # list_of_clear_lines.append(list_of_lines[i])

    print(list_of_clear_lines[:10])
    # dict = {}
    # for key in words:
    #     dict[key] = dict.get(key, 0) + 1
    # dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    # print (dict)


spell_check_file("Dracula.txt")
