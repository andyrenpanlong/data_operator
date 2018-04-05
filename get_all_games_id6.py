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


def get_all_type_url():
    # 查找所有游戏id
    for i in range(61974, 620000, 1):
        url = "https://www.taptap.com/app/" + str(i)
        search_content(url)

def search_content(url):
    r = requests.get(url)
    if r.status_code == 200:
        # time.sleep(1)
        bs = BeautifulSoup(r.text, 'html5lib')
        gameObj = {}
        gameObj["game_id"] = bs.select(".taptap-button-download")[0].get("data-app-id") #游戏id
        gameObj["game_name"] = bs.select(".header-icon-body img")[0].get("title")  # 游戏名称
        gameObj["url"] = r.url  # 游戏名称
        # print gameObj
        single_data_save_mysql(gameObj)


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
    get_all_type_url()
    endtime = datetime.datetime.now()
    print "爬取工作结束..."
    print (endtime - starttime).seconds
