# -*- coding: utf-8 -*-
#######################
# local.views
#######################

import demjson
from django.http import HttpResponse
from pipeline.check import check
from common.tools import exec_cmd

# 
def health(request):
    return HttpResponse("<h1>Yes, We Can!</h1>")


default_param="--single-transaction --skip-tz-utc"
# pipeline/dumpTableSchema
def dump_table_schema(request):
    params="{default} --no-data".format(default=default_param)
    return __dump_table(request,params)

# pipeline/dumpTableData
def dump_table_data(request):
    params="{default} --no-create-info".format(default=default_param)
    return __dump_table(request,params)


# pipeline/dumpTable
def dump_table(request):
    params=default_param
    return __dump_table(request,params)


# pipeline/dumpDatabaseSchema
def dump_database_schema(request):
    params="{default} --no-data".format(default=default_param)
    return __dump_database(request,params)


# pipeline/dumpDatabaseData
def dump_database_data(request):
    params="{default} --no-create-info".format(default=default_param)
    return __dump_database(request,params)


# pipeline/dumpDatabase 
def dump_database(request):
    params=default_param
    return __dump_database(request,params)


# pipeline/dumpTableDataByWhere
def dump_table_data_by_where(request):
    params="{default} --no-create-info".format(default=default_param)
    return __dump_table_by_where(request,params)


# pipeline/dumpTableByWhere
def dump_table_by_where(request):
    params=default_param
    return __dump_table_by_where(request,params)

# pipeline/dumpAllSchema
def dump_all_schema(request):
    params="{default} --no-data --add-drop-database".format(default=default_param)
    return __dump_all(request,params)


# pipeline/dumpAllData
def dump_all_data(request):
    params="{default} --no-create-info".format(default=default_param)
    return __dump_all(request,params)


# pipeline/dumpAll
def dump_all(request):
    params="{default} --add-drop-database".format(default=default_param)
    return __dump_all(request,params)


##########################
def __dump_table(request,params):
    infos={"status":False,"msg":""}
    vars=demjson.decode(request.body)
    check_info=check(vars,db_tag=True,tb_tag=True)
    if check_info["status"]:
        s_dump=check_info["s_dump"]
        d_conn=check_info["d_conn"]
        src_database=check_info["s_database"]
        dest_database=check_info["d_database"]
        table=check_info["table"]
        command="""{s_dump} {param} {src_database} {src_table} 2>/dev/null | {d_conn} {dest_database} 2>/dev/null""".format(s_dump=s_dump,d_conn=d_conn,param=params,src_database=src_database,src_table=table,dest_database=dest_database)
        if exec_cmd(command):
           infos["status"]=True
        else:
           infos["msg"]="exec command failed"
    else:
        return HttpResponse(demjson.encode(check_info))
    return HttpResponse(demjson.encode(infos))


def __dump_database(request,params):
    infos={"status":False,"msg":""}
    vars=demjson.decode(request.body)
    check_info=check(vars,db_tag=True,tb_tag=False)
    if check_info["status"]:
        s_dump=check_info["s_dump"]
        d_conn=check_info["d_conn"]
        src_database=check_info["s_database"]
        dest_database=check_info["d_database"]
        command="""{s_dump} {param} {src_database} 2>/dev/null | {d_conn} {dest_database} 2>/dev/null""".format(s_dump=s_dump,d_conn=d_conn,param=params,src_database=src_database,dest_database=dest_database)
        if exec_cmd(command):
           infos["status"]=True
        else:
           infos["msg"]="exec command failed"
    else:
        return HttpResponse(demjson.encode(check_info))
    return HttpResponse(demjson.encode(infos))


def __dump_all(request,params):
    infos={"status":False,"msg":""}
    vars=demjson.decode(request.body)
    check_info=check(vars,db_tag=False,tb_tag=False)
    if check_info["status"]:
        s_dump=check_info["s_dump"]
        d_conn=check_info["d_conn"]
        command="""{s_dump} {param} -A 2>/dev/null | {d_conn} 2>/dev/null""".format(s_dump=s_dump,d_conn=d_conn,param=params)
        if exec_cmd(command):
           infos["status"]=True
        else:
           infos["msg"]="exec command failed"
    else:
        return HttpResponse(demjson.encode(check_info))
    return HttpResponse(demjson.encode(infos))


def __dump_table_by_where(request,params):
    infos={"status":False,"msg":""}
    vars=demjson.decode(request.body)
    check_info=check(vars,db_tag=True,tb_tag=True,where_tag=True)
    if check_info["status"]:
        s_dump=check_info["s_dump"]
        d_conn=check_info["d_conn"]
        src_database=check_info["s_database"]
        dest_database=check_info["d_database"]
        table=check_info["table"]
        where=check_info["where"]
        command="""{s_dump} {param} {src_database} {src_table} --where="{where}" 2>/dev/null | {d_conn} {dest_database} 2>/dev/null""".format(s_dump=s_dump,d_conn=d_conn,param=params,src_database=src_database,src_table=table,dest_database=dest_database,where=where)
        if exec_cmd(command):
           infos["status"]=True
        else:
           infos["msg"]="exec command failed"
    else:
        return HttpResponse(demjson.encode(check_info))
    return HttpResponse(demjson.encode(infos))

