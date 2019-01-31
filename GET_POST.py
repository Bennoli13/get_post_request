#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
import json
import mysql.connector
import time
from mysql.connector import Error
from mysql.connector import errorcode
from time import gmtime, strftime

var=""
host="ip-sflow-rt"
url = "http://"+host+"/metric/10.0.0.11/tcp_minimal/json"
print(url)


# In[3]:


def get_req():
    g = requests.get(url)
    json_data = json.loads(g.text)
    return(json_data)


# In[4]:


def post_req(new_value):
    try:
        connection = mysql.connector.connect(host='localhost', database='test', user='root', password='')
        table_name = "tcp_database"
        sql_query = "INSERT INTO "+ table_name + "(ipsource, ipdestination, tcpsourceport, tcpdestinationport, tcpflags, tcpwindow, tcppayloadbytes, tcpseqno, tcpackno, bytes, lastUpdate) VALUES (" + new_value +")"
        cursor = connection.cursor()
        result = cursor.execute(sql_query)
        connection.commit()
        print ("inserted")

    except mysql.connector.Error as error :
        connection.rollback()
        print ("Failed to execute sql_query {}".format(error))

    finally:
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print ("Database Closed")


# In[5]:


def value_creator(data):
    bytes1 = repr(data['value'])
    lastUpdate1 = repr(data['lastUpdate'])
    value_sql = data['key']+','+bytes1+','+lastUpdate1
    value_sql_split = value_sql.split(',')
    value_sql_split[0] = "'"+value_sql_split[0]+"'"
    value_sql_split[1] = "'"+value_sql_split[1]+"'"
    value_sql_split[4] = "'"+value_sql_split[4]+"'"
    value_sql_join = ','.join(value_sql_split)
    print(value_sql_join)
    return(value_sql_join)


# In[6]:


def run_me():
    dict_json = get_req()
    data = dict_json[0]['topKeys']
    for i in range(len(data)):
        new_value = value_creator(data[i])
        new_value = str(new_value)
        post_req(new_value)


# In[7]:


try:
    while True:
        run_me()
        time.sleep(30)
except KeyboardInterrupt:
    print ('Manual break by user')


# In[ ]:





# In[ ]:




