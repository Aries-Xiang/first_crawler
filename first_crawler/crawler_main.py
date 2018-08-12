#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-12 16:19:13
# @Author  : XiangBingguang (18182556558@163.com)
# @Link    : ${link}
# @Version : $Id$


class crawler(object):
	"""docstring for crawler"""
	def __init__(self):
		# 初始化url管理器
		self.urls = url_manager.UrlManager()
		# 初始化url下载器
		self.downloader = url_downloader.HtmlDownloader()
		# 初始化url解析器
		self.parser = html_parser.HtmlParser()
		# 初始化url输出器
		self.outputer = html_outputer.HtmlOutputer()
		
	def start(self, root_url):
		count = 1
		self.urls.add_new_url(root_url)
		while self.urls.has_new_url():
			# 爬取1000条限制
			if count == 1000:
				break
			# 对无法的url报错
			try:
				new_url = self.urls.get_new_url()
				print('start craw &d 个: s%' %(count, new_url))
				# 获取当前url页面代码
				html_cont = self.downloader.download(new_url)
				# 解析出新的url和需要抓取的数据
				new_urls, new_data = self.parser.parse(new_url, html_cont)
				self.urls.add_new_urls(new_urls)
				self.outputer.collect(new_data)
				count = count + 1
			except:
				print('craw error')
		self.outputer.output_html()

if __name__ == '__main__':
	# 菜鸟教程Python主页
	root_url = 'http://www.runoob.com/python/python-tutorial.html'
	obj_crawler = CrawlerMain()
	obj_crawler.start()