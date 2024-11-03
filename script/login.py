from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions() 
options.add_experimental_option('excludeSwitches', ['enable-logging'])
    
def login_func():
    driver = webdriver.Chrome()
    driver.get('https://tronclass.ntou.edu.tw/user/index#/')

    time.sleep(3)

    username_field = driver.find_element(By.ID, 'username')  
    password_field = driver.find_element(By.ID, 'password')  

    username_field.send_keys('username')  
    password_field.send_keys('password')

    login_button = driver.find_element(By.CLASS_NAME, 'btn-submit')  
    login_button.click()

    time.sleep(5)
    
    driver.quit()
   
if __name__ == '__main__':
    login_func()


