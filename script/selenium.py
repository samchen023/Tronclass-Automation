from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 配置ChromeDriver
driver = webdriver.Chrome()

# 打开TronClass登录页面
driver.get('https://tronclass.ntou.edu.tw/user/index#/')

# 等待页面加载
time.sleep(2)

# 输入用户名和密码
username_field = driver.find_element(By.ID, 'username')  # 根据实际的元素ID或其他选择器替换
password_field = driver.find_element(By.ID, 'password')  # 根据实际的元素ID或其他选择器替换

username_field.send_keys('你的用户名')  # 输入用户名
password_field.send_keys('你的密码')  # 输入密码

# 提交登录表单
login_button = driver.find_element(By.ID, 'login-button')  # 根据实际页面替换
login_button.click()

# 等待登录完成并跳转到首页
time.sleep(5)

# 现在你可以继续抓取待办事项信息
