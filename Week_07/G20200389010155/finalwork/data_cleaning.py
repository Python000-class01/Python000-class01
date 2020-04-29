import pandas as pd

with open('./newsscrapy/newscom.txt','r+',encoding='utf-8') as f:
    content=f.read()
    f.seek(0,0)
    text='uid,area,ipadd,usertype,agree,cmttime,content'
    f.write(text+'\n'+content)
df = pd.read_csv('./newsscrapy/newscom.txt', encoding='utf-8',sep=',')
df.drop_duplicates(subset=None, inplace=True, keep='last')
print(df)
csv_file = open('cleanfile.csv', 'a', newline='', encoding='utf-8-sig')
df.to_csv('cleanfile.csv', encoding='utf-8-sig',index=0)

