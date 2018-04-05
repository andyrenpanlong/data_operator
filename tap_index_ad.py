#coding=utf-8

import time
from bs4 import BeautifulSoup
from pymongo import MongoClient
import requests
import json
import datetime
import redis
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def devide_ad_url():

    for i in range(0, 1, 1):
        get_tap_index_ad("https://www.taptap.com/?time=" + str(i+1))

def get_tap_index_ad(url):
    r = requests.get(url)
    if r.status_code == 200:
        print "adawd:", r.text
        # time.sleep(1)
        bs = BeautifulSoup(r.text, 'html5lib')
        gameObj = {}
        gameObj["ad"] = bs.select("#recList .index-ad .feed-rec-title")[0].get("href") #游戏id
        # gameObj["game_name"] = bs.select("#recList .index-ad a")[0].select("h2").get("title") # 游戏名称
        # gameObj["game_id"] = r.url  # 游戏名称
        print gameObj, bs.select("#recList .index-ad")
        # single_data_save_mysql(gameObj)


def single_data_save_mysql(data):
    job_redis = redis.Redis(host="127.0.0.1", port="6379", db="2")
    job_redis.sadd('detailUrl', data["url"])
    client = MongoClient('127.0.0.1', 27017)
    # 连接所需数据库,test为数据库名
    db = client.local
    print "存储数据：", data
    db.taptapGameId.insert(data)

if __name__ == '__main__':
    print "爬虫开始工作..."
    starttime = datetime.datetime.now()
    print starttime
    devide_ad_url()
    endtime = datetime.datetime.now()
    print "爬取工作结束..."
    print (endtime - starttime).seconds
