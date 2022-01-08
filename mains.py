import os 
import random as ran
from sqlite3.dbapi2 import Connection, Cursor
from typing import Mapping
import sqlite3
import json
r=1
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

connection = sqlite3.connect('data.db')
crsr = connection.cursor()
#sql_command = """CREATE TABLE data (
#    Vehicle_Number INTEGER,
#    Code INTEGER PRIMARY KEY)"""
#crsr.execute(sql_command)

def convert(list):
      
    # Converting integer list to string list
    s = [str(i) for i in list]
      
    # Join list items using join()
    res = int("".join(s))
      
    return(res)

while r==1:    
    option = input("Press 1 : If you want to park your vehicle\nPress 2 : If you want to recieve your vehicle\nResponce :")
    if option == "1":
        vehicle = int(input("Please enter your vehicle no. :"))
        list = [i for i in range(100,1000)]
        a = ran.choices(list, k=1)
        b = convert(a)
        list1 = [vehicle, b]
        var_string = ', '.join('?' * len(list1))
        sql = 'INSERT INTO data(Vehicle_Number, code) VALUES (%s);' % var_string
        #checking random no. is not same
        print("your code is :",b)
        crsr.execute(sql, list1)
        connection.commit()
    
    elif option == "2":
        veh = int(input("please enter your vehicle no. :"))
        
        for i in (0,3):
            code = int(input("please enter your alloted code :"))
            #checking the info in database
            crsr.execute("SELECT code FROM data WHERE (Vehicle_number = '{veh}')")
            datacode = crsr.fetchall()
            print(datacode)
            if code == datacode:
                print("Your vehicle is placed at this spot")
                crsr.execute('''DELETE FROM data WHERE code={code}''')
                connection.commit()
                break
            else:
                print("Your code is wrong!")
        
    else:
        print("Option out of bound")
    x=input("Press enter to exit :")
    cls()
