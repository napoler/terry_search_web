# 导入 webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
# 要想调用键盘按键操作需要引入keys包
from selenium.webdriver.common.keys import Keys
import time
import re
import random
from bs4 import BeautifulSoup
from .config import CHROMEDRIVER,DEBUG
import logging

from cacheout import Cache
cache = Cache()
import sqlite3

DB='xigua.db'
class XiGua:
    def int_db(self):
        conn = sqlite3.connect(DB)
        c = conn.cursor()
        # Create table
        #创建链接表
        c.execute('''CREATE TABLE `xg_links` ( `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, `url` TEXT NOT NULL UNIQUE, `title` TEXT NOT NULL, `num` NUMERIC, `comment` NUMERIC )''')

        pass

    def gethtml(self,url):
        key = 'gethtml_'+url
        if cache.get(key) is None:
            items=[]
            # 创建chrome启动选项
            chrome_options = webdriver.ChromeOptions()

            # 指定chrome启动类型为headless 并且禁用gpu
            if DEBUG:
                print("开启了调试打开浏览器窗口")
            else:
                chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')

            # 调用环境变量指定的chrome浏览器创建浏览器对象
            driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=CHROMEDRIVER)

            # 如果没有在环境变量指定Chrome位置
            # driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='/home/wx/application/chromedriver')
            # keyword ="阿拉斯加雪撬犬 site:163.com"
            # get方法会一直等到页面被完全加载，然后才会继续程序，通常测试会在这里选择 time.sleep(2)
            # driver.get("https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd="+keyword)
            # input_element = driver.find_element_by_name("wd")
            # input_element.send_keys(keyword)
            # input_element.submit()
            # input_element.send_keys(Keys.ENTER)
            # click_btn = driver.find_element_by_id("su")
            # click_btn.click()

            #发送请求
            driver.get(url)
            # WebDriverWait(driver, 10).until(
            #     expected_conditions.title_contains(keyword))
            print(driver.title)
            bsobj = BeautifulSoup(driver.page_source,features="lxml")
            elements = bsobj.findAll('div', {'class': re.compile('card-cont__title')})
            data =[]
            for element in elements:
                # print(element.findAll('span', {'class': re.compile('text-icon__txt')})[0].text)
                num=self.claer_num(element.findAll('span', {'class': re.compile('text-icon__txt')})[0].text)
                comment=self.claer_num(element.findAll('span', {'class': re.compile('text-icon__txt')})[1].text)
                item={
                    'url':element.a['href'],
                    'title':element.a.text,
                    'num':num,
                    'comment':comment,
                }
                print(item)
                self.add_link(item)
                # item= {
                #     'title':element.h3.a.text,
                #     'url':element.h3.a['href']

                items.append(item)
            
            # self.add_links(items) 
            pass
        else:
            pass
    def claer_num(self,num):
        t='万'
        if t in num:
            n=num.replace('万','')
            n=float(n)
            new=n*10000
            new=int(new)
            # print(new)
        else:
            # reurn float(num)
            new=int(num)
            pass
        return new
    def add_links(self,items):
        sql="INSERT INTO xg_links VALUES (?,?,?,?,?)"
        conn = sqlite3.connect(DB)
        c = conn.cursor()
        ls=[]
        for i,item in enumerate(items):
            # if video_check(item["id"]["videoId"])!=None:
            #     # 判断是否是已经发布过的
            #     print("跳过已存在")
            #     continue
            
            # time.sleep(15)
            # p= checkup_image(item["id"]["videoId"])
            # video_check(item["id"]["videoId"])

            ls.append((None,item['url'],item['title'],item['num'],item['comment']))
            c.executemany(sql,ls)
            conn.commit()
            ls=[]
            # if i % 10 ==0:
            #     print(ls)
            #     c.executemany(sql,ls)
            #     conn.commit()
            #     ls=[]
        conn.close()
    def add_link(self,item):
        if self.url_check(item['url']):
            print("这里执行更新")

            pass
        else:
            self.add_links([item])
            print("添加新数据")
    def random_links(self):
        conn = sqlite3.connect(DB)
        c = conn.cursor()
        sql="SELECT * FROM xg_links ORDER BY RANDOM() limit 1000"
        c.execute(sql)
        all = c.fetchall()
        # print(one)

        conn.close()
        return all
    def url_check(self,url):
        conn = sqlite3.connect(DB)
        c = conn.cursor()
        sql= "select * from xg_links where xg_links.url='"+url+"'"
        # print(sql)
        # conn.commit()
        c.execute(sql)
        one= c.fetchone()
        # print(one)
        conn.close()
        return one
    def update_link(self,item):
        conn = sqlite3.connect(DB)
        c = conn.cursor()
        sql= 'update xg_links set num="'+item['num']+'",comment="'+item['comment']+'" where xg_links.url="'+item['url']+'"'  
        c.execute(sql)
        print("已经更新",item)

# def video_update(vid,ty):
#     conn = sqlite3.connect(DB)
#     c = conn.cursor()
#     sql= 'update video set verify="yes",quality="'+ty+'" where video.vid="'+vid+'"'
#     # update video set verify="yes",quality="good" where video.vid="iXLFTkjTCs8"
#     print(sql)
#     c.execute(sql)


#     sql= "select * from video where video.vid='"+vid+"'"
#     print(sql)
#     # conn.commit()
#     c.execute(sql)
#     all = c.fetchone()
#     print(all)
#     conn.close()
#     # with conn:
#     #     update_task(conn, (2, '2015-01-04', '2015-01-06',2))

#     return all