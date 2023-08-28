import os
import re
import zipfile as zf
import shutil
from bs4 import BeautifulSoup
def modify_word(word):
    new_word="<b>"+word[:len(word)//2+1]+"</b>"+word[len(word)//2+1:]
    if len(word)<7: new_word="<b>"+word[:len(word)//2]+"</b>"+word[len(word)//2:]
    if len(word)==1: new_word="<b>"+word+"</b>"
    if len(word)==5: new_word="<b>"+word[:3]+"</b>"+word[3:]
    return new_word

def bold_text(node):
    accentedCharacters = "àèìòùÀÈÌÒÙáéíóúýÁÉÍÓÚÝâêîôûÂÊÎÔÛãñõÃÑÕäëïöüÿÄËÏÖÜŸçÇßØøÅåÆæœ"
    new_node=""
    matches=re.split(r"([a-zA-Z"+accentedCharacters+"-]+’?[a-zA-Z"+accentedCharacters+"-]+|[a-zA-Z"+accentedCharacters+"-])",node)
    for match in matches:
        if "<" in match or ">" in match:
            continue
        if re.match(r"([a-zA-Z"+accentedCharacters+"-]+’?[a-zA-Z"+accentedCharacters+"-]+|[a-zA-Z"+accentedCharacters+"-])",match):
            new_node+=modify_word(match)
        else:
            new_node+=match
    # print("#######################")
    # print(node)
    # print(new_node)
    return new_node

def get_textfile_loc(folder_path):
    content_path=""

    for line in open(folder_path+"/META-INF/container.xml",encoding='utf-8'):
        if "full-path" in line:
            x=line.split("\"")
            for y in x:
                if "content.opf" in y:
                    content_path=y
                    break
            break
    content_file=folder_path+"/"+content_path
    cps=content_path.split("/")
    path_add=""
    for x in cps[:-1]:
        path_add+=x+"/"
    for line in open(content_file,encoding='utf-8'):
        if "item" in line and "html" in line:
            x=line.split("href")[1].split("\"")
            for y in x:
                if "html" in y:
                    z=y.split("/")
                    for folder in z[:-1]:
                        path_add+=folder+"/"
                    break
            break
    new_file=""
    for line in open(content_file,encoding='utf-8'):
        if "dc:title" in line:
            x=line.split("dc:title")
            new_line=x[0]+"dc:title"+x[1][:-2]+" (b)"+x[1][-2:]+"dc:title"+x[2]
            new_file+=new_line
        else:
            new_file+=line
    with open(content_file,'w',encoding='utf-8') as blah:
        blah.write(str(new_file))
    return path_add



epub_list=[]
for file in os.listdir("./input"):
    if file.endswith(".epub"):
        epub_list.append(file)

for book in epub_list:
    print("working on: "+str(book)+"...")
    new_dir="./output/"+book.split(".epub")[0]
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
    shutil.unpack_archive(filename="./input/"+book,extract_dir=new_dir,format="zip")
    path_add=get_textfile_loc(new_dir)
    for chapter in os.listdir(new_dir+"/"+path_add):
        if not chapter.endswith("html"):
            continue
        content=open(new_dir+"/"+path_add+chapter,encoding='utf-8')
        soup = BeautifulSoup(content.read(), 'html.parser')
        content.close()
        for node in soup.find_all(string=lambda x: x.strip()):
            if "xml" in node or "html" in node or "folio=" in node:
                continue
            new_text=bold_text(node)
            node.replace_with(BeautifulSoup(new_text,'html.parser'))
        style = soup.new_tag('style')
        soup.head.append(style)
        soup.select_one("style").append("b{font : inherit;font-family : inherit;font-size : inherit;font-style : inherit;font-variant : inherit;font-weight : bold;}")
        with open(new_dir+"/"+path_add+chapter, "w+", encoding='utf-8') as new_file:
            new_file.write(str(soup))
    shutil.make_archive(base_name="./output/"+book.split(".epub")[0]+"(b).epub",root_dir=new_dir,format="zip")
    os.rename("./output/"+book.split(".epub")[0]+"(b).epub.zip", "./output/"+book.split(".epub")[0]+" (b).epub")
    shutil.rmtree(new_dir)
    print("book finished!")

print("Finished!")