import requests
from bs4 import BeautifulSoup


class Weather():
    def __init__(self, place, url):
        self.place = place
        self.url = url
        self.html = requests.get(url, timeout=30)  # 用requests抓取网页信息
        self.html.encoding = self.html.apparent_encoding
    def getweather(self):
        soup = BeautifulSoup(self.html.text, 'html.parser')  # 用BeautifulSoup库解析网页
        body = soup.body
        data = body.find('div', {'id': '7d'})
        ul = data.find('ul')
        lis = ul.find_all('li')
        self.list = [self.place]
        for day in lis:
            date = day.find('h1').string  # 找到日期
            info = day.find_all('p')  # 找到所有的p标签
            weath = info[0].string
            str = date+weath
            """
            if info[1].find('span') is None:  # 找到p标签中的第二个值'span'标签——最高温度
                temperature_highest = ' '  # 用一个判断是否有最高温度
            else:
                temperature_highest = info[1].find('span').string
                temperature_highest = temperature_highest.replace('℃', ' ')
            if info[1].find('i') is None:  # 找到p标签中的第二个值'i'标签——最高温度
                temperature_lowest = ' '  # 用一个判断是否有最低温度
            else:
                temperature_lowest = info[1].find('i').string
                temperature_lowest = temperature_lowest.replace('℃', ' ')
            temp_list.append(temperature_highest)  # 将最高气温添加到temp_list中
            temp_list.append(temperature_lowest)  # 将最低气温添加到temp_list中
            wind_scale = info[2].find('i').string  # 找到p标签的第三个值'i'标签——风级，添加到temp_list中
            temp_list.append(wind_scale)
            """
            self.list.append(str)  # 将temp_list列表添加到final_list列表中
        return self.list


