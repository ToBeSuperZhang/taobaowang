# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest
from selenium import webdriver
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals


class TaobaoSpider(scrapy.Spider):
    name = 'taobao'
    allowed_domains = ['taobao.com']
    start_urls = ['https://login.m.taobao.com/login.htm']

    def __init__(self):
        mobilesetting = {'deviceName': 'iPhone 6 Plus'}# 设备设置
        options = webdriver.ChromeOptions()# 网页设置
        options.add_experimental_option('mobileEmulation', mobilesetting)#设备名称加入网页设置
        self.browser = webdriver.Chrome(chrome_options=options)#开启网页
        self.browser.set_window_size(400,800)# 设置屏幕大小
        super(TaobaoSpider,self).__init__()# 传递给父类
        dispatcher.connect(self.spider_closed,signals.spider_closed)# 结束爬虫,并调用 自己的函数parse

    def spider_closed(self):
        print('爬虫关闭')
        self.browser.close()

    def parse(self, response):
        print('===================================')
        print(response.url)
        print(response.body.decode('utf-8'))
        pass
