from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from login import login_func

login_func()

def todo_func():
    driver = webdriver.Chrome()
    todos = driver.find_elements(By.CLASS_NAME, 'todo-item-class')  

    todo_list = []
    for todo in todos:
        title = todo.find_element(By.CLASS_NAME, 'title-class').text  
        due_date = todo.find_element(By.CLASS_NAME, 'due-date-class').text  
        todo_list.append({'title': title, 'due_date': due_date})


    for item in todo_list:
        print(item)
    
    driver.quit()

if __name__ == '__main__':
    login_func()
    todo_func()

