import pymysql

def connectmariadb():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='python_train',
        cursorclass=pymysql.cursors.DictCursor
        )
    return conn

# print(connectmariadb())