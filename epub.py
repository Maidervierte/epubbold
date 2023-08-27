import os
import ebooklib
import re
from ebooklib import epub
from html.parser import HTMLParser
from bs4 import BeautifulSoup

epub_list=[]
for file in os.listdir("./input"):
    if file.endswith(".epub"):
        epub_list.append(file)

def modify_word(word):
    new_word=""
    if len(word)<7:
        new_word="<b>"+word[:len(word)//2]+"</b>"+word[len(word)//2:]
    else:
        new_word="<b>"+word[:len(word)//2+1]+"</b>"+word[len(word)//2+1:]
    return new_word

def bold_text(node):
    new_node=""
    matches=re.split(r"([a-zA-ZäüöÄÜÖß-]+’?[a-zA-ZäüöÄÜÖß-]+|[a-zA-ZäüöÄÜÖ-])",node)
    for match in matches:
        if re.match(r"([a-zA-ZäüöÄÜÖß-]+’?[a-zA-ZäüöÄÜÖß-]+|[a-zA-ZäüöÄÜÖ-])",match):
            new_node+=modify_word(match)
        else:
            new_node+=match
    # print("#######################")
    # print(node)
    # print(new_node)
    return new_node

for file in epub_list:
    print(str(file))
    new_dir="./output/"+file.split(".epub")[0]
    book = epub.read_epub("./input/"+file)
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            content=item.get_content()
            content=content.decode()
            soup = BeautifulSoup(content, 'html.parser')
            for node in soup.find_all(string=lambda x: x.strip()):
                if "xml" in node or "html" in node or "folio=" in node:
                    continue
                new_text=bold_text(node)
                node.replace_with(BeautifulSoup(new_text,'html.parser'))
            if not os.path.exists(new_dir):
                os.makedirs(new_dir)
            with open(new_dir+"/"+item.get_name().split("/")[-1], "w+", encoding='utf-8') as file:
                file.write(str(soup))