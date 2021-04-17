import nltk
from urllib import request, response
import re
import random


with open ("mexica.txt", "r") as ff:
    story = ff.read()
print(story)

list_of_words = nltk.word_tokenize(story)

tagged_words = nltk.pos_tag(list_of_words)

list_adj = [x for x, i in tagged_words if i == "JJ"]
metaphor_dict = {}
for i in list_adj:
    url = "http://bonnat.ucd.ie/jigsaw/index.jsp?q=" + i
    with request.urlopen(url) as response:
        page_source = response.read()
    x = {i: [y for y in re.findall('longvehicle=(.*?)">', str(page_source))]}
    metaphor_dict.update(x)

connectors = ['like', 'as']
list_of_words_2 = nltk.word_tokenize(story)
for i, j in enumerate(list_of_words):
    if j in list_adj:
        if len(metaphor_dict.get(j)) == 0:
            continue
        else:
            y = str(random.choice(connectors) + " " + random.choice(metaphor_dict[str(j)]))
            for z, k in enumerate(list_of_words_2):
                if k == j:
                    list_of_words_2.insert(z+1, y)
                    break
    else:
        continue

print(' '.join(list_of_words_2))

