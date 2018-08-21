#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-12 16:20:30
# @Author  : XiangBingguang (18182556558@163.com)
# @Link    : ${link}
# @Version : $Id$

import urllib.request

class HtmlDownloader(object):
	"""docstring for HtmlDownloader"""
	def download(self, url):
		if url is None:
			return

		response = urllib.request.urlopen(url)

		if response.getcode() != 200:
			return None

		return response.read()