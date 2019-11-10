import subprocess as sp
import pymysql
import pymysql.cursors



#Removing and deleting fns
def closeStore():
    global cur
    row = {}
    row["StoreID"] = input("Enter Store ID to close: ")

    query2 = "DELETE FROM STORE WHERE StoreID='%s' " %(row["StoreID"])

    cur.execute(query2)
    con.commit()
    return

def fireEmp():
    global cur
    row = {}
    row["HRID"] = input("Enter Employee HR ID to remove: ")

	query1 = "DELETE FROM EMPLOYEE WHERE HRID='%s' " %(row["HRID"])
    cur.execute(query1)
    con.commit()

    query2 = "DELETE FROM HR WHERE HRID='%s' " %(row["HRID"])
    cur.execute(query2)
    con.commit()
    return

def removeSale():
    row = {}
    row["SaleID"] = input("Enter Sale ID to delete: ")

	query1 = "DELETE FROM SALE WHERE SaleID='%s' " %(row["SaleID"])
    cur.execute(query1)
    con.commit()

    return

def removeItemFromStore():
   row = {}
    row["StoreID"] = input("Enter Store ID: ")
    row["ItemName"] = input("Enter Item Name: ")


	query1 = "DELETE FROM HAS WHERE StoreID='%s' AND ItemName='%s'" %(row["StoreID"],row["ItemName"])
    cur.execute(query1)
    con.commit()

    return
