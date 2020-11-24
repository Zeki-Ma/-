import selenium.webdriver
import time
import random
import json
import requests

 


def daka(Tim,TempList):
    with open("/home/yiban/cookies_list.txt", "r", encoding="utf-8")as fl:
        kk = 0
        option =selenium.webdriver.ChromeOptions()
        option.add_argument('--no-sandbox')
        option.add_argument('--headless')
        # 注意path，我这里是chromedriver放在/home/apk/chromedriver
        driver = selenium.webdriver.Chrome(executable_path='/home/software/chromedriver', chrome_options=option)
        driver.get("http://www.yiban.cn/")
        driver.implicitly_wait(8)
        time.sleep(2)
        # driver = selenium.webdriver.Chrome()
        # driver.get("http://www.yiban.cn/")
        # driver.implicitly_wait(5)
        # time.sleep(2)
        for line in fl.readlines():
            kk = kk + 1
            if(kk % 5 == 0):
                print("更换浏览器")
                driver.quit()
                time.sleep(8)
                option =selenium.webdriver.ChromeOptions()
                option.add_argument('--no-sandbox')
                option.add_argument('--headless')
                driver = selenium.webdriver.Chrome(executable_path='/home/software/chromedriver', chrome_options=option)
                driver.get("http://www.yiban.cn/")
                driver.implicitly_wait(8)
                time.sleep(2)
            cookies = json.loads(line)
            print("%d读取cookies！" %kk )
            driver.delete_all_cookies()
            driver.get("http://www.yiban.cn/")
            for co in cookies:
                driver.add_cookie(co)
            try:
                driver.get("http://app.yiban.cn/apps/appinfo?id=278033")
                time.sleep(3)        
                driver.find_element_by_xpath('/html/body/main/div/div/section/div[2]/div[2]/p[5]/a/button').click()
                time.sleep(3)
                driver.get("http://power.modsdom.com/sccloudV5/LAB1/Index/Index/index#/User/User/tempEdit")
                time.sleep(1)
                if(Tim == 1):
                    driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]").click()    #/html/body/div[1]/div/div[2]/div[2]/div[1]/div
                    time.sleep(0.5)
                    driver.find_element_by_xpath("/html/body/div[1]/div/div[5]/div/div[2]/div[1]/div/input").clear()
                    tmp=TempList[random.randint(0,2)]
                    driver.find_element_by_xpath("/html/body/div[1]/div/div[5]/div/div[2]/div[1]/div/input").send_keys(tmp)
                    driver.find_element_by_xpath("/html/body/div[1]/div/div[5]/div/div[2]/div[3]/input").click()
                    driver.find_element_by_xpath("/html/body/div[1]/div/div[5]/div/div[2]/div[4]/span").click()

                elif(Tim == 2):
                    driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]").click()    #/html/body/div[1]/div/div[2]/div[2]/div[1]/div
                    time.sleep(0.5)
                    driver.find_element_by_xpath("/html/body/div[1]/div/div[5]/div/div[2]/div[1]/div/input").clear()
                    tmp=TempList[random.randint(0,2)]
                    driver.find_element_by_xpath("/html/body/div[1]/div/div[5]/div/div[2]/div[1]/div/input").send_keys(tmp)
                    driver.find_element_by_xpath("/html/body/div[1]/div/div[5]/div/div[2]/div[3]/input").click()
                    driver.find_element_by_xpath("/html/body/div[1]/div/div[5]/div/div[2]/div[4]/span").click()

                elif(Tim == 3):
                    driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[3]").click()
                    time.sleep(0.5)
                    driver.find_element_by_xpath("/html/body/div[1]/div/div[5]/div/div[2]/div[1]/div/input").clear()
                    tmp=TempList[random.randint(0,2)]
                    driver.find_element_by_xpath("/html/body/div[1]/div/div[5]/div/div[2]/div[1]/div/input").send_keys(tmp)
                    driver.find_element_by_xpath("/html/body/div[1]/div/div[5]/div/div[2]/div[3]/input").click()
                    driver.find_element_by_xpath("/html/body/div[1]/div/div[5]/div/div[2]/div[4]/span").click()
            except:
                print("%d打卡失败！" % kk)
            else:
                print("%d打卡成功！" % kk)
    driver.quit()

            

if __name__ == "__main__":
    ss = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(time.time()))
    print(ss)
    ss = time.strftime("%H", time.localtime(time.time()))
    if(ss == "10"):
        daka(1,["36.6","36.7","36.8"])
    elif(ss == "11"):
        daka(2,["36.6","36.8","36.9"])
    elif(ss == "18"):
        daka(3,["36.7","36.8","36.9"])

                
            
