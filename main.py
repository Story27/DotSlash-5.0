import os 
import random as ran
from sqlite3.dbapi2 import Connection, Cursor, Row
from typing import Mapping
import sqlite3

r=1
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def insertVaribleIntoTable(vehno, code):
    try:
        sqliteConnection = sqlite3.connect('data.db')
        cursor = sqliteConnection.cursor()

        sqlite_insert_with_param = """INSERT INTO data
                          (Vehicle_Number, Code) 
                          VALUES (?, ?);"""

        data_tuple = (vehno, code)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()

        cursor.close()

    except sqlite3.Error as error:
        print(error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()

def delete_task(id):
    sqconnect = sqlite3.connect('data.db')
    cur = sqconnect.cursor()
    sql = 'DELETE FROM data WHERE Code=?'
    cur.execute(sql, (id,))
    sqconnect.commit()

def task(priority):
    sqconnect = sqlite3.connect('data.db')
    cur = sqconnect.cursor()
    cur.execute("SELECT Code FROM data WHERE Vehicle_Number=?", (priority,))
    rows = cur.fetchone()
    for row in rows:
        return row

connection = sqlite3.connect('data.db')
crsr = connection.cursor()
#sql_command = """CREATE TABLE data (
#    Vehicle_Number VARCHAR,
#    Code VARCHAR PRIMARY KEY)"""
#crsr.execute(sql_command)

def convert(list):
# Converting integer list to string list
    s = [str(i) for i in list]
    # Join list items using join()
    res = int("".join(s))
    return(res)

while r==1:    
    option = input("Press 1 : If you want to park your vehicle\nPress 2 : If you want to recieve your vehicle\nResponce : ")
    if option == "1":
        vehicle = int(input("Please enter your vehicle no. :"))
        list = [i for i in range(100,1000)]
        a = ran.choices(list, k=1)
        b = convert(a)
        c = int(b)
        insertVaribleIntoTable(vehicle, c)
        print("your code is :",b)
    
    elif option == "2":
        veh = int(input("please enter your vehicle no. :"))
        row = int(task(veh))
        for i in (0,4):
            code = int(input("please enter your alloted code :"))
            #checking the info in database
            if code == row:
                list = [i for i in range(100,1000)]
                l = ran.choices(list, k=1)
                m = convert(l)
                o = int(m)
                print("Your vehicle is placed at: ",o," parking spot.\nThanks for coming.")
                delete_task(code)
                break
            else:
                print("Your code is wrong!")
        
    else:
        print("Option out of bound")
    x=input("Press enter to exit :")
    cls()
