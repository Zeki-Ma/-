import selenium.webdriver
import time
import json
# import pickle

driver = selenium.webdriver.Firefox()
driver.get("http://www.yiban.cn")
driver.implicitly_wait(10)
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