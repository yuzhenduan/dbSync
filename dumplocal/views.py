# -*- coding: utf-8 -*-
#######################
# dumplocal.views
#######################

import demjson,time
from django.http import HttpResponse
from dumplocal.check import check
from common.tools import exec_cmd

# 
def health(request):
    return HttpResponse("<h1>Yes, We Can!</h1>")

location="data"
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
        date = time.strftime('%Y-%m-%d', time.localtime())
        dump=check_info["dump"]
        database=check_info["database"]
        table=check_info["table"]
        command="""{dump} {param} {database} {table} > {location}/{database}.{s_table}.sql-{date} 2>/dev/null """.format(date=date,dump=dump,param=params,database=database,location=location,table=table,s_table=table.replace(" ","-"))
        if exec_cmd(command):
           infos["status"]=True
        else:
           infos["msg"]="exec command failed"
           infos["msg"]=str(command)
    else:
        return HttpResponse(demjson.encode(check_info))
    return HttpResponse(demjson.encode(infos))


def __dump_database(request,params):
    infos={"status":False,"msg":""}
    vars=demjson.decode(request.body)
    check_info=check(vars,db_tag=True,tb_tag=False)
    if check_info["status"]:
        date = time.strftime('%Y-%m-%d', time.localtime())
        dump=check_info["dump"]
        database=check_info["database"]
        command="""{dump} {param} {database} > {location}/{database}.sql-{date} 2>/dev/null""".format(date=date,dump=dump,param=params,database=database,location=location)
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
        dump=check_info["dump"]
        command="""{dump} {param} -A > {location}/{database}.{table}.sql-{date} 2>/dev/null""".format(dump=dump,date=date,param=params,location=location)
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
        date = time.strftime('%Y-%m-%d', time.localtime())
        dump=check_info["dump"]
        database=check_info["database"]
        table=check_info["table"]
        where=check_info["where"]
        command="""{dump} {param} {database} {table} --where="{where}" > {location}/{database}.{s_table}.sql-{date} 2>/dev/null""".format(dump=dump,param=params,date=date,database=database,table=table,s_table=table.replace(" ","_"),where=where,location=location)
        if exec_cmd(command):
           infos["status"]=True
        else:
           infos["msg"]="exec command failed"
    else:
        return HttpResponse(demjson.encode(check_info))
    return HttpResponse(demjson.encode(infos))

