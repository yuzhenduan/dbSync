# -*- coding: utf-8 -*-
#######################
# common.dbInfo
#######################

import pymysql
class DbInfo:
    def __init__(self,conn_info):
        self.conn_info=conn_info

    def create_database(self,database):
        sql='create database if not exists `{database}`'.format(database=database)
        return self.mysql_exec(sql)


    def mysql_exec(self,sql,cursor_type=pymysql.cursors.DictCursor):
        infos={"status":False,"data":[],"message":None}
        if "database" in self.conn_info.keys():
             database=self.conn_info["database"]
        else:
             database=None
        try: 
            conn=pymysql.connect(host=self.conn_info["host"],
                           port=int(self.conn_info["port"]),
                           user=self.conn_info["username"],
                           passwd=self.conn_info["password"],
                           db=database)
        except pymysql.err.OperationalError as e:
            infos["message"]="Access denied"
            return infos
        except pymysql.err.InternalError as e:
            infos["message"]="Unknown database"
            return infos
        except Exception as e:
            infos["message"]=e
            return infos
        with conn.cursor(cursor=cursor_type) as cursor:
            try:
                cursor.execute(sql)
                infos["data"]=cursor.fetchall()
                infos["status"]=True
            except pymysql.err.ProgrammingError as e:
                infos["message"]="Syntax error"
            except pymysql.err.InternalError as e:
                infos["message"]="Unknown column"
            except Exception as e:
                infos["message"]=e 
        return infos

    def check_conn(self):
        infos={"status":False,"data":[],"message":None}
        if "database" in self.conn_info.keys():
             database=self.conn_info["database"]
        else:
             database=None
        try:
            conn=pymysql.connect(host=self.conn_info["host"],
                           port=int(self.conn_info["port"]),
                           user=self.conn_info["username"],
                           passwd=self.conn_info["password"],
                           db=database)
            infos["status"]=True
        except pymysql.err.OperationalError as e:
            infos["message"]="Access denied"
        except pymysql.err.InternalError as e:
            infos["message"]="Unknown database"
        except Exception as e:
            infos["message"]=e
        return infos

if __name__=="__main__":
   data={"host":"192.168.137.4","port":3306,"username":"yuzhen","password":"yuzhen","database":"env"}
   db=DbInfo(data)
   print(db.mysql_exec("select * from env"))
