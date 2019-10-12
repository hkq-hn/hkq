import sys,os
from socket import *

#全局变量
HOTS = '127.0.0.1'
POST = 8888
ADDR = (HOTS,POST)
s = socket()
s.connect(ADDR)

def select(s):
    #查询
    while True:
        sel = input("请输入要查询的关键字 建议输入姓名查找:")
        if sel != "":
            break
        else:
            print("输入不能为空")
    msg = "Q "+sel
    s.send(msg.encode())
    data = s.recv(4096).decode()
    if data =="F":
        print("未能查询到相关内容")
    else:
        print(data)

def insert(s):
    #增加
    elemt2 = input("输入车型:")
    elemt3 = input("输入批次号及编号:")
    elemt4 = input("输入车辆VIN码:")
    elemt5 = input("输入发动机号:")
    elemt6 = input("输入验收日期:")
    elemt7 = input("输入发运日期:")
    elemt8 = input("输入调拨单号:")
    elemt9 = input("输入接装单位:")
    elemt10 = input("输入接装单位地址:")
    elemt11 = input("输入联系人:")
    elemt12 = input("输入联系人电话:")
    sel = (elemt2,elemt3,elemt4,elemt5,elemt6,elemt7,elemt8,elemt9,elemt10,elemt11,elemt12)
    msg = "Z "+"%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s"%sel
    s.send(msg.encode())
    data = s.recv(1024).decode()
    if data =="OK":
        print("增加成功")
    else:
        print("添加失败")

def delete(s):
    #删除
    while True:
        sel = input("请输入需要删除的编号:")
        if sel != "":
            break
        else:
            print("输入有误")
    msg = "R "+sel
    s.send(msg.encode())
    data = s.recv(1024).decode()
    if data == "OK":
        print("删除成功")
    else:
        print("删除失败")

def quite(s):
    #退出
    s.send("EXIT".encode())
    print("谢谢使用")

def modify(s):
    #修改
    sel1 = input("请输入需要修改的编号:")
    sel2 = input("请输入需要修改的名称:")
    sel3 = input("请输入需要修改的内容:")
    sel4 = "%s,%s,%s"%(sel1,sel2,sel3)
    msg = "M "+sel4
    s.send(msg.encode())
    data = s.recv(1024).decode()
    if data =="OK":
        print("修改成功")
    else:
        print("修改失败")

#客户端函数入口
def main():
    while True:
        print("""
        ========welcome========
         1.查询 2.增加 3.修改
            4.删除  5.退出
        =======================
        """)
        cmd = input("命令(1,2,3,4,5):")
        if cmd == '1':
            select(s)
        elif cmd == '2':
            insert(s)
        elif cmd == '3':
            modify(s)
        elif cmd == '4':
            delete(s)
        elif cmd == '5':
            quite(s)
            break

if __name__ == '__main__':
    main()