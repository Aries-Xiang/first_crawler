#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-12 16:20:30
# @Author  : XiangBingguang (18182556558@163.com)
# @Link    : ${link}
# @Version : $Id$

import bs4, re, urllib


class HtmlParser(object):

    def parse(self, page_url, html_content):
        if page_url is None or html_content is None:
            return

        soup = bs4.BeautifulSoup(page_url, 'html.parser')

        new_urls = self._get_new_urls(soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, soup):
        new_urls = set()
        root_url = 'https://en.wikipedia.org'

        # /wiki/*Python*
        links = soup.find_all('a', href=re.compile(r'/wiki/([a-z]+)Python([a-z]+)', re.I))
        for link in links:
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(root_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}

        # url
        res_data['url'] = page_url

        # <h1 id="firstHeading" class="firstHeading" lang="en">Python</h1>
        title_node = soup.find('h1', class_='firstHeading')
        res_data['title'] = title_node.get_text()

        # <div id="bodyContent" class="mw-body-content">
        content_node = soup.find('div', id='bodyContent')
        res_data['content'] = content_node.get_text()

        return res_data