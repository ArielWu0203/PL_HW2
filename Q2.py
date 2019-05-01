import urllib.request
import re
from collections import Counter
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
pattern = 'authors">[\s\S]*?</p>'
result = re.findall(pattern,html_str)
tmp_str = ""
tmp_list = list()
index = 0

for r in result:
    author_str = r
    author_pattern = 'a href=[\s\S]*?</a>'
    author_result = re.findall(author_pattern,author_str)
    for author_r in author_result:
        title = author_r.split("a href=")[1].split("\">")[1].split("</a>")[0]
        if index == 0:
            index+=1
        else:
            tmp_str+='?'
        if title[0] == ' ':
            title = title[1:len(title)]
        tmp_str+=title
        

#print(tmp_str)    
tmp_list = tmp_str.split('?')
recounted = Counter(tmp_list)
#print(recounted)

name = list()

for key in recounted:
        name.append(key)
name.sort()
#print(name)

for i in name:
    if i != author_tmp:
        print(i + ': ' + str(recounted[i]) + ' times')
#print(times)
