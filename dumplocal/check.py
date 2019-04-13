# -*- coding: utf-8 -*-
#######################
# dumplocal.check
######################
"""
jsonn={"host":"host",
       "port":port,
       "username":"username",
       "password":"password",
       "database":"database",
       "tables":[],
       "check":False,
       "location":"location"}
"""

from common.dbInfo import DbInfo

def check(vars,db_tag=False,tb_tag=False,where_tag=False):
    check_result={"status":False,"type":"","msg":""}
    try:
        if "check" in vars.keys() and type(vars["check"]) is bool and vars["check"]:
            # skip check
            check_result["conn"],check_result["dump"]=get_conn_dump_str(vars)
            if db_tag:
                check_result["database"]=vars["database"]
            if tb_tag:
                if type(vars["tables"]) is str:
                    check_result["table"]=vars["tables"]
                elif type(vars["tables"]) is list:
                    check_result["table"]=" ".join(vars["tables"])
            if where_tag:
                if type(vars["where"]) is str:
                    str_where=vars["where"]
                    if ">" in str_where:
                       where_str=str_where.replace(">","\>")
                    elif "<" in str_where:
                       where_str=str_where.replace("<","\<")
                    else:
                       where_str=str_where
                check_result["where"]=where_str

            check_result["status"]=True
        else:
            # start check vars
            # check database tables
            if where_tag:
                if "where" not in vars.keys() or type(vars["where"]) is not str or len(vars["where"].split())==0:
                    check_result["msg"]="where must exist and cannot be empty"
                    return check_result
                str_where=vars["where"]
                if ">" in str_where:
                    where_str=str_where.replace(">","\>")
                elif "<" in str_where:
                    where_str=str_where.replace("<","\<")
                else:
                    where_str=str_where
                check_result["where"]=where_str

            if tb_tag:
                check_tb=check_tables(vars)
                if not check_tb[0]:
                    check_result["msg"]="tables must exist and cannot be empty"
                    return check_result
                check_result["table"]=check_tb[1]

            if db_tag: 
                check_db=check_database(vars)
                if not check_db[0]:
                    check_result["msg"]="database must exist and cannot be empty"
                    return check_result
                check_result["database"]=check_db[1]

            # check conn
            db=DbInfo(vars)
            check_conn=db.check_conn()
            if not check_conn["status"]:
                return check_result.update(check_conn)

            check_result["conn"],check_result["dump"]=get_conn_dump_str(vars)
            check_result["status"]=True
    except Exception as e:
        check_result["msg"]=str(e)
    return check_result  


def check_database(infos):
    if "database" in infos.keys() and type(infos["database"]) is str and len(infos["database"].split())>0:
        return True,infos["database"]
    else:
        return False,None


def check_tables(infos):
    if "tables" in infos.keys():
        if type(infos["tables"]) is str and len(infos["tables"].split())>0:
            return True,infos["tables"]
        elif type(infos["tables"]) is list and len(infos["tables"])>0:
            return True," ".join(set(infos["tables"]))
        else:
            return False,None
    else:
        return False,None


def get_conn_dump_str(inputs):
    conn="""mysql -h{host} -P{port} -u{username} -p{password}""".format(host=inputs["host"],port=inputs["port"],username=inputs["username"],password=inputs["password"])
    dump="""mysqldump -h{host} -P{port} -u{username} -p{password}""".format(host=inputs["host"],port=inputs["port"],username=inputs["username"],password=inputs["password"])
    return conn,dump


