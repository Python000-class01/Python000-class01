import pandas as pd

df = pd.read_csv('./sina/comment_last.txt', encoding='utf-8',sep=',')
df.drop_duplicates(subset='mid', inplace=True, keep='last')
print(df)
df.to_csv('cleanfile.csv', encoding='utf-8',index=0)
