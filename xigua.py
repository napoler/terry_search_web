import src
import Terry_toolkit as tkit
import time
import random
import csv
import os
import hashlib
def xigua():
    links=['https://www.ixigua.com/i6712943938602271239/']
    getxigua = src.XiGua()
    its= getxigua.random_links()
    # print(a)
    for i,url,title,num,comment in its:
        print(url)
        getxigua.gethtml(url='https://www.ixigua.com'+url)

def init():
    """
    开始初始化
    创建数据库之类的
    """
    getxigua = src.XiGua()
    getxigua.int_db()

if __name__=='__main__':
    for i in range(0,100000):
       xigua()
    # init()