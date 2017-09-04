# coding=utf-8

from user_conn import conn, pwd_sh1
from pymysql import *


if __name__ == '__main__':
    uname = raw_input("用户名：")
    upasswd = raw_input("密码：")

    # 加密
    upwd = pwd_sh1(upasswd)

    try:
        # 查询用户名是否存在
        result = conn(uname)
        # 若用户不存在，返回None，
        if result:
            print '用户名已存在'
        else:
            conn = connect(host='localhost', port=3306, user='root', password='mysql', database='fanfan',
                           charset='utf8')
            cursor = conn.cursor()
            sql = 'insert into py_user(uname, upasswd) VALUES(%s, %s)'
            params = [uname, upwd]
            result = cursor.execute(sql, params)
            if result == 1:
                print "注册成功"
            conn.commit()
            conn.close()

    except Exception as e:
        print e
        conn.rollback()
        print "注册失败"

