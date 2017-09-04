# coding=utf-8

from pymongo import *
from user_conn import conn, pwd_sh1


if __name__ == '__main__':
    uname = raw_input("用户名:")
    upasswd = raw_input("密码:")

    # 加密
    pwd = pwd_sh1(upasswd)

    try:
        # mongodb中查询
        client = MongoClient(host='localhost', port=27017)
        db = client.fanfan
        result = db.py_user.find_one({'uname':uname}, {'_id': 0, 'upasswd': 1})

        if result is None:
            # mongodb中无数据，去MySQL查询
            result = conn(uname)
            if not result:
                print "不存在，MySQL"
            else:
                upwd_db = result[0]
                # 加到MongoDB中
                db.py_user.insert({'uname': uname, 'upasswd': upwd_db})

                # 提示信息
                if pwd == upwd_db:
                    print "登录成功，加入MongoDB"
                else:
                    print '账号或密码错误 mysql'

            pass
        else:
            # MongoDB中有数据
            if result['upasswd'] == pwd:
                print "登录成功, mongo"
            else:
                print "用户名或密码错误"

    except Exception as e:
        print e
    finally:
        client.close()
