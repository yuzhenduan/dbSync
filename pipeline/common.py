# -*- coding: utf-8 -*-
#######################
# pipeline.common
#######################

"""
jsonn={"src":{"host":"host",
              "port":port,
              "username":"username",
              "password":"password",
              "database":"database"},
       "dest":{"host":"host",
               "port":port,
               "username":"username",
               "password":"password",
               "database":"database",},
       "tables":[],}
"""

def check_grants(request):
  pass

def get_dump_sql();
  pass

def get_conn_sql():
  pass

def exec_command(command):
    if os.system(command)==0:
        return True
    else:
        return False
