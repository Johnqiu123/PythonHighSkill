# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 15:51:36 2017

@author: Administrator

问题：如何实现可迭代对象和迭代器对象
可迭代对象具备两个方法之一:__iter__方法和__getitem__方法
1)实现一个迭代器对象WeatherIterator,next方法每次返回一个城市
2)实现一个可迭代对象WeatherIterable,__iter__方法返回一个迭代器对象

调用中华万年历API
抓包中华万年历得到的接口（JSON）：
http://wthrcdn.etouch.cn/weather_mini?city=北京
通过城市名字获得天气数据，json数据
http://wthrcdn.etouch.cn/weather_mini?citykey=101010100
通过城市id获得天气数据，json数据
数据和中国天气网（www.weather.com.cn）一致
"""
from collections import Iterable, Iterator
import requests

class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0
    
    def getWeather(self, city):
        r = requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city='+ city)
        data = r.json()['data']['forecast'][0]
        return '%s:%s, %s' % (city, data['low'], data['high'])
    
    def next(self):
        """必须实现的方法"""
        if self.index == len(self.cities):
            raise StopIteration # 抛出异常
        city = self.cities[self.index]
        self.index += 1
        return self.getWeather(city)

class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities
    
    def __iter__(self):
        return WeatherIterator(self.cities)

if __name__=='__main__':
    for x in WeatherIterable([u'北京',u'上海',u'广州',u'长春']):
        print x
        


