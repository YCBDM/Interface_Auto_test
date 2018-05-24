"""
1. 从config文件读取配置
2. 连接数据库
3. 执行sql并返回结果
"""

import psycopg2

import sys

sys.path.append("..")
from util.config import Config


class DB():
    def __init__(self):
        cf = Config()
        self.conn = psycopg2.connect(host=cf.get_db('db_host'),
                                     port=cf.get_db('db_port'),
                                     dbname=cf.get_db('db_name'),
                                     user=cf.get_db('db_user'),
                                     password=cf.get_db('db_passwd'))
        self.cur = self.conn.cursor()

    def __del__(self):
        self.cur.close()
        self.conn.close()

    def exec_sql(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchall()


if __name__ == '__main__':
    db_name = DB()
    print(db_name.exec_sql("select * from users where username='jqx17'"))
    # print(Config.get_db('db_name'))
