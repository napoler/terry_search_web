# 导入 webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
# 要想调用键盘按键操作需要引入keys包
from selenium.webdriver.common.keys import Keys
import time
import re
from bs4 import BeautifulSoup
from .config import CHROMEDRIVER
import logging

# import requests
# import requests
from readability import Document
import html2text


class UrlText:

    def get_text(self,url ):
        html = self.url_html(url)
        text= self.html_text(html)
        return text
    def remove_HTML_tag(self,tag, string):
        """
        
        
        """
        string = re.sub(r"<\b(" + tag + r")\b[^>]*>", r"", string)
        return re.sub(r"<\/\b(" + tag + r")\b[^>]*>", r"", string)
    def html_text(self,html):
        # response = requests.get(url)
        # logging.info(response.text)
        # html = request.urlopen(url)

        # logging.info(html)

        doc = Document(html)
        # doc = Document(html)
        # logging.info(doc.title())

        html= doc.summary(True)
        #   logging.info(doc.get_clean_html())
        # t =html2text.html2text(html)
        text_maker = html2text.HTML2Text()
        text_maker.ignore_links = True
        text_maker.bypass_tables = False
        text_maker.ignore_images = True
        text_maker.images_to_alt = True
        # html = function_to_get_some_html()
        text = text_maker.handle(html)
        text=self.remove_HTML_tag('img',text)
        # print(text)
        return text
    def url_html(self,url):
        # 创建chrome启动选项
        chrome_options = webdriver.ChromeOptions()

        # 指定chrome启动类型为headless 并且禁用gpu
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')

        # 调用环境变量指定的chrome浏览器创建浏览器对象
        driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=CHROMEDRIVER)
        # driver.set_timeout(30) # seconds
        #发送请求
        driver.get(url)
        html = ''
        try:
            #最多等待10秒直到浏览器标题栏中出现我希望的字样（比如查询关键字出现在浏览器的title中）
            # WebDriverWait(driver, 10).until(
            #     expected_conditions.title_contains(keyword))
            time.sleep(3)
            # print(driver.title)
            logging.info('加载成功网页: '+driver.title)
            html = driver.page_source #浏览器中elements的内容

        finally:
            #关闭浏览器
            driver.close()


        return html

    # def content
# ut = UrlText()
# url= "http://www.baidu.com/link?url=RosX1iVIyGGkaNKwndNTiZ2dSOoTT4BLLTxfyhFmzfGihgfws81VaGHrmBLhiHOnQzoYim-o9f16xd20aDTA8_"
# html = ut.url_html(url)
# print(html)
