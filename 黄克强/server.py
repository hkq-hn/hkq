import signal
import sys
from multiprocessing import Process
from socket import *
from time import sleep
from mysql01 import *
#全局变量
HOTS = '0.0.0.0'
POST = 8888
ADDR = (HOTS,POST)
db = Wuhan(database='online_dict')

def do_select(c,data):
    name = data[1]
    r = db.select(name)
    if r:
        msg = "序号:%s, 车型:%s, 批次号及编号:%s ,车辆VIN码:%s ,发动机号:%s ,验收日期:%s, " \
              "发运日期:%s ,调拨单号:%s, 接装单位:%s ,接装单位地址:%s, " \
              "联系人:%s, 联系人电话:%s"%(r[0])
        c.send(msg.encode())
    else:
        c.send("F".encode())


def do_delete(c, data):
    #删除
    number = data[1]
    r = db.delete(number)
    if r :
        c.send("OK".encode())
    else:
        c.send("F".encode())


def do_insert(c, data):
    #增加
    data = data[1]
    data = data.split(",")
    db.insert(data)
    c.send("OK".encode())


def do_modify(c, data):
    #修改
    data = data[1]
    data = data.split(",")
    number= data[0]
    name = data[1]
    text = data[2]
    r = db.modify(number,name,text)
    if r:
        c.send("OK".encode())
    else:
        c.send("F".encode())

def request(c):
    db.create_cur()
    while True:
        data = c.recv(1024).decode()
        data = data.split(' ',1)
        #处理来自客户端的请求
        if data[0] == "EXIT":
            sys.exit()
        elif data[0] == "Q":
            do_select(c,data)
        elif data[0] == "Z":
            do_insert(c,data)
        elif data[0] == "M":
            do_modify(c,data)
        elif data[0] == "R":
            do_delete(c,data)


#服务端主函数入口
def main():
    #创建网络连接
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(20)

    #处理僵尸进程
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)

    #等待连接
    print("Listen the port 8888")
    while True:
        try:
            c ,addr = s.accept()
            print("connect from ",addr)
        except KeyboardInterrupt:
            sys.exit("服务退出")
        except Exception as e:
            print(e)
            continue
        #创建进程
        p = Process(target=request , args = (c,))
        p.daemon = True
        p.start()

if __name__ == '__main__':
    main()
