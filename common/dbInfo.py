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


    def mysql_exec(self,sql,cursor_type=None):
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
        tag=sql.lower().startswith('select')
        if tag:
            cursor_type=pymysql.cursors.DictCursor
        with conn.cursor(cursor=cursor_type) as cursor:
            try:
                cursor.execute(sql)
                if tag:
                    infos["data"]=cursor.fetchall()
                else:
                    conn.commit()
                infos["status"]=True
            except pymysql.err.ProgrammingError as e:
                infos["message"]="Syntax error"
            except pymysql.err.InternalError as e:
                infos["message"]="Unknown column"
            except Exception as e:
                infos["message"]=e 
        try:
            conn.close()
        except Exception as e:
            infos["message"]="db connection already close!"
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

