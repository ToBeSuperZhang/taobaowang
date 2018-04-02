from scrapy import cmdline
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
cmdline.execute('scrapy crawl taobao'.split())