# -*- coding: utf-8 -*-
from pymongo import MongoClient
import time
client = MongoClient('127.0.0.1', 27017)
# 连接所需数据库, test为数据库名
db = client.local
old = time.time()
one = list(db.taplist20170911001.find())
# print one


for i in one:
    search_result = list(db.taplist20170910001.find({"game_id": i["game_id"]}))
    # print search_result
    # if(len(search_result) > 0):
    #     # print type(i["Installs"]), i["Installs"], type(search_result[0]["Installs"]), search_result[0]["Installs"]
    #     i["install_reduce"] = int(i["Installs"]) - int(search_result[0]["Installs"])
    #     i["reserved_reduce"] = int(i["reserved"]) - int(search_result[0]["reserved"])
    #     i["attention_reduce"] = int(i["attention"]) - int(search_result[0]["attention"])
    # else:
    #     i["install_reduce"] = int(i["Installs"])
    #     i["reserved_reduce"] = int(i["reserved"])
    #     i["attention_reduce"] = int(i["attention"])
    # db.taplistrank20170911.insert(i)

print time.time() - old