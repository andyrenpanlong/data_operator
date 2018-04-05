# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from pymongo import MongoClient
from bs4 import BeautifulSoup
import scrapy
import json
import requests
import redis
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def search_content(url):
    r = requests.get(url)
    if r.status_code == 200:
        time.sleep(1)
        bs = BeautifulSoup(r.text, 'html5lib')
        gameObj = {}
        print bs.select(".header-icon-body img")[0].get("title")
        gameObj["game_id"] = bs.select(".taptap-button-download")[0].get("data-app-id") #游戏id
        gameObj["game_name"] = bs.select(".header-icon-body img")[0].get("title")    #游戏名称
        gameObj["game_icon"] = bs.select(".header-icon-body img")[0].get("src")   #游戏图标
        gameObj["Installs"] = "0"
        print gameObj["game_name"]
        gameObj["reserved"] = "0"
        gameObj["attention"] = "0"
        if bs.select(".text-download-times"):
            yuyue = bs.select(".text-download-times")[0].text   #游戏下载预约次数
            yuyue = yuyue.split("|")
            print yuyue
            for i in yuyue:
                print i
                if ("Installs" in i):
                    gameObj["Installs"] = i.replace("Installs", "").strip()

                if ("reserved" in i):
                    gameObj["reserved"] = i.replace("reserved", "").strip()

                if ("Reserved" in i):
                    gameObj["reserved"] = i.replace("Reserved", "").strip()

                if ("人安装" in i):
                    print "awdada", i
                    gameObj["Installs"] = i.replace("人安装", "").strip()
                    print gameObj["Installs"]

                if ("人关注" in i):
                    gameObj["attention"] = i.replace("人关注", "").strip()
        print gameObj["attention"]
        if bs.select(".app-rating-score"):
            gameObj["score"] = bs.select(".app-rating-score")[0].text   #游戏评分
        else:
            gameObj["score"] = "0"

        if bs.select(".taptap-button-download"):
            gameObj["game_bag_name"] = bs.select(".taptap-button-download")[0].get("data-app-identifier")  # 游戏包名
        else:
            gameObj["game_bag_name"] = ""

        if bs.select(".main-header-tab ul li")[1].select("a small"):
            gameObj["review"] = bs.select(".main-header-tab ul li")[1].select("a small")[0].text    #游戏评论数
        else:
            gameObj["review"] = "0"

        if bs.select("#reviewsList li"):
            gameObj["last_comment_time"] = bs.select("#reviewsList li")[0].select(".item-text-header a span")[0].text    #最后评论时间
        else:
            gameObj["last_comment_time"] = "0"

        for i in bs.select(".info-item-content"):
            if(i.get("itemprop") ==  "datePublished"):
                gameObj["refresh_time"] = i.text    #游戏更新时间

        if bs.select(".header-text-author span"):
            for i in bs.select(".header-text-author span"):
                if i.get("itemprop") == "name":
                    gameObj["developer"] = i.text
        else:
            gameObj["developer"] = ""
        print "游戏相关信息如下：", json.dumps(gameObj)

# url = "https://www.taptap.com/app/56907"  #名称不对
url = "https://www.taptap.com/app/61351" #关注人数不对
search_content(url)