import pyodbc
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import math

def dbConnect():

    ServerName = "localhost"
    MySQLDatabase = "game_of_11"
    username = "root"
    password = "C+*rbon@123"

    conn = pyodbc.connect("DRIVER={{MySQL ODBC 8.0 Driver}};SERVER={0}; database={1};UID={2};PWD={3}".format(ServerName, MySQLDatabase, username,password))
 
    return conn

def getData(query):
    cur = dbConnect().cursor()
    cur.execute(query)
    data = cur.fetchall()
    print(data)
    return data

def getResults():
    adv_profit = getData("SELECT adv_id, SUM(booking_rev_EURcent) - (SUM(booking_rev_EURcent)*0.15) as profit FROM phpmyadmin.XXX GROUP BY adv_id order BY profit DESC")
    adv_profit = [(users, int(count)) for users, count in adv_profit]

    cols = ['adv_id', 'profit']
    adv_profit = pd.DataFrame(adv_profit, columns=cols)
    print(adv_profit)

    profit_dataframe = adv_profit.sort_values(by = 'profit', ascending = False)

    top = profit_dataframe.iloc[:9] 

    all_data = top.append(profit_dataframe, ignore_index=True)
    all_data.index = all_data['adv_id']

    profit_dataframe.plot(kind='bar', y = 'profit')

    plt.figure()
    plt.subplot(121)

    cell_text = []
    for row in range(len(profit_dataframe)):
        cell_text.append(profit_dataframe.iloc[row])

    plt.table(cellText=cell_text, colLabels=profit_dataframe.columns, loc='center')
    plt.axis('off')
    plt.show()

getResults()
