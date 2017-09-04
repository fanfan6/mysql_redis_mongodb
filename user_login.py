# coding=utf-8

from user_conn import conn, pwd_sh1

if __name__ == '__main__':
    uname = raw_input("用户:")
    upasswd = raw_input("密码:")

    # 加密
    upwd = pwd_sh1(upasswd)

    try:
        conn = conn()
        # 根据用户名查询密码
        sql = 'select upasswd from py_user where uname=%s'
        params = [uname]
        cursor = conn.cursor()
        cursor.execute(sql, params)
        result = cursor.fetchone()

        # 若无结果返回None
        if not result:
            print "用户名或密码错误"
        else:
            if result[0] == upwd:
                print "success"
            else:
                print "用户名或密码错误"

    except Exception as e:
        print e
    finally:
        conn.close()
