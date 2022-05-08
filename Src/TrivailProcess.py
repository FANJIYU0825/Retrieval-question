#Tell the people how to get the Trivail 
import json
import os
#建立corpus資料夾
if not os.path.isdir("corpus"):
    os.mkdir("corpus")
content_use=[]   
with open('NLP_LAB_Homework.json',) as jfile:
    ITContent = json.load(jfile)
    content=ITContent['內文']
    content_use.append(content)
contents = content_use[0] 
json_corpus=[]

for i in contents.items():
    json_corpus.append({"id":int(i[0]),"contents":i[1]})
with open('./corpus/format_for_pyserini.json', 'w', encoding='utf-8') as f:
    json.dump(json_corpus, f, ensure_ascii=False, indent=4)
    