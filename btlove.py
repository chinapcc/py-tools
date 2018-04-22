#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-
#
# +-----------------------------------------------------------------------
# | (c)2018年 如此生活. All rights reserved.
# +-----------------------------------------------------------------------
# | File:       btlove.py
# | Describe:   通过网站下查找BT链接地址，并且下载
# | Author:     Tony Wang <4588567@qq.com>
# | Created:    2018-04-22
# +-----------------------------------------------------------------------
import re
import urllib

'''
保存torrent文件
'''
def get_torrent(url):
    data = ''
    try:
        with urllib.urlopen(url) as q:
            data = q.read()
    except  urllib.HTTPError as e:
        print("下载.torrent失败,%s" % e)
    #保存文件，把bt文件保存到磁盘上
    return (data if data == '' else data)

'''
解析网页中含有 .torrent 的超链接
'''
def pattern_torrent(url):
    url_torrent = ''
    try:
        with urllib.urlopen(url) as q:
            data = q.read()
            if q.status == 200:
                urls = re.findall(r"http://.*?torrent", data.decode('utf-8'), re.I)
                for u in urls:
                    file = get_torrent(u)
    except:
        print("地址出错，%s" % url)

    return url_torrent

'''
下载 BT 文件
'''
def download_torrent(filename):
    return

# 主程序
def main():
    url = 'http://ok.we5200.com/a/omav/%d.html'
    # for x in range(2353,2779):
    for x in range(2353, 2354):
        xxx = url % x
        pattern_torrent(xxx)

if __name__ == "__main__":
    main()