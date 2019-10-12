"""
    数据库
"""
import pymysql

class Wuhan:
    def __init__(self, host='localhost', port=3306, user='root',
                 passwd='123456', database=None, charset='utf8'):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.database = database
        self.charset = charset

        # # 建立数据连接
        self.db = pymysql.connect(host=self.host,
                                  port=self.port,
                                  user=self.user,
                                  passwd=self.passwd,
                                  database=self.database,
                                  charset=self.charset)

    def create_cur(self):
        # 创建游标
        self.cur = self.db.cursor()

    def close(self):
        # 关闭游标和数据库
        self.cur.close()
        self.db.close()

    def select(self,name):
        #查询
        sql = "select * from wuhan where 联系人 = '%s' "%name
        self.cur.execute(sql)
        resule = self.cur.fetchall()
        return resule

    def delete(self,number):
        sql = "select * from wuhan where 调拨单号 = %s " %number
        self.cur.execute(sql)
        resule = self.cur.fetchall()
        if resule:
            sql = "delete from wuhan where 调拨单号 = %s " % number
            self.cur.execute(sql)
            sql = "select * from wuhan where 调拨单号 = %s " % number
            self.cur.execute(sql)
            resule1 = self.cur.fetchall()
            self.db.commit()
            if resule1:
                return False
            else:
                return True
        else:
            return False

    def insert(self,data):
        #增加
        sql = "insert into wuhan (车型,批次号及编号,车辆VIN码	,发动机号,验收日期," \
              "发运日期,调拨单号,接收单位,接收单位地址,联系人	,联系人电话) " \
              "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        try:
            self.cur.execute(sql,data)
            self.db.commit()
        except:
            self.db.rollback()

    def modify(self,number,name,text):
        sql = "select * from wuhan where 调拨单号 = %s " % number
        self.cur.execute(sql)
        resule1 = self.cur.fetchall()
        if resule1:
            #update 表名 set 字段1=值1,字段2=值2,... where 条件;
            sql = "update wuhan set %s = '%s'  where 调拨单号 = %s"%(name,text,number)
            try:
                self.cur.execute(sql)
                self.db.commit()
            except:
                self.db.rollback()
            return True
        else:
            return False




















