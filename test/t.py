import re
import Terry_toolkit as tkit
def remove_HTML_tag(tag, string):
    string = re.sub(r"<\b(" + tag + r")\b[^>]*>", r"", string)
    return re.sub(r"<\/\b(" + tag + r")\b[^>]*>", r"", string)

text ="""

萌照镇楼。\n

<img data-rawwidth="1393" data-rawheight="1104"
src="https://pic3.zhimg.com/50/63f68657ef2e5c22fef8b982a141cfd0_hd.jpg"
class="origin_image zh-lightbox-thumb" width="1393" data-
original="https://pic3.zhimg.com/63f68657ef2e5c22fef8b982a141cfd0_r.jpg"/>

她的名字是Ollie，现在有十一周大了。虽然才养了两周半，但是已经超级超级爱她啦！

"""


#text = remove_HTML_tag('img',text)
#print(text)


#ttext= tkit.Text()
#nt = ttext.clear(text)
cx= tkit.CxExtractor()
nt= cx.filter_tags(text)
print('犬欧美化',nt)


nt = nt.replace(' ','')

print('犬欧美化',nt)

nt =  re.sub('[\n]+', '\n', 'dfadf   d\n \n\n \nfa  ds ')

print('犬欧美化',nt)
