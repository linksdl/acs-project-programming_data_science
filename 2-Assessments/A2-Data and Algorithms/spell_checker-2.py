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


# Q3 answer code cell
# Modify this function definition to fulfill the given requirements.
# Maximum code length: 50 lines

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


def count_words(words):
    dicts = {}
    for key in words:
        dicts[key] = dicts.get(key, 0) + 1
    dicts = sorted(dicts.items(), key=lambda x: x[1], reverse=True)
    return dicts


# Get the common words of top n in text.
def get_top_word(dicts, n=1):
    common_words = [k for k, v in dicts if v >= n and k != '' and not k.isdigit()]
    return common_words


# compute reliability of every word
def compute_word_reliability(n, word_count):
    # 1. If the word is in english_words, then the reliability is 100
    # 2. If the number of word occur in text more than 1 and less than 4, the reliability range in [10, 30]
    # 3. if the number of word occur in text more than 4 and less than 19, the reliability range in [50, 100)
    # 4. if the number of word occur in text more than 20, the reliability is 100.
    word_reliability = {}
    for k, v in word_count.items():
        if k != '' and is_english_word(k):
            w = {k: 100}
        elif v >= 16:
            w = {k: 90 + (v - 15) * 1}
        elif n <= v < 16:
            w = {k: 50 + (v - n) * 3}
        else:
            w = {k: v * 10}
        word_reliability.update(w)

    return word_reliability


# spell checking function
def spell_check_file(filename):
    # Open the source text
    with open(filename) as f:
        lines = f.readlines()

    special_char = ',;!?_()"*[]{}&#'
    words_count = {}
    list_lines = []
    number_for_reliable = 3
    score_for_reliable = 55
    for i in range(len(lines)):
        line = lines[i]
        # step1, remove the special char in the text
        for char in special_char:
            line = line.strip().replace(char, ' ').replace('--', ' ') \
                .replace("=>", ' ').replace('...', ' ').replace(".'", ' ')
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
        for k, v in count_words(list_line):
            temp = {k: words_count.get(k) + v} if k in words_count else {k: v}
            words_count.update(temp)

        list_lines.append(list_line)

    # compute the every word reliability.
    words_reliability = compute_word_reliability(number_for_reliable, words_count)
    ''.endswith()
    for j in range(len(list_lines)):
        list_line = list_lines[j]
        init_common_words = ['the', 'be', 'of', 'and', 'a', 'to', 'in', 'he', 'have', 'had']
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
                elif "www." in lw or "http:" in lw:
                    continue
                elif words_reliability.get(lw) < score_for_reliable:
                    d = {lw: words_reliability.get(lw)}
                    error_words.append(d)

                else:
                    init_common_words.append(lw)  # if the word is english word, then add to the common words list

        if len(error_words) > 0:
            print(j, ':', error_words)


spell_check_file("Dracula.txt")
# spell_check_file("spelling.txt")
