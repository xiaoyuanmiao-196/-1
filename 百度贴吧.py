import requests
import pymysql
import random
import time
from lxml import etree

url="https://tieba.baidu.com/f?ie=utf-8&kw=lol&fr=search"
response=requests.get(url)
html=response.text
#print(html)
selector=etree.HTML(html)
ls=selector.xpath('//li[@class=" j_thread_list clearfix"]')
print("len:",len(ls))
base_url='https://tieba.baidu.com'
for each in ls:
        title=each.xpath('.//a[@class="j_th_tit "]/text()')[0]
        print('title',title)
        lianjie=base_url+each.xpath('.//a[@class="j_th_tit "]/@href')[0]
        print('链接：',lianjie)
        zuozhe=each.xpath('.//span[@class="frs-author-name-wrap"]/a/text()')[0]
        print('作者：',zuozhe)
        huifushu=each.xpath('.//span[@class="threadlist_rep_num center_text"]/text()')[0]
        print('回复数：',huifushu)
        print('='*200)
        parmas = [title, lianjie, zuozhe, huifushu]
        print("111111111")
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456', db='beidutieba')
        cur = conn.cursor()
        strsql = 'insert into baidutieba VALUES (0,%s,%s,%s,%s)'
        cur.execute(strsql, parmas)
        conn.commit()
        time.sleep(random.random())
        #爬取百度贴吧 并存入数据库
