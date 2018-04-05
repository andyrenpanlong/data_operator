# -*- coding: utf-8 -*-
from pymongo import MongoClient

client = MongoClient('127.0.0.1', 27017)
# 连接所需数据库, test为数据库名
db = client.local
print
# print db.taplist8.find().sort({"game_id": 1})
html = ""
result = list(db.taplistrank20170910.find({}).sort([("install_reduce", -1)]).limit(100))
# result = list(db.taplist0908001.find({}).sort([("install_reduce", -1)]))
# result = list(db.taplist10.find({}).sort([("reserved_reduce", -1)]).limit(100))
# result = list(db.taplist10.find({}).sort([("attention_reduce", -1)]).limit(100))
# result = list(db.taptapGameId.find({}).sort([("game_id", 1)]))
# client = MongoClient('localhost', 27017)
# db = client.local
# collection = db.taptapGameId
# collection = db.hhhhahah
# print len(collection.distinct('game_id'))
# for game_id in collection.distinct('game_id').sort([("install_reduce", -1)]):  # 使用distinct方法，获取每一个独特的元素列表
# for game_id in collection.distinct('game_id'):  # 使用distinct方法，获取每一个独特的元素列表
#     result = list(db.hhhhahah.find({"game_id": game_id}))[0]
#     db.tap_game_id_unique.insert(result)
    # print result
# print len(result)
for i in range(len(result)):
    print result[i]
    print result[i]["refresh_time"]
    html += "<tr>"
    html += "<td>" + str(i+1) + "</td>"
    html += "<td><a target='_blank' href=https://www.taptap.com/app/"+str(result[i]["game_id"])+">" + result[i]["game_name"] + "</a></td>"
    html += "<td>" + str(result[i]["game_id"]) + "</td>"
    html += "<td><img width='50' height='50' src='" + result[i]["game_icon"] + "'></td>"
    html += "<td>" + result[i]["developer"] + "</td>"
    html += "<td>" + str(result[i]["score"]) + "</td>"
    html += "<td>" + str(result[i]["Installs"]) + "</td>"
    html += "<td>" + str(result[i]["reserved"]) + "</td>"
    html += "<td>" + str(result[i]["attention"]) + "</td>"
    html += "<td>" + str(result[i]["install_reduce"]) + "</td>"
    html += "<td>" + str(result[i]["reserved_reduce"]) + "</td>"
    html += "<td>" + str(result[i]["attention_reduce"]) + "</td>"
    html += "<td>" + str(result[i]["review"]) + "</td>"
    html += "<td>" + result[i]["refresh_time"] + "</td>"
    html += "<td>" + str(result[i]["last_comment_time"]) + "</td>"
    html += "</tr>"
print "awdwa", html