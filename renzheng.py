# %%
# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 目标URL
url = "https://sslvpn.xjtu.edu.cn/"
# 用户名和密码
usr = '3123108013'
pwd = '20010628.jyh'

# 实例化 Microsoft Edge 浏览器的选项对象 
option = webdriver.EdgeOptions() 
# 设置一个自定义的 User-Agent 字符串
option.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188"')
driver = webdriver.Edge(options=option)
driver.maximize_window()  # 最大化窗口
# 访问网址
driver.get(url)

# %%
time.sleep(1.4)
form_user = driver.find_element(By.CSS_SELECTOR, "#form1 > input.username")
form_user.clear()
form_user.send_keys(usr)
form_pwd = driver.find_element(By.CSS_SELECTOR, "#form1 > input.pwd")
form_pwd.clear()
form_pwd.send_keys(pwd)

# 确认按钮
btn = driver.find_element(By.CSS_SELECTOR, '#account_login')
btn.click() 

time.sleep(15)
driver.quit()
# %%



