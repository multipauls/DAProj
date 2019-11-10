import subprocess as sp
import pymysql
import pymysql.cursors


#Loading and adding fns
def showEmp():
    global cur
    print("Displaying all employees...\n");

    query2 = "SELECT * FROM EMPLOYEE"

    cur.execute(query2)
    blah = cur.fetchall()
    for value in blah:
        print value

    return

def showStoreProfit():
    global cur

    StoreID=input("Enter store ID to show profit: ")

    query2 = "SELECT SUM(TotalProfit) FROM REGISTER WHERE StoreID= '%s'" %(StoreID)

    cur.execute(query2)
    blah = cur.fetchall()
    blah=int(blah[0])

    return

def showItem():
    global cur


    query2 = "SELECT * FROM ITEM"

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
    query2 = "SELECT * FROM CUSTOMER"

    cur.execute(query2)
    blah = cur.fetchall()
    for value in blah:
        print value
    return
