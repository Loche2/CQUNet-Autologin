import subprocess
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# noinspection PyBroadException
def login(username, password):
    browser = webdriver.Edge()
    # browser.maximize_window()
    time.sleep(1)

    def element(e):
        return browser.find_element(By.CSS_SELECTOR, f'input.edit_lobo_cell[name="{e}"]')

    try:
        browser.get('https://login.cqu.edu.cn/')
        time.sleep(3)
        try:
            if element('logout'):
                print('CQUnet is still logged in!')
                browser.close()
        except:
            element('DDDDD').clear()
            element('upass').clear()
            element('DDDDD').send_keys(username)
            element('upass').send_keys(password)
            element('0MKKey').click()
            time.sleep(3)
            print('CQUnet is now logged in!')
    except:
        print('Login Failed..')
        browser.close()


def is_online():
    result = subprocess.run(['ping', 'baidu.com'],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=subprocess.CREATE_NO_WINDOW)
    # 检查返回码来确定是否在线
    return result.returncode == 0


# noinspection PyBroadException
def always_online(username, password, check_interval):
    try:
        login(username, password)
    except Exception:
        pass

    while 1:
        time.sleep(check_interval)
        if not is_online():
            try:
                login(username, password)
            except Exception:
                pass


if __name__ == "__main__":
    username = 'your_username'
    password = 'your_password'
    always_online(username, password, check_interval=300)
