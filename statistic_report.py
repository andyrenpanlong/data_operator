# -*- coding: utf-8 -*-
from pymongo import MongoClient

client = MongoClient('127.0.0.1', 27017)
# 连接所需数据库, test为数据库名
db = client.local
print len(list(db.tap_game_id_unique20170923.find()))
print len(list(db.tap_game_id_unique20170922.find()))

for i in list(db.tap_game_id_unique20170923.find()):
    search_result = list(db.tap_game_id_unique20170922.find({"game_id": i["game_id"]}))
    # if(len(search_result) > 0):
        # i["install_reduce"] = int(i["Installs"]) - int(search_result[0]["Installs"])
        # i["reserved_reduce"] = int(i["reserved"]) - int(search_result[0]["reserved"])
        # i["attention_reduce"] = int(i["attention"]) - int(search_result[0]["attention"])
    # else:
        # i["install_reduce"] = int(i["Installs"])
        # i["reserved_reduce"] = int(i["reserved"])
        # i["attention_reduce"] = int(i["attention"])
        # db.taplistrank20170911.insert(i)
    if (len(search_result) <= 0):
        print i
        db.tap_game_id_unique20170924.insert(i)