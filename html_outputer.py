#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-12 16:20:30
# @Author  : XiangBingguang (18182556558@163.com)
# @Link    : ${link}
# @Version : $Id$


class HtmlOutputer(object):
	"""docstring for HtmlOutputer"""
	def __init__(self, arg):
		self.datas = []

		super(HtmlOutputer, self).__init__()
		self.arg = arg
		
	def collect_data(self, data):
		if data is None:
			return
		self.datas.append(data)

	def output_data(self):
		fout = open('output.html', 'w')

		fout.write('<html>')
		fout.write('<body>')
		fout.write('<table>')
		for data in datas:
			fout.write('<tr>')
			fout.write('<td>%s</td>' % data['url'].encode('utf-8'))
			fout.write('<td>%s</td>' % data['title'].encode('utf-8'))
			fout.write('<td>%s</td>' % data['content'].encode('utf-8'))
			fout.write('</tr>')
		fout.write('<、table>')
		fout.write('<、body>')
		fout.write('<、html>')