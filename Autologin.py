import configparser
import socket
import subprocess
import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

config = configparser.ConfigParser()
config.read('config.ini')


# noinspection PyBroadException
def login(username, password):
    browser = webdriver.Edge()
    browser.maximize_window()
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
        IP = send_IP()
    except Exception:
        IP = '404'
        pass

    while 1:
        time.sleep(check_interval)
        if not is_online():
            try:
                login(username, password)
                if IP != socket.gethostbyname(socket.gethostname()):
                    IP = send_IP()
            except Exception:
                pass


# 通过推送加API发送当前IP地址
def send_IP():
    IP = socket.gethostbyname(socket.gethostname())
    # 获取config里的token
    token = config['Credentials']['token']
    # 检查token是否为空
    if not token or token == 'your_pushplus_token':
        print("Token is empty in the configuration file.")
        return
    # 推送加请求地址目标URL
    url = 'https://www.pushplus.plus/send/'
    # POST请求的数据
    data = {'token': token,
            'title': f'{socket.gethostname()}-IP',
            'content': str(IP)
            }
    print(data)
    # 发送POST请求
    requests.post(url, data)
    return IP


if __name__ == "__main__":
    always_online(config['Credentials']['username'], config['Credentials']['password'], check_interval=300)
