#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-12 16:20:29
# @Author  : XiangBingguang (18182556558@163.com)
# @Link    : ${link}
# @Version : $Id$

class UrlManager(object):
	"""docstring for UrlManager"""
	def __init__(self, arg):
		self.new_urls = set()
		self.old_urls = set()

	def add_new_url(self, url):
		if url is None:
			return
		if url is not in self.new_urls and url is not in self.old_urls:
			self.new_urls.add(url)

	def add_new_urls(self, urls):
		if len(urls) == 0 or urls is None:
			return
		for url in urls:
			if url not in self.new_urls and url not in self.old_urls:
				self.new_urls.add(url)

	def has_new_url(self):
		return len(self.new_urls) != 0

	def get_new_url(self):
		new_url = self.new_urls.pop()
		self.old_urls.add(new_url)
		return new_url
