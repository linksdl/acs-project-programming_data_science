# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Project : acs-project-programming_data_science      
@File    : demo.py
@Author  : Billy Sheng 
@Contact : shengdl999links@gmail.com  
@Date    : 2020/12/9 11:35 上午
@Version  : 1.0.0
@License : Apache License 2.0
@Desc    : None
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.core.display import display

df = pd.read_csv('./bread_basket_1.csv')


import datetime

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori

# 设置数据集
records = [['牛奶', '洋葱', '肉豆蔻', '芸豆', '鸡蛋', '酸奶'],
           ['莳萝', '洋葱', '肉豆蔻', '芸豆', '鸡蛋', '酸奶'],
           ['牛奶', '苹果', '芸豆', '鸡蛋'],
           ['牛奶', '独角兽', '玉米', '芸豆', '酸奶'],
           ['玉米', '洋葱', '洋葱', '芸豆', '冰淇淋', '鸡蛋']]

te = TransactionEncoder()
# 进行 one-hot 编码
te_ary = te.fit(records).transform(records)
df = pd.DataFrame(te_ary, columns=te.columns_)
# 利用 Apriori 找出频繁项集
freq = apriori(df, min_support=0.5, use_colnames=True)

display(freq)

from mlxtend.frequent_patterns import association_rules, apriori
from mlxtend.preprocessing import TransactionEncoder

trans_items = []
for i in range(1, df['Transaction'].nunique() + 1):
    temp = df[df['Transaction'] == i]
    items = list(temp['Item'])
    if (len(items) > 0):
        trans_items.append(items)

te = TransactionEncoder()
# 进行 one-hot 编码
te_ary = te.fit(trans_items).transform(trans_items)
df = pd.DataFrame(te_ary, columns=te.columns_)
# 利用 Apriori 找出频繁项集
frequent_items = apriori(df, min_support=0.01, use_colnames=True)
display(frequent_items)

# now making the rules from frequent itemset generated above
rules = association_rules(frequent_items, metric="lift", min_threshold=1)
rules.sort_values('confidence', ascending=False, inplace=True)

# arranging the data from highest to lowest with respect to 'confidence'
rules.sort_values('confidence', ascending=False)
