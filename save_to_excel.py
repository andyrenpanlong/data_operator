# -*- coding:utf-8 -*-

import sys
import xlwt
import datetime
from pymongo import MongoClient

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    print sys.getdefaultencoding()
    reload(sys)
    sys.setdefaultencoding(default_encoding)

if __name__ == '__main__':
    startTime = datetime.datetime.now()

    mongoClient = MongoClient("127.0.0.1", 27017)
    # 连接库
    db = mongoClient.admin

    print db.taplist10.count()

    workbook = xlwt.Workbook(encoding='utf-8')

    # datas = db.user.find()
    datas = db.taplist10.find()

    EXCEL_ROWS = 65535
    EXCEL_COLS = 256
    nrows, total_rows, sheet_num = 0, 0, 0

    for data in datas:
        # print data
        if (nrows % EXCEL_ROWS == 0):
            wsheet = workbook.add_sheet('sheet' + str(sheet_num), cell_overwrite_ok=True)
            nrows = 0
            sheet_num = sheet_num + 1
        keys = data.keys()
        print keys
        cols_num = EXCEL_COLS if len(keys) > EXCEL_COLS else len(keys)
        for ncol in xrange(cols_num):
            value = data[keys[ncol]]
            print nrows, ncol, value
            if(ncol != 12):
                wsheet.write(nrows, ncol, value)
        nrows = nrows + 1
        total_rows = total_rows + 1

    workbook.save("D:\\Spider\\huiwan\\taptap2.xls")
    endTime = datetime.datetime.now()
    print "import xls success ! spend time %s seconds" % ((endTime - startTime).seconds)