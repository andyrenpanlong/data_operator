# -*- coding: utf-8 -*-
from pymongo import MongoClient
import time
client = MongoClient('127.0.0.1', 27017)
# 连接所需数据库, test为数据库名
db = client.local
dataObj = []
old = time.time()
for i in list(db.taplist20170909002.find()):
    search_result = list(db.taplist20170909001.find({"game_id": i["game_id"]}))
    if(len(search_result) > 0):
        # search_result[0][""]
        print type(i["Installs"]), i["Installs"], type(search_result[0]["Installs"]), search_result[0]["Installs"]
        i["install_reduce"] = int(i["Installs"]) - int(search_result[0]["Installs"])
        i["reserved_reduce"] = int(i["reserved"]) - int(search_result[0]["reserved"])
        i["attention_reduce"] = int(i["attention"]) - int(search_result[0]["attention"])
        # print search_result[0]["game_id"],  int(int(i["Installs"] - search_result[0]["Installs"]))
        # print i
        dataObj.append(i)
        # db.taplistrank20170909.insert(i)

print "awd", dataObj
print "话费时间为：", time.time() - old