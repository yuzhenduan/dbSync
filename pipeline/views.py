# -*- coding: utf-8 -*-
#######################
# local.views
#######################
from django.http import HttpResponse

# 
def health(request):
    return HttpResponse("<h1>Yes, We Can!</h1>")

# pipeline/dumpTableSchema
def dump_table_schema(request):
    param="--single-transaction --no-data"
    command="""mysqldump -h{src_host} -P{src_port} -u{src_username} -p{src_password} {param} {src_database} {src_table} 2>/dev/null | mysql -h{dest_host} -P{dest_port} -u{dest_username} -p{dest_password} {dest_database} 2>/dev/null"""
    

# pipeline/dumpTableData
def dump_table_data(request):
	pass


# pipeline/dumpTable
def dump_table(request):
	pass

# pipeline/dumpDatabaseSchema
def dump_database_schema(request):
	pass


# pipeline/dumpDatabaseData
def dump_database_data(request):
	pass


# pipeline/dumpDatabase
def dump_database(request):
	pass


# pipeline/dumpAllSchema
def dump_all_schema(request):
	pass


# pipeline/dumpAllData
def dump_all_data(request):
	pass

# pipeline/dumpAll
def dump_all(request):
	pass
