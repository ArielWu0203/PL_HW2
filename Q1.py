import urllib.request
import re
from collections import Counter
#import matplotlib.pyplot as plt
import pygal

author_tmp = input ("Input Author: ")
author_list = author_tmp.split()
author = ""
index = 0
for i in author_list:
    if index > 0:
        author+="+"
    author+=i
    index+=1
url = "https://arxiv.org/search/?query="+author+"&searchtype=author&abstracts=show&size=200&order=submitted_date"
content = urllib.request.urlopen(url)
html_str = content.read().decode('utf-8')
pattern = 'is-size-7"><span class=[\s\S]*?</p>'
result = re.findall(pattern,html_str)
year_list = list()
year_str = ""

for r in result:
    title = r
    title = r.split("is-size-7\"><span class=\"has-text-black-bis has-text-weight-semibold\">Submitted</span>")[1].split(",")[1].split(";")[0]
    year_str += title+""

year_list = year_str.split()
recounted = Counter(year_list)
#print(recounted)

## x : x axis
## y : y axis
x = list()
y = list()
for key in recounted:
    x.append(key)
x.sort()
#print(x)

for i in x:
    y.append(recounted[i])
#print(y)

hist = pygal.Bar()
hist.title = "Author's papers"
hist.x_labels = x
hist.x_title = "year"
hist.y_title = "the number of papers"
hist.add(author_tmp, y)
hist.render_to_file("Author_"+author+".svg")


