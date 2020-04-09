from os import path
from snownlp import SnowNLP

dir = path.dirname(__file__)
text = open(path.join(dir, 'comment.txt'), encoding='utf-8').read()
s = SnowNLP(text)
s2 = SnowNLP(text)
print(s2.sentiments)
