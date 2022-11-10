#!/bin/python3
# Usage: 
# dvc metrics show | ./pivot-metrics.py

import sys
import pandas as pd


df = pd.read_table(sys.stdin, delim_whitespace=True)

df.columns = df.columns.str.strip()
df['Path'] = df['Path'].str.replace('reports/', '', regex=True)
s = df['Path'].str.split('-', n=2, expand=True)
df['algo'] = s[0]
df['lang'] = s[1]
df['test_set'] = s[2].str.replace('.json', '', regex=True).str.strip()
df.drop(columns='Path', inplace=True)
df.rename(columns={'Documents_evaluated': 'documents'}, inplace=True)

pivoted = df.pivot(
    index=['test_set', 'lang', 'documents'],
    columns=['algo'],
    values='F1@5'
    ).swaplevel(0,1).sort_values('lang')

print(pivoted.to_csv(sep='\t'))
