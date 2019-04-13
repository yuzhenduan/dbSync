# -*- coding: utf-8 -*-
#######################
# pipeline.urls
#######################
from django.urls import path
from pipeline import views

urlpatterns = [
    #path('dump/', views.dump,name="dump"),
    path('dumpTableSchema/', views.dump_table_schema,name="dumpTableSchema"),
    path('dumpTableData/', views.dump_table_data,name="dumpTableData"),
    path('dumpTable/', views.dump_table,name="dumpTable"),
    path('dumpDatabaseSchema/', views.dump_database_schema,name="dumpDatabaseSchema"),
    path('dumpDatabaseData/', views.dump_database_data,name="dumpDatabaseData"),
    path('dumpDatabase/', views.dump_database,name="dumpDatabase"),
    path('dumpAllSchema/', views.dump_all_schema,name="dumpAllSchema"),
    path('dumpAllData/', views.dump_all_data,name="dumpAllData"),
    path('dumpAll/', views.dump_all,name="dumpAll"),
    path('dumpTableDataByWhere/', views.dump_table_data_by_where,name="dumpTableDataByWhere"),
    path('dumpTableByWhere/', views.dump_table_by_where,name="dumpTableByWhere"),
]

