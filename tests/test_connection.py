#!/bin/env python

'''
script to check if a database exists under port 3307

do not forget to give the permissions to the user rookie

'''


import pymysql

connection = pymysql.connect(
    host="127.0.0.1",
    port=3307,      # forwarded Colima port
    user="erp",
    password="erp"
)

with connection.cursor() as cursor:
    cursor.execute("CREATE DATABASE IF NOT EXISTS erp_test;")
    print("erp_test db created... (or already exists)")

connection.close()
