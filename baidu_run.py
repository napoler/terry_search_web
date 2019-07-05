import src
import Terry_toolkit as tkit
import time
import random
import csv
import os
import hashlib
# TEXT_PATH ="./data/corpu/"
TEXT_PATH ="./data/article/"
ARTICLE_PATH ="./data/article/"
KEYWORD_FILE ="./keywords.csv"
PAGE_NUM =10 #最大搜索翻页次数
def bsearch():
    bsearch = src.BaiduSearch()
    # csvFile = open(KEYWORD_FILE, "r")
    # reader = csv.reader(csvFile)
    # rows = []
    with open(KEYWORD_FILE,'r') as csvfile:
        reader = csv.reader(csvfile)
        rows= [row for row in reader]
        # print (rows)#输出所有数据
        #数组进行打乱
        random.shuffle(rows)
        print (rows)#输出所有数据
        for item in rows:
            # keyword = item[0]+' site:sina.com.cn'
            keyword = item[0]+''
            print('搜索关键词:',keyword)

            # keyword="柯基犬 site:zhihu.com"
            lis,kws = bsearch.search(keyword=keyword,num = PAGE_NUM)
            print(lis)
            #存储获取的关键词
            with open(KEYWORD_FILE,'r') as csvfile:
                reader = csv.reader(csvfile)
                old_rows= [row for row in reader]
                kws=[[i for i in ii.split(',')] for ii in kws]
                reList = kws+ old_rows
                reList = list(set([tuple(t) for t in reList]))
                new_rows = [list(v) for v in reList]
                # reList
                print('new_rows')
                print(new_rows)

            #写入新的关键词
            with open(KEYWORD_FILE,'w',newline='') as t:#numline是来控制空的行数的
                writer=csv.writer(t)#这一步是创建一个csv的写入器（个人理解）
                # writer.writerow(b)#写入标签
                writer.writerows(new_rows)#写入样本数据


            ut = src.UrlText()
            ttext= tkit.Text()
            t = time.time()
            file_name= TEXT_PATH+'corpu'+str(t)+".txt"
            n = 0
            print("搜索到的链接数目"+str(len(lis)))
            for item in lis:
                print("开始处理 "+str(n))
                t = time.time()





                if n % 10 == 0:
                    # file_name= PATH+'corpu'+str(hash(item['url']))+".txt"
                    file_name= TEXT_PATH+'corpu'+str(t)+".txt"

                # 这是整合五篇文章
                # my_open = open(file_name, 'a')

                print(item)
                # print(item['url'])
                #获取正文
                text = ut.get_text(item['url'])


                # print(text)
                sentence = ttext.sentence_segmentation_v1(text) #分句
                sentence = tkit.List().remove_empty(sentence) #删除多余空元素
                print(len(sentence))
                if len(sentence)>5:
                    print("优质内容 准备存储...")
                    text = "\n".join(sentence)
                    #保存单篇文章
                    save_article(str(text))



                    # while '' in n:
                    #     n.remove('')
                    # # whe
                    # print(n)
                    # print("\n".join(n))

                    # 这是整合五篇文章
                    # my_open.write(str(text)+'\n\n')
                    # my_open.close()
                else:
                    print("内容过短 准备丢弃...")
                n = n+1
                print("**"*50)
    # time.sleep(10)
def save_article(text):
    # 存储单篇文章
    # ARTICLE_PATH
    md5_val = hashlib.md5(text.encode('utf8')).hexdigest()
    articlefile= 'article_'+str(md5_val)+'.txt'
    if os.path.isfile(ARTICLE_PATH+articlefile):
        print("文件已经存在跳过")
    else:
        my_open = open(ARTICLE_PATH+articlefile, 'a')
        my_open.write(str(text)+'\n\n')
        my_open.close()
if __name__=='__main__':
    bsearch()
