import os
os.chdir("../")   #修改当前工作目录

import src
ut = src.UrlText()
url= "http://www.baidu.com/link?url=RosX1iVIyGGkaNKwndNTiZ2dSOoTT4BLLTxfyhFmzfGihgfws81VaGHrmBLhiHOnQzoYim-o9f16xd20aDTA8_"
# html = ut.url_html(url)
# print(html)

#获取正文
text = ut.get_text(url)
print(text)