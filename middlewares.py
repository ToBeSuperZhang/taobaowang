# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium import webdriver
from scrapy.http import HtmlResponse
import time
import random
from .settings import USER_AGENTS


class RandomUserAgent:
    def process_request(self,request,spider):
        user_agent = random.choice(USER_AGENTS)
        request.headers.setdefault('User-Agent',user_agent)





class LoginTaobaowangDownloaderMiddleware(object):

    def process_request(self,request,spider):
        if spider.name=='taobao':
            if "login" in request.url:
                spider.browser.get(request.url)
                time.sleep(10)
                print('登录页面')
                username= spider.browser.find_element_by_id('username')
                password = spider.browser.find_element_by_id('password')
                time.sleep(3)
                username.send_keys('可')
                time.sleep(0.52)
                username.send_keys('惜')
                time.sleep(0.32)
                username.send_keys('张')
                time.sleep(0.66)
                username.send_keys('q')
                time.sleep(0.81)
                username.send_keys('不')
                time.sleep(1)
                username.send_keys('会')
                time.sleep(0.12)
                username.send_keys('飞')
                time.sleep(2)
                password.send_keys('')
                time.sleep(2)
                click = spider.browser.find_element_by_id('btn-submit')
                click.click()
                time.sleep(25)


            else:

                spider.browser.get(request.url)

                time.sleep(10)

                # request.访问，调用selenium cookie

            return HtmlResponse(url=spider.browser.current_url,  # 当前连接

                                body=spider.browser.page_source,  # 源代码

                                encoding="utf-8")  # 返回页面信息





class TaobaowangSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class TaobaowangDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
