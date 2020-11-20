import selenium.webdriver
import time
import json
# import pickle
with open("users.txt", "r")as f:
    num = f.readlines()
    if len(num) <= 0:
#    f.close()
    print("无内容")
    else:
        users = []
        for i in num:
            lst = i.strip().split(",")
            users.append(lst)



driver = selenium.webdriver.Firefox()
driver.get("https://www.yiban.cn/login?go=http%3A%2F%2Fwww.yiban.cn%2F")
driver.implicitly_wait(10)
driver.find_element_by_id("account-txt").send_keys("19955874832")
driver.implicitly_wait(10)
driver.find_element_by_id("password-txt").send_keys("19955874832")
driver.implicitly_wait(10)
driver.find_element_by_id("login-btn").click()
time.sleep(30)
cookies = driver.get_cookies()
print("cookies:")
print(cookies)
print("正在保存cookies")
jsoncookies = json.dumps(cookies)
with open("cookies.txt", "w")as f:
    f.write(jsoncookies)
    print("cookies已保存在cookies.txt,请尽快取走！")
time.sleep(1.5)
driver.quit()