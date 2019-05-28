import os
os.chdir("../")   #修改当前工作目录
import Terry_toolkit as tkit
import src
ut = src.UrlText()
url= "https://www.zhihu.com/question/34562079"
# html = ut.url_html(url)
# print(html)

#获取正文
text = ut.get_text(url)
print(text)
ttext= tkit.Text()
n = ttext.sentence_segmentation_v1(text)
n = tkit.List().remove_empty(n) #删除多余空元素
# while '' in n:
#     n.remove('')
# # whe
print(n)
print("\n".join(n))