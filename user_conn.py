# coding=utf-8

from pymysql import *
from hashlib import sha1


# 连接MySQL
def conn(uname):
    conn = connect(host='localhost', port=3306, user='root', password='mysql', database='fanfan', charset='utf8')
    sql = 'select upasswd from py_user where uname=%s'
    params = [uname]
    cursor = conn.cursor()
    cursor.execute(sql, params)
    result = cursor.fetchone()
    conn.close()
    return result


# 密码sha1加密
def pwd_sh1(passwd):
    s1 = sha1()
    s1.update(passwd)
    upwd = s1.hexdigest()
    return upwd

if __name__ == '__main__':
    print pwd_sh1('12')
