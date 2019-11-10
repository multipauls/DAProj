import subprocess as sp
import pymysql
import pymysql.cursors


#Loading and adding fns
def showEmp():
    global cur
    row = {}
    print("Displaying all employees...\n");

    query2 = "SELECT * FROM EMPLOYEE

    cur.execute(query2)
    blah = cur.fetchall()
    for value in blah:
        print value

    return


def showItem():
    global cur


    query2 = "SELECT * FROM ITEM

    cur.execute(query2)
    blah = cur.fetchall()
    for value in blah:
        print value
    return

def showStore():
    global cur
    query2 = "SELECT * FROM STORE

    cur.execute(query2)
    blah = cur.fetchall()
    for value in blah:
        print value
    return

def showCustomer():
    global cur
    query2 = "SELECT * FROM CUSTOMER

    cur.execute(query2)
    blah = cur.fetchall()
    for value in blah:
        print value
    return
