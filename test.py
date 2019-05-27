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
#设置chromedriver路径
CHROMEDRIVER="./tools/chromedriver"
def search(keyword,num = 10):
    s_data = search_first(keyword)
    data = s_data['data']
    next_url = s_data['next_url']
    n = 0 
    while  n < num:
        print(num)
        if len(next_url) >5:
            s_data = search_next(keyword,s_data['next_url'])
            data = data + s_data['data']
            next_url = s_data['next_url']
        n = n+1
    return data
    

def search_first(keyword):
    # 创建chrome启动选项
    chrome_options = webdriver.ChromeOptions()

    # 指定chrome启动类型为headless 并且禁用gpu
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
    driver.get("http://www.baidu.com")

    #进行页面截屏
    # driver.save_screenshot("./baidu.png")

    #元素定位的方法
    # driver.find_element_by_id("kw").send_keys("python")
    # # driver.find_element_by_id("su").click()

    # elem.send_keys(Keys.RETURN)
    # driver 获取html字符串
    # print(driver.page_source) #浏览器中elements的内容
    elem=driver.find_element_by_id('kw')
    elem.send_keys(keyword)
    elem.send_keys(Keys.RETURN)
    print(driver.current_url)
    elem.send_keys(Keys.RETURN)
    #找到“百度一下”
    baidu_click=driver.find_element_by_id('su')
    #点击“百度一下”
    baidu_click.click()
    try:
        #最多等待10秒直到浏览器标题栏中出现我希望的字样（比如查询关键字出现在浏览器的title中）
        WebDriverWait(driver, 10).until(
            expected_conditions.title_contains(keyword))
        # print(driver.title)
        bsobj = BeautifulSoup(driver.page_source)
    
        num_text_element = bsobj.find('span', {'class': 'nums_text'})
        print(num_text_element.text)
        nums = filter(lambda s: s == ',' or s.isdigit(), num_text_element.text)
        # print(''.join(nums))
        #下一页链接
        next_url = bsobj.find('a', {'class': 'n'})
        elements = bsobj.findAll('div', {'class': re.compile('c-container')})
        data =[]
        for element in elements:
            item= {
                'title':element.h3.a.text,
                'url':element.h3.a['href']

            }
            # print('标题：', element.h3.a.text)
            # print('链接：', element.h3.a['href'])
            # print(
            #     '===============================================================')
            data.append(item)
        
        full = {'data':data,
                'next_url':'http://www.baidu.com'+next_url['href']
                }
    
    finally:
        #关闭浏览器
        driver.close()
    # full= driver(driver)

    return full
def search_next(keyword,url):
    # 创建chrome启动选项
    chrome_options = webdriver.ChromeOptions()

    # 指定chrome启动类型为headless 并且禁用gpu
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    # 调用环境变量指定的chrome浏览器创建浏览器对象
    driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=CHROMEDRIVER)

    #发送请求
    driver.get(url)

    try:
        #最多等待10秒直到浏览器标题栏中出现我希望的字样（比如查询关键字出现在浏览器的title中）
        WebDriverWait(driver, 10).until(
            expected_conditions.title_contains(keyword))
        # print(driver.title)
        bsobj = BeautifulSoup(driver.page_source)
    
        num_text_element = bsobj.find('span', {'class': 'nums_text'})
        print(num_text_element.text)
        nums = filter(lambda s: s == ',' or s.isdigit(), num_text_element.text)
        # print(''.join(nums))
        #下一页链接
        next_url = bsobj.find('a', {'class': 'n'})
        elements = bsobj.findAll('div', {'class': re.compile('c-container')})
        data =[]
        for element in elements:
            item= {
                'title':element.h3.a.text,
                'url':element.h3.a['href']

            }
            # print('标题：', element.h3.a.text)
            # print('链接：', element.h3.a['href'])
            # print(
            #     '===============================================================')
            data.append(item)
        
        full = {'data':data,
                'next_url':'http://www.baidu.com'+next_url['href']
                }
    
    finally:
        #关闭浏览器
        driver.close()
    # full= driver(driver)

    return full



# def search_item(driver):
#     try:
#         #最多等待10秒直到浏览器标题栏中出现我希望的字样（比如查询关键字出现在浏览器的title中）
#         WebDriverWait(driver, 10).until(
#             expected_conditions.title_contains(keyword))
#         # print(driver.title)
#         bsobj = BeautifulSoup(driver.page_source)
    
#         num_text_element = bsobj.find('span', {'class': 'nums_text'})
#         print(num_text_element.text)
#         nums = filter(lambda s: s == ',' or s.isdigit(), num_text_element.text)
#         # print(''.join(nums))
    
#         elements = bsobj.findAll('div', {'class': re.compile('c-container')})
#         data =[]
#         for element in elements:
#             item= {
#                 'title':element.h3.a.text,
#                 'url':element.h3.a['href']

#             }
#             # print('标题：', element.h3.a.text)
#             # print('链接：', element.h3.a['href'])
#             # print(
#             #     '===============================================================')
#             data.append(item)
#         full = data
    
#     finally:
#         #关闭浏览器
#         driver.close()
    

#     return full
    
 
    #driver获取cookie
    # cookies = driver.get_cookies()
    # print(cookies)
    # print("*"*100)
    # cookies = {i["name"]:i["value"] for i in cookies}
    # print(cookies)
    # print(driver.page_source) #浏览器中elements的内容

    # driver.save_screenshot("./baidu1.png")
    # #退出浏览器
    # time.sleep(3)
    # driver.quit()
d = search(keyword="柯基犬",num=2)


print(d)