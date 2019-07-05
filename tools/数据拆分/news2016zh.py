# from libs import TerrySearch
# import src
import Terry_toolkit as tkit
import time
import random
import csv
import os
from random import choice
import hashlib
import json
from tqdm import tqdm
ARTICLE_PATH ="/home/terry/pan/github/bert/data/text/news2016zh/"
PATH ="/media/terry/65F33762C14D581B/tdata/news2016zh/"
tfile=tkit.File()
ttext=tkit.Text()

def run():
        tfile = tkit.File()
        path =PATH
        to_path = ARTICLE_PATH
        file_list = tfile.all_path(path)
        # print(file_list)

        tfile.mkdir(to_path)
        do_path_one = to_path+str(time.time())+'/'
        tfile.mkdir(do_path_one)
        i = 0 
        for file in file_list:
                # print(file)
                for line in tqdm(open(file)): 
                        json_line=json.loads(line)
                        # print (json_line) 
                        # print (json_line['text']) 
                        

                        if i%5000 ==0:
                                # 创建一层目录
                                if len(os.listdir(do_path_one))<1000:
                                        pass
                                # elif len(os.listdir(do_path_one))==1000:
                                #     do_path_one = path+str(time.time())+'/'
                                else:
                                        do_path_one = path+str(time.time())+'/'
                                        tfile.mkdir(do_path_one)

                                # 创建二层目录
                                do_path= do_path_one+str(time.time())+'/'
                                # do_path= path+str(time.time())
                                tfile.mkdir(do_path)
                        save_article(json_line['content'],do_path)
                        i =i+1

# def creat_path(path):
#         tfile.mkdir(path)
#         do_path_one = path+str(time.time())+'/'
#         tfile.mkdir(do_path_one)


def save_article(text,path):
    # 存储单篇文章
    # ARTICLE_PATH
    #text = 'kngines'
    md5_val = hashlib.md5(text.encode('utf8')).hexdigest()

    articlefile= 'article_'+str(md5_val)+'.txt'
    if os.path.isfile(path+articlefile):
        print("文件已经存在跳过")
    else:
        my_open = open(path+articlefile, 'a')
        my_open.write(str(text)+'\n\n')
        my_open.close()
 
if __name__=='__main__':
        run()