from snownlp import SnowNLP
import pprint
text = f'contents.text'

s = SnowNLP(text)

pprint(s.words)

