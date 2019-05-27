import os
os.chdir("../")   #修改当前工作目录

import src
bsearch = src.BaiduSearch()
keyword="柯基犬 site:zhihu.com"
lis = bsearch.search(keyword=keyword,num = 2)
print(lis)
PATH ="./test/book"
ut = src.UrlText()
for item in lis:
    #获取正文
    text = ut.get_text(item['url'])
    
    # print(text)
    file_name= PATH+'corpu'+str(hash(item['url']))+".txt"
    my_open = open(file_name, 'a')
    # logging.info(text)
    my_open.write(str(text)+'\n\n')
    my_open.close()
        