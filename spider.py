import selenium.webdriver
import time
import json
import smtplib
from email.mime.text import MIMEText
import requests
from bs4 import BeautifulSoup



class SendMail():
    def __init__(self, Address, Content):
        self.address = Address
        self.content = Content
        msg_from = '480167196@qq.com'  # 发送方邮箱
        passwd = 'dyirfvfdcxucbhhg'  # 填入发送方邮箱的授权码
        subject = "web自动化测试"  # 主题
        msg = MIMEText(self.content)
        msg['Subject'] = subject
        msg['From'] = msg_from
        msg['To'] = self.address
        try:
            s = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 邮件服务器及端口号
            s.login(msg_from, passwd)  # 登录SMTP服务器
            s.sendmail(msg_from, self.address, msg.as_string())  # 发邮件 as_string()把MIMEText对象变成str
            print("发送成功")
        except s.SMTPException:
            print("发送失败")
        finally:
            s.quit()

fs = open('shuzu.txt', 'r')
num = fs.readlines()
if len(num) <= 0:
    fs.close()
    print("无内容")
else:
    users = []
    for i in num:
        lst = i.strip().split(",")
        users.append(lst)
i = -1

driver = selenium.webdriver.Firefox()
driver.get("http://www.yiban.cn/")
driver.implicitly_wait(10)
with open("cookies_list.txt", "r", encoding="utf-8")as fl:
    for line in fl.readlines():
        cookies = json.loads(line)
        print("正在执行脚本程序，请勿退出！")
        driver.delete_all_cookies()
        driver.get("http://www.yiban.cn/")
        for co in cookies:
            driver.add_cookie(co)
        time.sleep(1)
        driver.get("http://app.yiban.cn/apps/appinfo?id=278033")
        time.sleep(6)
        
        driver.find_element_by_xpath('/html/body/main/div/div/section/div[2]/div[2]/p[5]/a/button').click()
        time.sleep(10)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[1]/div').click()    #/html/body/div[1]/div/div[2]/div[2]/div[1]/div
        time.sleep(10)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[5]/div/div[2]/div[1]/div/input').send_keys("36.7")    #/html/body/div[1]/div/div[5]/div/div[2]/div[1]/div/input
        time.sleep(10)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[5]/div/div[2]/div[3]/input').click()    #ele = driver.find_element_by_xpath('/html/body/div[1]/div/div[5]/div/div[2]/div[3]/input')  print("点击之前，选择状态是：  " + ele.is_selected())
        time.sleep(10)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[5]/div/div[2]/div[4]/span').click()
        
        
        j = 0
        try:
            i = i + 1
            
            driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[1]').click()
            time.sleep(10)
            driver.find_element_by_link_text("立即预约").click()
            driver.find_element_by_id("signUp").click()
            driver.find_element_by_name("mobile").clear()
            driver.find_element_by_name("mobile").send_keys(users[i][0])
        except:
            j = 1
            users[i].append('预约失败')
            print(users[i])
        else:
            users[i].append('预约成功')
            print(users[i])
        time.sleep(2)   # 别给人服务器造成太大压力
driver.quit()
time.sleep(2)
for e in range(i+1):
        test = SendMail(users[e][1], "预约信息:\n邮箱:"
                      + users[e][1] + "\n手机号:"
                      + users[e][0]
                      + users[e][-1])
print("脚本已经执行完成，即将自动退出！")
time.sleep(5)
