import selenium.webdriver
import time
import json
# import pickle


driver = selenium.webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.yiban.cn/")
driver.delete_all_cookies()

fs = open('shuzu.txt', 'r')
num = fs.readlines()
if len(num) <= 0:
    print("无内容")
else:
    for i in num:
        driver.delete_all_cookies()
        time.sleep(1)
        driver.get("http://www.yiban.cn/")
        time.sleep(3)
        driver.delete_all_cookies()
        driver.get("https://www.yiban.cn/login?go=http%3A%2F%2Fwww.yiban.cn%2F")
        lst = i.strip().split(",")
        driver.find_element_by_id("account-txt").send_keys(lst[0])
        driver.find_element_by_id("password-txt").send_keys(lst[1])
        driver.find_element_by_id("login-btn").click()
        print("登录过程可能需要手动输入验证码\n完成登录后，键入y，开始提取用户cookies\n无法登录情况下，键入n或其他任意字符，跳过此次提取")
        dd = input("是否完成登录?(y/n)")
        if(dd == 'y'):
            # driver.find_element_by_id("login-captcha").send_keys(captcha)
            # driver.find_element_by_id("login-btn").click()
            time.sleep(1)
            cookies = driver.get_cookies()
            print(cookies)
            jsoncookies = json.dumps(cookies)
            with open("cookies.txt", "a+")as f:
                ss = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
                f.write("\n"+ss+"#"+str(lst[0])+"#"+str(lst[1])+"#"+"cookies-->#"+jsoncookies)
                print("cookies已添加在cookies.txt！")
        else:
            print("未提取cookies，并跳过此用户")
fs.close()

driver.quit()