import src
import Terry_toolkit as tkit
import time
import random
import csv
import os
from random import choice
import hashlib

# TEXT_PATH ="./data/corpu/"
# TEXT_PATH ="/home/terry/pan/github/bert/test/book/"
TEXT_PATH ="./data/article/"
ARTICLE_PATH ="./data/article1/"
KEYWORD_FILE ="./keywords.csv"
PAGE_NUM =10 #最大搜索翻页次数
    # file_List('/home/','txt')
def run():
    ts  =tkit.File()
    ls = ts.file_List(TEXT_PATH,'txt')
    for it in ls:
        quchong(it)

'''
文件去重复

'''
def quchong(filepath):

    with open(filepath,'r') as f:			                #打开txt文件
        text = ''
        for line in f.readlines():		                #将txt文件逐行读取
        # rows= [row for row in f.readlines()]
            text =text + line +''
            if line =='\n':
                print(text)
                save_article(text)
                print('分段')
                text= ''

def save_article(text):
    # 存储单篇文章
    # ARTICLE_PATH
    #text = 'kngines'
    md5_val = hashlib.md5(text.encode('utf8')).hexdigest()

    articlefile= 'article_'+str(md5_val)+'.txt'
    if os.path.isfile(ARTICLE_PATH+articlefile):
        print("文件已经存在跳过")
    else:
        my_open = open(ARTICLE_PATH+articlefile, 'a')
        my_open.write(str(text)+'\n\n')
        my_open.close()
def openf(file):
    ts  =tkit.File()
    text = ts.open_file(file)
    return  text
if __name__=='__main__':
    run()
