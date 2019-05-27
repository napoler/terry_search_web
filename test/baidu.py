import os
os.chdir("../")   #修改当前工作目录

import src
bsearch = src.BaiduSearch()
keyword="柯基犬"
lis = bsearch.search(keyword=keyword,num = 10)
print(lis)