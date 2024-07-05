# -*- coding: utf-8 -*-

import pymssql
import toml

config = toml.load('config.toml')

server = config['host']
database = config['database']
username = config['username']
password = config['password']

try:
    connection = pymssql.connect(server=server, user=username, password=password, database=database)
    print("成功连接到 SQL Server")
    
    cursor = connection.cursor()
    cursor.execute('SELECT @@VERSION')
    
    row = cursor.fetchone()
    while row:
        print(row[0])
        row = cursor.fetchone()
    
    cursor.close()
    
except Exception as e:
    print("连接失败")
    print(str(e))
finally:
    if 'connection' in locals() and connection:
        connection.close()