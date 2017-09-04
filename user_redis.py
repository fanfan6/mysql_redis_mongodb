# coding=utf-8

from user_conn import conn, pwd_sh1
from redis import StrictRedis

if __name__ == '__main__':
    uname = raw_input("用户名:")
    upasswd = raw_input("密码:")

    # 加密
    upwd = pwd_sh1(upasswd)

    try:
        # 从redis读取，若没有，从MySQL找
        redis_user = StrictRedis()
        upwd_redis = redis_user.get(uname)
        # print upwd_redis
        if upwd_redis is None:
            # 未找到,从MySQL查询
            result = conn(uname)
            if not result:
                print "用户名错误,mysql"
            else:
                # 存到redis
                upwd_mysql = result[0]
                redis_user.set(uname, upwd_mysql)

                if upwd_mysql == upwd:
                    print "登录成功,mysql"
                else:
                    print "登录失败， MySQL"
        else:
            # 存在
            if upwd_redis == upwd:
                print "登录成功，redis"
            else:
                print "用户名或密码错误 redis"

    except Exception as e:
        print e

    finally:
        pass
