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
    if (s.islower() or s.istitle() or s.isupper()) and s.lower() in ENGLISH_WORDS:
        return True
    else:
        return False


# spell checking function
def spell_check_file(filename):
    with open(filename) as f:
        lines = f.readlines()

    special_char = ',;!?_()"*[]{}&#'
    common_words = ['the', 'be', 'of', 'and', 'a', 'to', 'in', 'he', 'have', 'had', 'it', 'that', 'for', 'they', 'I',
                    'with',
                    'as', 'not', 'on', 'she', 'at', 'by', 'this', 'we', 'you', 'do', 'but', 'from', 'or', 'which',
                    'one', 'would', 'all', 'will', 'there', 'say', 'who', 'make', 'when', 'can', 'more', 'if', 'no',
                    'man', 'out', 'other', 'so', 'what', 'time', 'up', 'go', 'about', 'than', 'into', 'could', 'only',
                    'new', 'year', 'some', 'take', 'come', 'these', 'know', 'see', 'use', 'get', 'like', 'then', 'is',
                    'give', 'gave', 'title', 'may', 'copy', 'my', 'me', 'us', 'were', 'was', 'day', 'did', 'its',
                    'went']
    list_of_lines = []
    for i in range(len(lines)):
        line = lines[i]
        # step1, remove the special char in the text
        for char in special_char:
            line = line.strip().replace(char, ' ').replace('--', ' ').replace("=>", ' ').replace('...', ' ')
        list_line = (' '.join(line.split())).split(' ')
        # print('---', list_line)

        # step2, remove the special char in the word
        for j in range(len(list_line)):
            if len(list_line[j]) > 0 and (list_line[j][-1] == '.' or list_line[j][-1] == ':'):
                list_line[j] = list_line[j][:-1]
        # print('===', list_line)

        # step3, remove the common words and digit base on the common words list
        for k in range(len(common_words)):
            w = common_words[k]
            list_line = [ls for ls in list_line if w != ls and w.upper() != ls and w.title() != ls and not ls.isdigit()]
        print('***', list_line)

        error_words = []
        for lw in list_line:
            if len(lw) > 1 and not is_english_word(lw):
                error_words.append(lw)

            if len(lw) > 1 and is_english_word(lw):
                common_words.append(lw)

        # error_words = [lw for lw in list_line if len(lw) > 1 and not is_english_word(lw)]
        if len(error_words) > 0:
            print(i, ':', error_words)

        # list_of_lines.append(list_line)

    # step2, remove the common words and digit base on the common words list
    # for i in range(len(list_of_lines)):
    #     line = list_of_lines[i]
    #     for j in range(len(common_words)):
    #         w = common_words[j]
    #         line = [l for l in line if w != l and w.upper() != l and w.title() != l and not l.isdigit()]
    #     list_of_lines[i] = line
    #     print(line)

    # dict = {}
    # for key in words:
    #     dict[key] = dict.get(key, 0) + 1
    # dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    # print (dict)


# spell_check_file("Dracula.txt")
spell_check_file("spelling.txt")
