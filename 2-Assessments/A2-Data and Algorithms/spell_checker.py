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


# Get the common words of top n in text.
def get_top_word(filename, n=5):
    with open(filename) as f:
        words = f.read().replace('\n', ' ').replace('--', ' ').replace('_', ' ') \
            .replace(';', ' ').replace('*', ' ').replace(',', ' ') \
            .replace('!', ' ').replace('?', ' ').replace('"', ' ').split(' ')

    # print(words)
    dicts = {}
    for key in words:
        dicts[key] = dicts.get(key, 0) + 1
    dicts = sorted(dicts.items(), key=lambda x: x[1], reverse=True)
    # common_words = [k for k, v in dicts if v > n and k != '' and not k.isdigit()]
    return dicts


# compute reliability of every word
def compute_word_reliability(word_dicts):
    # 1. If the word is in english_words, then the reliability is 100
    # 2. If the number of word occur in text more than 2 and less than 4, the reliability range in [10, 30]
    # 3. if the number of word occur in text more than 4 and less than 19, the reliability range in [50, 100)
    # 4. if the number of word occur in text more than 20, the reliability is 100.
    word_reliability = {}
    for k, v in word_dicts:
        w = {}
        if k is is_english_word(k):
            w = {k: 100}
        elif v >= 20:
            w = {k: 100}
        elif 4 <= v < 20:
            w = {k: 50 + (v - 4) * 3}
        else:
            w = {k: v * 10}
        word_reliability.update(w)

    return word_reliability


word_dict = get_top_word("spelling.txt")
print(compute_word_reliability(word_dict))


# spell checking function
def spell_check_file(filename):
    with open(filename) as f:
        lines = f.readlines()

    special_char = ',;!?_()"*[]{}&#'
    # most frequently used English words top 82.
    # init_common_words = ['the', 'be', 'of', 'and', 'a', 'to', 'in', 'he', 'have', 'had',
    #                      'it', 'that', 'for', 'they', 'I', 'with', 'as', 'not', 'on', 'she', 'at',
    #                      'by', 'this', 'we', 'you', 'do', 'but', 'from', 'or', 'which', 'one',
    #                      'would', 'all', 'will', 'there', 'say', 'who', 'make', 'when', 'can', 'more',
    #                      'if', 'no', 'man', 'out', 'other', 'so', 'what', 'time', 'up', 'go',
    #                      'about', 'than', 'into', 'could', 'only', 'new', 'year', 'some', 'take', 'come',
    #                      'these', 'know', 'see', 'use', 'get', 'like', 'then', 'is', 'give', 'gave',
    #                      'title', 'may', 'copy', 'my', 'me', 'us', 'were', 'was', 'day', 'did', 'its', 'went']

    init_common_words = get_top_word(filename, 5)
    # print(init_common_words)
    for i in range(len(lines)):
        line = lines[i]
        # step1, remove the special char in the text
        for char in special_char:
            line = line.strip().replace(char, ' ').replace('--', ' ').replace("=>", ' ').replace('...', ' ').replace(
                ".'", ' ')
        list_line = (' '.join(line.split())).split(' ')
        # print('---', list_line)

        # step2, remove the special char in the word
        for j in range(len(list_line)):
            if len(list_line[j]) > 0 and (
                    list_line[j][-1] == '.' or list_line[j][-1] == ':' or list_line[j][-1] == "'"):
                list_line[j] = list_line[j][:-1]

            if len(list_line[j]) > 0 and (list_line[j][0] == "'"):
                list_line[j] = list_line[j][1:]

        # print('===', list_line)

        # step3, remove the common words and digit base on the common words list
        for k in range(len(init_common_words)):
            w = init_common_words[k]
            list_line = [ls for ls in list_line if w != ls and w.upper() != ls and w.title() != ls and not ls.isdigit()]
        # print('***', list_line)

        error_words = []
        for lw in list_line:
            if len(lw) > 1:
                if "'s" in lw or "'d" in lw or "'t" in lw or "'ll" in lw or "'ve" in lw:
                    init_common_words.append(lw)
                    continue
                elif "-" in lw:
                    init_common_words.append(lw)
                    continue
                elif "www." in lw:
                    continue
                elif not is_english_word(lw):
                    error_words.append(lw)
                else:
                    init_common_words.append(lw)  # if the word is english word, then add to the common words list

        # error_words = [lw for lw in list_line if len(lw) > 1 and not is_english_word(lw)]
        if len(error_words) > 0:
            print(i, ':', error_words)

        # list_of_lines.append(list_line)

    # print(init_common_words)

# spell_check_file("Dracula.txt")
# spell_check_file("spelling.txt")
