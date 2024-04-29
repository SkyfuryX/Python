#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from datetime import date, datetime


now = datetime.now()
today = now.strftime('%m%d%Y')

#loads the file into a dataframe
file = pd.read_excel('Example Data.xlsx')
df = file.copy()

#Fixes the blank category and removes \n from column titles
titles = list(df.columns.values)
cat = list(titles[1])
cat[2] = ' '
titles[1] = ''.join(cat)
cat = list(titles[2])
cat[2] = ' '
titles[2] = ''.join(cat)
titles
df.columns = titles

df['Category'][0] = 'No Category'

# determines the Week over week, % change value
change = []
for i in range(df.shape[0]):
    change.append("{:.1%}".format(df[df.columns[2]][i] / df[df.columns[1]][i] - 1))

#adds in %Change column
df['% Change'] = change

#sorts by value of current week
df = df.sort_values(by = df.columns[2], ascending = False)

#creates checkpoint
df_change = df.copy()

#creates new file as a copy
df_change.to_excel('Example_Data' + today + '.xlsx', index = False)

