import src
import Terry_toolkit as tkit
import time

import csv


TEXT_PATH ="./data/corpu/"
KEYWORD_FILE ="./keywords.csv"
PAGE_NUM =10 #最大搜索翻页次数
def bsearch():
    bsearch = src.BaiduSearch()
    # csvFile = open(KEYWORD_FILE, "r")
    # reader = csv.reader(csvFile)
    # rows = []
    with open(KEYWORD_FILE,'r') as csvfile:
        reader = csv.reader(csvfile)
        # rows= [row for row in reader]
        # print (rows)#输出所有数据
        for item in reader:
            print(item[0])
            keyword = item[0]

            # keyword="柯基犬 site:zhihu.com"
            lis = bsearch.search(keyword=keyword,num = PAGE_NUM)
            # print(lis)

            ut = src.UrlText()
            ttext= tkit.Text()
            t = time.time()
            file_name= TEXT_PATH+'corpu'+str(t)+".txt"
            n = 0
            for item in lis:
                t = time.time()



                if n % 10 == 0:
                    # file_name= PATH+'corpu'+str(hash(item['url']))+".txt"
                    file_name= TEXT_PATH+'corpu'+str(t)+".txt"

                my_open = open(file_name, 'a')

                # print(item)
                # print(item['url'])
                #获取正文
                text = ut.get_text(item['url'])
                # print(text)
                sentence = ttext.sentence_segmentation_v1(text) #分句
                sentence = tkit.List().remove_empty(sentence) #删除多余空元素
                if len(sentence)>5:
                    # while '' in n:
                    #     n.remove('')
                    # # whe
                    # print(n)
                    # print("\n".join(n))
                    text = "\n".join(sentence)

                    my_open.write(str(text)+'\n\n')
                    my_open.close()
                n = n+1
    # time.sleep(10)
if __name__=='__main__':
    bsearch()
