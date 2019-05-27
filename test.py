# 导入 webdriver
from selenium import webdriver

# 要想调用键盘按键操作需要引入keys包
from selenium.webdriver.common.keys import Keys

# 创建chrome启动选项
chrome_options = webdriver.ChromeOptions()

# 指定chrome启动类型为headless 并且禁用gpu
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# 调用环境变量指定的chrome浏览器创建浏览器对象
driver = webdriver.Chrome(chrome_options=chrome_options,executable_path='./tools/chromedriver')

# 如果没有在环境变量指定Chrome位置
# driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='/home/wx/application/chromedriver')

# get方法会一直等到页面被完全加载，然后才会继续程序，通常测试会在这里选择 time.sleep(2)
driver.get("http://www.baidu.com/")

# 获取页面名为 wrapper的id标签的文本内容
data = driver.find_element_by_id("wrapper").text

# 打印数据内容
print (data)