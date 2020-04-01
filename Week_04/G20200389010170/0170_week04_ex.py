import pandas as pd

# data = pd.read_csv("book_utf8.csv")
# data.columns = ['star', 'vote', 'abstract']
# data = pd.DataFrame(data)

print(data)
print(data[:10])
print(data['id'])
print(data["id"].count())

print(data[data['id'] < "1000"][data['age'] > 30])

print(data.groupby("id").agg({'orderId': 'count'}))

print(pd.merge(pd.DataFrame(t1), pd.DataFrame(t2), on='id', how='inner'))

print(pd.merge(pd.DataFrame(t1), pd.DataFrame(t2), how='outer'))

print(t1.drop(t1[t1['id']==10].index))

t1.columns = [''] * len(t1.columns)