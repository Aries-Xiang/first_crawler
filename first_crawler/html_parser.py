#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-12 16:20:30
# @Author  : XiangBingguang (18182556558@163.com)
# @Link    : ${link}
# @Version : $Id$

import bs4, re

class HtmlParser(object):
	"""docstring for HtmlParser"""
	def __init__(self, arg):
		super(HtmlParser, self).__init__()
		self.arg = arg
		
	def parse(self, page_url, html_content):
		if page_url is None or html_content is None:
			return

		soup = bs4.BeautifulSoup(page_url, 'html.parser')

		new_urls = self.get_new_urls(page_url, soup)
		new_data = self.get_new_data(page_url, soup)
		return new_urls, new_data

	def get_new_urls(self, page_url, soup):
		# /python/python-
		links = soup.find_all('a', href = re.compile(r''))

	def get_new_data(self, page_url, soup):
		pass