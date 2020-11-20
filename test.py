import selenium.webdriver
import time
import json
import smtplib
from email.mime.text import MIMEText
import requests
from bs4 import BeautifulSoup



driver = selenium.webdriver.Firefox()
driver.get("http://211.86.195.226:85/book/more/type/4/lib/1")
driver.implicitly_wait(10)
with open("cookies_list.txt", "r", encoding="utf-8")as fl:
    for line in fl.readlines():
        cookies = json.loads(line)
        print("正在执行脚本程序，请勿退出！")
        driver.delete_all_cookies()
        driver.get("http://211.86.195.226:85/book/more/type/4/lib/1")
        for co in cookies:
            driver.add_cookie(co)
        time.sleep(1)
        driver.get("http://211.86.195.226:85/book/more/type/4/lib/1")
        time.sleep(2)
        j = 0
        try:
            i = i + 1
            driver.find_element_by_link_text("立即预约").click()
            driver.find_element_by_id("signUp").click()
            driver.find_element_by_name("mobile").clear()
            driver.find_element_by_name("mobile").send_keys(users[i][0])
            driver.find_element_by_xpath('/html/body/div[8]/div/table/tbody/tr[3]/td/div[2]/button[2]').click()
        except:
            
            
            print('预约失败')
        else:
            
            print('预约成功')
        time.sleep(2)   # 别给人服务器造成太大压力
driver.quit()
time.sleep(2)

print("脚本已经执行完成，即将自动退出！")
time.sleep(5)
